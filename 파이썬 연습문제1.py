#3번
print("홍길동씨의 주민등록번호")
pin = "881120-1068234"
YYYYMMDD = pin[0:6]
Rest = pin[7:]
print(YYYYMMDD)
print(Rest)

#4번
print(pin[7])

#5번
a = "a:b:c:d"
print(a.replace(":","#"))

#6번
list = [1,3,5,4,2]
list.sort()
list.reverse()
print(list)

#7번
list = ['life','is','too','short']
print(list[0] + " " + list[1] + " " + list[2] + " " +  list[3])
print(' '.join(list))

#8번
t = (1,2,3)
a = (4,)
n = t + a
print(n)

#9번
a = dict()

#10번
a = {'A': 90, 'B':80, 'C':70}
print(a['B'])

#11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s = set(a)
print(s)

#12번
a = b = [1, 2, 3]
a[1] = 4
print(b)
