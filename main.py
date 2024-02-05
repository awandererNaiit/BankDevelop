from bridge import executed_operation
import json
from pprint import pprint
from datetime import datetime

bank_list = []

result = executed_operation('bank_operation.json')
result_list = list(result)

bank_list.append(result_list)
data = bank_list[0]
print(bank_list)
print(data)



