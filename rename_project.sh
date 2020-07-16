#!/bin/bash

if [ "$1" != "" ]; then

    NAME_VAL=$1
    declare -a FilesContainingProjectName=("manage.py" "procfile" ".gitignore" "template_project/urls.py" "template_project/wsgi.py" "template_project/asgi.py" "template_project/components/common.py" "template_project/components/languages.py" "template_project/components/media.py" "template_project/components/database.py" "template_project/components/static.py" "template_project/environments/dev.py" "template_project/environments/prod.py")
     
    for file in ${FilesContainingProjectName[@]}; do
        sed -i "s/template_project/$NAME_VAL/g" $file

    done
    mv template_project $NAME_VAL
else
    echo "Project name is required"
fi
