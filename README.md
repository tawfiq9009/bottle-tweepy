# bottle-tweepy

## Installation

Install with the following commands:
``` 
$ pip install bottle-tweepy 
```

or download the latest version from github:
```
  $ git clone https://github.com/tawfiq9009/bottle-tweepy
  $ cd bottle-tweepy
  $ python setup.py install
```

## Usage

Once installed to an application, the plugin passes an open :class:`tweepy.API` instance to all routes that require a `api` keyword argument:

```
import bottle
from bottle_tweepy import TweepyPlugin

app = bottle.Bottle()
plugin = TweepyPlugin(consumer_key, consumer_secret, access_token, access_token_secret)
app.install(plugin)

@app.route('/screen/:username')
def screen_name(username, api):
   user = api.get_user(username)
   return user.screen_name
```
