# Scrapy settings for scrapy_firebase_feed_storage_example project
BOT_NAME = 'scrapy_firebase_feed_storage_example'
SPIDER_MODULES = ['scrapy_firebase_feed_storage_example.spiders']
NEWSPIDER_MODULE = 'scrapy_firebase_feed_storage_example.spiders'
ROBOTSTXT_OBEY = True

FIREBASE_CONFIG = {
    # your firebaseConfig of your firebase project goes here
}

# here the firebase storage is added to the list of available storages 
FEED_STORAGES = {
   'firebase': 'scrapy_firebase_feed_storage_example.extensions.FirebaseFeedStorage'
}

# Every key of the FEEDS setting is a feed uri
# the feed uri here saves the resulting feed to the folder fstest on firebase
# the filename will be a combination of the time at which the crawl ran and the spider name
# for example: 2020-11-23T13-14-03-quotes.csv
# for more about FEEDS, see: 
# https://docs.scrapy.org/en/latest/topics/feed-exports.html#std-setting-FEEDS
FEEDS = {
    'firebase://fstest/%(time)s-%(name)s.csv': {
        'format': 'csv'
    }
}