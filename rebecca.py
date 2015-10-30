#!/usr/bin/python
# -*- coding: utf-8 -*-

import rbbot
from pprint import pprint
import datetime
import signal
import time
import ConfigParser
from random import randint
import urllib2
import io
from isodate import parse_duration
from time import strftime
from time import gmtime

with open("config.ini") as f:
	config = f.read()
cfg = ConfigParser.RawConfigParser()
cfg.readfp(io.BytesIO(config))

### IRC INFO
server = cfg.get('becky','server')
port = int(cfg.get('becky','port'))
bot = rbbot.RBbot(server,port)
channel= cfg.get('becky','channel')
botnick= cfg.get('becky','botnick')
password= cfg.get('becky','password')

### TWEET INFO
urljs = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=officialjaden&count=200&include_rts=false"
urlrb = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=MsRebeccaBlack&count=100&include_rts=false"
urlrb1 = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=MsRebeccaBlack&count=1&include_rts=false"
key = cfg.get('becky','key')
secret = cfg.get('becky','secret')
ytkey = cfg.get('becky','ytkey')
urlyt = "https://www.googleapis.com/youtube/v3/search?safeSearch=none&part=snippet&type=video&maxResults=1&key="+ytkey+"&q="
ytstats = "https://www.googleapis.com/youtube/v3/videos?part=statistics,contentDetails&key="+ytkey+"&id="

### SET NICK AND JOIN CHANNEL
bot.set_nick(botnick,password)
bot.join(channel)
#bot.join(channel2)

### GET THE TWEET
tweetObject = rbbot.Tweets()
tweetrb = tweetObject.getTweet(urlrb,key,secret)
tweetrb1 = tweetObject.getTweet(urlrb1,key,secret)
tweetjs = tweetObject.getTweet(urljs,key,secret)


### RATE LIMITING
rate = 1.0
per = 2.0
allowance = rate;
last_check=time.time()
tweet_check = time.time() 
apiObject = rbbot.apis()

def cunt(text):
	t = text.split()
	t1=t[0]
	to = t1[1:t1.index('!')].strip()
	return to
	
def mysplit(s):
	words = []
	inword = 0
	for c in s:
		if c in " \r\n\t": # whitespace
			inword = 0
		elif not inword:
			words = words + [c]
			inword = 1
		else:
			words[-1] = words[-1] + c
	return words

