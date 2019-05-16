#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import scraperwiki
import json

#Twitter API credentials
consumer_key = #You will need to get a consumer_key and put it here as a string
consumer_secret = #You will need to get one and put it here as a string
access_key = #You will need to get one and put it here as a string
access_secret = #You will need to get one and put it here as a string


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#This section of code gets members of a Twitter list
#from https://stackoverflow.com/questions/8058858/how-to-get-all-users-in-a-list-twitter-api
#Create empty dict to store results
meprecord = {}
#Create empty list to loop through
meplist = []
#Specify the user and list name - loop through the members of the list
for member in tweepy.Cursor(api.list_members, 'EPinUK', 'uk-meps-2014-19').items():
    memid = member
    #the _json part has the json in it. Then drill into the 'id' branch etc.
    print(memid._json['id'])
    print(memid._json['name'])
    print(memid._json['screen_name'])
    #Add to the empty list
    meplist.append(memid._json['screen_name'])
    #Store in the dict
    meprecord['id'] = memid._json['id']
    meprecord['name'] = memid._json['name']
    meprecord['screenname'] = memid._json['screen_name']
    #Save to the datastore
    scraperwiki.sql.save(['id'], meprecord, table_name='mepaccounts')

#Function to get the tweets for a given account
def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	#Better to be api = tweepy.API(auth, parser=JSONParser())
	#See http://stackoverflow.com/questions/14856526/parsing-twitter-json-object-in-python

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	print "oldest: ", oldest
	print "alltweets[0]: ", alltweets[0]
	#Converts first tweet to text
	#see http://stackoverflow.com/questions/27900451/convert-tweepy-status-object-into-json
	json_str = json.dumps(alltweets[0]._json)
	#CONVERT TO LOOP TO DO SAME TO ALL TWEETS
	record = {}
	print "len(alltweets)", len(alltweets)
	for tweet in alltweets:
	    print "type(tweet)", type(tweet)
	    json_str = json.dumps(tweet._json)
	    print "type(tweet) 2", type(json_str)
	    print "json_str:", json_str
	    #Split tweet on commas to create an array
	    tweetarray = json_str.split(', "')
	    #tweetid2 = json_str.split('/status/')[1].split('/')[0]
	    tweetid = json_str.split('"id": ')[1].split(',')[0]
	    tweettxt = json_str.split('"text": ')[1].split(', "is_quote_status"')[0]
	    tweetdate = json_str.split('"created_at": "')[2].split('", "')[0]
	    name = json_str.split('"name": "')[1].split('", "')[0]
	    screenname = json_str.split('"screen_name": "')[1].split('", "')[0]
	    tweeturl = "https://twitter.com/"+screenname+"/status/"+tweetid
	    record['tweetid'] = tweetid
	    record['tweettxt'] = tweettxt
	    record['tweetdate'] = tweetdate
	    record['name'] = name
	    record['screenname'] = screenname
	    #The screen name in the code is the name of the person who's tweet is being responded to, so we need to store the account we were searching
	    record['account'] = screen_name
	    record['tweeturl'] = tweeturl
	    print "record: ", record
	    scraperwiki.sql.save(['tweetid'], record, table_name=namethetablehere)

    #keep grabbing tweets until there are no tweets left to grab - comment this out if it's scheduled but uncomment if you want to start anew

	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		#all subsequent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweetss
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))
		#transform the tweepy tweets into a 2D array that will populate the csv
		#outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
		#need to convert to a dict before saving - could do it in the loop above rather than at end
		for tweet in alltweets:
		    print "type(tweet)", type(tweet)
		    json_str = json.dumps(tweet._json)
		    print "type(tweet) 2", type(json_str)
		    print "json_str:", json_str
		    tweetarray = json_str.split(', "')
		    tweetid = json_str.split('"id": ')[1].split(',')[0]
		    tweettxt = json_str.split('"text": ')[1].split(', "is_quote_status"')[0]
		    tweetdate = json_str.split('"created_at": "')[2].split('", "')[0]
		    name = json_str.split('"name": "')[1].split('", "')[0]
		    screenname = json_str.split('"screen_name": "')[1].split('", "')[0]
		    tweeturl = "https://twitter.com/"+screenname+"/status/"+tweetid
		    record['tweetid'] = tweetid
		    record['tweettxt'] = tweettxt
		    record['tweetdate'] = tweetdate
		    record['name'] = name
		    record['screenname'] = screenname
		    #The screen name in the code is the name of the person who's tweet is being responded to, so we need to store the account we were searching
		    record['account'] = screen_name
		    record['tweeturl'] = tweeturl
		    print "record: ", record
		    scraperwiki.sql.save(['tweetid'], record, table_name=namethetablehere)

