student = {
    'name': 'John',
    'scores': {
        'math': 90,
        'science': 85
    }
}

print(student.get('scores', {}).get('math'))
print(student.get('math'))