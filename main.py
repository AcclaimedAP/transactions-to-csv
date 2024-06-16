import re
import sys

def read_file(file):
    transactions = []
    with open(file, encoding='utf-8') as f:
      for line in f:
        transactions.append(line)
    return transactions

def extract_date(transaction):
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', transaction)
    if date_match:
        return date_match.group()
    else:
        print("No date found in transaction")
        print(transaction)
        return None

def extract_balance(transaction):
    balance_match = re.search(r'-?\d{1,3}(?:\s\d{3})*,\d{2}', transaction)
    if balance_match:
        return balance_match.group()
    else:
        print("No balance found in transaction:")
        print(transaction)
        return None


def extract_amount(transaction):
    amount_match = re.search(r'-?\d{1,3}(?:\s\d{3})*,\d{2}', transaction)
    if amount_match:
        return amount_match.group()
    else:
        print("No amount found")
        print(transaction)
        return None
    

def main(file_path="data.txt"):
    transactions = read_file(file_path)
    formatted_transactions = []
    for transaction in transactions:
        formatted_transaction = {}
        date = extract_date(transaction)
        transaction = transaction.replace(date, "")
        amount = extract_amount(transaction)
        transaction = transaction.replace(amount, "")
        balance = extract_balance(transaction)
        transaction = transaction.replace(balance, "")
        reference = transaction.strip()
        formatted_transaction["reference"] = f"\"{reference}\""
        formatted_transaction["date"] = date
        formatted_transaction["balance"] = f"\"{balance}\""
        formatted_transaction["amount"] = f"\"{amount}\""
        formatted_transactions.append(formatted_transaction)

    with open("formatted_data.csv", "w", encoding="utf-8") as f:
        f.write("Reference, Date, Amount, Balance\n")
        for transaction in formatted_transactions:
            f.write(f"{transaction['reference']}, {transaction['date']}, {transaction['amount']}, {transaction['balance']}\n")

if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    main(file_path)