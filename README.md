# rates_app

 - https://apiary.io/how-apiary-works

 - redoc

- Data Source:
https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=165.YC.B.U2.EUR.4F.G_N_A.SV_C_YM.PY_11Y
TODO List

## Backend:q

### core
 - create a backend to query the ECB data warehouse and
   feed the results into the database

 - create a celery task which to execute the rate retrieval
    subtask:
      - pick a redis docker image
      - create the login credentials in the env` file
    Resources:
      - https://medium.com/swlh/python-developers-celery-is-a-must-learn-technology-heres-how-to-get-started-578f5d63fab3

 - create a docker based database for postgres
  - during that, try to create an in memory database
  - due to volatile disc, the data should be saved regularly to disc

 - create a 12 factor app proof environment variable based
   settings

 - create the API endpoint to retrieve
   - data as is
     - one row all columns: dt, (1y, 2y, 3y, ... 30y)
     - multiple rows all columns: dt, (1y, 2y, 3y, ... 30y)
     - ~~one row one column (dt, 30y)~~ (see issue-5)
     - one row multiple columns (dt, 1y) (dt, 30y)
   - rate differences
      - one record (column_a - column_b)

   - provide the selection of maturity and date
     - as data
     - as querystring

   - later if multiple rate providers are present
     the difference between those rates can be provided


   - set access allow origin headers, such that the front end
     can query for the latest rate

### packages
 - integrate `orjson` to the project
 - integrate ~~black~~, ~~isort~~, ~~pip-tools~~, ~~flake~~, ~~pytest~~, coverage, coverage tracking
 -
### find solution to serve static files
 - does not work like with flask =/

### devops
 - create docker images for the service
 - create a service file
 - write the nginx config
 - ansistrano, ansible ?

### deployment
 - rent a vulture VM
 - get heroku free tier for now
 - DBaaS for now

### documentation
 - openapi possible?
   https://codesource.io/django-rest-api-documentation-with-swagger-ui/
 - https://github.com/marcgibbons/django-rest-swagger

### filtering
 - ~~add filtering for dates~~ (see issue-7)

### testing
 - ~~initialize testing~~ (see issue-9)
   - in memory postgres via docker
 - ~~try to distinguish unit and integration tests with markers~~ (added `integration_test` marker to `pytest.ini`)

### create a loadtest

### members
  - create functionality for signups
    - real email adreses only

### metering

  - add redis based metering to the project
  - create a frontend to render the results of a query
## Frontend
  - react
  - create landing page with the latest rate
    - should be cached
      - cache should be invalidated after rates have been updated

  - create a subscription page to distribute access

### error pages
  - add static 404 page
  - add static 5XX page
