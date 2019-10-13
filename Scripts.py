#Introduction

#Ex.1 - Say "Hello, World!" With Python 
	
print("Hello, World!")

#Ex.2 - Python If-Else
	
import math
import os
import random
import re
import sys
if __name__ == '__main__':
	n = int(input().strip())
	if n%2 != 0 or 6<n<=20:
		print("Weird")
	elif n%2 == 0 and (2<=n<5 or n>20):
		print("Not Weird")

#Ex.3 - Arithmetic Operators

if __name__ == '__main__':
	a = int(input())
	b = int(input())
	print(a+b)
	print(a-b)
	print(a*b)

#Ex.4 - Python: Division

if __name__ == '__main__':
	a = int(input())
	b = int(input())
	print(a//b)
	print(a/b)

#Ex.5 - Loops

if __name__ == '__main__':
	n = int(input())
	for i in range(0,n):
		print(i**2)

#Ex.6 - Write a function

def is_leap(year):
    leap = False
    
    if (year%4 == 0 and year%100 !=0) or year%400 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

#Ex.7 - Print function

if __name__ == '__main__':
    n = int(input())
    a = ''
    for i in range(1,n+1):
        a += str(i)
    print(a)

#Basic Data Types

#Ex.8 - List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i,j,k] 
    for i in range(x+1) 
    for j in range(y+1) 
    for k in range(z+1) 
    if i+j+k != n])

#Ex.9 - Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = []
    for i in arr:
        l.append(i)
    m = max(l)
    a = [i for i in l if i != m]
    print(max(a))

#Ex.10 - Nested Lists

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    a = min(s[1] for s in students)
    l = [s for s in students if s[1] == a]
    students = [s for s in students if s not in l]
    b = min(s[1] for s in students)
    j = [s[0] for s in students if s[1] == b]
    j.sort()
    for i in j:
        print(i)

#Ex.11 - Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    n = 0
    s = 0
    if query_name in student_marks.keys():
        for i in student_marks[query_name]:
            s += i
            n += 1
    print("%.2f" % float(s/n))

#Ex.12 - Lists

if __name__ == '__main__':
    N = int(input())
    c = []
    for i in range(N):
        c.append(input().split())
    l = []
    for i in c:
        if i[0] == 'insert':             
            l.insert(int(i[1]), int(i[2]))
        elif i[0] == 'print':
            print(l)
        elif i[0] == 'remove':
            l.remove(int(i[1]))
        elif i[0] == 'append':
            l.append(int(i[1]))
        elif i[0] == 'sort':
            l.sort()
        elif i[0] == 'pop':
            l.pop()
        elif i[0] == 'reverse':
            l.reverse()

#Ex.13 - Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

#Strings

#Ex.14 - sWAP cASE

def swap_case(s):
    b = ''
    for i in s:
        if i.islower():
            b += i.upper()
        elif i.isupper():
            b += i.lower()
        else:
            b += i
    return b



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#Ex.15 - String Split and Join

def split_and_join(line):
    a = line.split(' ')
    b = '-'.join(a)
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#Ex.16 - What's Your Name?

