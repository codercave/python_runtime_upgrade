import json
import hashlib
import boto3
from flask import Flask


application = Flask(__name__)


@application.route('/hashme', methods=['GET'])
def hashme():

    digest = _pull_and_hash()
    return {
        "statusCode": 200,
        "body": json.dumps({"hash": digest})
    }


def lambda_handler(event, context):

    digest = _pull_and_hash()

    return {
        "statusCode": 200,
        "body": json.dumps({"hash": digest})
    }


def _pull_and_hash():
    s3 = boto3.client('s3')

    with open('/tmp/ids.csv', 'wb') as data:
        s3.download_fileobj('lambda-coldstart', 'ids.csv', data)

    with open('/tmp/ids.csv', 'r') as data:
        content = data.read()

    sha = hashlib.sha256()

    sha.update(content.encode())
    return sha.hexdigest()
