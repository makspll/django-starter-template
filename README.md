# django-starter-template

## description
this is my setup for production-ready django projects. It's designed to quickly allow you to develop and deploy your app for free using heroku as the server, dropbox as the media serving platform and whitenoise used to serve static files. 

This kind of setup is very scalable since whitenoise allows you to connect to a CDN if you need. Heroku is extremely scalable with it's multitude of apps and tiers and you can easilly purchase more storage with dropbox or simply swap it out for something more suitable.
This is perfect for hackathons or small websites which will not face a lot of traffic.

## features
debugging toolbars, live reload, sass/scss compilation, js/css/html minifying and compression, split settings files

check pipfile for package names

## setup 
todo - script which configures project

add a `.env` file in root directory with the following inside:
```
DJANGO_ENV={{ dev/prod }}
DJANGO_SECRET_KEY={{ secret key}}
DROPBOX_OAUTH2_TOKEN={{ dropbox oauth2 key }}
```

optionally create the file `template_project/environments/local.py`
this file contains additive settings, but if you want to override any settings set before, import them from the appropriate file and change them there

cd to root directory and run:
`pipenv install`

## heroku
the project is ready to be deployed on heroku since it contains a procfile and a post_compile hook, just link up your repo to heroku, set the config vars above and deploy.