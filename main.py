import illness
import illnesshandler
import illness_app_menu

def main():

    
    illness_handler = illnesshandler.IllnessHandler()

    while True:
        choice = illness_app_menu.printMenu()

        if choice == "1": 

            list_illnesses = illness_handler.readSqliteTable()
            illnes = illness_app_menu.printlistIllness(list_illnesses)

        elif choice == "2":
            illnes = illness_app_menu.createIllness()
            illness_handler.addIllness(illnes)

        elif choice == "3":
            t_id = illness_app_menu.printDeleteIllness()
            illness_handler.deleteIllness(t_id)
            input("\tContinue? click enter: ")
        
        elif choice == "4":
            break

        else:
            print("Oi dickhead, you can't do that.")

main()
