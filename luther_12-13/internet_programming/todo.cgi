#!/usr/local/bin/python

# When running on knuth, switch the shebang to #!/usr/local/bin/python

import yaml
import cgitb
import os
import urlparse
from datetime import datetime

cgitb.enable()

data = urlparse.parse_qs(os.environ['QUERY_STRING'])

# Checking the query string to see if an entry is being deleted or inserted
if data != {}:
  # Opening the yaml file
  f = open('todo.dat','r')
  d = yaml.load(f)
  f.close()
  # Checking to see if a list item is being deleted
  if 'delete_item' in data.keys():
    if data != {}:
      for i in data['delete_item']:
        x = i.split("&")
        category = x[0]
        iden = x[1]
        del d[category][iden] #Deletes the selected item from the yaml file
  else:
    yaml_id = str(datetime.now()).replace(" ","-")

    data = eval(str(data))
    print data
    for key,value in data.iteritems():
        data[key] = value[0]

    date = "%s/%s/%s" % (data["month"],data["day"],data["year"])
    task = {'description' : data['description'], 'due' : date, 'priority': data['priority'], 'task' : data['title']}
    d[data['category']][yaml_id] = task

  f = open('todo.dat','w')
  f.write(yaml.dump(d))
  f.close()

f = open('todo.dat','r')
d = yaml.load(f)

date = datetime.now()

print "Content-type: text/html" #important to tell the browser what kind of data is coming
print "\n\n" #important to also separate by a pair of newline char's

print '''<html>
<head>
<title>To Do List</title>
<link rel="stylesheet" href="todo.css">
<script type="text/javascript" src="main.js"></script>
</head>
<body>'''

# The header of the todo page
print '''<div id="header">
<h1>To Do List</h1>
</div>'''

# The div that prints out the current todo list
task_list = "<div id='content'>\n"

print "<form name='delete_item' action='todo.cgi' method='GET'>"
for project,tasks in d.iteritems():
    task_list += "<h2>" + str(project) + "</h2>"
    for iden,item in tasks.iteritems():
        date_split = item['due'].split("/")
        if int(date_split[2]) > date.year:
          task_list += "<span class='" + str(item['priority']) + "'>"
        elif int(date_split[2]) < date.year:
          task_list += "<span class='overdue'>"
        elif int(date_split[0]) > date.month:
          task_list += "<span class='" + str(item['priority']) + "'>"
        elif int(date_split[0]) < date.month:
          task_list += "<span class='overdue'>"
        elif int(date_split[1]) >= date.day:
          task_list += "<span class='" + str(item['priority']) + "'>"
        else:
          task_list += "<span class='overdue'>"
        task_list += '''<h3>%(task)s</h3>
        <ul>
            <li>Description: %(description)s</li>
            <li>Due Date: %(due)s</li>
            <li>Priority: %(priority)s</li>
	    <li>Delete?: <input type="checkbox" name="delete_item" value=''' %item + str(project)+'&'+str(iden) + ''' id="''' + str(iden) + '''"  onclick="isChecked(this);"></input></li>
        </ul>
        </span>'''
print task_list + "\n<input type='submit' value='Update List'/></form></div>"

# The div that the form for creating a new task is placed
print '''<div id="new_task">
    <form name="new_item" action="todo.cgi" method="GET" onsubmit="return validateForm();">
        New To Do Item<br>
        Title: <input type="text" name="title"/><br>
        Description: <input type="text" name="description" size="50"/><br>
        Due Date: <input type="text" name="month" size="1"/> / <input type="text" name="day" size="1"/> / <input type="text" name="year" size="3" value="2013"/><br>
        Priority: <select name="priority" value="Normal">
            <option value="Low">Low</option>
            <option value="Normal">Normal</option>
            <option value="High">High</option>
        </select><br>
        Category: <select name="category">
            <option value="School">School</option>
            <option value="Work">Work</option>
            <option value="Other">Other</option>
        </select><br><br>
        <input type="submit" value="Add Task"/>
    <form>
</div>'''

print '''</body>
</html>'''