def print_full_name(a, b):
    print("Hello " + a +' ' + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Ex.17 - Mutations

def mutate_string(string, position, character):
    s = string[:position] + character + string[(position + 1):]
    return s
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Ex.18 - Find a string

def count_substring(string, sub_string):
    l = len(sub_string)
    c = 0
    s = string
    for i in range(len(s)-l+1):
        if s[i:i+l] == sub_string:
            c += 1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#Ex.19 - String Validators

if __name__ == '__main__':
    s = input()
    an = False
    al = False
    di = False
    lo = False
    up = False
    for i in s:
        if i.isalnum():
            an = True
        if i.isalpha():
            al = True
        if i.isdigit():
            di = True
        if i.islower():
            lo = True
        if i.isupper():
            up = True
    print(an)
    print(al)
    print(di)
    print(lo)
    print(up)

#Ex.20 - Text Allignment

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Ex.21 - Text Wrap

import textwrap

def wrap(string, max_width):
    a = ''
    for i in range(len(string)):
        if i % max_width == 0 and i != 0:
            a += '\n'
        a += string[i]  
    return a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Ex.22 - Designer Door Mat

i = input()
i = i.split()
N = int(i[0])
M = int(i[1])
a = ''
for h in range(N):
    if h < ((N-1)/2):
        print(('.|.'*(h*2+1)).center(M,'-'))
    elif h == ((N-1)/2):
        print('WELCOME'.center(M,'-'))
    elif ((N-1)/2) < h < N:
        print(('.|.'*(2*(N-h)-1)).center(M,'-'))

#Ex.23 - String Formatting

def print_formatted(number):
    # your code goes here
    s = len(str(bin(number)[2:]))
    w1 = len(str(number))
    
    for i in range(number):
        print(str(i+1).rjust(s), 
        str(oct(i+1)[2:]).rjust(s), 
        str(hex(i+1)[2:]).upper().rjust(s), 
        str(bin(i+1)[2:]).rjust(s))

#Ex.24 - Alphabet Rangoli

def print_rangoli(size):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = alphabet[size-1]
    for i in range(size):
         
        a = s[-2::-1]
        print(s.rjust(size*2-1,'-') + a.ljust(size*2-2,'-'))
        s = s + '-'+ alphabet[size-i-2] 
    s = s[:-2]
    for i in range(size-1):
        s = s[:-2]
        a = s[-2::-1]
        print(s.rjust(size*2-1,'-') + a.ljust(size*2-2,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#Ex.25 - Capitalize!

def solve(s):
    a = s.split(' ')
    for i in range(len(a)):
        a[i] = a[i].capitalize()
    return ' '.join(a)

#Ex.26 - The Minion Game

def minion_game(string):
    vow = 'AEIOU'
    p = 0
    cs= 0
    ck= 0
    for i in string:
        if i in vow:
            ck += len(string) - p
        else:
            cs += len(string) - p
        p += 1
    #Stuart
    st = 'Stuart ' + str(cs)
    #Kevin
    ke = 'Kevin ' + str(ck)
    if ck > cs:
        print(ke)
    elif ck < cs:
        print(st)
    else:
        print('Draw')

#Ex.27 - Merge the Tools!

def merge_the_tools(string, k):
    l = []
    for i in range(int(len(string)/k)):
        l.append(string[i*k:(i+1)*k])
    for s in l:
        a = ''
        c = 0
        for i in s:
            if i not in s[:c]:
                a += i
            c += 1
        print(a)

#Sets

#Ex.28 - Introduction to sets

def average(array):
    a = set(array)
    return sum(a)/len(a)

#Ex.29 - Symmetric Difference

m = int(input())
M = set(map(int, input().split()))
n = input()
N = set(map(int, input().split()))
diff = M.symmetric_difference(N)
l = list(diff)
l.sort()
for i in l:
    print(i)

#Ex.30 - No idea!

l = list(map(int, input().split()))
n = l[0]
m = l[1]
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
h = 0
for i in arr:
    if i in A:
        h += 1
    elif i in B:
        h -= 1
print(h)

#Ex.31 - Set.add()

N = int(input())
s = set()
for i in range(N):
    s.add(input())
print(len(s))

#Ex.32 - Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
com = []
for i in range(int(input())):
    com.append(input().split())
for c in com:
    if len(c) == 1:
        s.pop()
    elif c[0] == 'remove':
        s.remove(int(c[1]))
    elif c[0] == 'discard':
        s.discard(int(c[1]))
print(sum(s))

#Ex.33 - Set .union() Operation

a = input()
s_a = set(map(int, input().split()))
b = input()
s_b = set(map(int, input().split()))
u = s_a.union(s_b)
print(len(u))

#Ex.34 - Set .intersection() Operation

a = input()
s_a = set(map(int, input().split()))
b = input()
s_b = set(map(int, input().split()))
i = s_a.intersection(s_b)
print(len(i))

#Ex.35 - Set .difference() Operation

a = input()
s_a = set(map(int, input().split()))
b = input()
s_b = set(map(int, input().split()))
diff = s_a.difference(s_b)
print(len(diff))

#Ex.36 - Set .symmetric_difference() Operation

a = input()
s_a = set(map(int, input().split()))
b = input()
s_b = set(map(int, input().split()))
sd = s_a.symmetric_difference(s_b)
print(len(sd))

#Ex.37 - Set Mutations

n_A = input()
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    com = input().split()[0]
    if com == 'intersection_update':
        A.intersection_update(set(map(int, input().split())))
    elif com == 'update':
        A.update(set(map(int, input().split())))
    elif com == 'symmetric_difference_update':
        A.symmetric_difference_update(set(map(int, input().split())))
    elif com == 'difference_update':
        A.difference_update(set(map(int, input().split())))
print(sum(A))

#Ex.38 - The Captain's Room

k = int(input())
l = sorted(list(input().split()))
a = sorted(set(l))
for i in range(int(len(l)/k)):
    if l[i*k +1] != a[i]:
        out = l[i*k]
        break
    else:
        out = l[-1]
print(out)

#Ex.39 - Check Subset

T = int(input())
out = []
for i in range(T):
    a = input()
    A = set(map(int, input().split()))
    b = input()
    B = set(map(int, input().split()))
    out.append(A.issubset(B))
for i in out:
    print(i)

#Ex.40 - Check Strict Superset

A = set(map(int, input().split()))
n = int(input())
c = True
for i in range(n):
    s = set(map(int, input().split()))
    if s == A:
        c = False
        break
    elif not A.issuperset(s):
        c = False
        break
print(c)

#Collections

#Ex.41 - Collections.counter()

from collections import Counter
X = int(input())
size = input().split()
avail = Counter(size)
earn = 0
N = int(input())
for i in range(N):
    c = input().split()
    if avail[c[0]] >0 :
       earn += int(c[1])
       avail[c[0]] -= 1
print(earn)

#Ex.42 - Collections.namedtuple()

from collections import namedtuple
N = int(input())
cols = input().split()
s = 0
l = namedtuple('stud', cols)
for i in range(N):
    line = input().split()
    stud = l(line[0], line[1], line[2], line[3])
    s += int(stud.MARKS)
print("%.2f" % float(s/N))

#Ex.43 - collections.OrderedDict()

from collections import OrderedDict

N = int(input())
d = OrderedDict()
names = []
for i in range(N):
    s = input().split()
    key = ' '.join(s[:-1])
    value = int(s[-1])
    if key in d:
        d[key] = d[key] + value
    else:
        d[key] = value
for k in d.keys():
    print(str(k) + ' ' + str(d[k]))

#Ex.44 - Word Order

from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(len(d))
for k in d:
    d[k] = str(d[k])
print(' '.join(d.values()))

#Ex.45 - Collections.deque()

from collections import deque
d = deque()
N = int(input())

for i in range(N):
    com = input().split()
    if com[0] == 'append':
        d.append(com[1])
    elif com[0] == 'appendleft':
        d.appendleft(com[1])
    elif com[0] == 'pop':
        d.pop()
    elif com[0] == 'popleft':
        d.popleft()
print(' '.join(d))

#Ex.46 - Piling Up!

from collections import deque
T = int(input())
for t in range(T):
    out = 'Yes'
    n = int(input())
    cubes = deque(map(int, input().split()))
    for i in range(n-1):
        if cubes[0]>=cubes[1]:
            cubes.popleft()
        elif cubes[-1]>=cubes[-2]:
            cubes.pop()
        else:
            out = 'No'
    print(out)

#Ex.47 - Company Logo

from collections import Counter

if __name__ == '__main__':
    s = input()
    a = list(s)
    a.sort()
    occ = Counter(a)
    l = []
    for i in range(3):
        for k in occ.keys():
            if int(occ[k]) == max(occ.values()):
                l.append((k, occ[k]))
                occ.pop(k)
                break
        print(l[i][0] + ' ' + str(l[i][1]))

#Ex.48 - DefaultDict

from collections import defaultdict
inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
A = defaultdict(list)
B = []
c = 1
for i in range(n):
    A[(input())].append(c)
    c+=1
for i in range(m):
    B.append(input())
for s in B:
    if not s in A.keys():
        A[s].append('-1')
    print(*A[s])


#Date and Time

#Ex.49 - Calendar Module

import calendar

d = list(map(int, input().split()))
wd = calendar.weekday(year = d[-1], month = d[0], day = d[1])
a =  calendar.TextCalendar(0).formatweekday(day = wd, width = 9).upper()
print(a.replace(' ', ''))

#Ex.50 - Time Delta

def is_leap(year):
        leap = False
    
        if (year%4 == 0 and year%100 !=0) or year%400 == 0:
            leap = True
    
        return leap

def time_delta(t1, t2):
    #Number of days before first day of each month in a year
    d = { 'Jan' : 0, 'Feb' : 31, 'Mar' : 59,
     'Apr' : 90, 'May' : 120, 'Jun' : 151, 'Jul' : 181,
      'Aug' : 212, 'Sep' : 243, 'Oct' : 273, 'Nov' : 304, 'Dec' : 334}
    #and in a leap year
    dl = { 'Jan' : 0, 'Feb' : 31, 'Mar' : 60,
     'Apr' : 91, 'May' : 121, 'Jun' : 152, 'Jul' : 182,
      'Aug' : 213, 'Sep' : 244, 'Oct' : 274, 'Nov' : 305, 'Dec' : 335}

    T1 = t1.split()
    T2 = t2.split()
    #removing week-days from the input
    T2.remove(T2[0])
    T1.remove(T1[0])
    #timezone to seconds
    tz1 = T1.pop(-1)
    tz2 = T2.pop(-1)
    tz1 = int(tz1[0]+'1')*(int(tz1[1:3])*3600 + int(tz1[3:5])*60)
    tz2 = int(tz2[0]+'1')*(int(tz2[1:3])*3600 + int(tz2[3:5])*60)
    #days
    d1 = int(T1[0])
    d2 = int(T2[0])
    #years
    y1 = int(T1[2])
    y2 = int(T2[2])
    #days before month of the input
    if is_leap(y1):
        md1 = int(dl[T1[1]])
    else:
        md1 = int(d[T1[1]])
    if is_leap(y2):
        md2 = int(dl[T2[1]])
    else:
        md2 = int(d[T2[1]])
    
    
    #number of leapdays in the range of years of the input
    leapday = 0
    for y in range(min(y1, y2), max(y1, y2)):
        if is_leap(y):
            leapday += 1

    #hour, minute and second of the day in input
    h1 = list(map(int, T1[-1].split(':')))
    h2 = list(map(int, T2[-1].split(':')))
    
    #relative time coordinates expressed in seconds, starting at smallest year
    s1 = (d1 + md1 + (y1 - min(y1, y2)) * 365)*86400 + int(h1[0])*3600 + int(h1[1])*60 + int(h1[2]) -tz1
    s2 = (d2 + md2 + (y2 - min(y1, y2)) * 365)*86400 + int(h2[0])*3600 + int(h2[1])*60 + int(h2[2]) -tz2
    
    #leapdays in the range of years must be summed to the biggest year's days count, converted to seconds and summed to relative time coordinate  
    if y1 > y2:
        s1 += leapday*86400
    else:
        s2 += leapday*86400
    return str(abs(s1 - s2))

#Errors and Exceptions

#Ex.51 - Exceptions

n = int(input())
for i in range(n):
    l = input().split()
    a = l[0]
    b = l[1]
    
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as v:
        print('Error Code:', v)

#Built-ins
        
#Ex.52 - Zipped!

a = list(map(int, input().split()))
N = a[0]
X = a[1]
l = []
for x in range(X):
    l.append (list(map(float, input().split())))
studs = list(zip(*l))
for i in studs:
    print("%.1f" % float(sum(i)/X))

#Ex.53 - Athlete Sort

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    def takeK(elem):
        return elem[k]
    
    for i in sorted(arr, key = takeK):
        print(*i)

#Ex.54 - ginortS

s = input()

def low(s):
    ns = ''
    for i in s:
        if i.islower():
            ns += i 
    return ns

def up(s):
    ns = ''
    for i in s:
        if i.isupper():
            ns += i 
    return ns

def digodd(s):
    ns = ''
    for i in s:
        if i.isdigit() and int(i)%2 != 0:
            ns += i 
    return ns

def digev(s):
    ns = ''
    for i in s:
        if i.isdigit() and int(i)%2 == 0:
            ns += i 
    return ns

print(''.join(sorted(low(s))+sorted(up(s))+sorted(digodd(s))+sorted(digev(s))))

#Python Functionals

#Ex.55 - Map and Lambda

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    l = []
    if n == 0:
        return l
    elif n == 1:
        l.append(0)
    elif n >= 2:
        l = [0,1]
        for i in range(2,n):
            l.append(l[i-1] + l[i-2])
    return l

#Regex and Parsing

#Ex.56 - Detect Floating Point Numbers

T = int(input())
def isfloat(s):
    sign = ['+','-']
    cyph = map(str, range(10))
    ok = ['.', *sign, *cyph]
    if s.find('.') in [-1, len(s)-1] :
        return False
    if s.count('.') > 1:
        return False
    for i in s:
        if i not in ok:
            return False
    for i in sign:
        if s[1:].find(i) != -1:
            return False
    return True

    
for i in range(T):
    print(isfloat(input()))

#Ex.57 - Re.split()

regex_pattern = r"\D"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Ex.58 - Group(), Groups() & Groupdict()

import re 
pat = re.compile(r'([a-zA-Z0-9])\1{1,}') 
occ = pat.search(input()) 
if occ != None:
    print(*occ.groups())
else:
    print(-1)

#Ex.59 - Re.findall() & Re.finditer()

import re 
pat = re.compile(r'([aeiouAEIOU])([aeiouAEIOU]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]+') 
s = input()
occ = pat.findall(s) 
if len(occ) > 0:
    if s[0] in 'aeiouAEIOU' and s[1] in 'aeiouAEIOU':
        for i in occ[1:]:
            print(''.join(i))
    else:
        for i in occ:
            print(''.join(i))
else:
    print(-1)

#Closures and Decorators

#Ex.60 - Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            l[i] = '+91 ' + l[i][-10:-5] + ' ' + l[i][-5:]
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#Ex.61 - Decorators 2

def person_lister(f):
    def inner(people):
        people = sorted(people, key = lambda x: int(x[2]))
        out = []
        for p in people:
            out.append(f(p))
        return(out)
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), 

#Numpy

#Ex.62 - Arrays

import numpy

def arrays(arr):
    arr.reverse()
    a = numpy.array(arr, float)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Ex.63 - Shape and Reshape

import numpy

arr = list(map(int, input().split()))
print(numpy.reshape(arr, (3,3)))

#Ex.64 - Transpose and Flatten

import numpy

nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
arr = numpy.array(a)
print(numpy.transpose(arr))
print(arr.flatten())

#Ex.65 - Concatenate

import numpy

nmp = list(map(int, input().split()))
n = nmp[0]
m = nmp[1]
p = nmp[2]
l = []
k = []
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(m):
    k.append(list(map(int, input().split())))
print(numpy.concatenate((numpy.array(l), numpy.array(k)),axis = 0))

#Ex.66 - Zeros and Ones

import numpy

t = tuple(map(int, input().split()))
print(numpy.zeros(t, dtype = numpy.int))
print(numpy.ones(t, dtype = numpy.int))

#Ex.67 - Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
a = numpy.eye(n, m, k = 0)
print(a)

#Ex.68 - Array Mathematics

import numpy

n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int,input().split())))
for _ in range(n):
    b.append(list(map(int,input().split())))
