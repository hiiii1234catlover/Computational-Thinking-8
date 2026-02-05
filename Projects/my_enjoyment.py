def run_cool_tester():
    """
    An interactive 'cool tester' that checks for a secret code.
    """
    print("Welcome to the Cool Tester 3000!")
    print("Test your knowledge and see if you are cool enough to proceed.")

    secret_code = "fire"
    
    while True:
        # Get user input
        user_input = input("Enter the secret code: ").strip().lower()

        # Check the input and provide "cool" feedback
        if user_input == secret_code:
            print("\n🎉 Access Granted! 🎉")
            print("You are officially cool. Welcome to the club!")
            input("now that you are officially cool I can trust you with this info")
            input("I am planing to have a sleep over with all cool people ")
            input("since you know the passcode you can come")
            input("text me march 20 2026")
            input("bye")
            
            break  # Exit the loop/tester
        elif user_input == "exit":
            print("\nGoodbye! You can try again anytime.")
            break
        
        else:
            print("\n❌ Incorrect code. ❌")
            print("Hint: It involves me.")
            print("Try again, or type 'exit' to quit.")
        
if __name__ == "__main__":
    run_cool_tester()