import boto3

def lambda_handler(event, context):
    # Entrada
    nombre_bucket = event['body']['bucket']
    directory_name = event['body']['directory'] 
    # Proceso
    s3 = boto3.client('s3')
    response = s3.put_object(Bucket=nombre_bucket, Key=(directory_name+'/'))

    
    # Salida
    return {
        'statusCode': 200,
        'message': "Carpeta Creada"
    }