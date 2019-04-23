# vue_flask

A pythonic flask app.

## Backend

### Build

You can build backend with [pipenv](https://github.com/pypa/pipenv)

``` bash
git clone https://github.com/lrenz/app
cd app
pipenv install --dev
pipenv shell
```

### Database Migration

``` bash
flask db init
flask db migrate
flask db upgrade
```

### Run

``` bash
flask run
```

## Frontend

### Build

``` bash
npm i
```

### Run

``` bash
npm run dev
```

## Notice

To ensure that the app runs properly, you must keep the frontend and the backend running at the same time.
