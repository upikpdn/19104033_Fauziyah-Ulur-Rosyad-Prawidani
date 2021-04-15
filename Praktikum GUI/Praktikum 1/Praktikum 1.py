Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 9
>>> type(x)
<class 'int'>
>>> x = true
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x = true
NameError: name 'true' is not defined
type
>>> x = 9
>>> type(x)
<class 'int'>
>>> x = True
>>> type(x)
<class 'bool'>
>>> x = 'contoh'
>>> type(x)
<class 'str'>
>>> 
>>> x = 9
>>> id(x)
2108763892272
>>> y = 3
>>> id(y)
2108763892080
>>> del y
>>> y
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> x
9
>>> id(x)
2108763892272
>>> x = True
>>> 
>>> posisi = (300, 300)
>>> posisi
(300, 300)
>>> 
>>> Posisi
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    Posisi
NameError: name 'Posisi' is not defined
>>> 
>>> a = 1; b = 1; c = 3
>>> print(a); print (b); print(c)
1
1
3
>>> x = 9
>>> if isinstance(x, int) and \
   x > 0 and \
   x%2 == 1 :
	print(%d "adalah bilangan bulat ganjil positif" %x)
	
SyntaxError: invalid syntax
>>> x = 9
if isinstance(x, int) and \
   x > 0 and \
   x%2 == 1 :
	print("%d adalah bilangan bulat ganjil positif" %x)
	
SyntaxError: multiple statements found while compiling a single statement
>>> x = 9
>>> if isinstance(x, int) and \
   x > 0 and \
   x%2 == 1 :
	print("%d adalah bilangan bulat ganjil positif" %x)
	
SyntaxError: multiple statements found while compiling a single statement
>>> x = 9
>>> if isinstance(x, int) and \
   x > 0 and \
   x%2 == 1 :
	print("%d adalah bilangan bulat ganjil positif" %x)

	
9 adalah bilangan bulat ganjil positif
>>> print("Pemrograma GUI" + "dengan Python dan PyQt")
Pemrograma GUIdengan Python dan PyQt
>>> data = [
	100,
	200,
	300
	]
>>> kamus = {
	'one' : 'satu',
	'book' : 'buku',
	'what' : 'apa'
	}
>>> data
[100, 200, 300]
>>> kamus
{'one': 'satu', 'book': 'buku', 'what': 'apa'}
>>> a = 0b1001 #bil biner
>>> b = 0o23 #bil oktal
>>> c = 0x2f #bil heksadesimal
>>> a
9
>>> b
19
>>> c
47
>>> a = True
>>> type(a)
<class 'bool'>
>>> int(a)
1
>>> a = 12
>>> id(a)
2108763892368
>>> a +=3
>>> a
15
>>> id(a)
2108763892464
>>> a = 12.432
>>> a
12.432
>>> a*3
37.296
>>> s1 = 'Pemrograman Python'
>>> s2 = "Pemrograman Python 2"
>>> s3 = '''Pemrograman
python 3'''
>>> 
>>> s1 = 'Pemrograman Python'
>>> s2 = "Pemrograman Python 2"
>>> s3 = '''Pemrograman Python 3'''
>>> s1[0], s1[1], s1[2]
('P', 'e', 'm')
>>> data = 'p023\tbolpoin\t\bp2\tpenghapus\t\t3000
SyntaxError: EOL while scanning string literal
>>> data = 'p023\tbolpoin\t\bp2\tpenghapus\t\t3000'
>>> print(data)
p023	bolpoin	p2	penghapus		3000
>>> data = 'p023\tbolpoin\t\nj2\tpenghapus\t\t3000'
>>> print(data)
p023	bolpoin	
j2	penghapus		3000
>>> s1 = 'Python'
>>> s2 = 'PYTHON'
>>> s1 == s2
False
>>> s1 != s2
True
>>> s1 < s2
False
>>> s1 > s2
True
>>> s = 'Pemrograman Python dan PyQt'
>>> s1 = s[0:11]
>>> s1
'Pemrograman'
>>> len(s1)
11
>>> s = s[:11]
>>> s = s[:8]
>>> s = s[8:]
>>> s = s[0:11:2]
>>> s = s[0:11:1]
>>> s = s[0:11:3]
>>> s
''
>>> 
>>> s = 'balonku ada %d, meletus %d tinggal %f' %(5,1,4.5)
>>> s
'balonku ada 5, meletus 1 tinggal 4.500000'
>>> s = 'balonku ada %d, meletus %d tinggal %f' %(5,1,4)
>>> s
'balonku ada 5, meletus 1 tinggal 4.000000'
>>> list = ['piring', 'ani', 'ada', 2]
>>> list
['piring', 'ani', 'ada', 2]
>>> for item in list :
	print(item)

	
piring
ani
ada
2
>>> del list ['piring']
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    del list ['piring']
TypeError: list indices must be integers or slices, not str
>>> del list['piring']
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    del list['piring']
TypeError: list indices must be integers or slices, not str
>>> del list['piring_list']
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    del list['piring_list']
TypeError: list indices must be integers or slices, not str
>>> list.insert(2, 'kaca')
>>> list
['piring', 'ani', 'kaca', 'ada', 2]
>>> list.del('kaca')
SyntaxError: invalid syntax
>>> list.del['kaca']
SyntaxError: invalid syntax
>>> del list(2,'kaca')
SyntaxError: cannot delete function call
>>> del list[2]
>>> list
['piring', 'ani', 'ada', 2]
>>> list.insert(1, 'kaca')
>>> list
['piring', 'kaca', 'ani', 'ada', 2]
>>> del list[0]
>>> list
['kaca', 'ani', 'ada', 2]
>>> extend(['besar'])
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    extend(['besar'])
NameError: name 'extend' is not defined
>>> list.extend(['besar'])
>>> list
['kaca', 'ani', 'ada', 2, 'besar']
>>> list[5] = 'kecil'
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    list[5] = 'kecil'
IndexError: list assignment index out of range
>>> 