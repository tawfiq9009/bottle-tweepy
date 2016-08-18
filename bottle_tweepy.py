import tweepy 
import inspect
from bottle import PluginError

class TweepyPlugin(object):
    
    name = 'tweepy'
    api = 2
    
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, keyword='api'):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.keyword = keyword
        
    def setup(self, app):
        for other in app.plugins:
            if not isinstance(other, TweepyPlugin): continue
            if other.keyword == self.keyword:
                raise PluginError("Found another tweepy plugin with "\
                "conflicting settings (non-unique keyword).")
                    
    def apply(self, callback, context):
        conf = context.config.get('tweepy') or {}
        consumer_key = conf.get('consumer_key', self.consumer_key)
        consumer_secret = conf.get('consumer_secret', self.consumer_secret)
        access_token = conf.get('access_token', self.access_token)
        access_token_secret = conf.get('access_token_secret', self.access_token_secret)
        keyword = conf.get('keyword', self.keyword)
        
        args = inspect.getargspec(context.callback)[0]
        if keyword not in args:
            return callback
            
        def wrapper(*args, **kwargs):
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)

            kwargs[self.keyword] = tweepy.API(auth)
            rv = callback(*args, **kwargs)
            return rv
        
        return wrapper