# scrapy-firebase-feed-storage-example
This is an example of how one could create and use a feed storage class to store files on Firebase using Scrapy.
It does not handle `feed_options`. 

## requirements
You will need to install the [pyrebase](https://github.com/thisbejim/Pyrebase) package for this example to work.

## settings 
It is mandatory to set `FIREBASE_CONFIG` in `settings.py` for the storage to actually work.

### FIREBASE_CONFIG 
`FIREBASE_CONFIG` is basically the `firebaseConfig` you can find on your project's settings tab converted from JavaScript to a Python Dictionary. 
In `settings.py` it should look like this:
```python
FIREBASE_CONFIG = {
    'apiKey': 'your api key',
    'authDomain': 'your auth domain',
    'databaseURL': 'https://your-database-url.firebaseio.com',
    'projectId': 'your-project-id',
    'storageBucket': 'your-storage-bucket.appspot.com',
    'messagingSenderId': 'your-messaging-sender-id',
    'appId': 'your-app-id'
}
```
If you did not yet create a Firebase project, feel free to follow this tutorial on how to use Firebase Cloud Storage with Python:
[Python + Firebase Cloud Storage - Upload/Download Files | Pyrebase](https://www.youtube.com/watch?v=I1eskLk0exg&t=470s)

## test your feed storage
This project comes with an example spider which scrapes the first two pages of [quotes.toscrape.com](http://quotes.toscrape.com/).
After cloning the repository and setting everything up, you should be able to start the spider with: `scrapy crawl quotes`
