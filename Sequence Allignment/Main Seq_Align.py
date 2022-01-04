print("\t\t\t==> Welcome To <==\t")
print("\t |===>> Sequence Alignment <<===|\n")
print("\t(1)> DNA\t\t(2)> Protein\n")

choice_x = choice_y = 0

while (choice_x != 1 and choice_x != 2):
    choice_x = int(input("Your Choice is: "))
    ##################################################
    if (choice_x == 1):  # DNA
        print('\n' * 50)
        print("\t |===>>   DNA Seq Align  <<===|\n")
        print("\t(1)> Global\t\t(2)> Local\n")

        while (choice_y != 1 and choice_y != 2):
            choice_y = int(input("Your Choice is: "))
            #########################
            if (choice_y == 1):  # Global DNA
                print('\n' * 50)
                exec(open('DNA/Global_Dna.py').read())

            #########################
            elif (choice_y == 2):  # Local DNA
                print('\n' * 50)
                exec(open('DNA/Local_Dna.py').read())

            #########################
            else:
                print("\t\tInvalid Choice")

    ##################################################
    elif (choice_x == 2):  # Protein
        print('\n' * 50)
        print("\t |===>> Protein Seq Align <<===|\n")
        print("\t(1)> Global\t\t(2)> Local\n")

        while (choice_y != 1 and choice_y != 2):
            choice_y = int(input("Your Choice is: "))
            #########################
            if (choice_y == 1):  # Global Protein
                print('\n' * 50)
                exec(open('PROTEIN/Global_Protein.py').read())

            #########################
            elif (choice_y == 2):  # Local Protein
                print('\n' * 50)
                exec(open('PROTEIN/Local_Protein.py').read())

            #########################
            else:
                print("\t\tInvalid Choice")

    ##################################################
    else:
        print("\t\tInvalid Choice")