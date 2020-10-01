# r_twitoff
A second version of twitoff, but following Mike R.

## To install

Download the repo and navigate there from the command line

```sh
git clone <address>
cd into r_twitoff
```

## setup

Set and up activate a virtual enviroment

```sh
pipenv install 
pipenv shell
```

## To run web_app
```sh
FLASK_APP=web_app flask run
```

## To get a new html template
1. open a new file in the form some_file.html
2. type HTML and then select html:5 and hit tab
3. Put your code inbetween the two </body> snipets

## The commands I used to set the database up
```sh
FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables
```