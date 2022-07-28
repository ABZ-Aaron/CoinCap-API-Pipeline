# CoinCap ETL Project

This is a simple data pipeline extracting cryptocurrency data from [CoinCap API](https://docs.coincap.io) utilising tools such as Docker, cron, PostgreSQL, and Metabase.

It is based on a project by [Joseph Machado](https://www.startdataengineering.com/post/data-engineering-project-to-impress-hiring-managers/). I've made some amendments, including a different endpoint and extraction script.

## Motivation

I wanted to create a simple ETL which would help develop my skills further. I also have a passing interest in crypto, and the API used in [Joseph's](https://www.startdataengineering.com/post/data-engineering-project-to-impress-hiring-managers/) project was a good place to explore this.

## Architecture

<img src="https://github.com/ABZ-Aaron/CoinCap-API-Pipeline/blob/master/images/architecture.png" width=70% height=70%>

1. Extract data using [CoinCap API](https://docs.coincap.io)
1. Load data into [PostgreSQL](https://www.postgresql.org)
1. Connect with [Google Data Studio](https://datastudio.google.com) dashboard
1. Orchestrate using [cron](https://en.wikipedia.org/wiki/Cron) within [Docker](https://www.docker.com)
1. Data visualisation with [Metabase](https://www.metabase.com)


## Output

<img src="https://github.com/ABZ-Aaron/CoinCap-API-Pipeline/blob/master/images/dashboard.png" width=70% height=70%>

Link ~ [here](http://ec2-3-8-21-66.eu-west-2.compute.amazonaws.com:3000/public/dashboard/6255ca8f-3c8c-4e1d-a7da-094a730dd1f8)

## Setup & Design 

For an overview of the project, along with some design decisions, see [here](notes/design.md).

If you would like to set this project up yourself, I've provided some prerequisite steps and instructions [here](notes/instructions.md).


