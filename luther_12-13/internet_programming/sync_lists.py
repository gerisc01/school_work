import urllib
import urllib2
import json
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
from evernote.edam.notestore.ttypes import NoteFilter

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

def create_google_list(auth,title):
	data = {"title":title}
	data = json.dumps(data)

	request = urllib2.Request("https://www.googleapis.com/tasks/v1/users/@me/lists",data)
	request.add_header("Authorization",auth)
	request.add_header("Content-Type",'application/json')

	f = urllib2.urlopen(request)
	response = f.read()
	f.close()

def create_evernote_list(client,noteStore,title):
	noteStore = client.get_note_store()
	notebook = Types.Notebook()
	notebook.name = title
	notebook = noteStore.createNotebook(notebook)

def iterate_through_evernote(evernote_lists,noteStore,google_lists,google_auth):
	evernote_dev_token = 'S=s317:U=2a12764:E=14524e2f945:C=13dcd31cd47:P=1cd:A=en-devtoken:V=2:H=4ae170cd15a53f88d0b2150c23fcae0b'
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
		google_guid = google_lists[1][google_lists[0].index(notebook_name)]
		gList = get_google_list_items(google_guid)
		for n in notes.notes:
			if n.title not in gList:
				create_google_list_item(google_guid,n.title,google_auth)

def iterate_through_google(google_lists,noteStore):
	eDict = get_evernote_list_items(noteStore)
	for i in range(len(google_lists[1])):
		gList = get_google_list_items(google_lists[1][i])
		eList = eDict[google_lists[0][i]]
		for i in gList:
			if i not in eList:
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

def create_google_list_item(guid,title,auth):
	url = "https://www.googleapis.com/tasks/v1/lists/%s/tasks" % guid
	data = {"title":title}
	data = json.dumps(data)

	request = urllib2.Request(url,data)
	request.add_header("Authorization",auth)
	request.add_header("Content-Type",'application/json')

	f = urllib2.urlopen(request)
	response = f.read()
	f.close()

def create_evernote_list_item(noteStore,guid,title):
	evernote_dev_token = 'S=s317:U=2a12764:E=14524e2f945:C=13dcd31cd47:P=1cd:A=en-devtoken:V=2:H=4ae170cd15a53f88d0b2150c23fcae0b'
	note = Types.Note()
	note.title = title
	note.notebookGuid = guid
	noteStore.createNote(evernote_dev_token,note)


client = authenticate_evernote()
noteStore = client.get_note_store()

access_token = authenticate_google()

auth = "Bearer "
auth += str(access_token)

google_lists = get_google_lists(auth)
evernote_lists = get_evernote_lists(client,noteStore)
title_list = google_lists[0]

# checking google lists to see if cooresponding evernote list exists
for i in title_list:
	if i not in evernote_lists:
		if i != "testing55318's list":
			create_evernote_list(client,noteStore,str(i))

# checking evernote lists to see if cooresponding google list exists
for i in evernote_lists:
	if i not in title_list:
		if i != "gophersbball17's notebook":
			create_google_list(auth,str(i))

iterate_through_evernote(evernote_lists,noteStore,google_lists,auth)
iterate_through_google(google_lists,noteStore)
