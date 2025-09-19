import json
import boto3
from datetime import datetime, UTC

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy',
    region_name='us-east-1'
)
table = dynamodb.Table('tb_proposta_tombamento')

def lambda_handler(event, context):
    data_atual = datetime.now(UTC).strftime('%Y-%m-%d')
    response = table.query(
        IndexName='status-dt-liquidacao-index',
        KeyConditionExpression='#st = :status_val AND dt_liquidacao <= :dt_val',
        ExpressionAttributeNames={
            '#st': 'status'
        },
        ExpressionAttributeValues={
            ':status_val': 'represado',
            ':dt_val': data_atual
        }
    )
    itens = response.get('Items', [])

    result = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Consulta realizada!",
            "resultados": itens
        })
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result