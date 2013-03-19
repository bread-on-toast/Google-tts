#!/usr/bin/python
# -*- coding: utf-8 -*-

# by breadontoast

import os 
import sys


lines = [line.strip() for line in open('input')]
print lines
input=""
for i in lines:
	input=input+i

#input text

# first part creates the outputfile
def getf(i):
        os.system("curl -A 'Mozilla' 'http://translate.google.com/translate_tts?tl=de&q="+i+"' > out.mp3")
#gets spoken text and append to outputfile
def get(i):
	os.system("curl -A 'Mozilla' 'http://translate.google.com/translate_tts?tl=de&q="+i+"' > tmp.mp3")
	os.system("cat out.mp3 tmp.mp3 > out1.mp3")
	os.system("mv out1.mp3 out.mp3")
	os.system("rm tmp.mp3")

#gets size of string, important because google tts only allows texts smaler than 100 chars
def size(a):
	n=0
	for i in a:
		n=n+1
	return n

#for german language replaces Umlaute
input=input.replace("Ü","Ue")
input=input.replace("Ä","Ae")
input=input.replace("Ö","Oe")
input=input.replace("ß","ss")
input=input.replace("ü","ue")
input=input.replace("ä","ae")
input=input.replace("ö","oe")

input=input.replace("’","")
input=input.replace("\"","")

#seperate words
tts=input.split(" ")

out=""
start=1
for i in tts:
	#fills out until is max 100 chars long
	if size(out)+size(i)<101:
		out=out+"+"+i
	else:
		if start==1:
			getf(out)
			out=i+"+"
			start=0
		else:
			get(out)
			out=i+"+"
get(out)#if out not empty