A = numpy.array(a)
B = numpy.array(b)
print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(A//B)
print(A%B)
print(numpy.power(A,B))

Ex.69 - Floor, Ceil, Rint

import numpy
numpy.set_printoptions(legacy='1.13')

a = list(map(float, input().split()))
A = numpy.array(a)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

#Ex.70 - Sum and Prod

import numpy

n,m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
A = numpy.array(l)
print(numpy.prod(numpy.sum(A, axis = 0)))

#Ex.71 - Min and Max

import numpy

n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
A = numpy.array(l)
print(numpy.max(numpy.min(A, axis = 1)))

#Ex.72 - Mean, Var, and Std

import numpy as np
np.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
arr = np.array(a)
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.std(arr))

#Ex.73 - Dot and Cross

import numpy as np

n = int(input())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))
A = np.array(a)
B = np.array(b)
print(np.dot(A,B))

#Ex.74 - Inner and Outer

import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print(np.inner(A,B))
print(np.outer(A,B))

#Ex.75 - Polynomials

import numpy
coeff = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(coeff, x))

#Ex.76 - Linear Algebra

import numpy

N = int(input())
a = []
for i in range(N):
    a.append(list(map(float, input().split())))
print(round(numpy.linalg.det(a), 2))

#XML

#Ex.77 - XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    ch = list(node)
    l = len(node.attrib)
    for i in ch:
        l +=  get_attr_number(i)

    return l 

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#Ex.78 - XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    
    level += 1

    if level > maxdepth:
        maxdepth = level
    
    for ch in elem:
        depth(ch, level)

    return(maxdepth)
    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