#Here is the resulting list
meplist = [u'NosheenaMobarik', u'RMatthewsMEP', u'JProcterMEP', u'Janice4Brexit', u'Jane_CollinsMEP', u'DianeJamesMEP', u'AmjadBashirMEP', u'KaySwinburneMEP', u'GVOMEP', u'NathanGillMEP', u'Ashleyfoxmep', u'JohnFlackMEP', u'anthea_mcintyre', u'PaulBrannenNE', u'NeenaGmep', u'julie4nw', u'RCorbettMEP', u'IanDuncanHMG', u'WajidKhanMEP', u'JamesJimCarver', u'RichardAshMEP', u'CharlesTannock', u'JSeymourUKIP', u'JNicholsonMEP', u'TheresaMEP', u'LucyAndersonMEP', u'Claude_Moraes', u'Tim_Aker', u'MollyMEP', u'NirjDeva', u'Steven_Woolfe', u'catherinemep', u'GreenJeanMEP', u'Coburn4Brexit', u'DianeDoddsMEP', u'GreenKeithMEP', u'hudghtonmepSNP', u'juliegirling', u'GerardBattenMEP', u'ClareMoodyMEP', u'Afzal4Gorton', u'SHKMEP', u'M_AndersonSF', u'LindaMcAvanMEP', u'oflynnmep', u'billethmep', u'SyedKamall', u'MargotLJParker', u'davidmartinmep', u'JonathanArnott', u'RogerHelmerMEP', u'GlenisWillmott', u'JillEvansMEP', u'EmmaMcClarkin', u'DanielJHannan', u'DCBMEP', u'jfoster2019', u'SebDance', u'julia_reid', u'Jude_KD', u'ddalton40', u'JohnHowarth1958', u'AlynSmith', u'Rory_Palmer', u'alexlmayer', u'derekvaughan', u'maryhoneyball', u'MEPNeenaGill', u'Nigel_Farage', u'C_Stihler', u'sionsimon']
#the account 'GVOMEP' seems to cause a problem - it's because the account hasn't tweeted so it needs to be removed
meplist = [u'NosheenaMobarik', u'RMatthewsMEP', u'JProcterMEP', u'Janice4Brexit', u'Jane_CollinsMEP', u'DianeJamesMEP', u'AmjadBashirMEP', u'KaySwinburneMEP', u'NathanGillMEP', u'Ashleyfoxmep', u'JohnFlackMEP', u'anthea_mcintyre', u'PaulBrannenNE', u'NeenaGmep', u'julie4nw', u'RCorbettMEP', u'IanDuncanHMG', u'WajidKhanMEP', u'JamesJimCarver', u'RichardAshMEP', u'CharlesTannock', u'JSeymourUKIP', u'JNicholsonMEP', u'TheresaMEP', u'LucyAndersonMEP', u'Claude_Moraes', u'Tim_Aker', u'MollyMEP', u'NirjDeva', u'Steven_Woolfe', u'catherinemep', u'GreenJeanMEP', u'Coburn4Brexit', u'DianeDoddsMEP', u'GreenKeithMEP', u'hudghtonmepSNP', u'juliegirling', u'GerardBattenMEP', u'ClareMoodyMEP', u'Afzal4Gorton', u'SHKMEP', u'M_AndersonSF', u'LindaMcAvanMEP', u'oflynnmep', u'billethmep', u'SyedKamall', u'MargotLJParker', u'davidmartinmep', u'JonathanArnott', u'RogerHelmerMEP', u'GlenisWillmott', u'JillEvansMEP', u'EmmaMcClarkin', u'DanielJHannan', u'DCBMEP', u'jfoster2019', u'SebDance', u'julia_reid', u'Jude_KD', u'ddalton40', u'JohnHowarth1958', u'AlynSmith', u'Rory_Palmer', u'alexlmayer', u'derekvaughan', u'maryhoneyball', u'MEPNeenaGill', u'Nigel_Farage', u'C_Stihler', u'sionsimon']
#There are two more missing:
moremeps = ['JonathanMEP','mikehookemMEP']
#Add those at the front of the list
meplist = ['JonathanMEP','mikehookemMEP',u'NosheenaMobarik', u'RMatthewsMEP', u'JProcterMEP', u'Janice4Brexit', u'Jane_CollinsMEP', u'DianeJamesMEP', u'AmjadBashirMEP', u'KaySwinburneMEP', u'NathanGillMEP', u'Ashleyfoxmep', u'JohnFlackMEP', u'anthea_mcintyre', u'PaulBrannenNE', u'NeenaGmep', u'julie4nw', u'RCorbettMEP', u'IanDuncanHMG', u'WajidKhanMEP', u'JamesJimCarver', u'RichardAshMEP', u'CharlesTannock', u'JSeymourUKIP', u'JNicholsonMEP', u'TheresaMEP', u'LucyAndersonMEP', u'Claude_Moraes', u'Tim_Aker', u'MollyMEP', u'NirjDeva', u'Steven_Woolfe', u'catherinemep', u'GreenJeanMEP', u'Coburn4Brexit', u'DianeDoddsMEP', u'GreenKeithMEP', u'hudghtonmepSNP', u'juliegirling', u'GerardBattenMEP', u'ClareMoodyMEP', u'Afzal4Gorton', u'SHKMEP', u'M_AndersonSF', u'LindaMcAvanMEP', u'oflynnmep', u'billethmep', u'SyedKamall', u'MargotLJParker', u'davidmartinmep', u'JonathanArnott', u'RogerHelmerMEP', u'GlenisWillmott', u'JillEvansMEP', u'EmmaMcClarkin', u'DanielJHannan', u'DCBMEP', u'jfoster2019', u'SebDance', u'julia_reid', u'Jude_KD', u'ddalton40', u'JohnHowarth1958', u'AlynSmith', u'Rory_Palmer', u'alexlmayer', u'derekvaughan', u'maryhoneyball', u'MEPNeenaGill', u'Nigel_Farage', u'C_Stihler', u'sionsimon']
print(meplist)
#It runs out of time on SHKMEP so we need to find that index and run from there
#print(meplist.index('SHKMEP'))

#Run the functions above in a loop
for account in meplist:
    if __name__ == '__main__':
    	#pass in the username of the account you want to download
    	get_all_tweets(account)
