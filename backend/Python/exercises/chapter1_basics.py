def ex_1_1_and_1_2():
    print("--Exercise 1.1 & 1.2")
    print("3 + 1 =",3+1)
    print("3 * 3 =",3*3)
    print("2 ** 3 =",2**3)
    print("Hello, world!")

def ex_1_3():
    print("\n--Exercise 1.3")
    print("'py' + 'thon' =",'py'+'thon')

    print("'py' * 3 + 'thon' =",'py'*3+'thon')

    #print("'py' - 'py' =",'py'-'y') # dòng này lỗi, nên comment lại

    #print("'3' + '3' =",'3'+3) # dòng này lỗi, nên comment lại

    print("3 * '3' =",3*'3')        

    #print(a) # dòng này lỗi, nên comment lại

    a = 3

    print("a =",a)

def ex_1_4():
    print("\n--Exercise 1.4")
    print("1 == 1 :",1==1) 
    print("1 == True :",1==True)
    print("0 == True :",0==True)
    print("3 == 1 * 3 :",3==1*3)  
    print("(3 == 1) * 3 :",(3 == 1) * 3) 
    print("(3 == 3) * 4 + 3 == 1 :",(3 == 3) * 4 + 3 == 1) 
    print("3**5 >= 4**4 :",3**5 >= 4**4) 

def ex_1_5():
    print("\n--Exercise 1.5")
    print("5 / 3 =",5 / 3)
    print("5 % 3 =",5 % 3) 
    print("5.0 / 3 =",5.0 / 3)
    print("5 / 3.0 =",5 / 3.0)
    print("5.2 % 3 =",5.2 % 3)
    print("2001 ** 200 =",2001 ** 200)

def ex_1_6():
    print("\n--Exercise 1.6")
    # Kết quả sẽ quá lớn OverflowError
    #print("2000.3 ** 200 =",2000.3 ** 200) # dòng này lỗi, nên comment lại
    
    print("1.0 + 1.0 -1.0 =",1.0 + 1.0 -1.0)  
    print("1.0 + 1.0e20 -1.0e20 =",1.0 + 1.0e20 -1.0e20)  

def ex_1_7():
    print("\n--Exercise 1.7") 
    name = "Hung"
    print("Hello, "+name+"!") 

def ex_1_8():
    print("\n--Exercise 1.8:")
    print("float(123) ->",float(123))
    print("float('123') ->",float('123'))
    print("float('123.23') ->",float('123.23')) 
    print("int(123.23) ->",int(123.23)) 

    # ValueError int không chấp nhận ép chuỗi số thập phân
    #print("int('123.23') ->",int('123.23')) # dòng này lỗi nên comment lại

    print("int(float('123.23')) ->",int(float('123.23')))
    print("str(12) ->", str(12)) 
    print("str(12.2) ->",str(12.2))
    print("bool('a') ->",bool('a'))    
    print("bool(0) ->",bool(0))           
    print("bool(0.1) ->",bool(0.1))        

if __name__ == "__main__":
    ex_1_1_and_1_2()
    ex_1_3()
    ex_1_4()
    ex_1_5()
    ex_1_6()
    ex_1_7()
    ex_1_8()