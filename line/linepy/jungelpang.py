# -*- coding: utf-8 -*-
from datetime import datetime
from .channel import Channel

import json, time, base64

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin

class Jungelpang(Channel):

    def __init__(self):
        Channel.__init__(self, self.channel, self.server.CHANNEL_ID['JUNGEL_PANG'], False)
        self.jp = self.getChannelResult()
        self.jpToken = self.getChannelResult().token
        self.__loginJungelpang()

    def __loginJungelpang(self):
        self.server.setJungelpangHeadersWithDict({
            'Content-Type': 'application/json',
            'User-Agent': self.server.USER_AGENT,
        })
        self.profileDetail = self.getProfileDetail()

    """Jungelpang"""

    @loggedIn
    def postJungelpang(self, to, messages=[]):
        data = {
            "cc": self.jpToken,
            "to": to,
            "messages": messages
        }
        data = json.dumps(data)
        sendPost = self.server.postContent(self.server.LINE_JUNGEL_PANG, data=data, headers=self.server.jungelpangHeaders)
        return sendPost.json()