##Regex

#Ex.79 - Re.start() & Re.end()

import re

s = input()
k = input()
regp = re.compile('(?=' + k + ')')
if re.search(regp, s) == None:
    print((-1,-1))
else:
    print(*[(m.start(), m.start()+len(k)-1) for m in re.finditer(regp, s)], sep = '\n')
    

#Ex.80 - Regex Substitution

import re

N = int(input())
s = ''
for i in range(N):
    s += input() + '\n'

sn = re.sub(r"( && )", "", str(re.sub(r"(?= && )", ' and ', s)))
print(re.sub(r"( \|\| )", "", str(re.sub(r"(?= \|\| )", ' or ', sn))))

#Ex.81 - Validating Roman Numerals

regex_pattern = r"M{,3}(C(M|D)|D?C{,3})(X(C|L)|L?X{,3})(I(V|X)|V?I{,3})$"	# Do not delete 'r'.
import re
print(str(bool(re.match(regex_pattern, input()))))

#Ex.82 - Validating phone numbers

import re
regnum = r'^[789]\d{9}$'
n = int(input())
St = [input() for _ in range(n)]
for i in St:
    if bool(re.match(regnum, i)):
        print('YES')
    else:
        print('NO')

#Ex.83 - Validating and Parsing email addresses

import re
import email.utils
n = int(input())
ems = [input() for _ in range(n)]
pat = r'^[a-zA-Z][\w\.\-]*\@[a-zA-Z]*\.[a-zA-Z]{1,3}$'
for i in ems:
    if re.match(pat, email.utils.parseaddr(i)[1]):
        print(i)

