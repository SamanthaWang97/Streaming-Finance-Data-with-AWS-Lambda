import json
import boto3
import yfinance as yf 

def lambda_handler(event, context):
    kinesis = boto3.client('kinesis', "us-east-2")
    stocks = ["FB", "SHOP", "BYND", "NFLX", "PINS", "SQ", "TTD", "OKTA", "SNAP", "DDOG"]
    
    for stock in stocks:
        hist = yf.Ticker(stock).history(start="2021-05-11", end="2021-05-12", interval="5m")
        
        for index, row in hist.iterrows(): 
            json_string = {"high":round(row["High"], 2), "low":round(row["Low"], 2), "ts":str(index), "name":stock}
            
            data = json.dumps(json_string)+"\n"
            kinesis.put_record(StreamName="STA9760S2021_stream0", Data=data, PartitionKey="partitionkey")
        
    return {
        'statusCode': 200,
        'body': json.dumps("Success")
    }
