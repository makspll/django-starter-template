# django-starter-template

## description
this is my setup for production-ready django projects. It's designed to quickly allow you to develop and deploy your app for free using heroku as the server, dropbox as the media serving platform and whitenoise used to serve static files. 

This kind of setup is very scalable since whitenoise allows you to connect to a CDN if you need. Heroku is extremely scalable with it's multitude of apps and tiers and you can easilly purchase more storage with dropbox or simply swap it out for something more suitable.
This is perfect for hackathons or small websites which will not face a lot of traffic.

## features
debugging toolbars, sass/scss compilation, js/css/html minifying and compression, split settings files

check pipfile for package names

## setup 
run `./rename_project.sh {{ your_project_name }}` to rename the project

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

## loading js/css

to link your js and css/scss/sass files use the following:
```
{% load compress %}
  #scss/sass
  {% compress css %}
  <link rel="stylesheet" href="{% static "personal_site/css/main.scss"%}" type="text/x-scss">
  {% endcompress %}
  
  #css
  {% compress css %}
  <link rel="stylesheet" href="{% static "personal_site/css/main.css"%}" type="text/css">
  {% endcompress %}

  #js
  {% compress js %}
  <script src="{% static "jquery-3.5.1/jquery-3.5.1.min.js" %}"></script>
  <script src="{% static "popper-1.16.0/popper.min.js" %}" ></script>
  <script src="{% static "bootstrap-4.5.0/js/bootstrap.min.js" %}" ></script>
  {% endcompress %}

{% endcompress %}
```

## heroku
the project is ready to be deployed on heroku since it contains a procfile and a post_compile hook, just link up your repo to heroku, set the config vars above and deploy.
