//Background.js acts as service worker

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {             //this listens to the message sent from popup.js
    if (request.type === 'scanLinks') {
        fetch('https://deployment-430020.el.r.appspot.com/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ urls: request.filteredLinks })
        })
        .then(response => response.json())                                            //this is a part of the promise chain in a JavaScript fetch request. It means that once the HTTP request (initiated by fetch) gets a response from the server, the response will be processed to extract the JSON body
        .then(data => {
            sendResponse({ maliciousLinks: request.links.filter((_, idx) => data.predictions[idx] === 1) });      // this is part of a JavaScript promise chain that processes the data returned from a server and filters out malicious links based on the server's response.
        })
        .catch(errorHandler);

        return true;                                                                 // Required to send response asynchronously
    }
});

const errorHandler = (error) => {
    console.error('Error:', error);                                                  // Used for handling any errors that might occur during the execution of the fetch request or any of the preceding .then()
};
