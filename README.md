## Lordtech Sales API
This is the project for lordtech sales

It is power by:
- Django
- Postgres

### Features
The details of the features can be found [here](APIDOC.md)

### How to setup locally
There are 2 ways to setup this project

#### Docker
- create a new file called `.env` and copy the content from `.env.sample`. Assign appropraite values to the keys
- build and run the stack `docker-compose up --build` (this isn't in detach mode)
- vist `localhost:8003` on the browser
```
For windows home users and assessing the stack and it's resources, get the forward IP with `docker-machine IP`
```

### Without Docker
- create a postgres db with a name (lordtech looks good)
- create a new file called `.env` and copy the content from `.env.sample`. Assign appropraite values to the keys
* We recoomend to use a virtual environment*
- install the dependencies from requirements.txt
- start the project `python manage.py runserver`




