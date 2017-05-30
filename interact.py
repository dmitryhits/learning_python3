while True:
    reply = input("Enter a word (enter spam to stop): ")
    if reply== 'spam': break
    try:
        print(reply + ' squared is ' + str(float(reply) ** 2))
    except:
        print(reply.upper() +  ' is ' + "bad! ".upper()*8)
print('bye')