#Ex.84 - Hex Color Code

import re

colpat = r'#[0-9a-fA-F]{3,6}'
n = int(input())
S = [input() for _ in range(n)]
for s in S:
    l = s.split()
    if len(l)>1 and len(re.findall(colpat, s)) and '#' not in l[0]:
        print(*re.findall(colpat, s), sep = '\n')

#Ex.85 - Validating UID

import re

n = int(input())
pat = r'^(?:([A-Za-z0-9])(?!.*\1))*$'

for _ in range(n):
    s = input()
    if re.match(pat, s) and len(s)==10 and len(re.findall(r'[A-Z]', s)) > 1 and len(re.findall(r'[0-9]', s)) > 2:
        print('Valid')
    else:
        print('Invalid')

#Ex.86 - Validating Credit Card Numbers

import re

pat = '^[456]\d{3}(\-?\d{4}){3}$'
n = int(input())
for i in range(n):
    s = input()
    if re.match(pat, s) and not re.search(r'^\d*(\d)\1\1\1\d*$', s.replace('-', '')):
        print('Valid')
    else:
        print('Invalid')

#Ex.87 - Validating Postal Codes

regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=((\d)\d\2))"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Ex.88 - Matrix Script

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decode = ''

for i in range(m):
    for j in matrix:
        decode += j[i]

