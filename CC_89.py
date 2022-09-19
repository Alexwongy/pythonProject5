#创建一个列表，包含一系列简短文本信息的函数，
#将列表传递给函数show_message(),这个函数会打印出每条文本信息


def show_message(messages):
    """这个个打印所有文本信息的函数"""
    for message in messages:
        print(message)


def send_message(messages, sent_messages):
    while messages:
        sent_message = messages.pop()
        print(f'\nThe message {sent_message} have sent')
        sent_messages.append(sent_message)



messages = ['Hello', 'hi', 'how are you']
sent_messages = []

send_message(messages[:], sent_messages) #加上[:]，不改变原messages中的元素，只是创建了副本来使用
print('-----' * 3)
print(messages)
print(sent_messages)
