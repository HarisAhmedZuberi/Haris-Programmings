# ================ Try Except ========================

'''try:
    print(x)
except:
    print('an error occured!')'''

# when more than one error occurs
'''try:
    print(x)
except NameError:
    print('variable x is not defined!')
except:
    print('an error occured!')'''

# when more than one error occurs and use of else statement
'''try:
    x = 'Haris Chingezi'
    print(x)
except NameError:
    print('variable x is not defined!')
except:
    print('an error occured!')
else:
    print('there is no error')'''

# when more than one error occurs and use of finally statement
'''try:
    #x = 'Haris Chingezi'
    print(x)
except NameError:
    print('variable x is not defined!')
except:
    print('an error occured!')
finally:
    print('the \'try except\' statement executed')'''

'''try:
    try:
        #x = 5
        print(x)
    except:
        print('there is no error!')
except:
    print('executed')'''

'''f = open('haris.txt')
print(f)
print(f.read(5))


h = open('G:\\bilal.txt', 'rt')
print(h.read(10))
print(h.read(5))'''

'''d = open('haris.txt')
print(d.readline())
print(d.readline())
print(d.readline())'''

'''a = open('haris.txt')
for x in a:
    print(x)
'''

b = open('G:\\bilal.txt')
print(b.readline())
b.close()
