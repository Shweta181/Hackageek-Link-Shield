document.getElementById('scan').addEventListener('click', () => {             //document.getElementById() get the element with id scan and addEventListener() method attaches an event handler to element
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {      //chrome.tabs.query() retrieves the active tab from the current-focused window
        chrome.scripting.executeScript({                                      //using chrome.scripting namespace, extension can make decision at runtime.A function scanLinks is injected here
            target: { tabId: tabs[0].id },
            function: scanLinks
        });
    });
});

function scanLinks() {                                                                           //defining the function scanLinks
    const links = Array.from(document.getElementsByTagName('a')).map(link => link.href);         //collects all the links and stores them in const links
    const filteredLinks = links.filter(link => !link.startsWith('chrome://'));                   //excluding the links starting with chrome:// because chrome does not allows these links to be stored

    chrome.runtime.sendMessage({ type: 'scanLinks', links: filteredLinks }, (response) => {      //Using chrome.runtime.sendMessage(), the messages are send to the service worker 
        const { maliciousLinks } = response;                                                     //maliciousLinks is recieved as response from the service worker
        
        document.querySelectorAll('a').forEach(link => {                                         //document.querySelectorAll() selects all the elements with tag <a>
            if (maliciousLinks.includes(link.href)) {
                link.style.color = 'red';                                                        //highlights malicious links to red
            }
        });
    });
}
