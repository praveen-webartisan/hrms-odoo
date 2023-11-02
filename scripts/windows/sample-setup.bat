@echo off
setlocal

set installed=""
set odooFolder="\path to odoo 16"
set projectFolder="\path to project"

if exist %odooFolder% (
    @REM Odoo folder exists
) else (
    echo %odooFolder% does not exists.

    exit /b 1
)

where psql >nul 2>nul

if %ERRORLEVEL% EQU 0 (
    @REM Postgres installed
) else (
    echo Postgres is not found. Please install it to continue.

    exit /b 1
)

cd %projectFolder%

if exist .installed (
    set /p installed=<.installed
    set installed = trim(installed)
)

if %installed% == True (
    echo Already setup.
) else (
    echo Setting up...

    pip install --user virtualenv
    cd %odooFolder%
    python -m venv env
    env\Scripts\pip.exe install --upgrade pip
    env\Scripts\pip.exe install -r requirements.txt

    cd %projectFolder%

    echo True > .installed

    echo Setup completed. To start the project, Run: ".\scripts\windows\run.bat"
)
