#!/usr/bin/python

print "Content-type: text/html" #important to tell the browser what kind of data is coming
print "\n\n" #important to also separate by a pair of newline char's

print "<html>"
print "<head><title>ToDo List</title>"
print "<body>"
print '''<h1>Being Busy</h1> 
        <p>It's not easy being busy! But that doesn't mean it can't be fun.</p> 
        <h2>Important Things To Do</h2> 
        <ol> 
         <li><a href="phys.html">Turn in</a> Physics HW!</li> 
         <li>Do Reading for English</li> 
         <li>Go To the Store for Groceries</li> 
         <li>Pay Tuition</li> 
         <li>Make sure program compiles...</li> 
        </ol> 
        <h2>Fun Things To Do</h2> 
        <ul> 
         <li>Sleep In</li> 
         <li>Out to Dinner with Friends</li> 
         <li>Go Swimming</li> 
         <li>Finish Painting</li> 
         <li>Go to the Movies: <a href="movies.html">see what's playing</a></li> 
        </ul>'''
print "</body>"
print "</html>"
