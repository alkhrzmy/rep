# -*- coding: utf-8 -*-

import json
import telepot
import requests
from humanfriendly import format_timespan, format_size, format_number, format_length
from telepot.loop import MessageLoop
import time

bot = telepot.Bot('764533501:AAGE2qq8gedHAlXq-tnjfwPGyd-y2jxSn5c')
programStart = time.time()

my_id = '694351915'

def handle(self):
        content_type, chat_type, chat_id= telepot.glance(self)
        command = self['text'].strip().lower()
        if content_type == 'text' and chat_type == 'private':
                url = 'https://secureapp.simsimi.com/v1/simsimi/talkset?uid=271898762&av=6.8.7.1&lc=id&cc=ID&tz=Asia%2FJakarta&os=a&ak=alofKTlYS08reLe4gzCD2W7mijs%3D&message_sentence='+self['text']+'&normalProb=2&isFilter=1&talkCnt=1&talkCntTotal=1&reqFilter=0&session=udu6auK1LfyAQwLzupMPbdKVYDX9HkLnkYkU4jPWFmX6MysmRf6uFqg5RhqqVzVjKixAJaoNuxLi1YNFjLrs2Qu3&triggerKeywords=%5B%5D'
                headers = {
                        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_A007 Build/MMB29P)',
                        'Host': 'secureapp.simsimi.com',
                        'Connection': 'Keep-Alive',
                        'Accept-Encoding': 'gzip'
                }

                r = requests.get(url, headers=headers)
                thedata = json.loads(r.text)
                bot.sendMessage(chat_id, thedata['simsimi_talk_set']['answers'][0]['sentence'])
        elif command == '/check':
                timing = time.time()
                elapseTime = time.time() - timing
                elapseStart = time.time() - programStart
                bot.sendMessage(chat_id, 'Bot already running ' + format_timespan(elapseStart) + '\nBot send message speed %f'%elapseTime)
        else:
                pass
MessageLoop(bot, handle).run_as_thread()
print ('Running...')
# Keep the program running.
while 1:
    time.sleep(1)
