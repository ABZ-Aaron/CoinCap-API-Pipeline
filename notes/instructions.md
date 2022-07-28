## Prerequisites 

* Install [Docker & Docker Compose](https://docs.docker.com/compose/install/compose-desktop/)
* AWS [account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) & AWS [CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
* AWS [EC2 instance](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html) ~ Select Ubuntu image. Create key pair and download `.pem` file. This will allow you to connect to instance. Under Network Settings, set inbound rule for security group to include port `3000`. You can try this project using a free-tier instance (1 GiB memory) but I found this wasn't enough. If you opt for a non-free tier instance, use the [pricing calculator](https://calculator.aws/#/) to estimate cost. Once set up, take note of the Public IPv4 DNS.

## Setup

1. Clone repo

    ```bash
    # Clone Repo
    git clone
    cd
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