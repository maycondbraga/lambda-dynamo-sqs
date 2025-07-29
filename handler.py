import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NOME_DA_TABELA')  # Substitua pelo nome da sua tabela

def lambda_handler(event, context):
    data_atual = datetime.utcnow().strftime('%Y-%m-%d')
    filtro = {
        'status': {'AttributeValueList': ['represado'], 'ComparisonOperator': 'EQ'},
        'dt_liquidacao': {'AttributeValueList': [data_atual], 'ComparisonOperator': 'LE'}
    }
    response = table.scan(ScanFilter=filtro)
    itens = response.get('Items', [])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Consulta realizada!",
            "resultados": itens
        })
    }