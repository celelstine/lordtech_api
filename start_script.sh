#!/usr/bin/env bash

# check if we need to migrate
MISSING_MIGRATIONS=$(python manage.py showmigrations --list | grep '\[ \]')
if [ ${#MISSING_MIGRATIONS} != 0 ]; then
    echo "Database is outdated, migrating....."
    python manage.py migrate
else
    echo "Database is up to date"
fi

# get django port, set default
PORT=${SERVER_PORT:-80}

python  manage.py runserver  0.0.0.0:${PORT}
