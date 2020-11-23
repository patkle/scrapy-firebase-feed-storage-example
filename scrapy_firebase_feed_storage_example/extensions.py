# -*- coding: utf-8 -*-
from __future__ import annotations
from scrapy.extensions.feedexport import BlockingFeedStorage
import pyrebase

# Most of the logic is handled by BlockingFeedStorage
# see: https://github.com/scrapy/scrapy/blob/master/scrapy/extensions/feedexport.py
class FirebaseFeedStorage(BlockingFeedStorage):
    """FeedStorage to store data on firebase storage"""

    def __init__(self, uri: str=None, firebase_config: dict=None, *, feed_options=None) -> None:
        # feed_options are NOT honored here. Sorry!
        self._initialize_firebase_storage(uri, firebase_config)

    @classmethod
    def from_crawler(cls, crawler, uri) -> FirebaseFeedStorage:
        # if instantiated from crawler, pass crawler settings for Firebase here
        return cls(
            uri,
            crawler.settings['FIREBASE_CONFIG']
        )

    def _initialize_firebase_storage(self, uri, firebase_config) -> None:
        """Initializes a connection to the firebase storage"""
        self._storage = pyrebase.initialize_app(firebase_config).storage()
        path = self._get_path_from_uri(uri)
        # set path in which to store file
        self._storage.path = path

    def _get_path_from_uri(self, uri) -> None:
        """Extracts the path to save to from FEED_URI setting"""
        return uri.split('//', maxsplit=1)[1]

    def _store_in_thread(self, file) -> None:
        # go back to beginning of file
        file.seek(0)
        # upload the file to firebase storage        
        self._storage.put(file)
        file.close()
