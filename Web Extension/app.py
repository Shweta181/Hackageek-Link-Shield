print("Starting Flask app...")

#importing packages 
from flask import Flask, request, jsonify
import pickle
import numpy as np
import urllib
from urllib.parse import urlparse
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os

# function that loads environment variables to manage the configuration settings easily
load_dotenv()

# create a flask instance
app = Flask(__name__)
CORS (app)

# Get the environment variables
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

# Load the pre-trained XGBoost model
with open('XGBoostClassifier.pickle.dat', 'rb') as file:
    model = pickle.load(file)

# Defining functions for feature extraction
def havingIP(url):
    if "://" in url:
        return 1
    else:
        return 0

def haveAtSign(url):
    if "@" in url:
        return 1
    else:
        return 0

def getLength(url):
  if len(url) < 54:
    length = 0
  else:
    length = 1
  return length

def getDepth(url):
  s = urllib.parse.urlparse(url).path.split('/') 
  depth = 0
  for j in range(len(s)):
    if len(s[j]) != 0:
      depth = depth+1
  return depth

def redirection(url):
    if "?" in url:
        return 1
    else:
        return 0

def httpDomain(url):
  domain = urllib.parse.urlparse(url).netloc 
  if 'https' in domain:
    return 1
  else:
    return 0

def prefixSuffix(url):
    if "-" or "_" in urlparse(url).path:
        return 1
    else:
        return 0

def tinyURL(url):
    if "tinyurl" in urllib.parse.urlparse(url).netloc: 
        return 1
    else:
        return 0


def iframe(response):
    if "<iframe" in response.text.lower():
        return 1
    else:
        return 0

def mouseOver(response):
    if "onmouseover" in response.text.lower():
        return 1
    else:
        return 0

def rightClick(response):
    if "oncontextmenu" in response.text.lower():
        return 1
    else:
        return 0

def forwarding(response):
    if "javascript" in response.text.lower():
        return 1
    else:
        return 0

def featureExtractions(url): 
    features = []
    features.append(havingIP(url))
    features.append(haveAtSign(url))
    features.append(getLength(url))
    features.append(getDepth(url))
    features.append(redirection(url))
    features.append(httpDomain(url))
    features.append(prefixSuffix(url))
    features.append(tinyURL(url))

    # For features that require a response, make a request
    try:
        response = requests.get(url)
        features.append(iframe(response))
        features.append(mouseOver(response))
        features.append(rightClick(response))
        features.append(forwarding(response))
    except:
        # Handle cases where the request fails ( append 0 for the features)
        features.extend([0, 0, 0, 0])

    return features

@app.route('/')
def home():
    return "Welcome to the ML model API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    urls = data['urls']
    
    # Process the URLs to extract features suitable for your model
    features = [featureExtractions(url) for url in urls]

    # Convert features to the appropriate format for the model
    features_array = np.array(features)
    
    # Make predictions
    predictions = model.predict(features_array)
      
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run()