#!/bin/bash

if [ "`id -u`" != "0" ]
then
    echo "Please run this script as a sudo user."
    exit 1
fi

odooPath="/path to odoo folder"
projectPath="/path to project"

if ! [ -d "$odooPath" ]
then
    echo "$odooPath folder not found."
    exit 1
fi

cd "$projectPath"

if ! [ "`cat $projectPath/.installed 2>&1`" = "True" ]
then
    sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev python3.10 python3.10-dev software-properties-common libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev -y

    sudo add-apt-repository ppa:deadsnakes/ppa -y

    sudo apt-get update

    sudo apt-get install -y python3.10-venv

    cd "$odooPath"

    python3.10 -m venv env

    sudo chmod -R 777 env

    source "env/bin/activate"

    pip install --upgrade pip

    pip install -r requirements.txt

    cd "$projectPath"

    pip install -r requirements.txt

    echo "True" > "$projectPath/.installed"

    python odoo-bin -c "$projectPath/odoo.conf" -i base
else
    echo "Already setup."
fi
