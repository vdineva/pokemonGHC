# Pokemon Sample Application

A sample application created to use in the **Creating a Continuous Integration/Deployment System** workshop for the
**Grace Hopper Celebration of Women in Computing 2016**. This application returns a random starter Pokemon
as a web page and as an API call.

## To Run
```
pip install -r requirements.txt
python pokestarter/app.py
```

### Homepage
Open a browser and navigate to http://localhost:5000.

### API
**Request**
```
curl http://localhost:5000/api
```
**Response**
```
{
  "pokemon": "Squirtle"
}
```

## To Test
```
pip install -r test-requirements.txt
nosetests -sv tests/unit
nosetests -sv tests/functional
```
