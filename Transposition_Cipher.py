#Transposition-Cipher

#key is the amount of boxes in each row


def shift(message,key):
    my_list = list()
    text = ''
    length = len(message)
    count = 0
    key = int(key)

    for letters in message:
        #print(letters)
        text += letters
        
        if len(text) == key:
                my_list.append(text)
                count += len(text)
                text = ''

    if len(my_list) != length:
            my_list.append(message[count:length])
            
    result = output(my_list)
    print(result)


def output(the_list):
    result = ''
    looping = True
    amount = 0
    while looping: #loop running while it still can until something is encountered
        try:
            for list_values in the_list:
                    result += list_values[amount]
            amount += 1
        except:
            looping = False

    return result

while True:
    user = input('Enter your message: ')
    key = input('Enter your key: ')
    shift(user,key)
