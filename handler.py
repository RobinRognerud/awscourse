import json


def hello(event, context):
    body = {
        "message": "Go serverless v1.0!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def calculate(event, context):
    print(event)
    body = json.loads(event["body"])
    number1 = body["number1"]
    number2 = body["number2"]
    sum = number1 + number2

    body = {
        "message": "The sum of the numbers equals: " + str(sum),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response