# Healing Medical Record - Patient Record and Appointment Management API

This is the backend of an application designed to manage patient records and medical appointments.

Technologies used:
```
FastAPI - version 0.116.x
Python - version 3.12.x
Docker for containerization
OpenAPI (Swagger) for automatic API documentation
```

Running the Application

Create the .env file:
```
cp .env.example .env
```
And fill the variables needed.

To run the application, make sure you have Docker and Docker Compose installed.

Then, simply run:

```
docker compose up
```

If you're using VSCode, and somehow see errors like this:

```
"Cannot resolve import 'fastapi'" (Pylance reportMissingImports)
```

We highly recommend you to use the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension on VSCode.
This app is already configured to work plug-and-play with this extension. This corrects the warnings above.

Seed the datbase with the admin user:
```
docker exec healing-medical-record-python python -m app.database.seeders.user_admin_seed

```

Access:
```
The API will be available at: http://0.0.0.0:8080
OpenAPI documentation will be available at: http://0.0.0.0:8080/docs
```

This app is still in development. 👷‍♂️
