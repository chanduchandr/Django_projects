# Django_projects
I have my Django Projects here
pip install django

python -m venv env_name 

# On Windows:
env_name\Scripts\activate
# On macOS/Linux:
source env_name/bin/activate

add that path to Installed_app 



for jwt athontication
go to :https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

and then go to installation

in JWT Token we have two type of token athontication 
1. Access Token --> short term token --> only stay's for 5 mins
2. Refresh Token --> Long term token --> to regenarate Access Token we need to use Refresh token --> this refresh token is valid for 24 hr


we have Header Part
we have payload part
and we have signature part

