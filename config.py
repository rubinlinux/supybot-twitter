###
# Copyright (c) 2007-2012, Andy Berdan, Henry Donnay
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    Twitter = conf.registerPlugin('Twitter', True)
    consumer_key = something("twitter.com consumer key:");
    Twitter.consumer_key.setValue(consumer_key)
    consumer_secret = something("twitter.com consumer secret:");
    Twitter.consumer_secret.setValue(consumer_secret)

    access_key = something("twitter.com access token:");
    Twitter.access_key.setValue(access_key)
    access_secret = something("twitter.com access token secret:");
    Twitter.access_secret.setValue(access_secret)

Twitter = conf.registerPlugin('Twitter')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Twitter, 'someConfigVariableName',
#     registry.Boolean(False, """Help for someConfigVariableName."""))
conf.registerChannelValue(Twitter, 'enabled',
        registry.Boolean(False, 'Enable this plugin'))
conf.registerChannelValue(Twitter, 'tweetTopicSnarf', 
        registry.Boolean(False, 'Snarf new segments of the topic, and tweet them'))
conf.registerGlobalValue(Twitter, 'consumer_key',
        registry.String('', "twitter.com consumer_key", private=True))
conf.registerGlobalValue(Twitter, 'consumer_secret',
        registry.String('', "twitter.com consumer_secret", private=True))
conf.registerGlobalValue(Twitter, 'access_key',
        registry.String('', "twitter.com access_key", private=True))
conf.registerGlobalValue(Twitter, 'access_secret',
        registry.String('', "twitter.com access_secret", private=True))
conf.registerGlobalValue(Twitter, 'displayReplies',
        registry.Boolean(True, "Automatically display replies?", private=False))
conf.registerGlobalValue(Twitter, 'replyAnnounceMsg',
        registry.String("Here's what Twitter has to say:", "String to use when announcing replies.", private=False))
conf.registerGlobalValue(Twitter, 'postConfirmation',
        registry.String("Posted.", "String to use when confirming a post", private=False))
conf.registerGlobalValue(Twitter, 'channelList',
        registry.String("", "List of channels to broadcast in.", private=False))

# vim:set shiftwidth=4 tabstop=4 expandtab:
