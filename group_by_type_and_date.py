import re
import argparse

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()
    
def extract_date(transaction):
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', transaction)
    if date_match:
        return date_match.group()
    else:
        print("No date found in transaction:")
        print(transaction)
        return None

def extract_amount(transaction):
    amount_match = re.search(r'-?\d{1,3}(?:\s\d{3})*,\d{2}', transaction)
    if amount_match:
        return amount_match.group()
    else:
        print("No amount found in transaction:")
        print(transaction)
        return None
    


def main(file_path="data.txt", type="swish"):
    transactions = read_file(file_path)
    swish_transactions = []
    for transaction in transactions:
        if type.lower() in transaction.lower():
            date = extract_date(transaction)
            transaction = transaction.replace(date, "")
            amount = extract_amount(transaction)
            if amount.startswith("-"):
                continue
            swish_transactions.append((date, amount))
    swish_transactions_by_date = {}
    for date, amount in swish_transactions:
        if date in swish_transactions_by_date:
            swish_transactions_by_date[date] += float(amount.replace(",", ".").replace(" ", ""))
        else:
            swish_transactions_by_date[date] = float(amount.replace(",", ".").replace(" ", ""))
    with open(f"{type.lower()}_transactions_by_date.csv", "w", encoding="utf-8") as file:
        file.write("Date,Amount\n")
        for date, amount in swish_transactions_by_date.items():
            file.write(f"{date},\"{amount}\"\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="Type of transaction to extract", default="swish")
    parser.add_argument("--file", help="Path to the input file", default="data.txt")
    args = parser.parse_args()

    main(file_path=args.file, type=args.type)