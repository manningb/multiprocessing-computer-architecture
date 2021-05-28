def check_prime(num):
    from timeit import default_timer as timer 
    t1 = timer()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", int(timer()-t1))
                break
        else:
            print(num,"is a prime number")
            print("Time:", timer()-t1) 
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    return res
