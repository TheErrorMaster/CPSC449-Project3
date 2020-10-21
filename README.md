# CPSC449-Project3
 # Authors: 
Mauricio Macias (mauricio.macias@csu.fullerton.edu) 890741622 <br/>
Andrew Dinh	(decayingapple@csu.fullerton.edu) 893242255 <br/>


## 0 Installation
Make sure you are in the project root and run:

"foreman start"

## 1 Background 

For this project we will learn to make HTTP requests from a Python program and use this ability to store server-side session data in a separate service. 

This project was completed by 2 people. Whose names are listed in the very top of this paper.

## 2 Learning HTTP request
### Question #2
When USE_SESSION_STORE = False <br/>
Flask will use default session implementation: storing the session variables count in a signed cookie on the client side. <br/>
![](q2.png) <br/>
Notice that the two browsers do not share the same count variable.  <br/>
### Question #3
### Browser developer tools
Here are viewing the `Set-Cookies: response header ` <br/>
![](q3-1.png) <br/>
Notice that it changes each time the page is refreshed. <br/>
![](q3-2.png) <br/>


### Question 6
### counter.html
When USE_SESSION_STORE = True <br/>
Flask will load the counter page. <br/>
![](q6.png) <br/>
Notice the methods of keyVaueSessionStore have not yet been implemented.  <br/>

### Quesion 8
Flask will use now store sessions into a key-value store. <br/>
![](q8.png) <br/>
But,notice that the two browsers do not share the same count variable.  <br/>

### Question 9 
Here are viewing the `Set-Cookies: response header ` <br/>
![](q9-1.png) <br/>
Notice that it `Set-Cookies` does not change each time the page is refreshed. <br/>
![](q9-2.png) <br/>

### Question 10
Here are going to Click the Reset Button, Notice that the POST request clears the session cookie. <br/>
![](q10-1.png) <br/>
Then the subsequent GET request generates a new session id. <br/>
![](q10-2.png) <br/>

### Question 11
Then we are going to use our dump.py script to list the active sessions in the key-value store. <br/>
![](q11.png) <br/>
