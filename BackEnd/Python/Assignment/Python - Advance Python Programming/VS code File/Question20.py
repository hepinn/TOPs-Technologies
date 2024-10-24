# Q.20 Write python program that user to enter only odd numbers, else will raise an exception.

class OddNumberError(Exception):
    """Custom exception for even numbers."""
    pass

def get_odd_number():
    while True:
        try:
            user_input = input("Please enter an odd number: ")
            number = int(user_input)  
            
            if number % 2 == 0:  
                raise OddNumberError("That's an even number! Please enter an odd number.")
            
            print(f"Thank you! You entered the odd number: {number}")
            break  
        
        except ValueError:
            print("Invalid input! Please enter an integer.")
        
        except OddNumberError as e:
            print(e)

if __name__ == "__main__":
    get_odd_number()
