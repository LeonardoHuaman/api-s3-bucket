import boto3

def lambda_handler(event, context):
    # Entrada
    nombre_bucket = event['body']['bucket']

    # Proceso
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=nombre_bucket)
    
    # Salida
    return {
        'statusCode': 200,
        'message': "Bucket Creado"
    }