import json


def executed_operation(bank_operation):
    with open('bank_operation.json', 'r', encoding='utf8') as f:
        information = json.load(f)
        for entry in information:
            if entry.get('state') == "EXECUTED":
                date = entry.get('date')
                description = entry.get('description')
                from_account = entry.get('from')
                to_account = entry.get('to')
                operation_amount = entry.get('operationAmount').get('amount')
                currency = entry.get('operationAmount').get('currency').get('name')
                return date, description, from_account, to_account, operation_amount, currency







