# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# ADD YOUR CODE HERE

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savingsBalance = float(input ("What is your current savings balance? "))
    savingsInterestRate = float(input("What is your current interest rate? "))
    SavingsMonths = float(input("How many months? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savingsinterest_earned = create_cd_account(savingsBalance,savingsInterestRate,SavingsMonths)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'Your savings account has earned ${savingsinterest_earned:,.2F}')
    print(f'Your savings account now has ${updated_savings_balance:,.2F}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cdBalance = float(input("What is your CD balance? "))
    cdInterest = float(input("What is your CD interest? "))
    cdMonths = int(input("How many months? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, CDinterest_earned = create_cd_account(cdBalance, cdInterest, cdMonths)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"You have earned ${updated_cd_balance:,.2F} ")
    print(f"Your CD has earned ${CDinterest_earned:,.2F}")

if __name__ == "__main__":
    # Call the main function.
    main()

