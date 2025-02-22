#User function Template for python3

def fizzBuzz(number):
    # Write your code here.
    if(number%3==0 and number%5==0):
        print("FizzBuzz")
    elif(number%5==0):
        print("Buzz")
    elif number%3==0:
        print("Fizz") 
    else:
        print(number)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t=int(input())
    while(t>0):
        number = int(input())
        fizzBuzz(number)
        t-=1

        print("~")
if __name__ == "__main__": 
    main()


# } Driver Code Ends