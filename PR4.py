while True :
    sample = []
    print("(Welcome to the Data Analyzer and transformer Program!!)")
    print("_______________________________________________________________________________")
    print("Main Menu : ")
    print("1.Input Data")
    print("2.Display Data Summary")
    print("3.Calculate Factorial")
    print("4.Filter Data by Threshold")
    print("5.Sort Data")
    print("6.Display Dataset Statistics")
    print("7.Exit program")

    choice = int(input("Please Enter the choice = "))
    print()
    if choice==1 :
        number = int(input("Enter How Much Number You Want = "))
        for i in range(number):
            element = int(input("Enter the Data for 1D array(Separated by Spaces) = "))
            sample.append(element)
        print("_______________________________________________________________________________")
        print("Data Has Been Stored Successfully!!")
    elif choice==2 :
        print(sample)
        print("Data Summary!!")
        print("- Total element : ",len(sample))
        print("- Minimun Values : ",min(sample))
        print("- Maximun Values : ",max(sample))
        print("- Sum of all Values : ",sum(sample))
        print("- Average : ",sum(sample)/len(sample))
        print("_______________________________________________________________________________")
    elif choice==3 :
        def demo(n):
            if n<1 :
                return 1
            else :
                return n * demo(n-1)
        number = int(input("Enter a Number To Calculate its Factorial : "))
        value = demo(number)
        print()
        print(f"Factorial of {number} is {value}")
        print("_______________________________________________________________________________")
    elif choice==4 :
        pass
    elif choice==5 :
        print("Sort Data!!")
        print()
        print("Choose Sorting Option:")
        print("1.Ascending")
        print("2.Decending")
        
        choice = int(input("Enter your choice = "))
        print()
        if choice==1 :
            sample.sort()
            print("Sorted Data in Ascending Order:")
            print(sample)
            print("_______________________________________________________________________________")
        elif choice==2 :
            sample.sort(reverse = True)
            print("Sorted Data in Decending Order:")
            print(sample)
            print("_______________________________________________________________________________")
        else :
            print("Invalid Output")
            print("_______________________________________________________________________________")
    elif choice==6 :
        def project(sample):
            b = min(sample)
            c = max(sample)
            d = sum(sample)
            e = sum(sample)/len(sample)
            return b,c,d,e
        a,b,c,d = project(sample)
        print("Dataset Statistics!!")
        print(f"Minimun Value : {a}",)
        print(f"Maximun Value : {b}")
        print(f"Sum of all  Values : {c}")
        print(f"Average Value : {d}")
        print("_______________________________________________________________________________")
    elif choice==7 :
        print("Thank You For Using Data Analyzer and Transformer Program. Goodbyeee!!!")
        break
    else :
        print("Invalid")
      