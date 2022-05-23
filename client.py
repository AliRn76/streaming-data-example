import requests


res = requests.get('http://127.0.0.1:8000', stream=True)

lines_count = 0
percent = 0
line = ''
for c in res.iter_content():
    # print(c)
    line += c.decode()
    if c == b']':
        print(line)
        line = line.split(',')
        is_fraud = line[9].strip()[1:-1]
        line = ''
        if is_fraud == 'isFraud':
            continue
        percent = ((percent * lines_count) + int(is_fraud)) / (lines_count + 1)
        lines_count += 1

        print(f'{lines_count} - Fraud: {is_fraud} - {percent} %')
