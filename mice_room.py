from wsgiref import headers

import requests


url = "http://game.leethack.party/challenge/seagreen-sienna-riograndeescuerzo/archive/request"

while True:
    # sending get request and saving the response as response object
    r = requests.get(url)

    data = r.text

    if not int(r.text[0]):
        break

    data_list = data.split(' ')

    count = 0

    current_smallest = 0

    for line in data_list:
        if len(line) > 0:
            if line[0] == '#':
                if len(line) % 2 == 0:
                    count += len(line)
                    if len(line) < current_smallest:
                        current_smallest = len(line)
                    elif current_smallest == 0:
                        current_smallest = len(line)
    if count < 7:
        count += current_smallest


    headers = {'content-type': 'text/plain'}
    send = requests.post(url, data = str(count), headers = headers)

    print(send.text)


#print(data_list)

#url http://game.leethack.party/challenge/seagreen-sienna-riograndeescuerzo/archive/requestd:
# 1: ### ### #### #### ## ##   ####

#data sheet
'''
ERROR!
ERROR!
POSTED VALUE WAS NOT NUMERIC. IT MUST BE NUMERIC.
ERROR!
ERROR!

IMPORTANT: CONTENT-TYPE MUST BE text/plain!

IMPORTANT: CONTENT-TYPE MUST BE text/plain!

IMPORTANT: CONTENT-TYPE MUST BE text/plain!

'''
