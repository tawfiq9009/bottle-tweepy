import unittest
import os
import bottle

from bottle_tweepy import TweepyPlugin
import tweepy 

class TweepyTest(unittest.TestCase):
    
    def setUp(self):
        self.consumer_key = ''
        self.consumer_secret = ''
        self.access_token = ''
        self.access_token_secret = ''
        self.app = bottle.Bottle(catchall=False)
        plugin = TweepyPlugin(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        self.plugin = self.app.install(plugin)
        
        
    def test_with_keyword(self):
        @self.app.get('/')
        def test(api):
            self.assertEqual(type(api), type(tweepy.API()))
            self.assertTrue(api)
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)
        
    def test_get_screen_name(self):
        @self.app.get('/')
        def test(api):
            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            auth.set_access_token(self.access_token, self.access_token_secret)

            api_tweepy = tweepy.API(auth)
            
            user_plugin = api.get_user('tawfiqCs')
            from_plugin = user_plugin.screen_name
            
            user_tweepy = api.get_user('tawfiqCs')
            from_tweepy = user_tweepy.screen_name

            self.assertTrue(user_plugin)
            self.assertEqual(from_plugin, from_tweepy)
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x,y: None)
        
        
if __name__ == '__main__':
    unittest.main()