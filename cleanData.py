# Import Pythons built in csv lib
import csv


# In a normal project the file path would be a dynamic link passed in at runtime ideally from some sort of config file
# Since this is just a personal project I will keep this value static. If you want to run this yourself just edit
# The git_repo_path to point to wherever the git repo got cloned.
# There is also some value in using the Python Path library to standardize these paths 
# So they could work with any operating system as opposed to now where due to the \\ notation they only work on windows
git_repo_path = "C:\\Users\\aidan\\Documents\\GitHub\\DataAnalysis\\"

# These are the paths within the repo, these will always be static
input_path = "archive_unzip\\dirty_cafe_sales.csv"
output_path = "output\\clean_cafe_sales.csv"

# Output full path for logging purposes
print(git_repo_path + input_path)

# Here we will define a short function to help us later. This will let us quickly test if a value is a number or not
def is_any_num(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


# Here we create a dictionary of our valid items sold with their prices which will come in handy for checking
# All items are uppercase as we will be standardizing capitalization to all uppercase
valid_items = {"COFFEE" : 2, "TEA" : 1.5, "SANDWICH" : 4, "SALAD" : 5, "CAKE" : 3, "COOKIE" : 1, "SMOOTHIE" : 4, "JUICE" : 3}
# We can also define some other valid options for the other fields of data
valid_payments = {"CASH", "CREDIT CARD", "DIGITAL WALLET"}
valid_places = {"IN-STORE", "TAKEAWAY"}

# Our data comes in the form of a csv where each line is a different transaction record
# Here we will open the file and begin looping through each line
with open(git_repo_path + input_path) as file:

    # This reads in the data so we can begin looping
    reader = csv.DictReader(file)

    # We will be writing the cleaned data to a new csv which we open here
    with open(git_repo_path + output_path, 'w', newline = '') as out_file:
        #opens the output file we will be writing data to
        writer = csv.DictWriter(out_file, reader.fieldnames)
        # Writes the header with the same columns as the unclean data
        writer.writeheader()

        # Here we actually begin looping
        for response in reader:

            # In each loop we will do a seperate check for each field that is supposed to be here, defined as:
            # Transaction ID, Item, Quantity, Price Per Unit, Total Spent, Payment Method, Location, Transaction Date



            # Theres not a lot of checking we can do for the ID but we can check if it exists, is its proper length and 
            # That the first four characters are TXN_
            id = response["Transaction ID"]
            if not id:
                id = 'UNKNOWN'
            elif len(id) != 11:
                id = 'UNKNOWN'
            elif id[0:4] != "TXN_":
                id = 'UNKNOWN'


            # For the item we can check if its part of the valid_items dict we define above
            # We also will standardize each item to be all uppercase
            item = response["Item"].upper()
            if item not in valid_items:
                item = "UNKNOWN"


            # For the quantity we can check if its a whole number with the Python isdigit function
            quantity = response["Quantity"]
            if not quantity.isdigit():
                quantity = "UNKNOWN"

            # For the price_per_unit we can use the above defined function to check it is any number
            price_per_unit = response["Price Per Unit"]
            if not is_any_num(price_per_unit):
                # If price_per_unit is not a number but we do know what item it was then we can fix the error
                if item != "UNKNOWN":
                    price_per_unit = valid_items[item]
                else:
                    price_per_unit = "UNKNOWN"

    
            # Fir titak spent we will check its any number
            total_spent = response["Total Spent"]
            # if the total spent is not a valid value and we know the item and quantity then we can fix it
            # else we set it to unknown
            if not is_any_num(total_spent):
                if price_per_unit != "UNKNOWN" and quantity != "UNKNOWN":
                    total_spent = str(float(price_per_unit) * float(quantity))
                else:
                    total_spent = "UNKNOWN"

            # Now that weve cleaned quantity, price per unit, and total spent we can go back
            # and if we know two of the three we can calculate and fill in the third
            if quantity == "UNKNOWN" and price_per_unit != "UNKNOWN" and total_spent != "UNKNOWN":
                quantity = str(float(total_spent) / float(price_per_unit))
            if quantity != "UNKNOWN" and price_per_unit == "UNKNOWN" and total_spent != "UNKNOWN":
                price_per_unit = str(float(total_spent) / float(quantity))
            # We already checked the third case when we cleaned total_spent so we can skip it here

            # Here we check payment_methods against the above defined dict of valid_payments
            payment_method = response["Payment Method"].upper()
            if payment_method not in valid_payments:
                payment_method = "UNKNOWN"


            # Here we check location against the above defined dict of valid_places
            location = response["Location"].upper()
            if location not in valid_places:
                location = "UNKNOWN"

            transaction_date = response["Transaction Date"]    
            if transaction_date != "":
                if transaction_date.upper() == "ERROR" or transaction_date.upper() == "UNKNOWN":
                    transaction_date = "UNKNOWN"
                else:
                    # Here for fun lets say we wanted the dates to be in a different format from
                    # What the csv records. Currently the data are in yyyy-mm-dd but lets convert to 
                    # The format: yyyy MON dd 
                    date_split = transaction_date.split('-')
                    # Many possible ways to do this but I will just define a quick dictionary to help
                    num_to_mon = {"01" : "JAN", "02" : "FEB", "03" : "MAR", "04" : "APR", "05" : "MAY", "06" : "JUN",
                     "07" : "JUL", "08" : "AUG", "09" : "SEP", "10" : "OCT", "11" : "NOV", "12" : "DEC"}
                    transaction_date = f"{date_split[0]} {num_to_mon[date_split[1]]} {date_split[2]}"
                    #transaction_date = f"{date_split[1]}/{date_split[2]}/{date_split[0]}"

            else:
                transaction_date = "UNKNOWN"


            # Here we take all the work we did and write the clean line into the output sheet
            writer.writerow({"Transaction ID" : id, "Item" : item, "Quantity" : quantity, "Price Per Unit" : price_per_unit,
             "Total Spent" : total_spent, "Payment Method" : payment_method, "Location" : location,
              "Transaction Date" : transaction_date})
            



