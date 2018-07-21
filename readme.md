# Store App API

This is a Python Flask restful API used to store and retrive data for frontend store application

## Running locally

1.  install requirements:
    `pip install -r requirements.txt`
2.  create a mysql db for application
3.  update config.py file with allowed url for CORS and db information
4.  create tables in db with schema.sql file located in root of project
5.  run application:
    `ENVIRONMENT=dev python run_app.py`

*Repostirory for front end of application can be found [here](https://github.com/larryg727/store-app-frontend)*
