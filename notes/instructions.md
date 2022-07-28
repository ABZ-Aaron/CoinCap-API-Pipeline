## Prerequisites 

* Install [Docker & Docker Compose](https://docs.docker.com/compose/install/compose-desktop/)
* AWS [account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) & AWS [CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
* AWS [EC2 instance](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html) ~ Select Ubuntu image. Create key pair and download `.pem` file. This will allow you to connect to instance. Under Network Settings, set inbound rule for security group to include port `3000`. You can try this project using a free-tier instance (1 GiB memory) but I found this wasn't enough. You may need to upgrade to 2 GiB which could cost about $10 per month). If you opt for a non-free tier instance, use the [pricing calculator](https://calculator.aws/#/) to estimate cost. Once set up, take note of the Public IPv4 DNS.

## Setup

1. Clone repo

    ```bash
    # Clone Repo
    git clone https://github.com/ABZ-Aaron/CoinCap-API-Pipeline.git
    cd CoinCap-API-Pipeline
    ```

1. Change **password** & **username** in **env** file.

1. Zip folder

    ```bash
    zip -r project.gzip .
    ```

1. Send Zip file to EC2 instance (replace <> values below)

    ```bash
    scp -i <pem file full path> project.gzip ubuntu@<public IPv4 DNS>:/tmp
    ```

5. Connect to EC2 instance (replace <> values below)

    ```bash
    ssh -i <pem file full path> ubuntu@<public IPv4 DNS>
    ```

6. Install unzip onto instance

    ```bash
    # install docker and 
    sudo apt-get install unzip
    ```

7. Install Docker onto instance. Follow the "**Install using the repository**" instructions [here](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

8. Set permissions

    ```bash
    sudo chmod 666 /var/run/docker.sock
    ```

9. Move project files to home directory

    ```bash
    mkdir ~/project
    unzip /tmp/project.gzip -d ~/project
    cd ~/project
    ```
10. Run containers

    ```bash
    docker compose --env-file env up --build -d
    ```

## Access Metabase

After a few minutes, everything should be setup, and you can now access your Metabase instance (running in Docker on EC2).

To access, navigate to `<Public IPv4 DNS>:3000`, e.g., `ec2-x-x-xx-xx.eu-west-2.compute.amazonaws.com:3000`.

You can then log in to Metabase and setup your dashboard.

One setup, navigate to Metabase Admin settings and allow sharing. When you navigate back to dashboard, you'll have the option to share a link.

## Access Postgres from Local Machine

Postgres is running within a container on your EC2 instance. However, the container port is mapped to port `5439` on the host. Therefore to connect to Postgres, you'll need the  Public IPv4 DNS address of your EC2 instance (found in the details section in AWS EC2 console) along with database credentials. 

The way I like to connect is through PgAdmin. You can install it to your local machine [here](https://www.pgadmin.org/download/). 

Once setup, right-click **Servers** on left-hand pane, and register a new server. Enter the `Public IPv4 DNS` address, e.g., ec2-x-x-xx-xx.eu-west-2.compute.amazonaws.com, port `5439`, and database `Exchange`. Fill in password and username with what was defined in the **env** file.

You can now query the PostgreSQL table - `assets` stored under schema `crypto`.

## Shut Down Docker

Connect to EC2 instance, navigate to `~/project` and run:

```bash
docker compose down
```

To clear all stopped containers, networks, volumes, and images, run:

```bash
docker system prune -a --volumes
```
* Warning - this will delete all data

## Shut Down EC2

This can be terminated from the AWS console. Don't forget to terminate this if you don't plan on keeping the pipeline running, as you could be charged.