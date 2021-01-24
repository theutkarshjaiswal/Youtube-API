=>FamPay

Requirements:

Python
Django ( Django rest framework, Django filter)
APScheduler
Some google client
google-api-python-client==1.7.11
google-auth==1.7.0
google-auth-httplib2==0.0.3
google-auth-oauthlib==0.4.1


How to run this APP

If you are using docker 
-- Docker must be install on your machine
-- Goto the terminal and run the following command
-- docker build -t image_name .   "image_name can be anything"
-- docker images -a 
If everything work fine then
-- docker-compose up



Run without docker
You must have Python and Pip install on your machine (Simple google search will help you that)
Go to the project folder and run the following command 
-- python3 -m pip install --user virtualenv
<!-- Creating a virtual Enviroment -->
-- python3 -m venv env   "env can be anything"  
<!-- Activating a virtual environment -->
-- source env/bin/activate
-- pip install -r requirements.txt

In the scheduler folder you will get a file named youtubeApi.py there add your own Google API key
Refer this link '(https://developers.google.com/youtube/v3/getting-started)'


-- python manage.py makemigrations
-- python manage.py migrate
-- python manage.py runserver 



Function of this app in nutshell 
It basically fetch the latest video from the Youtube API continuously in background (async) and also it support multiple keys so if the quota is exausted then it automatically choose the second key.
Save the data to the database 
Fetch the rest to frontend with basic sorting and searching

