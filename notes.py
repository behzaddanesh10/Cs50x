import csv
def main():

    try:
        while True:
            x = input("Notes: ")
            y = "Was soll ich machen?  "
            with open("notes.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([y, x])


    except EOFError:
        pass

if __name__ == '__main__':
    main()






