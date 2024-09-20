def calculate_pay(hourly_wage, hours_worked, is_holiday):
    # If it's a holiday, add 50% to the hourly wage (holiday bonus pay)
    if is_holiday.lower() == 'yes':
        hourly_wage += hourly_wage / 2  # 50% bonus for holiday pay

    # Calculate the gross pay by multiplying hours worked with the (possibly modified) hourly wage
    gross_pay = round(hours_worked * hourly_wage, 2)

    # Calculate taxes based on the gross pay
    med = round(0.0145 * gross_pay, 2)      # Medicare tax is 1.45%
    osadi = round(0.062 * gross_pay, 2)     # Social Security tax is 6.2%
    withhold = round(0.0495 * gross_pay, 2) # State income tax (IL) is 4.95%

    # Total tax is the sum of the individual taxes
    total_tax = round(med + osadi + withhold, 2)

    # Net pay is what's left after taxes are subtracted from gross pay
    net_pay = round(gross_pay - total_tax, 2)

    # Return the gross pay, total tax, and net pay
    return gross_pay, total_tax, net_pay


def main():
    days = []  # List to store pay details for each day
    while True:  # Loop until the user decides to stop
        hourly_wage = float(input("Enter your hourly wage: "))
        
        # Get input for hours and convert to decimal format if necessary
        hours_input = input("Enter the number of hours (in decimal form or hours minutes separated by a dot): ")
        if '.' in hours_input:  # If there's a dot, split into hours and minutes
            hours, minutes = map(float, hours_input.split('.'))
            hours_worked = hours + minutes / 60  # Convert minutes into a fraction of an hour
        else:
            hours_worked = float(hours_input)  # If no dot, treat the input as decimal hours
            
        # Round hours worked to two decimal places
        hours_worked = round(hours_worked, 2)
        
        holiday_pay = input("Was this on a holiday? (yes/no): ")

        # Calculate the pay for this day using the calculate_pay function
        gross_pay, total_tax, net_pay = calculate_pay(hourly_wage, hours_worked, holiday_pay)
        
        # Display the results for this day including hours worked and hourly wage
        print(f"\n--- Pay for the day ---")
        print(f"Hours worked: ${hours_worked}")     # Print the hours worked
        print(f"Hourly wage: ${hourly_wage}")       # Print the hourly wage
        print(f"Gross Pay: ${gross_pay}")           # Print the gross pay
        print(f"Total Tax: ${total_tax}")           # Print the total tax
        print(f"Net Pay: ${net_pay}\n")             # Print the net pay

        # Store the hours worked along with the pay details in the list
        days.append((hours_worked, gross_pay, total_tax, net_pay))

        # Ask the user if they want to add another day
        continue_input = input("Do you want to add another day? (yes/no): ")
        if continue_input.lower() != 'yes':  # If the answer is not 'yes', exit the loop
            break

    # Calculate total hours worked, total gross pay, total tax, and total net pay
    total_hours_worked = sum(day[0] for day in days)  # Sum all hours worked
    total_gross = sum(day[1] for day in days)         # Sum all gross pay values from the list
    total_tax = sum(day[2] for day in days)           # Sum all tax values from the list
    total_net = sum(day[3] for day in days)           # Sum all net pay values from the list
    
    # Display the totals
    print("\nSummary for all days:")
    print(f"Total Hours Worked: ${total_hours_worked}")  # Print the total hours worked
    print(f"Total Gross Pay: ${total_gross}")
    print(f"Total Tax: ${total_tax}")
    print(f"Total Net Pay: ${total_net}")


# This Runs the program
if __name__ == "__main__":
    main()
