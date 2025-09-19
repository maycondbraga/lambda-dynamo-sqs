import boto3
import uuid
import random
from datetime import datetime, timedelta
from tqdm import tqdm

# Configuração do DynamoDB LocalStack
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy',
    region_name='us-east-1'
)
table = dynamodb.Table('tb_proposta_tombamento')

status_options = ['finalizado', 'cancelado', 'represado', 'validado', 'iniciado']
now = datetime.now()
start_date = now - timedelta(days=30)
end_date = now + timedelta(days=30)

def random_date():
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

def generate_item():
    return {
        'status': random.choice(status_options),
        'dt_liquidacao': random_date(),
        'id_proposta': str(uuid.uuid4())
    }

def batch_import(n=100_000):
    with table.batch_writer() as batch:
        for _ in tqdm(range(n), desc="Importando registros"):
            batch.put_item(Item=generate_item())

if __name__ == "__main__":
    batch_import()