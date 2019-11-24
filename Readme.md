# Serverless Microserviecs: Saga Transaction

# Usage
- AWS Lambda
- AWS Stepfunctions
- Amazon DynamoDB
- AWS SNS
- AWS SQS
- AWS CloudFormation

# How to Use

Python3が動作する環境で以下のコマンドを実行してください。

```bash
$ PROJECTNAME=serverless-saga
$ YOURNAME=yagita
$ YOURMAILADDR=yagita.takashi@gmail.com
```

lambdaをuploadするバケット
```bash
$ aws s3 mb s3://$YOURNAME-$PROJECTNAME
```

```bash
$ cd lambda/layer/python
$ pip install -r requirements.txt -t .
```

```bash
$ cd ../../..
$ aws cloudformation package \
    --template-file saga-sfn.yml \
    --s3-bucket $YOURNAME-$PROJECTNAME \
    --output-template-file packaged.yml

$ aws cloudformation deploy \
    --stack-name $PROJECTNAME \
    --region ap-northeast-1 \
    --template-file packaged.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --output text \
    --parameter-overrides \
        NotifyEmail=$YOURMAILADDR
    
```

sample event
```json
{
  "order_id": "40063fe3-56d9-4c51-b91f-71929834ce03",
  "order_date": "2019-12-01 12:32:24.927479",
  "customer_id": "2d14eb6c-a3c2-3412-8450-239a16f01fea",
  "items": [{
      "item_id": "0123",
      "qty": 1.0,
      "description": "item 1",
      "unit_price": 12.99
    },
    {
      "item_id": "0234",
      "qty": 2.0,
      "description": "item 2",
      "unit_price": 41.98
    },
    {
      "item_id": "0345",
      "qty": 3.0,
      "description": "item 3",
      "unit_price": 3.50
    }
  ]
}
```




# How to Test
