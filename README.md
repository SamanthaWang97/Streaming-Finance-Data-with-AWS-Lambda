# STA9760-Project-3
## Streaming Finance Data with AWS Lambda
In this project, we will be streaming "real-time" data, processing the data, and dumping it into a S3 bucket that will analyzed and queried in AWS Athena.
We will be using the yfinance module to get the stock information and price of the following stocks:
- Facebook (FB)
- Shopify (SHOP)
- Beyond Meat (BYND)
- Netflix (NFLX)
- Pinterest (PINS)
- Square (SQ)
- The Trade Desk (TTD)
- Okta (OKTA)
- Snap (SNAP)
- Datadog (DDOG)


### Kinesis Data Firehose Delivery Stream Monitoring
![cluster_iamge](assets/kinesis_config.png)

### S3 Bucket
![cluster_iamge](assets/screenshot_of_s3_bucket.png)

The README, in markdown, should contain the following items:
A brief blurb describing the project and the technology leveraged to conduct your analysis. This ought to be brief and informational, in case folks in the future want to recreate your results.
A screenshot of your AWS Kinesis configuration page (see appendix A below).
