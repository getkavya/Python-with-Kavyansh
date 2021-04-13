#GROCERY=["HARPIC", "COLGATE", "VIM BAR", "AERIAL", "65"]#LIST IS COLLECTION OF STR AND INT
#print(GROCERY[1])#it will print colgate because it is on 1st place...
numbers=[2, 7, 9, 11, 3,]
print(numbers[3])
print(numbers)
print(numbers[::2])
numbers.sort()#it will sort the no. in asscending order
numbers.reverse()#it will arrange the numbers in descending
print(max(numbers))#biggest no. in the list
print(min(numbers))#smallest no. in the list
numbers.append(6)#it wil print str,int and float at the end the list
numbers.insert(1, 45)#it will insert int at any place =1st no. is the place;;2nd is the no. you want to insert
numbers.remove(11)# it will removethe no. from the list
numbers.pop()
print(numbers)
numbers[1]=98
print(numbers)
#mutable-can change
#immutable-cannot change
tp=(1, 2, 3)
tp[1]=7 #we cannot change tuple::error
print(tp)
a= 1
b= 8
a,b = b,a#if we want to interchange the no.
print(a,b)




