import json
import boto3
from datetime import datetime, UTC

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tb_proposta_tombamento')

def lambda_handler(event, context):
    data_atual = datetime.now(UTC).strftime('%Y-%m-%d')
    filtro = {
        'status': {'AttributeValueList': ['represado'], 'ComparisonOperator': 'EQ'},
        'dt_liquidacao': {'AttributeValueList': [data_atual], 'ComparisonOperator': 'LE'}
    }
    response = table.scan(ScanFilter=filtro)
    itens = response.get('Items', [])

    result = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Consulta realizada!",
            "resultados": itens
        })
    }

    print(json.dumps(response, indent=2, ensure_ascii=False))
    return result