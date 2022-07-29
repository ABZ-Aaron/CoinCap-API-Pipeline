# CoinCap ETL Project

This is a simple data pipeline extracting cryptocurrency data from [CoinCap API](https://docs.coincap.io) utilising tools such as Docker, cron, AWS EC2, PostgreSQL, and Metabase.

It is based on a project by [Joseph Machado](https://www.startdataengineering.com/post/data-engineering-project-to-impress-hiring-managers/). I've made various amendments, including using a different endpoint and extraction script, updating containers to allow for data persistence, and documenting some design decisions.

## Motivation

I wanted to create a simple ETL which would help develop my skills and knowledge further. I also have a passing interest in crypto, and the CoinCap API was a good place to explore this.

## Architecture

<img src="https://github.com/ABZ-Aaron/CoinCap-API-Pipeline/blob/master/images/architecture.png" width=70% height=70%>

1. Extract data using [CoinCap API](https://docs.coincap.io)
1. Load data into [PostgreSQL](https://www.postgresql.org)
1. Connect with [Google Data Studio](https://datastudio.google.com) dashboard
1. Orchestrate using [cron](https://en.wikipedia.org/wiki/Cron) 
1. Run with [Docker](https://www.docker.com)
1. Data visualisation with [Metabase](https://www.metabase.com)


## Output

<img src="https://github.com/ABZ-Aaron/CoinCap-API-Pipeline/blob/master/images/dashboard.png" width=70% height=70%>

Link ~ [here](http://ec2-3-8-21-66.eu-west-2.compute.amazonaws.com:3000/public/dashboard/6255ca8f-3c8c-4e1d-a7da-094a730dd1f8)

## The Pipeline

1. [Setup](notes/instructions.md) ~ step-by-step instructions to setup pipeline.

1. [Design](notes/design.md) ~ pipeline description and design decisions.

1. [Improvements]() ~ listing of improvements I plan to make.

