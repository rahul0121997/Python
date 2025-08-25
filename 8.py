employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
d = {}

for keys in employees:
    d[keys] = defaults

print(d)