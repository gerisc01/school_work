#!/usr/local/bin/python

# When running on knuth, switch the shebang to #!/usr/local/bin/python

import yaml
import cgitb
import os
import urlparse
from datetime import datetime

cgitb.enable()

data = urlparse.parse_qs(os.environ['QUERY_STRING'])

f = open('newtodo.dat','r')
d = yaml.load(f)

print "Content-type: text/html" #important to tell the browser what kind of data is coming
print "\n\n" #important to also separate by a pair of newline char's

print '''<html>
<head>
<title>To Do List</title>
<link rel="stylesheet" href="todo.css">
<script type="text/javascript" src="sync.js"></script>'''

if data != {}:
  if 'delete_item' in data.keys():
    if data != {}:
      for i in data['delete_item']:
        x = i.split("&")
        category = x[0]
        iden = x[1]
        index = d[category].index(iden) 
        d[category].pop(index) #Deletes the selected item from the yaml file
        f = open('newtodo.dat','w')
        f.write(yaml.dump(d))
        f.close()

        print '''<script src='//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js'></script>
        <script>
        $.ajax({
        type:'get',
        url:'http://knuth.luther.edu/~gerisc01/delete.cgi',
        success:function(data) {
            window.location.replace("http://knuth.luther.edu/~gerisc01/newtodo.cgi");
        }
        });</script>'''
  else:
    data = eval(str(data))
    print type(data)
    if data['category'][0] in d:
      d[data['category'][0]] += data['title']
    else:
      d[data['category'][0]] = data['title']
    f = open('newtodo.dat','w')
    f.write(yaml.dump(d))
    f.close()

    print '''<script src='//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js'></script>
    <script>
    $.ajax({
    type:'get',
    url:'http://knuth.luther.edu/~gerisc01/add.cgi',
    success:function(data) {
        window.location.replace("http://knuth.luther.edu/~gerisc01/newtodo.cgi");
    }
    });</script>'''
    

  f = open('newtodo.dat','w')
  f.write(yaml.dump(d))
  f.close()

print'''</head>
<body>'''

# The header of the todo page
print '''<div id="header">
<h1>To Do List</h1>
</div>'''

# The div that prints out the current todo list
task_list = "<div id='content'>\n"

print "<form name='delete_item' action='newtodo.cgi' method='GET'>"
for project,tasks in d.iteritems():
    task_list += "<h2>"+ str(project) + "</h2>"
    for i in tasks:
        iden = str(project) + "&" + str(i)
        task_list += '''<h3><input type="checkbox" name="delete_item" value="%s"></input>&nbsp;''' % iden
        task_list += '''%s</h3>''' % i
print task_list + "\n<input type='submit' value='Delete Item(s)'/></form>"

print "<form name='sync' action='syncing.html' method='GET'>"
print "<input type='hidden' name='sync' value='true'/>"
print "<input type='submit' value='Sync Lists'/></form></div>"

# The div that the form for creating a new task is placed
print '''<div id="new_task">
    <form name="new_item" action="newtodo.cgi" method="GET"">
        New To Do Item<br>
        Title: <input type="text" name="title"/><br>
        Category: <input type="text" name="category"/><br><br>
        <input type="submit" value="Add Task"/>
    </form>
</div>'''

print '''</body>
</html>'''