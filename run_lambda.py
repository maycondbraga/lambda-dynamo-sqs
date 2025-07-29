from handler import lambda_handler

if __name__ == "__main__":
    event = {}
    context = None
    lambda_handler(event, context)