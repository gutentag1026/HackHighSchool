import csv

def prep_data(csv_file):
    data = {
        "states": {},
        "capitals": {}
    }
    with open(csv_file) as cap_csv:
        reader = csv.DictReader(cap_csv)
        for row in reader:
            state = row["states"].lower()
            capital = row["capitals"].lower()
            data["states"][state] = capital
            data["capitals"][capital] = state
    return data


if __name__ == "__main__":
    data = prep_data("capitols.csv")
    query = None
    while query != "done":
        query = input("Ready: ").strip().lower()
        print(data["states"].get(query,data["capitals"].get(query, "nil")))
