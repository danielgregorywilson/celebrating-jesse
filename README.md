# Getting started with Django on Google Cloud Platform on App Engine Standard

[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=appengine/standard_python38/django/README.md

This repository is an example of how to run a [Django](https://www.djangoproject.com/) 
app on Google App Engine Standard Environment. It uses the 
[Writing your first Django app](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) as the 
example app to deploy.


# Tutorial
See our [Running Django in the App Engine Standard Environment](https://cloud.google.com/python/django/appengine) tutorial for instructions for setting up and deploying this sample application.



# Run app locally
In a separate terminal instance, start the Cloud SQL Proxy to connect to the remote MySQL DB
`./cloud_sql_proxy -instances="celebrating-jesse:us-west1:celebrating-jesse"=tcp:3306`
Activate Python Environment
`source ../env/bin/activate`
Run local server
`python manage.py runserver`

# Deploy app
Deploy app
`gcloud app deploy`
Open app in browser
`gcloud app browse`


Authenticate with credentials for billing and quotas
`gcloud auth application-default login`

Production Frontend
http://celebrating-jesse-frontend.s3-website-us-west-2.amazonaws.com
Production Backend (API)
https://celebrating-jesse.wl.r.appspot.com/api/

Local Frontend
http://jesse-memorial:8080/dashboard
Local Backend (API)
http://jesse-memorial:8000/api/





# Quasar App (lcog-hr)

A Quasar Framework app

## Install the dependencies
```bash
yarn
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```

### Lint the files
```bash
yarn run lint
```

### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.conf.js](https://quasar.dev/quasar-cli/quasar-conf-js).

# Run the frontend locally
`cd frontend`
`quasar dev`

# Deploy frontend
`cd frontend`
`quasar build`
Navigate to https://s3.console.aws.amazon.com/s3/buckets/celebrating-jesse-frontend/
Under the 'Objects' tab is the list of files
Drag the contents of frontend/dist/spa to the window to upload the build