import itertools

#PERMUTATIONS
print 'For the permutations enter the begining number of the range'
#beginP is the begining of the list
beginP = int(raw_input())
print 'and now enter a number up to but not included in the list'
#endP is the end of the list up to but not including
endP = int(raw_input())
print 'and finally the number of r-permutations'
#perm is the number of permutations
perm = int(raw_input())

permut = itertools.permutations(range(beginP,endP),perm)
#permut = itertools.permutations([1,2,3,4,5,6],3)
count_permut = []
for i in permut:
    count_permut.append(i)
    #print all permutations
    #print count_permut.index(i)+1, i
#print the total number of permutations
print'number of permutations', len(count_permut)

#COMBINATIONS
print 'enter the begining number of the range'
beginC = int(raw_input())
#beginC is the beginign of the set
print 'now enter the end number of the range'
#endC is the end of the set up to but not including
endC = int(raw_input())
print 'and finally the number of r-combinations'
#comb is the number of combinations
comb = int(raw_input())
combin = itertools.combinations(range(beginC,endC),comb)
#combin = itertools.combinations([1,2,3,4,5,6,7,8,9,10],3)
count_combin = []
for i in combin:
    count_combin.append(i)
    #print all combinations
    #print count_combin.index(i)+1, i
#print total number of combinations
print 'number of combinations', len(count_combin)
