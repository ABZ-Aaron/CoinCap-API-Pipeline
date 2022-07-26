# CoinCap ETL Project

This is a simple data pipeline extracting cryptocurrency data from [CoinCap API](https://docs.coincap.io) utilising tools such as Docker, cron, and PostgreSQL.

It is based on a project by [Joseph Machado](https://www.startdataengineering.com/post/data-engineering-project-to-impress-hiring-managers/). I've made some amendments, including a different endpoint, dashboard, and extraction script. I've also explained each step throughout this repo, explaining design decisions where necessary.

## Motivation

I wanted to create a simple ETL which would help develop my skills further. I also have a passing interest in crypto, and the API used in [Joseph's](https://www.startdataengineering.com/post/data-engineering-project-to-impress-hiring-managers/) project was a good place to explore this.

## Architecture

1. Extract data using [CoinCap API](https://docs.coincap.io). 
1. Load data into [PostgreSQL](https://www.postgresql.org).
1. Connect with [Google Data Studio](https://datastudio.google.com) dashboard.
1. Orchestrate using [cron](https://en.wikipedia.org/wiki/Cron) within [Docker](https://www.docker.com).


## Output

## Setup

### Prerequisites 

* Install [Docker & Docker Compose](https://docs.docker.com/compose/install/compose-desktop/)


### Quick Setup

If you would like to quickly set this up, follow the below steps. If you would like a more detailed setup where I explain things, skip to next section.

```bash
# Clone Repo
git clone
cd

# Run Docker Container
docker compose --env-file env up --build
```

Once this is running, navigate to [Google Data Studio](https://datastudio.google.com/overview) and sign-in. Once in, click **Create** > **Report**. Then from the tool bar of your newly created report, select **Add data**, and search for **PostgreSQL**.



### Detailed Setup








1. To connect via PGADMIN, use credentials Warehouse and port 5432.



Docker allows you to package and run services or applications in an isolated environment called a container that resides on a host, such as your laptop. 

They contain everything that's needed to run the application. They are easy to share, allowing multiple people to use a container that works the same way as one another. 

Docker daemon listens for Docker requests and managed Docker objects such as images and containers. 

This is included with Docker Desktos. 

With Docker, you are createing an using images, containers, networks, volumes and plugins. 

An image is like a blueprint or template, with instructurions for creating a docker container. 

Often, an image is based on another image, with some additional customisations added. For example, you may build an emage which is based on the ubuntu image, but installs the apache web server and your application. 

To create your own image, you use a Dockerfile with steps needed to create the image and run it. EAch instruction in the dockerfile creates a layer in the image. When you change the Dockerfile and rebuild the image, only those layers which ahve changed are rebuilt. 

A contain is a runnable instance of an image. 

A contains is definied by it's image, as well as any config options you provide when you create or start it. When a container is removed, changes to its stated are not stored, and dissapear. 


docker build -t getting-started .
- This creates a docker image called getting-started based on the DockerFile within the current directory. When we make a change to code, we want to rebuild this with the same command.

docker run -dp 3000:3000 getting-started
- This creates a container from the image

docker rm -f <container id> 
- stop and remove container

Volumes provide the ability to connect specific filesytem paths of the container back to the host machine. So changes in the directory within a container are also seen on the host machine. 

Named volumes are where docker maintains the physical location on the disk and you only need to remember the name of the volume. Everytime you use the volume, docker will make sure the correct data is provided. 

docker volume inspect <volume name>
- the mountpoint is the location on disk where the data is stored. 

When running docker desktop, the docker commadns are actually running inside a small VM on your machine. If you wanted to look at the actual contents of the mountpoint directory, you would need access to the VM.

Another kidn of volume are bind mounts. Here we control the exact location on the host. This is useful to provide additional data into containers. 

For multi container application, we use docker compose. We create a yaml file to define services and with a single command, spin everything up.


- Cron won't find the environemtals variables we defined in the env file. However, in ubuntu, variables in /etc/environment are loaded into cron. So we need to make sure the environmental variables we defined in the env file are added here. For this, I've created the commands.sh script which is run once the Docker coontainer is loaded. This adds the environmental variables into /etc/environment. The commands fiel then runs `cron -f` to start the cron job as a foreground process, rather than a background process.


- Create AWS account, selecting free tier option.
- Navigate to IAM from the search menu. 
- Select Users
- Add Users
- Give a Username
- For access type, select access key (this will give you programmatic access to AWS) and password (this allows you to login to the AWS console with your user account). Select custom password and input a password
- untick require password reset.
- Click attach existing policies directly, and select AdministratorAccess
- Skip the next steps, and click create user
- On the next scree, click download csv agove your username. This is your security credentials, so don't share this with anyone. 
- Install AWS CLI
- Run aws configure, and input the values from the csv you downloaded
- 