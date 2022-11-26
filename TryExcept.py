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

try:
    try:
        #x = 5
        print(x)
    except:
        print('there is no error!')
except:
    print('executed')
