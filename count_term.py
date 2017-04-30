#!/usr/bin/python
# -*- coding: UTF-8 -*-

import operator 
import json
from collections import Counter
import re

import xlwt

search_words = {'พร้อมส่ง','Pre','฿','DM','Line','ส่งฟรี','#ถูกบอกต่อ','#พื้นที่ขายของ','Preorder','บาท','ราคา','เดม','ขาย','โปร','นัดรับ','ค่าส่ง','สำหรับลูกค้า','รับส่วนลด','รวมส่ง','สนใจสอบถาม','นัดรับ','โปรโมชั่น','#ถูกบอกต่อ','#พรีออเดอร์','#ชี้เป้าโปรถูก','ยินดีคืนเงิน','inbox','โอน','ลด','สนใจเมนชั่น','#ripไอดอ','#ชี้เป้าโปรถูก'}
review_words = {}

# fname = 'data/stream__howtoperfect.json'
fname = 'dataOld/stream_#howtoperfect.json'
saler_counter = 0



book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(saler_counter, 0, "text")
sheet1.write(saler_counter, 1, "fav_count")
sheet1.write(saler_counter, 2, "retweet_count")
with open(fname, 'r') as f:
	# count_all = Counter()
	for line in f:
		# isFound = False
		tweet = json.loads(line)
		# for search_word in search_words:
		# 	if (tweet['text'].encode('utf-8')).find(search_word) != -1 :
		# 		isFound = True
		# 	# o.write((tweet['text']+'\n').encode('utf-8'))
		# 		# o.write(json.dumps(tweet, indent=4))
		# 		saler_counter = saler_counter+1
		# 		break	# if find search words,break loop
		# if isFound:
			# fav_count = tweet['quoted_status']['favorite_count']
			# retweet_count = tweet['quoted_status']['retweet_count']
			# o.write(json.dumps(tweet, indent=4))
			# # o.write(tweet['entities']['urls'][0]['url'])
			# if tweet['quoted_status']['entities']['urls'] == []:
			# 	url = tweet['quoted_status']['entities']['media'][0]['url']
			# # elif tweet['quoted_status']['entities']['urls'][0]['url'] == "":
			# # 	print tweet['quoted_status']['entities']['media'][0]['url']
			# else :
			# 	url = tweet['quoted_status']['entities']['urls'][0]['url']
		saler_counter = saler_counter+1
		fav_count = tweet['favorite_count']
		retweet_count = tweet['retweet_count']
		text = tweet['text'].encode('utf-8')

		# print url
		# print fav_count
		# print retweet_count

		sheet1.write(saler_counter, 0, text)
		sheet1.write(saler_counter, 1, fav_count)
		sheet1.write(saler_counter, 2, retweet_count)

	print saler_counter
	book.save("trial2.xls")
	        # terms_all = [term for term in tweet['text']]

	        # for term in tweet['text']:
	        # 	if term = 'te':
	        # 		print term

	        # Update the counter