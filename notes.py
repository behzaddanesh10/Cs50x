import csv
def main():

    try:
        while True:
            x = input("Was soll ich machen? ")
            y = "Notes:  "
            with open("notes.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([y, x])


    except EOFError:
        pass

if __name__ == '__main__':
    main()






