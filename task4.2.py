
data = [{"name": "Sergey", "age": 5}, {"name": "Maxim", "age": 6}, {"name": "Ivan", "age": 7}]


def filter_age(data, age):
    # return sum(map(lambda x: x['age'] < age, data))
    return sum(map(lambda x: x.get('age', -1) < age, data)) # если нет age
    
    # return len(list(filter(lambda x: age < x['age'], data)))


print(filter_age(data, 6))
