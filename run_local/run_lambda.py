import json
from handler import lambda_handler

if __name__ == "__main__":
    # Simula um evento de agendamento do EventBridge
    event = {
        "version": "0",
        "id": "12345678-1234-1234-1234-123456789012",
        "detail-type": "Scheduled Event",
        "source": "aws.events",
        "account": "123456789012",
        "time": "2024-06-10T12:00:00Z",
        "region": "us-east-1",
        "resources": ["arn:aws:events:us-east-1:123456789012:rule/MyRule"],
        "detail": {}
    }
    context = None  # Context pode ser None para testes locais

    response = lambda_handler(event, context)
    print("Resposta do Lambda:")
    print(json.dumps(response, indent=2, ensure_ascii=False))