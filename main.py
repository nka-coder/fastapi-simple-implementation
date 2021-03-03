from fastapi import FastAPI, Form
from pydantic import BaseModel
import requests
import multipart

app = FastAPI()

db = []

class City(BaseModel):
    name: str
    timezone: str

class CityForm(BaseModel):
    name: str = Form(...)
    timezone: str = Form(...)

@app.get('/')
def index():
    return {'key':'value'}

@app.get('/cities/get/json')
def json_get_cities():
    results = []
    for city in db:
        r= requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
        current_time = r.json()['datetime']
        results.append({'name':city['name'], 'timezone':city['timezone'], 'current_time':current_time})
    return results

@app.get('/city/get/json/{city_id}')
async def json_get_city(city_id: int):
    city = db[city_id-1]
    city['current_time'] = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}').json()['datetime']
    return city

@app.post('/city/create/json')
def json_create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.post('/city/create/form')
def form_create_city(name: str = Form(...), timezone: str = Form(...)):
    db.append({'name':name, 'timezone':timezone})
    return db[-1]


@app.delete('/city/delete/json/{city_id}')
def json_delete_city(city_id: int):
    db.pop(city_id-1)
    return db
