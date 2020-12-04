ask_and_reply = {' How are you?': 'Good!', ' What do you do?': 'make up a program'}

def ask_user():
    ask_user = input('Ask your question')
    if ask_user in ask_and_reply:
        return ask_and_reply[ask_user]
    
while True: 
    a = ask_user()
    if a == None:
        print('Ask again')
    else:
        print(a)
        break


