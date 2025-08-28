import boto3  # Importa a biblioteca boto3 para interagir com serviços AWS

# Cria um recurso S3 configurado para a região us-east-1
s3_client = boto3.resource("s3", region_name="us-east-1")

# Seleciona o bucket S3 chamado "waltercoan1980"
bucket = s3_client.Bucket("waltercoan1980")

# Percorre todos os objetos armazenados no bucket e imprime o nome (key) e o tamanho (size) de cada um
for obj in bucket.objects.all():
    print(f"- {obj.key} - {obj.size}")
