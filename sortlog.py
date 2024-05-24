# bash equiv
# awk '!line[$0]++' data.log | sort -t = -k 2 -n

# generate data.log (100MB ish)
# truncate -s 0 data.log; while [[ $(wc -c data.log|awk '{print $1}') -lt $((1024 * 100000 )) ]]; do tail -n $RANDOM  /usr/share/dict/words | grep -v "'s" | awk '{print $1"="int(rand()*10000)}' >>data.log; done

# python: 5m and counting......!
# bash: 31s

data=[]

def print_list(data):
    print('printing list:')
    for item in data:
        print(item, end='')
    print('---')

# line: i, word=N
def insert_in_position(data, new_element):
    for i, existing in enumerate(data):
        ne_value=int(new_element.split('=')[1])
        ex_value=int(existing.split('=')[1])
        # print(f'checking {ne_value} >= {i}: {ex_value} ?', end='')
        if ne_value >= ex_value:
            # print(f'yes: new element {ne_value} is greater than existing element {ex_value}, continue')
            continue
        else:
            # print('adding in position ', i, new_element)
            data.insert(i, new_element)
            break
    # print_list(data)            

with open("data.log") as my_file:
    for i, line in enumerate(my_file.readlines()):
        # print(i, line, end='')
        if line not in data:
            if len(data) == 0:
                # print('adding first element: ', line, end='')
                data.append(line)
            else:
                insert_in_position(data, line)

print_list(data)