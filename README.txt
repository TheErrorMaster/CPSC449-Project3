CPSC449-Project3

Authors: 
Mauricio Macias (mauricio.macias@csu.fullerton.edu) 890741622
Andrew Dinh (decayingapple@csu.fullerton.edu) 893242255

0 Installation
Make sure you are in the project root and run:

"foreman start"

1 Background 

Look at the README.md if you want to see our readme in md version. 

For this project we will learn to make HTTP requests from a Python program and use this ability to store server-side session data in a separate service. 

This project was completed by 2 people. Whose names are listed in the very top of this paper.

2 Learning HTTP request

Question 2
When USE_SESSION_STORE = False 
Flask will use default session implementation: storing the session variables count in a signed cookie on the client side. 
 
We notice that the two browsers do not share the same count variable. This is the reason they outputing different numbers. 

Question 3 

When we view the Set-Cookies: response header we notice that it changes each time the page is refreshed. 
 

Question 6

But when we turn USE_SESSION STORE (USE_SESSION_STORE = True)
Flask will note load the counter page because methods of keyVaueSessionStore have not yet been implemented.  

Question 8

So we when overide keyValueSessionStore Flask will use now store sessions into a key-value store. 
 
Then we notice that the two browsers do not share the same count variable. 

Question 9 
But when we are viewing the Set-Cookies: response header
 
we notice that it Set-Cookies does not change each time the page is refreshed. 
 

Question 10
Here are going to Click the Reset Button, notice that the POST request clears the session cookie. 
 
Then the subsequent GET request generates a new session id. 
 

Question 11
Then we we use our dump.py script it will list the active sessions in the key-value store. 
 

