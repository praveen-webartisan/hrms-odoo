@echo off
setlocal

set initialized=""
set odooFolder="\path to odoo 16"
set projectFolder="\path to project"

cd %projectFolder%\

if exist .initialized (
    set /p initialized=<.initialized
    set initialized = trim(initialized)
)

if %initialized% == True (
    cd %odooFolder%

    env\Scripts\python.exe odoo-bin -c "%projectFolder%\odoo.conf"
) else (
    echo Initiating...

    cd %projectFolder%

    echo True > .initialized

    cd %odooFolder%

    env\Scripts\python.exe odoo-bin -c "%projectFolder%\odoo.conf" -i base
)

cd %projectFolder%
