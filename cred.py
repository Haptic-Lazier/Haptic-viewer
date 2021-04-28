import praw

client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""
# creating an authorized reddit instance 
cred = praw.Reddit(client_id = client_id,  
	client_secret = client_secret,  
	username = username,  
	password = password, 
	user_agent = user_agent
		) 

