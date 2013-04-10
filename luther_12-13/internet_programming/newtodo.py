#!/usr/local/bin/python

# When running on knuth, switch the shebang to #!/usr/local/bin/python

import yaml
import cgitb
import os
import urlparse
from datetime import datetime

cgitb.enable()

f = open('todo.dat','r')
d = yaml.load(f)

print "Content-type: text/html" #important to tell the browser what kind of data is coming
print "\n\n" #important to also separate by a pair of newline char's

print '''<html>
<head>
<title>To Do List</title>
</head>
<body>'''

# The header of the todo page
print '''<div id="header">
<h1>To Do List</h1>
</div>'''

# The div that prints out the current todo list
task_list = "<div id='content'>\n"

print "<form name='delete_item' action='newtodo.cgi' method='GET'>"
for project,tasks in d.iteritems():
    task_list += "<h2>" + str(project) + "</h2>"
    for iden,item in tasks.iteritems():
        task_list += '''<h3>%(task)s</h3>'''
print task_list + "\n<input type='submit' value='Update List'/></form>" + str(d) + "</div>"

# The div that the form for creating a new task is placed
print '''<div id="new_task">
    <form name="new_item" action="todo.cgi" method="GET" onsubmit="return validateForm();">
        New To Do Item<br>
        Title: <input type="text" name="title"/><br>
        Description: <input type="text" name="description" size="50"/><br>
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