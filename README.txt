SupyBot Twitter Plugin
======================

This is a twitter plugin for supybot. It can post to twitter, and show your
friend list. It will add (ircnick) after tweets. We use it to post to an
organizational twitter account from our channel.

This code is forked from
http://code.google.com/p/supybot-twitter which has not been
updated in a long time. This version has been updated to post using the new
twitter API (and so, works, again)

This plugin uses the Twitter API from http://code.google.com/p/python-twitter/
so it must be installed and available for use.

It can be installed via pip like so:

    pip install python-twitter

To use:
  !post <msg>
    Sends <msg> to the twitter network.
    If <msg> is one of the twitter commands, it is sent raw, via the
    	associated twitter user.
    If not, the IRC user's name is appended to <msg> and is then sent.

