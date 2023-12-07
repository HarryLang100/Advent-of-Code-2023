   # swaps = True
   # while swaps:
   #     swaps = False
   #     for i in range(number_hands - 1):
   #         if not compare_two_hands(hands_bid_list[i][0], 
   #                                  hands_bid_list[i + 1][0]):
   #             temp = hands_bid_list[i]
   #             hands_bid_list[i] = hands_bid_list[i + 1]
   #             hands_bid_list[i + 1] = temp
   #             swaps = True
   # return hands_bid_list
   

# I wish to order the list from lowest to highest.
   
mylist = [5, 3, 1, 9]

print(mylist)

print("Performing bubble sort")

swaps = True
while swaps:
    swaps = False
    for i in range(len(mylist) - 1):
        if mylist[i] > mylist[i + 1]:
            temp = mylist[i]
            mylist[i] = mylist[i + 1]
            mylist[i + 1] = temp
            swaps = True
        
print(mylist)