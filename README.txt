SupyBot Twitter Plugin
======================

This is a twitter plugin for supybot. It can post to twitter, and show your
friend list. It will add (ircnick) after tweets. We use it to post to an
organizational twitter account from our channel.

The current version is always available from
https://github.com/rubinlinux/supybot-twitter.

This code is forked from http://code.google.com/p/supybot-twitter which
has not been updated in a long time. This version has been updated to
post using the new twitter API (and so, works, again).

You'll have to create a Twitter API key. See http://dev.twitter.com. Steps are:
1. Create a new twitter account (if you plan to use a dedicated one)
2. Go to dev.twitter.com and log in. 
3. Click create an application
4. put in info (yoru bots name and irc network for project name and descr)
5. when app is created, go to settings (on dev.twitter.com) and change it to
   read-write
6. on the main app page, (toward the bottom) click regenerate button
   (otherwise your account will still only be authed for read-only access)
7. Your 4 magic strings (2 tokens and 2 secrets) are shown.

This plugin uses the Twitter API from http://code.google.com/p/python-twitter/
so it must be installed and available for use. It can be installed via
pip like so:

    pip install python-twitter

To Setup:
  Login to bot

  Set private keys from step 7 above:
      /msg bot config plugins.twitter.consumer_key xxxxx
      /msg bot config plugins.twitter.consumer_secret xxxxx
      /msg bot config plugins.twitter.access_key xxxxx
      /msg bot config plugins.twitter.access_secret xxxxx
  Enable the plugin in the channel you want:
      !config channel plugins.twitter.enabled True

  If you want topic snarfing:
      !config channel plugins.twitter.tweettopicsnarf True

#!!!!
# Twitter has deprecated the mechanism we used to do this as a part of their war on 3rd party clients.
# http://code.google.com/p/python-twitter/issues/detail?id=144
# currently enabling displayReplies will result in the plugin crashing. :(
#  If you want replies (mentions):
#      !config plugins.twitter.displayReplies True
#      !config plugins.twitter.channelList #yourchannel
#!!!!

To use:
  post <msg>
    Sends <msg> to the twitter network.
    If <msg> is one of the twitter commands, it is sent raw, via the
        associated twitter user.
    If not, the IRC user's name is appended to <msg> and is then sent.

    The value of postConfirmation will be used as the confirmation
    for a successful post.

  mentions <number>
    Display latest <number> mentions.

  listfriends
    List followers.

  tweets
    Display latest page of tweets.

Automatic actions:
    Mentions
    The bot will automatically post mentions the channels in
    channelList. To disable this behaviour, set displayReplies to
    'False'

    Topic Snarfing
    If tweetTopicSnarf is enabled, newly seen segments of the topic will be
    auto-tweeted.


