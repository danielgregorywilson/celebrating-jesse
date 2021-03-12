# Backend: Django on Google Cloud Platform/App Engine

## Run app locally
In a separate terminal instance, start the Cloud SQL Proxy to connect to the remote MySQL DB
```bash
cd backend && ./cloud_sql_proxy -instances="celebrating-jesse:us-west1:celebrating-jesse"=tcp:3306
```
Activate Python Environment
```bash
source ../env/bin/activate && cd backend && python manage.py runserver
```

## Deploy app
```bash
gcloud app deploy
```
Open app in browser
```bash
gcloud app browse
```

## Other useful things
Authenticate with credentials for billing and quotas
```bash
gcloud auth application-default login
```
Set up with: https://cloud.google.com/python/django/appengine

# Frontend: Quasar (Vue) on AWS S3

## First time setup
Install the dependencies
```bash
npm install
```

## Other userful things
Lint the files
```bash
yarn run lint
```



# Run the frontend locally
```bash
cd frontend && quasar dev
```

# Deploy frontend
```bash
cd frontend
quasar build
```
Navigate to https://s3.console.aws.amazon.com/s3/buckets/celebrating-jesse-frontend/
Under the 'Objects' tab is the list of files
Drag the contents of frontend/dist/spa to the window to upload the build

# Locations
Production Frontend
```url
http://celebrating-jesse-frontend.s3-website-us-west-2.amazonaws.com
```
Production Backend (API)
```url
https://celebrating-jesse.wl.r.appspot.com/api/
```

Local Frontend
```url
http://jesse-memorial:8080/dashboard
```
Local Backend (API)
```url
http://jesse-memorial:8000/api/
```