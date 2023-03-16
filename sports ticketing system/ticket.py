import string
#to write data to "ticket_output.txt"
ticket_writer = open("ticket_output.txt","w")
category_list = []
category_row_dict = {}
category_column_dict = {}
information_list = []
seat_dict = {}
job_dict = {}
letters_to_numbers_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
#This function creates category
def CREATECATEGORY(category,capacity,information):
    capacity_calculator = int(capacity.split("x")[0])*int(capacity.split("x")[1])
    if category not in category_list:
        print(f"The category '{category}' having {capacity_calculator} seats has been created.")
        ticket_writer.write(f"The category '{category}' having {capacity_calculator} seats has been created."+"\n")
        category_list.append(category)
        seat_dict[category] = []
        category_row_dict[category] = int(capacity.split("x")[0])
        category_column_dict[category] = int(capacity.split("x")[1])
        information_list.append(information)
    else:
        print(f"Warning: Cannot create the category for the second time. The stadium has already {category}")
        ticket_writer.write(f"Warning: Cannot create the category for the second time. The stadium has already {category} "+"\n")
#This function sells tickets
def SELLTICKET(name,job,category,seat):
    if category in category_list:
        for i in seat:
            seat_number = 0
            if "-" in i:
                if category_row_dict[category] < int(i.split("-")[1]):
                    print("Error: The category '{}' has less column than the specified index {}!".format(category,i))
                    ticket_writer.write("Error: The category '{}' has less column than the specified index {}!\n".format(category,i))
                else:
                    for j in range(int(i.split("-")[0][1:]),int(i.split("-")[1])+1):
                        if i.split("-")[0][0]+str(j) not in seat_dict[category]:
                            if seat_number == 0:
                                seat_dict[category].append(i.split("-")[0][0]+str(j))     
                                job_dict[i.split("-")[0][0]+str(j)] = job
                        else:
                            seat_number += 1
                    if seat_number == 0:
                        print("Success: {} has bought {} at {}".format(name,i.rstrip("\n"),category))
                        ticket_writer.write("Success: {} has bought {} at {}\n".format(name,i.rstrip("\n"),category))
                    else:
                        print("Error: The seats {} cannot be sold to {} due some of them have already been sold!".format(i.rstrip("\n"),name))
                        ticket_writer.write("Error: The seats {} cannot be sold to {} due some of them have already been sold!\n".format(i.rstrip("\n"),name))
            else:
                if category_row_dict[category] < int(i[1:]):
                    print("Error: The category '{}' has less column than the specified {}!".format(category,i))
                    ticket_writer.write("Error: The category '{}' has less column than the specified {}!\n".format(category,i))
                else:
                    if i not in seat_dict[category]:
                        print("Success: {} has bought {} at {}".format(name,i.rstrip("\n"),category))
                        ticket_writer.write("Success: {} has bought {} at {}\n".format(name,i.rstrip("\n"),category))
                        seat_dict[category].append(i.rstrip("\n"))
                        job_dict[i.rstrip("\n")] = job
                    else:
                        print("Warning: The seat {} cannot be sold to {} since it was already sold!".format(i.rstrip("\n"),name))
                        ticket_writer.write("Warning: The seat {} cannot be sold to {} since it was already sold!\n".format(i.rstrip("\n"),name))
                        seat_number += 1
    else: 
        print("No such '{}' has been created.".format(category))
        ticket_writer.write("No such '{}' has been created.".format(category))
