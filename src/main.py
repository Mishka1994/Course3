import os
from src import utils
import operations_data

PATH = os.path.join('fixture', 'operations.json')

operations = operations_data.get_operations_from_json(PATH)
operations = operations_data.choose_only_executed_operation(operations)
operations = operations_data.sorted_operations_by_date(operations)

for x in range(5):
    print(utils.get_date_operation(operations[x]), end=' ')
    print(utils.get_description_operation(operations[x]))
    if 'from' in operations[x]:
        set_with_data = utils.get_name_and_number_product_from(operations[x])
        print(set_with_data[0], set_with_data[1], end=' -> ')
    set_with_data = utils.get_name_and_number_product_to(operations[x])
    print(set_with_data[0], set_with_data[1])
    print(utils.get_amount_operation(operations[x]), end=' ')
    print(utils. get_currency_operation(operations[x]))

    print()


