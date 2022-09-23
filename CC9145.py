#from random import choice


# posibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd']
# winning_ticket = []
# print("let's see what the winning ticket is：")
#
# #中奖的组合不能包含重复的数字或字母，因此使用了while循环
# while len(winning_ticket) < 4:
#     pulled_item = choice(posibilities)
#
#
#     #仅当要出的数字或字母不在组合中时，才会将其添加到组合中
#     if pulled_item not in winning_ticket:
#         print(f'We pulled a {pulled_item} ！')
#         winning_ticket.append(pulled_item)
#
#
# print(f'The finnal winning-ticket is :{winning_ticket}!')


from random import choice


def get_winnign_ticket(possibilities):
    """摇出中奖组合"""
    winning_ticket = []


    #中奖组合不能包含重复数字或者字母，因此使用while 循环
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)


        #仅当摇出的数字或字母不再组合中，才将其添加到组合中
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)


    return winning_ticket


def check_random_ticket(possibilities):
    """随机生成彩票"""
    ticket = []
    #彩票不能包含重复的数字或字母，因此使用了while循环
    while len(ticket) < 4:
        pulled_item = choice(possibilities)


        #仅当随机生成的数字或字母不在彩票中时，才将其添加到彩票中
        if pulled_item not in ticket:
            ticket.append(pulled_item)


    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd']
winning_ticket = get_winnign_ticket(possibilities)


plays = 0
won = False


#为了避免程序执行时间太长，设置最多随机生成多少张机票
max_tries = 1000000


while not won:
    new_ticket = check_random_ticket(possibilities )
    won = check_random_ticket(new_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
 print("We have a winning ticket!")
 print(f"Your ticket: {new_ticket}")
 print(f"Winning ticket: {winning_ticket}")
 print(f"It only took {plays} tries to win!")
else:
 print(f"Tried {plays} times, without pulling a winner. :(")
 print(f"Your ticket: {new_ticket}")
 print(f"Winning ticket: {winning_ticket}")
