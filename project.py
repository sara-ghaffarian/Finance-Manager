import json

class Transaction:

    def __init__(self, amount, category, transaction_type):
        self.amount=amount
        self.category=category
        self.transaction_type=transaction_type


    def to_dict(self):
        return{
            "amount": self.amount,
            "category": self.category,
            "transaction_type": self.transaction_type
        }


class FinanceManager:
    def __init__(self):
        self.transactions=[]


    def add_transaction(self, amount, category, transaction_type):

        if not validate_amount(amount):
            raise ValueError("Amount must be positive")

        if not validate_transaction_type(transaction_type):
            raise ValueError("Invalid transaction type")

        transaction = Transaction(amount, category, transaction_type)

        self.transactions.append(transaction)


    def delete_transaction(self, index):
        if 0 <= index < len(self.transactions):
            self.transactions.pop(index)
        else:
            raise IndexError("invalid index")


    def calculate_balance(self):

        balance=0
        for transaction in self.transactions:
            if transaction.transaction_type=="income":
                balance+=transaction.amount

            else:
                 balance-=transaction.amount
        return balance


    def get_top_category(self):
        category_totals={}

        for transaction in self.transactions:
            if transaction.transaction_type=="expense":
                if transaction.category not in category_totals:
                    category_totals[transaction.category] = 0
                category_totals[transaction.category] += transaction.amount

        if not category_totals:
                return None

        return max(
            category_totals,
            key=category_totals.get)


    def save_data(self):
        data=[]

        for transaction in self.transactions:
            data.append(transaction.to_dict())

        with open("transactions.json","w") as file:
            json.dump(data,file,indent=4)


    def load_data(self):

        try:
            with open("transactions.json", "r") as file:
                data=json.load(file)

            self.transactions=[]

            for item in data:
                transaction = Transaction(
                    item["amount"],
                    item["category"],
                    item["transaction_type"]
                )

                self.transactions.append(transaction)

        except FileNotFoundError:
            self.transactions=[]


    def get_total_income(self):
        total=0

        for transaction in self.transactions:
            if transaction.transaction_type=="income":
               total+=transaction.amount

        return total

    def get_total_expense(self):
        total=0

        for transaction in self.transactions:
            if transaction.transaction_type=="expense":
               total+=transaction.amount

        return total


    def list_transactions(self):
        return self.transactions


    def search_by_category(self, category):
        result=[]

        for transaction in self.transactions:
            if transaction.category.lower()==category.lower():
                result.append(transaction)
        return result


def validate_amount(amount):
    return amount > 0



def validate_transaction_type(transaction_type):
    return transaction_type in [
        "income",
        "expense"
    ]


def main():
    manager = FinanceManager()
    manager.load_data()

    while True:
        print("\n--- Finance Manager ---")
        print("1. Add transaction")
        print("2. Show balance")
        print("3. Show total income")
        print("4. Show total expense")
        print("5. Top category (expenses)")
        print("6. Show all transactions")
        print("7. Search by category")
        print("8. Delete transaction")
        print("9. Save and exit")
        choice = input("Choose an option: ")

        if choice == "1":

            try:
                amount = float(input("Amount: "))

                category = input("Category: ")

                t_type = input("Type (income/expense): ")

                manager.add_transaction(amount, category, t_type)

            except ValueError as e:
                print(e)

        elif choice == "2":
            print("Balance:", manager.calculate_balance())

        elif choice == "3":
            print("Total income:", manager.get_total_income())

        elif choice == "4":
            print("Total expense:", manager.get_total_expense())

        elif choice == "5":
            print("Top category:", manager.get_top_category())

        elif choice == "6":

            transactions = manager.list_transactions()

            if not transactions:
                print("No transactions found")

            else:
                for i, transaction in enumerate(transactions):
                    print(i, transaction.amount, transaction.category, transaction.transaction_type)


        elif choice == "7":

            category = input("Category: ")
            result = manager.search_by_category(category)
            if not result:
                print("No transactions found")
            else:
                for transaction in result:
                    print(transaction.amount, transaction.category, transaction.transaction_type)


        elif choice == "8":

            try:
                index = int(input("Transaction index: "))
                manager.delete_transaction(index)
                print("Transaction deleted")

            except (ValueError, IndexError):
                print("Invalid index")

        elif choice == "9":
            manager.save_data()
            print("Saved. Goodbye!")
            break


        else:
            print("Invalid option")




if __name__=="__main__":
    main()
