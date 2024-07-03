import bill
import flatmate as flat
import pdf_report as report

def ask_for_bill() -> tuple:
    """
    Asks for a bill amount and data, then asks for user input for two flatmates - names and days spend in house
    """    
    
    bill_amount = float(input("Enter the bill amount: "))
    bill_date = input("Enter the bill date. E.g. June 2024: ")
    print("Flatmate 1 information ->")
    flatmate1_name = input("Enter the name of the flatmate: ")
    flatmate1_days = int(input("Enter the number of the days that {} in house: ".format(flatmate1_name)))
    print("Flatmate 2 information ->")
    flatmate2_name = input("Enter the name of the flatmate: ")
    flatmate2_days = int(input(f"Enter the number of the days that {flatmate2_name} stayed in house: "))
    
    bill_to_pay = bill.Bill(amount = bill_amount, period = bill_date)
    flatmate1 = flat.Flatmate(name = flatmate1_name, days_in_house= flatmate1_days)
    flatmate2 = flat.Flatmate(flatmate2_name, flatmate2_days)
    
    return  bill_to_pay, flatmate1, flatmate2

if __name__ == "__main__":
    
    print("-----Flatmate bill splitting-----")
    bill_to_pay, flatmate1, flatmate2 = ask_for_bill() 
    print("Thank you for your input! Calculating the due amounts....")
    print(f"{flatmate1.name} pays: {flatmate1.pays(bill = bill_to_pay, other_flat_mate_days = flatmate2)}")
    print("{}: {}".format(flatmate2.name, flatmate2.pays(bill = bill_to_pay, other_flat_mate_days = flatmate1)))
    print("Report ready - please check the bill")
    
    pdf = report.PdfReport("bill")
    pdf.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill_to_pay)
    