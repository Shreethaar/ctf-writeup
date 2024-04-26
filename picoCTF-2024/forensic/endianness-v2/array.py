with open('analyze.txt', 'r') as f:
    data = f.read()

grouped_data = [data[i:i+8] for i in range(0, len(data), 8)]

result = ', '.join(grouped_data)

with open('array.txt', 'w') as f:
    f.write(result)