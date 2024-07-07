# Hackageek-Link-Shield
Dynamic Malicious Link Detection and Highlighting Web Extension

## iDEA / OBJECTIVE

The idea of this project is to develop a web extension that enhances user security by dynamically identifying malicious or suspicious links on webpages by using machine learning models that are trained on dataset . It alerts the user visually by highlighting potentially malicious or suspicious links on webpages  without requiring their active intervention.The extension utilizes a machine learning model to classify links in real-time.


## WORKFLOW 

**1)URL Collection**: The extension collects URLs from the webpages the user visits .

**2)URL Analysis**: The data is send to machine learning model through an api to analyze each URL by its features (like domain of URL, @ symbol of URL, http/https in domain name, redirection // in URL, etc.)

**3)Classification**: The machine learning model classifies each URL as malicious or benign.

**4)Highlighting**: If a URL is classified as malicious, the extension highlights it visually on the webpage using CSS styles.


## COMPONENTS

**Frontend**: HTML, CSS, and JavaScript code that interacts with the user and renders the visual cues.

**Backend**: Integration of web extension to machine learning model through an API to analyse the URLs. Using Javascript with node.js and express framework for creating API.

**Machine Learning Model**: A trained model that classifies URLs as phishing and legitimate.The model is trained on Tensorflow, a free and open-source software library for machine learning.
The dataset used here is taken from https://github.com/goodycy3/Detection-of-Phishing-Website-Using-Machine-Learning/tree/master/ML%20work/DataSets. The dataset contains 5000 phishing links and 5000 legitimate links, in total 1000 links which are classified into training and testing dataset after preprocessing the data.

For training the model, following steps are to be followed -

1- Data Collection

2- Data Pre-processing

3- Data Analysis : Feature extraction 

4- Splitting of dataset into training and testing dataset

5- Model Training on trained dataset using classification model

6- Model evaluation using testing dataset

7- Saving the model

8- Model deployment
