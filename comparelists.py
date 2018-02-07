tl1 = [1,2,5,6,2]
tl2 = [1,2,5,6,2]

tl3 = [1,2,5,6,5]
tl4 = [1,2,5,6,5,3]

tl5 = [1,2,5,6,5,16]
tl6 = [1,2,5,6,5]

tl7 = ['celery','carrots','bread','milk']
tl8 = ['celery','carrots','bread','cream']
#test cases defined above

def compare(x, y):
    a = "The lists are the same."
    b = "The lists are not the same."
    i = 0
    c = 0
    if len(x) != len(y):        #sanity check comparison.  Lists of non-equal lenght cannot be the same.
        print b
    else:
        while i < len(x):       
            if x[i] != y[i]:    #line 22-25 loops through list comparing items. If any pair is not equal, the not equal message is printed and the loop breaks.
                print b
                break
            else:               #line 26 - 28 counts each matched pair
                c += 1
            i += 1
    if len(x) == len(y) and c == len(x):  #checks number of matched pairs against list lengths and if true, prints confirmation if identical lists.
        print a

compare(tl7, tl8)
        
# compare(tl1, tl2) expected output: The lists are the same.
# compare(tl3, tl4) expected output: The lists are not the same.
# compare(tl5, tl6) expected output: The lists are not the same.
# compare(tl7, tl8) expected output: The lists are not the same.

#There is an edge case where lists with identical contents in different orders will fail this comparison and return "The lists are not the same."
#Allowing this exception was intentional on the premise that lists in different orders are not "the same".
