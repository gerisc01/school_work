#!/usr/local/bin/python

import sys
import os
sys.path.insert(0,os.path.abspath("/home/students/gerisc01/bin/lib/python"))
sys.path.insert(0,os.path.abspath("/home/students/gerisc01/bin/lib/python/evernote-1.23.2-py2.7.egg"))
sys.path.insert(0,os.path.abspath("/home/students/gerisc01/bin/lib/python/oauth2-1.5.211-py2.7.egg"))

import urllib
import urllib2
import json
import yaml
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
from evernote.edam.notestore.ttypes import NoteFilter

print "Content-type: text/html" #important to tell the browser what kind of data is coming
print "\n\n" #important to also separate by a pair of newline char's

def authenticate_evernote():
	evernote_dev_token = 'S=s317:U=2a12764:E=14524e2f945:C=13dcd31cd47:P=1cd:A=en-devtoken:V=2:H=4ae170cd15a53f88d0b2150c23fcae0b'
	note_store_url = 'https://www.evernote.com/shard/s317/notestore'

	return EvernoteClient(token=evernote_dev_token,sandbox=False)

def authenticate_google():
	url = 'https://accounts.google.com/o/oauth2/token'
	refTok = '1/LoAFyOW3YqRKT5dmUF7bppHQPcc8H3J3UqowY_mrJ1U'

	params = urllib.urlencode({
	  'client_id': '89402054840.apps.googleusercontent.com',
	  'client_secret': 'xCwi9nr33u4hl1lKSWSImq53',
	  'refresh_token':refTok,
	  'grant_type':'refresh_token'
	})
	response = urllib2.urlopen(url, params).read()

	loaded = json.loads(response)
	access_token = loaded['access_token']
	return access_token

def get_google_lists(auth):
	request = urllib2.Request("https://www.googleapis.com/tasks/v1/users/@me/lists")
	request.add_header("Authorization",auth)

	task_lists = urllib2.urlopen(request).read()
	list_dict = json.loads(task_lists)
	lists = [[],[]]
	for i in list_dict['items']:
		lists[0].append(i['title'])
		lists[1].append(i['id'])
	return lists

def get_evernote_lists(client,notestore):
	notebooks = noteStore.listNotebooks()
	lists =[]
	for n in notebooks:
		lists.append(n.name)
	return lists

def iterate_through_google(google_lists,noteStore):
	eDict = get_evernote_list_items(noteStore)
	for i in range(len(google_lists[1])):
		gList = get_google_list_items(google_lists[1][i])
		eList = eDict[google_lists[0][i]]
		for i in gList:
			if i not in eList:
				if i != '':
					create_evernote_list_item(noteStore,eList[0],i)


def get_google_list_items(guid):
	url = "https://www.googleapis.com/tasks/v1/lists/%s/tasks" % guid
	request = urllib2.Request(url)
	request.add_header("Authorization",auth)

	task_lists = urllib2.urlopen(request).read()
	list_dict = json.loads(task_lists)
	items = []
	if 'items' in list_dict:
		for i in list_dict['items']:
			items.append(i['title'])
	return items

def get_evernote_list_items(noteStore):
	evernote_dev_token = 'S=s317:U=2a12764:E=14524e2f945:C=13dcd31cd47:P=1cd:A=en-devtoken:V=2:H=4ae170cd15a53f88d0b2150c23fcae0b'
	dict = {}
	notebooks = noteStore.listNotebooks()
	for i in notebooks:
		filter = NoteFilter()
		filter.notebookGuid = i.guid
		notes = noteStore.findNotes(evernote_dev_token,filter,0,100)
		notebook_name = ''
		if i.name == "gophersbball17's notebook":
			notebook_name = "testing55318's list"
		else:
			notebook_name = i.name
		note_names = [i.guid]
		for n in notes.notes:
			note_names.append(n.title)
		dict[notebook_name] = note_names
	return dict

def delete_items(localDict,noteStore,google_lists,google_auth):
	eDict = get_evernote_list_items(noteStore)
	notebooks = noteStore.listNotebooks()
	for k,v in localDict.iteritems():
		if v != []:
			if k == "Default":
			   localList = eDict["testing55318's list"]
			else:
			   localList = eDict[k]
			for i in range(1,len(localList)):
				if localList[i] not in v:
					filter = NoteFilter()
					filter.words = localList[i]
					delete_evernote_item(filter,noteStore)

	for i in range(len(google_lists[1])):
		url = "https://www.googleapis.com/tasks/v1/lists/%s/tasks" % google_lists[1][i]
		request = urllib2.Request(url)
		request.add_header("Authorization",google_auth)

		task_lists = urllib2.urlopen(request).read()
		list_dict = json.loads(task_lists)
		gList = get_google_list_items(google_lists[1][i])
		eList = eDict[google_lists[0][i]]
		for j in gList:
			if j not in eList:
				if j != '':
					delete_google_list_item(google_lists[1][i],list_dict,j,google_auth)

def delete_evernote_item(filter,noteStore):
	evernote_dev_token = 'S=s317:U=2a12764:E=14524e2f945:C=13dcd31cd47:P=1cd:A=en-devtoken:V=2:H=4ae170cd15a53f88d0b2150c23fcae0b'
	notes = noteStore.findNotes(evernote_dev_token,filter,0,100)
	for n in notes.notes:
		noteStore.deleteNote(evernote_dev_token,n.guid)

def delete_google_list_item(listGUID,task_dict,word,auth):
	for i in task_dict['items']:
		if word == i['title']:
			url = "https://www.googleapis.com/tasks/v1/lists/%s/tasks/%s" % (listGUID,i['id'])
			opener = urllib2.build_opener(urllib2.HTTPHandler)
			request = urllib2.Request(url)
			request.add_header("Authorization",auth)
			request.get_method = lambda: 'DELETE'
			url = opener.open(request)

client = authenticate_evernote()
noteStore = client.get_note_store()

access_token = authenticate_google()

auth = "Bearer "
auth += str(access_token)

google_lists = get_google_lists(auth)
evernote_lists = get_evernote_lists(client,noteStore)
title_list = google_lists[0]

f = open('newtodo.dat','r')
localDict = yaml.load(f)
delete_items(localDict,noteStore,google_lists,auth)