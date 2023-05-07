import boto3
import yaml


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


config = load_yaml('config.yaml')
credentials = {
    'aws_access_key_id': config['access_key_id'],
    'aws_secret_access_key': config['secret_access_key'],
    'region_name': 'eu-west-2'
}

s3 = boto3.resource('s3', **credentials)

bucket_name = 'danhtestbucket2'
object_key = 'test1.txt'

bucket = s3.Bucket(bucket_name)
bucket.download_file(object_key, 'localtest1.txt')