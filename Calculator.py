def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

def subtract(*args):
    diff = args[0]
    for num in args[1:]:
        diff -= num
    return diff

def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product

def divide(*args):
    quotient = args[0]
    for num in args[1:]:
        quotient /= num
    return quotient

# Initialize output files
#report_file = open('report.txt', 'w')


def print_function(nums,choice):
    if choice == 1 :
        num = ' + '.join([str(i) for i in nums])
        final_result = f"Addition of {num} : {result}\n" 
        
    elif choice == 2 :
        num = ' - '.join([str(i) for i in nums])
        final_result = f"Substract {num} : {result}\n"
        
    
    elif choice == 3 :
        num = ' * '.join([str(i) for i in nums])
        final_result = f"Multi of {num} : {result}\n"
        
    elif choice == 4 :
        num = ' / '.join([str(i) for i in nums])
        final_result = f"Divide of {num} : {result}\n"
        
    with open("report.txt", mode="w") as file:
        file.write(final_result)

def print_error(err):
    with open("error.txt", mode="w") as file:
        file.write(err)
    
    
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.exit")

# Initialize output files
#error_file = open('error.txt', 'w')

# Initialize choice
choice = None

while True:
    # Take input from the user
    try:
        choice = int(input("Enter choice(1/2/3/4/5): "))
        if choice==5:
            exit()
    except ValueError:
        print(' invalid input ')
        continue  # Restart the loop if there was an exception

    # Check that choice has been assigned a value
    if choice is None:
        continue

    # Reset the nums list for each operation
    nums = []
    err = None

    while True:
            try:
                
                num = input("Enter a number (or 'done' to finish): ")
                if num == "done":
                    break
                num = int(num)
            except:
                err = 'You Entered The String Plaase Try Again '
                print(err)
                continue

            nums.append(int(num))

            # Perform the selected calculation and write the result or error to the corresponding output file
            if choice == 1:
                try:
                    result = add(*nums)
                    print("Result:", result)
                except Exception as e:
                    err = f"Error: {str(e)}\n"
            elif choice == 2:
                try:
                    result = subtract(*nums)
                    
                    print("Result:", subtract(*nums))
                except Exception as e:
                    err = f"Error: {str(e)}\n"
            elif choice == 3:
                try:
                    result = multiply(*nums)
                    
                    print("Result:", multiply(*nums))
                except Exception as e:
                    err = f"Error: {str(e)}\n"
            elif choice == 4:
                try:
                    result = divide(*nums)
                    
                    print("Result:", divide(*nums))
                except Exception as e:
                    err = f"Error: {str(e)}\n"
            else:
                err = "Invalid input\n"

        # Close the output files outside the while loop
    if err:    
        print_error(err)
    else:
        print_function(nums,choice)
    
    print("Operation complete. Results written to report.txt and any errors written to error.txt.")
    
    

