# FastAPI tutorial

## Intro
This project contains simple implementation of a REST API using FastAPI framework. The main advantages of FastAPI is that it is easy to learn, fast to code and ready for product.

## What it does
It allows to:
- Save a city name and timezone in a database
- request the list of cities in the database including their *name*, *timezone* and *current time*
- request a specific city info by sending its *id* to the API
- delete a specific city in the database by sendind it *id* to the API

## Intallation
1. Clone this repo in your python environment using the code below:
```
git clone https://github.com/nka-coder/fastapi-simple-implementation.git
```
2. Install `fastapi` library
```
pip install fastapi
```
3. Install `hypercorn` server
```
pip install hypercorn
```
4. Open your navigator and launch hypercorn server with the url: http://127.0.0.1:8000/docs
