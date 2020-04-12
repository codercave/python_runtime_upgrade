import json
import hashlib


def lambda_handler(event, context):
    body = json.loads(event['body'])
    document = body['document']

    sha256 = hashlib.sha256()
    sha256.update(document.encode())

    digest = sha256.hexdigest()

    return {"statusCode": 200, "body": json.dumps({'hash': digest})}
