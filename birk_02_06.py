import json

def employsees_rewrite(sort_type):
    valid_keys = ['firstname', 'lastname', 'department', 'salary']
    if sort_type.lower() not in valid_keys:
        raise ValueError('Bad key sorting')

    with open('employees.json', 'r') as file:
        data = json.load(file)
        employees = data['employees']

        sorted_employees = []
        for employee in employees:
            if sort_type in employee:
                sorted_employees.append(employee)

        if sort_type.lower() == 'department':
            sorted_employees.sort(key=lambda x: x[sort_type], reverse=True)
        else:
            sorted_employees.sort(key=lambda x: x[sort_type])

    output_filename = f'employees_{sort_type.lower()}'
    with open(output_filename, 'w') as output_file:
        json.dump({'employees': sorted_employees},output_file, indent=4)

employsees_rewrite('firstName')
employsees_rewrite('lastName')
employsees_rewrite('department')
employsees_rewrite('salary')
