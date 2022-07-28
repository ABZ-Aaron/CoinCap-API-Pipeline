## Improvements

### Tests

Integration and unit testing could be implemented to check all the components of this project work as expected, and work together without issue.

Data validation checks could also be utilised to ensure the data we're receiving is of the expected quality and amount. 

Tools such as [great expectations](https://greatexpectations.io) and [pytest](https://docs.pytest.org/en/7.1.x/) could be useful here. 

### Architecture

Using cron works, but makes extending this pipeline more challenging, and limits our ability to backfill. Other schedulers could be explored, such as [airflow](https://airflow.apache.org) or [prefect](https://www.prefect.io). 

We could also look into utilising AWS serverless functionality such as [lambda](https://aws.amazon.com/lambda/) which we could trigger with [cloudwatch](https://aws.amazon.com/cloudwatch/). 

In a real production environment, we'd most likely want to load our data into a real data warehouse such as [Redshift](https://aws.amazon.com/redshift/), or a more easily managed database system like [RDS](https://aws.amazon.com/rds/).

### Streaming

Right now we're running batch jobs every 5 minutes. However, it would make more sense to implement streaming, perhaps with something like [Kafka](https://kafka.apache.org). This would be more complex, but would allow us to extract real-time data without the 5 minute delay.