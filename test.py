print("---STAR TREK CHARACTER LIST---")
n = ["Kirk", "Riker", "Picard", "Data", "Worf"]
r = ["Captain", "Commander", "Captain", "Lt. Commander", "Lieutenant" ]
d = ["Command", "Command", "Command", "Operations", "Sciences"]
i = ["1010", "1001", "0001", "1111", "1011"]
def main():
    init_database()
    display_menu()
    add_member()
    remove_member()
    update_rank()
    display_roster()
    search_crew()
    filter_by_division()
    calculate_payroll()
    count_officers()

def init_database():
    for b in range(len(n)):
        print(n[b] + " - " + r[b] + " - " + d[b] + " - " + i[b])

def display_menu():
    name = str(input("What is your full name? "))
    fav_character = str(input("Who is your favourite character from the list provided above? "))
    print(f"Student logged in is: {name} \nYour favourite character is {fav_character}!")

def add_member():
    add_name = str(input("Enter full name of new member: "))
    add_rank = str(input("Enter the rank of the new member: "))
    while add_rank not in r:
        print("Not a valid TNG rank, Try Again!")
        add_rank = str(input("Enter the rank of the new member: "))
    add_division = str(input("Enter the division of the new member: "))
    while add_division not in d:
        print("Not a valid division, Try Again!")
        add_division = str(input("Enter the division of the new member: "))
    add_id =  str(input("Enter the ID of the new member: "))
    while add_id in i:
        print("Not a unique ID number entered, Try Again!")
        add_id = str(input("Enter the ID of the new member: "))

    n.append(add_name)
    r.append(add_rank)
    d.append(add_division)
    i.append(add_id)

def remove_member():
    find_id = str(input("Enter the value of the ID you want to remove: "))
    while True:
        if find_id in i:
            idx1 = i.index(find_id)

            n.pop(idx1)
            r.pop(idx1)
            d.pop(idx1)
            i.pop(idx1)

            print("Member successfully removed!")
            break
        else:
            print("ID not found in database, Try Again!")
            find_id = str(input("Enter the name of the ID you want to remove: "))

def update_rank():
    find_member = str(input("Enter an ID value for the member you wish to update: "))
    while True:
        if find_member in i:
            idx2 = i.index(find_member)
            new_rank = str(input("Enter the new rank: "))
            r[idx2] = new_rank
            break
        else:
            print("ID value not found in database, Re-enter the ID!")
            find_member = str(input("Enter an ID value for the member you wish to update: "))

def display_roster():
    for l in range(len(n)):
        print(f"Name: {n[l]} | Rank: {r[l]} | Division: {d[l]} | ID's: {i[l]}.")

def search_crew():
    search_term = str(input("Enter a search term: "))
    for term in range(len(n)):
        if search_term in n[term] or search_term in r[term] or search_term in d[term] or search_term in i[term]:
            print(f"Matches found in:\nName: {n[term]}.\nRank: {r[term]}.\nDivision: {d[term]}.\nID: {i[term]}.")
            break
        else: 
            print("-----The term you inputted does not appear in this exact database!-----")

def filter_by_division():
    filter = str(input("Choose Command, Operations, or Sciences: "))
    for w in range(len(d)):
        match d[w]:
             case x if x == filter:
                print(f"--------------------\nName: {n[w]}.\nRank: {r[w]}.\nDivision: {d[w]}.\nID: {i[w]}.\n--------------------")

def calculate_payroll():
    credit_value = {
        "Captain" : 1000,
        "Commander": 500,
        "Lt. Commander": 750,
        "Lieutenant": 250
    }
    
    total_credit_value = 0
    for rank in r:
        total_credit_value += credit_value.get(rank, 0)
    print(f"The total cost of this crew is: £{total_credit_value}!")

def count_officers():
    captain_count = r.count("Captain")
    commander_count = r.count("Commander")
    print(f"--------------------\nFor Officer count:\nCaptain appears in the database {captain_count} times!\nCommander appears in the database {commander_count} times!\n--------------------")

main()