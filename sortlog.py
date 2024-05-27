# bash equiv
# awk '!line[$0]++' data.log | sort -t = -k 2 -n

# generate data.log (100MB ish) ensure some duplicates!
# truncate -s 0 data.log; while [[ $(wc -c data.log|awk '{print $1}') -lt $((1024 * 100000 )) ]]; do tail -n $RANDOM  /usr/share/dict/words | grep -v "'s" | awk '{x=int(rand()*100); print $1"="x; if (x>=95) print $1"="x}' >>data.log; done

# times depend on input data:
# python: 5m and counting......!
# python: now ~15s
# bash: 31s

import time

data=[]

def print_list(data):
    print('printing list:')
    for item in data:
        print(item, end='')
    print('---')

# line: i, word=N - not great at O(n^2)
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
    start_time=time.time()
    for i, line in enumerate(my_file.readlines()):
        data.append(line)
    end_time=time.time()
print(f'load time taken: {end_time-start_time}s')

start_time=time.time()
data=set(data)
end_time=time.time()
print(f'dedup time taken: {end_time-start_time}s')

start_time=time.time()
data=sorted(data, key=lambda x: int(x.split('=')[1]))
end_time=time.time()
print(f'sort time taken: {end_time-start_time}s')

start_time=time.time()
f=open('data_sorted.log', 'w')
f.writelines(data)
f.close()
end_time=time.time()
print(f'write time taken: {end_time-start_time}s')



