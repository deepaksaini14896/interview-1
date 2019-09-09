# Coordiante-System


## Download Project & Install Packages


```sh
$ git clone https://github.com/deepaksaini14896/interview-1.git

$ pip install -r requirements.txt
```


## Run Project locally & By using Pytest


```sh
$ cd interview_1

$ uvicorn sql_app.main:app --reload

$ pytest

```


## Run Project on Heroku

```sh
Interview-Stage-1

Post api - /post_location : Post lat,lng of any location with pin code+address+city. This api will add new pin code in db.

Get api - /get_location : Given lat,lng ... it will fetch pin code, address, city as a json response.



https://interview-stage-1.herokuapp.com

## For Better experience Please use 

https://interview-stage-1.herokuapp.com/docs
```

## Note In above Projects link are run on different apps on Heroku because the whole project are divided into Three section that's why we use three apps on Heroku.