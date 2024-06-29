# Hackageek-Link-Shield
Dynamic Malicious Link Detection and Highlighting Web Extension

IDEA / OBJECTIVE-

The objective of this project is to Develop a web extension that enhances user security by dynamically identifying malicious or suspicious links on webpages by using machine learning models that are trained on dataset . It alerts the user visually by highlighting potentially malicious or suspicious links on webpages  without requiring their active intervention.The extension utilizes a machine learning model to classify links in real-time

WORKFLOW -

1)URL Collection: The extension collects URLs from the webpages the user visits .

2)URL Analysis: The data is send to machine learning model through an api to analyze each URL by its features (like domain of URL, @ symbol of URL, http/https in domain name, redirection // in URL, etc.)

3)Classification: The machine learning model classifies each URL as malicious or benign.

4)Highlighting: If a URL is classified as malicious, the extension highlights it visually on the webpage using CSS styles.


COMPONENTS:

Frontend: HTML, CSS, and JavaScript code that interacts with the user and renders the visual cues.

Backend: Integration of API to machine learning model to analyse the URLs.

Machine Learning Model: A trained model that classifies URLs as malicious or benign.