### START
while bot.connected == True:
	signal.signal(signal.SIGINT, bot.exitGracefully)
	current = time.time()
	time_passed = current - tweet_check
	time_passedS = current - last_check
	if (time_passed > 14400):
		tweet_check = current
		tweetrb = tweetObject.getTweet(urlrb,key,secret)
		tweetjs = tweetObject.getTweet(urljs,key,secret)

	text=bot.ircsock.recv(2048)
	print (text)
	if text.find("JOIN "+channel) != -1 and cunt(text) != "rebeccablack":
			time.sleep(1)
			bot.messg("lil bish "+cunt(text),"g")
	if text.find("PRIVMSG "+channel) != -1:
			if text.find("jaden") != -1 or text.find("JADEN") != -1:
				try: 
					if cunt(text).lower() != "shoh":
						#bot.messg(tweetjs,"t")
						gif = apiObject.getAPI("sad")
						bot.messg(gif,"a")
				except ValueError:
					print("value error on cunt")
			if text.find("tell me more becky") != -1:
				if cunt(text).lower() != "shoh":
					bot.messg(tweetrb,"t")
			if text.find("rebecca tell me stuff") != -1:
				if cunt(text).lower() != "shoh":
					bot.messg(tweetrb1,"t")

			if text.lower().find("fuck you ") != -1 or text.lower().find("fuck off ") != -1:
				last_check=current
				allowance += time_passedS * (rate / per)
				if (allowance > rate):
					allowance = rate;
				if (allowance < 1.0):
					print "allowance under 1"
					bot.messg("av it u slag","g")
				else:
					try:
						s=text.split()
						s1=s[3:]
						bot.messg(cunt(text)+", "+s1[2]+" feels offended by your recent action(s). Please read http://stop-irc-bullying.eu/stop","g")
						allowance -= 1.0
					except IndexError:
						bot.messg("suttin is a cunt","g")

			if text.find("rektasdasdasdas") != -1:
				try: 
					gif = apiObject.getAPI("fuck+you")
					bot.messg(gif,"a")
				except ValueError:
					print("value error on cunt")
			
			if text.find("relt") != -1:
				try: 
					gif = apiObject.getAPI("laugh")
					bot.messg(gif,"a")
				except ValueError:
					print("value error on cunt")

			if text.find("IS IT FRIDAY") != -1:
				last_check=current
				allowance += time_passedS * (rate / per)
				if (allowance > rate):
					allowance = rate;
				if (allowance < 1.0):
					print "allowance under 1"
					bot.messg("av it u slag","g")
				else:
					cunts = cunt(text).lower()
					if cunts != "dong" or cunts != "dongerdong":
						#bot.messg('yes it is '+cunts,"g")
						bot.messg(datetime.datetime.now(),"YT")
						time.sleep(randint(1,3))
						bot.messg('lil bish '+cunt(text),"g")
					allowance -= 1.0

			if text.find(":.yt ") != -1 or text.find(":.YT ") != -1:
				last_check=current
				allowance += time_passedS * (rate / per)
				if (allowance > rate):
					allowance = rate;
				if (allowance < 1.0):
					print "allowance under 1"
					bot.messg("av it u slag","g")
				else:
					cunts = cunt(text).lower()
					if cunts == "shoh" or cunts == "felda" or cunts == "dong" or cunts == "dongerdong" or cunts == "rebeccablack" or cunts == "stulander":
						bot.messg("yer a cunt harry","g")
					else:
						line = text.lower()[text.lower().index(":.yt"):].split()
						searchterm = []
						searchterm = "+".join(line[1:]).strip()
						if searchterm:
							urlytube = urlyt+searchterm
							urlytube = urlytube.translate(None,'!#$@%*')
							result = apiObject.getYT(urlytube)
							try:
								yts = ytstats+result["items"][0]["id"]["videoId"]
								stats = apiObject.getYT(yts)
								dur = strftime('%M:%S',gmtime(parse_duration(stats["items"][0]["contentDetails"]["duration"]).seconds))
								tellthecunts = result["items"][0]["snippet"]["title"]+" ("+dur+") by "+result["items"][0]["snippet"]["channelTitle"]+" -> Views: "+"{:,}".format(int(stats["items"][0]["statistics"]["viewCount"]))+" | L/D: "+stats["items"][0]["statistics"]["likeCount"]+"/"+stats["items"][0]["statistics"]["dislikeCount"]+" -> https://youtu.be/"+result["items"][0]["id"]["videoId"]
								bot.messg(tellthecunts,"g")
							except (IndexError, urllib2.HTTPError) as e:
								bot.messg("can't find your shit video","g")

						allowance -= 1.0
			
			if text.lower().find("is it friday") != -1 and text.find("IS IT FRIDAY") == -1:
				last_check=current
				allowance += time_passedS * (rate / per)
				if (allowance > rate):
					allowance = rate;
				if (allowance < 1.0):
					print "allowance under 1"
					bot.messg("av it u slag","g")
				else:
					cunts = cunt(text).lower()
					if cunts == "dong" or cunts == "dongerdong":
						bot.messg("yer a cunt harry","g")
					else:
						#bot.messg('yes it is '+cunts,"g")
						bot.messg(datetime.datetime.now(),"yt")
						time.sleep(randint(1,3))
						bot.messg('lil bish '+cunt(text),"g")

					allowance -= 1.0
			if text.lower().find ("just do it") != -1 or text.lower().find ("let your dreams be dreams") != -1:
				bot.messg("http://i.imgur.com/vpUhtN0.gif","g")
			if text.find ("help me becky") != -1:
				helpmenu = "tell me more becky, rebecca tell me stuff, is it friday, rekt, relt, jaden, .yt"
				bot.messg("talk to me like one of your french girls","g")
				bot.messg(helpmenu,"g")
	if text.find ( 'PING' ) != -1:
		bot.messg(text.split()[1],"p")
