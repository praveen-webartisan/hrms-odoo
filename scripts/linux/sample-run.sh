#!/bin/bash

odooPath="/path to odoo folder"
projectPath="/path to project"

if ! [ -d "$odooPath" ]
then
    echo "$odooPath folder not found."
    exit 1
fi

cd "$odooPath"
source "venv/bin/activate"

if ! [ "`cat $projectPath/.initialized 2>&1`" = "True" ]
then
    echo "True" > "$projectPath/.initialized"

    python odoo-bin -c "$projectPath/odoo.conf" -i base
else
    python odoo-bin -c "$projectPath/odoo.conf"
fi
