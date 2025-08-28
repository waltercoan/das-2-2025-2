import boto3

s3_client = boto3.client("s3", region_name="us-east-1")
s3_client.upload_file("./s3/exemplo.txt", "waltercoan1980", "exemplo.txt")

print("Arquivo carregado com sucesso")
