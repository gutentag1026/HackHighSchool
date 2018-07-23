import collections 
import csv


if __name__ == "__main__":
    with open("names.csv") as file:
        shared_firstnames = collections.defaultdict(list)
        shared_lastnames = collections.defaultdict(list)
        reader = csv.DictReader(file)
        for line in reader:
            shared_firstnames[line["First"]].append(line["Last"])
            shared_lastnames[line["Last"]].append(line["First"])

        print("** Shared First Names! **")
        for key, value in shared_firstnames.items():
            print(f"{key} ({len(value)}): {value}")


        print("** Shared Last Names! **")
        for key, value in shared_lastnames.items():
            print(f"{key} ({len(value)}): {value}")
