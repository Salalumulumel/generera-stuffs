import os
import illness
from prettytable import PrettyTable

def printMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n---------------------------------\n")
    print("\t-MENU- \U0001F603")
    print("\t1. List of Mentall Illnesses")
    print("\t2. Add Mental Illnesses")
    print("\t3. Remove Mental Illness")
    print("\t4. End")

    choice = input("\n\tInsert choice: ")
    return choice

def createIllness():
    os.system('cls' if os.name =='nt' else 'clear')
    print("\n----------------------------------")
    type = input("\n\tChoose type: ")
    symptoms = input("\n\tChoose symptoms: ")
    treatment = input("\n\tChoose treatment: ")
    medicine =input("\n\tChoose medicine: ")
    support = input("\n\tChoose support: ")
    financialaid = input("\n\tChoose financial aid: ")

    return illness.Illness(None, type, symptoms, treatment, medicine, support, financialaid)

def printlistIllness(list_illnesses):
    os.system('cls' if os.name == 'nt' else 'clear')
    t_table = PrettyTable(['Id', 'Type', 'Symptoms', 'Treatment', 'Medicine', 'Support', 'Financial aid'])

    for illnes in list_illnesses:
        t_table.add_row([illnes.id, illnes.type, illnes.symptoms, illnes.treatment, illnes.medicine, illnes.support, illnes.financialaid])

        print(t_table)
        input("Continue? Click enter: ")

def printDeleteIllness():
    os.system('cls' if os.name == 'nt' else 'clear')
    return input("\tChose the illness you want to get rid of: ")