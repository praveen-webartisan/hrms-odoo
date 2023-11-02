# HRMS Odoo

HRMS module for Odoo

## Setup

### Setup Database

1. Copy `scripts/sample-dbSetup.psql` to `dbSetup.psql` and update the variables.

2. Run `scripts/dbSetup.psql` file in Postgres prompt to create a user and database for the project.

### In Windows

1. Copy `scripts\windows\sample-setup.bat` to `scripts\windows\setup.bat` and update the project paths.

2. Copy `scripts\windows\sample-run.bat` to `scripts\windows\run.bat` and update the project paths.

3. Run: `.\scripts\windows\setup.bat`

### In Linux

1. Copy `scripts/linux/sample-setup.sh` to `scripts/linux/setup.sh` and update the project paths.

2. Copy `scripts/linux/sample-run.sh` to `scripts/linux/run.sh` and update the project paths.

3. Run: `./scripts/linux/setup.sh`

## Run

### In Windows

`.\scripts\windows\run.bat`

### In Linux

`./scripts/linux/run.sh`
