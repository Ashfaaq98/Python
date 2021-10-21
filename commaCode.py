

## program to take the values in a list and print it in human readable form

spam = ['Ronaldo','Messi','Barca','Madrid']

def comma(li):

    for i in range(len(li)-2):
        print(li[i],end=',')

    print(li[-2] + ' and ' + li[-1])

comma(spam)