pat = r'(?<=\w)\W+(?=\w)'
print(re.sub(pat, ' ', decode))

#Ex.89 - HTML Parser - Part 1

from html.parser import HTMLParser 

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for a in attrs:
            print('->', a[0], '>', a[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for a in attrs:
            print('->', a[0], '>', a[1])
   

parser = MyHTMLParser()

N = int(input())
for _ in range(N):
    s = input()
    parser.feed(s)

#Ex.90 - HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment", data, sep= '\n')
            
        else:
            print(">>> Single-line Comment", data, sep = '\n')
            
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data", data, sep = '\n')
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Ex.91 - Detect HTML Tags, Attributes, and Attribute Values

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ( tag)
        for a in attrs:
            print('->', a[0], '>', a[1])
   
parser = MyHTMLParser()
N = int(input())
for _ in range(N):
    s = input()
    parser.feed(s) 


##Problem 2 - Challenges

#Ex.1 - Birthday Cake Candles

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    m = max(ar)
    return(ar.count(m))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

#Ex.2 - Kangaroo

def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        out = 'NO'
    else:
        p1 = x1 + v1
        p2 = x2 + v2
        out = 'NO'
        while p1 <= p2:
            if p1 == p2:
                out = 'YES'
            p1 += v1
            p2 += v2
    return out
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Ex.3 - Viral Advertising

def viralAdvertising(n):
    l = math.floor(5/2)
    s = l*3
    for i in range(1, n):
        l += math.floor(s/2)
        s = math.floor(s/2)*3
    return(l)

#Ex.4 - Recursive Digit Sum

def superDigit(n, k):
    c = str(n)
    s = sum([int(i) for i in c])*k
    if len(str(s))>1:
        s = superDigit(s, 1)
    return s

#Ex.5 - Insertion Sort - Part 1

def insertionSort1(n, arr):
    el = arr[n-1]
    while el < arr[n-2] and n>1:
        arr[n-1] = arr[n-2]
        n -= 1
        print(*arr)
    arr[n-1] = el
    print(*arr)   

#Ex.6 - Insertion Sort - Part 2

def insertionSort1(n, arr):
    el = arr[n-1]
    while el < arr[n-2] and n>1:
        arr[n-1] = arr[n-2]
        n -= 1
    arr[n-1] = el
    return arr 

def insertionSort2(n, arr):
    for i in range(2, n+1):
        arr[:i] = insertionSort1(i, arr[:i])
        print(*arr)







