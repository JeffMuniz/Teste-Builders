import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Obtenha as informações relevantes sobre o grupo de segurança modificado
    group_id = event['detail']['requestParameters']['groupId']
    group_name = event['detail']['requestParameters']['groupName']
    # ...

    # Crie um arquivo de texto contendo as informações relevantes
    file_content = f"Security group ID: {group_id}\nSecurity group name: {group_name}\n"
    file_path = '/tmp/modified_sg.txt'
    with open(file_path, 'w') as file:
        file.write(file_content)

    # Faça upload do arquivo para um bucket S3
    bucket_name = 'my-bucket-name'
    s3.upload_file(file_path, bucket_name, 'modified_sg.txt')
