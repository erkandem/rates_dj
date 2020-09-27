# a django rates app

app to collect and redistribute interest rate data from django  
and then migrate through all versions currently at 3.1


# TODO List

## Backend

### core
 - ~~create a backend to query the ECB data warehouse and~~
   ~~feed the results into the database~~ (issue-11)
 - same for USD
 - same for JPY?
 - CHF?
 - GBP?
 
 - create a celery task which to execute the rate retrieval
    subtask:
      - pick a redis docker image
      - create the login credentials in the .envs(dev, prod, template) 
    Resources:
      - https://medium.com/swlh/python-developers-celery-is-a-must-learn-technology-heres-how-to-get-started-578f5d63fab3

 - ~~create a docker based database for postgres~~ (done)
 - ~~environment variable based settings~~ (inplace since yesterday)

 - create the API endpoint to retrieve
   - data as is
     - one row all columns: dt, (1y, 2y, 3y, ... 30y)
     - multiple rows all columns: dt, (1y, 2y, 3y, ... 30y)
     - ~~one row one column (dt, 30y)~~ (see issue-5)
     - one row multiple columns (dt, 1y) (dt, 30y)
   - rate differences
      - one record dt (column_a - column_b)

   - provide the selection of maturity and date
     - as data/body
     - ~~as querystring~~ (see issue-5)

   - later if multiple rate providers are present
     the difference between those rates can be provided


   - set access allow origin headers, such that the front end
     can query for the latest rate

#
### packages
 - integrate `orjson` to the project
 - integrate  coverage, ~~black~~, ~~isort~~, ~~pip-tools~~, ~~flake~~, ~~pytest~~,
 - add coverage rate tracking
 -
 
### find solution to serve static files
 - ~~does not work like with flask~~ =/ (whitenoise for now)
 - serve statics via nginx
 
### devops
 - create docker images for the service
 - create a systemd service file
 - create an nginx config
 - try supervisor
 - try ansistrano, ansible?

### deployment
 - deploy on cloud VM (vulture, DO, Linode?)
 - ~~get heroku free tier for now~~ (https://django-rates.herokuapp.com)
 - ~~DBaaS for now~~ (elephantsql.com)

### documentation
 - web API docs:
   - OpenAPI possible?
     - https://codesource.io/django-rest-api-documentation-with-swagger-ui/
     - https://github.com/marcgibbons/django-rest-swagger
   - redoc possible ?
 - code documentation
   - build sth with sphinx
   - try https://pypi.org/project/sphinxcontrib-django/

### filtering
 - ~~add filtering for dates~~ (see issue-7)

### testing
 - ~~initialize testing~~ (see issue-9)
   - in memory postgres via docker (tmpfs)
 - ~~try to distinguish unit and integration tests with markers~~ (added `integration_test` marker to `pytest.ini`)

### create a loadtest
  - locust
  
### members
  - create functionality for signups
    - real email addresses only

### metering

  - add redis based metering to the project
  - create a frontend to render the results of a query
  
### premium
  - create a subscription page
    - billing
    - chargig
    - https://apiary.io/how-apiary-works

## frontend
  - react !
  - or vue ?
  - ~~create landing page with the latest rate~~ (issue 15)
    - should be cached for static
      - cache should be invalidated after rates have been updated

### error pages
  - add static 404 page
  - add static 5XX page



- data source EUR rates: https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=165.YC.B.U2.EUR.4F.G_N_A.SV_C_YM.PY_11Y
