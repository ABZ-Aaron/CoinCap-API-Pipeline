# Overview & Design

## Overview

1. Every 5 minutes a cron job is run.
1. This runs a Python script which connects to CoinCap API and extracts data relating to 10 different cryptocurrency coins. 
1. The same script inserts this data into a PostgreSQL database.
1. Metbase connects to PostgreSQL for data viz.
1. This all runs within Docker with 3 containers:

    - `runpipeline` ~ contains the code and cronjob.
    - `warehouse` ~ launches PostgreSQL 14.
    - `metabase` ~ launches metabase server on port 3000.

1. Docker is run on an AWS EC2 instance.

## Design & Notes

### Cron

There are some limitations of course, compared to something like Airflow, but Cron is a simple way to schedule tasks, and works well for small personal projects like this.

You'll notice the `runpipeline` service in the docker-compose file is looking at a Dockerfile. The CMD here is a shell script which runs. 

```bash
printenv > /etc/environment && cron -f
```

The `cron -f` runs cron in the foreground. If we instead set it as a background process, then if this process failed, the docker container would continue to run and we wouldn't notice.

The `printenv > /etc/environment` puts all environmental variables into `etc/environment` which is used by cron. Otherwise, cron won't be able to find the environmental variables we have referenced in the Python script.

### Extract & Load Script

The `cost_data_etl.py` script is fairly basic. It extracts a small amount of data from the CoinCap API, runs some basic transformations e.g., adds a UTC update column, and inserts data into a PostgreSQL database.

It would normally be good practice to split out extract, transform, and load steps. However, given that this is a simple etl pipeline for a personal project, it makes sense to do it all in once script.

The UTC update column was added so we know the time associated with each coin's stats. This is important for data viz and analysis. 

### SQL

The `init.sql` script creates a schema and table (if they don't already exist) with relevant columns based on what we're extracting from the API. This will be our PostgreSQL table.

You might be wondering at what point this gets run in our pipeline. Well, if you check under the postgres `warehouse` service in the docker-compose file, you'll see the volume `- ./sql:/docker-entrypoint-initdb.d/`. Any SQL file that is added to the `/docker-entrypoint-initdb.d/` folder on the postgres container will be automatically run when the container starts. 

### Docker Compose

As mentioned, there are 3 services run here. When we run the command `docker compose --env-file env up --build -d` this specifies that environmental variables should be taken from the `env` file. In our case, this contains our database details. You can see these being referenced in the docker-compose file, e.g., `${POSTGRES_DB}`. 

Note the ports as well. For PostgreSQL the port 5432 in the container is mapped to the port 5439 on the host. Meaning we can connect to PostgreSQL on the host machine using port 5439.

### Metabase

In the docker-compose file, we've added some environmental variables for Metabase. These allow for persistent data. This means that even if we stop and remove the Metabase container, the data associated with Metabase will remain.

Essentially, Metabase is storing this data in the PostgreSQL database we are using to store CoinCap data, which itself is being persisted through the use of docker volumes.


### EC2

Running on EC2 is useful as it means we don't exert our own personal machines running a Docker container 24/7 without rest. It also means that we can share our Metabase dashboard publicly. 