#This function cancels the ticket
def CANCELTICKET(category,seat):
    if category in category_list:
        for i in seat:
            if category_row_dict[category] < int(i[1:]):
                print("Error: The category '{}' has less column than the specified {}!".format(category,i.rstrip("\n")))
                ticket_writer.write("Error: The category '{}' has less column than the specified {}!\n".format(category,i.rstrip("\n")))
            else:
                if i.rstrip("\n") in seat_dict[category]:
                    print("Success: The seat {} at '{}' has been canceled and now ready to sell again".format(i.rstrip("\n"),category))
                    ticket_writer.write("Success: The seat {} at '{}' has been canceled and now ready to sell again\n".format(i.rstrip("\n"),category))
                    seat_dict[category].remove(i.rstrip("\n"))
                    del job_dict[i.rstrip("\n")]
                else:
                    print("Error: The seat {} at '{}' has already been free! Nothing to cancel".format(i.rstrip("\n"),category))
                    ticket_writer.write("Error: The seat {} at '{}' has already been free! Nothing to cancel\n".format(i.rstrip("\n"),category))
    else:
        print("No such '{}' has been created.".format(category))
        ticket_writer.write("No such '{}' has been created.\n".format(category))
#This function shows the number of students, full and season tickets in the selected category, as well as the total money.
def BALANCE(category):
    if category in category_list:
        number_of_students = 0
        number_of_full = 0
        number_of_season = 0
        print("Category report of '{}'".format(category.rstrip("\n")))
        ticket_writer.write("Category report of '{}'\n".format(category.rstrip("\n")))
        print("--------------------------------")
        ticket_writer.write("--------------------------------\n")
        for j in seat_dict[category]:
                if job_dict[j] == "student":
                    number_of_students += 1
                elif job_dict[j] == "full":
                    number_of_full += 1
                elif job_dict[j] == "season":
                    number_of_season += 1
        print("Sum of students = {}, Sum of full pay = {}, Sum of seasons ticket = {} and Revenues = {} Dollars".format(number_of_students,number_of_full,number_of_season,10*number_of_students+20*number_of_full+250*number_of_season))
        ticket_writer.write("Sum of students = {}, Sum of full pay = {}, Sum of seasons ticket = {} and Revenues = {} Dollars\n".format(number_of_students,number_of_full,number_of_season,10*number_of_students+20*number_of_full+250*number_of_season))
#this function shows the tickets with empty tickets sold by category
def SHOWCATEGORY(category):
    print("Printing category layout of {}".format(category))
    ticket_writer.write("Printing category layout of {}\n".format(category))
    matrix = [["X" for i in range(category_row_dict[category])] for j in range(category_column_dict[category])]
    for i in seat_dict[category]:
        if job_dict[i] == "student":
            matrix[letters_to_numbers_dict[i[0]]][int(i[1:])] = "S"
        elif job_dict[i] == "full":
            matrix[letters_to_numbers_dict[i[0]]][int(i[1:])] = "F"
        elif job_dict[i] == "season":
            matrix[letters_to_numbers_dict[i[0]]][int(i[1:])] = "T"
    for i in range(category_row_dict[category]):
        row = category_row_dict[category] - i - 1
        print(f"{chr(row+65)}  {'  '.join(matrix[row])}")
        ticket_writer.write(f"{chr(row+65)} {'  '.join(matrix[row])}"+"\n")
    print(" ",end=" ")
    ticket_writer.write(" ")
    for i in range(category_row_dict[category]):
        if i < 10:
            print(" {}".format(i),end=" ")
            ticket_writer.write(" {} ".format(i))
        elif 10 <= i < category_row_dict[category] - 1:
             print("{}".format(i),end=" ")
             ticket_writer.write("{} ".format(i))
        else:
            print("{} ".format(i))
            ticket_writer.write("{} \n".format(i))
##to read data from "ticket_input.txt"
file = open("ticket_input.txt","r")
data = file.readlines()
data = [a.split(" ") for a in data]
for i in data:
    if i[0] == "CREATECATEGORY":
        CREATECATEGORY(i[1],i[2],i)
    elif i[0] == "SELLTICKET":
        SELLTICKET(i[1],i[2],i[3],i[4:])
    elif i[0] == "CANCELTICKET":
        CANCELTICKET(i[1],i[2:])
    elif i[0] == "BALANCE":
        BALANCE(i[1].rstrip("\n"))
    elif i[0] == "SHOWCATEGORY":
        SHOWCATEGORY(i[1].rstrip("\n"))
