class Customer:
    def __init__(self, name, surname, personal_id):
        self.name = name
        self.surname = surname
        self.personal_id = personal_id

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.clients = {}
 
    def register_account(self, customer, initial_balance=0):
        if customer.personal_id in self.clients:
            print("ამ მომხმარებელს უკვე აქვს ბანკში ანგარიში.")
        else:
            self.clients[customer.personal_id] = {
                'name': customer.name,
                'surname': customer.surname,
                'balance': initial_balance
            }
            print(f"{customer.name} {customer.surname} წარმატებით დარეგისტრირდა. საწყისი ბალანსი: {initial_balance} ლარი")

    def deposit(self, personal_id, amount):
        if personal_id in self.clients:
            self.clients[personal_id]['balance'] += amount
            print(f"{amount} ლარი დამატებულია. ახალი ბალანსი: {self.clients[personal_id]['balance']} ლარი")
        else:
            print("მითითებული პირადი ნომრით მომხმარებელი არ არსებობს.")

    def withdraw(self, personal_id, amount):
        if personal_id in self.clients:
            if self.clients[personal_id]['balance'] >= amount:
                self.clients[personal_id]['balance'] -= amount
                print(f"{amount} ლარი გამოტანილია. დარჩენილი ბალანსი: {self.clients[personal_id]['balance']} ლარი")
            else:
                print("არასაკმარისი თანხა გაქვთ.")
        else:
            print("მითითებული პირადი ნომრით მომხმარებელი არ არსებობს.")

    def check_balance(self, personal_id):
        if personal_id in self.clients:
            return self.clients[personal_id]['balance']
        print("მითითებული პირადი ნომრით მომხმარებელი არ არსებობს.")
        return None

    def get_clients(self):
        sorted_clients = sorted(self.clients.items(), key=lambda x: x[1]['balance'], reverse=True)
        for personal_id, info in sorted_clients:
            print(f"{info['name']} {info['surname']}: {info['balance']} ლარი")


# მომხმარებლების შექმნა
customer1 = Customer("გიორგი", "მელქაძე", "0101406030")
customer2 = Customer("ნანა", "პანიევი", "0195400620")
customer3 = Customer("ესმირა", "აღამედოვა", "0108706030")

# ბანკის შექმნა
bank = Bank("თბს ბანკი", "თბილისი")

# ანგარიშების რეგისტრაცია
bank.register_account(customer1, 4600)
bank.register_account(customer2, 1490)
bank.register_account(customer3, 2980)

# თანხის შეტანა
bank.deposit("0101406030", 3286)

# თანხის გამოტანა
bank.withdraw("0195400620", 1000)

# შეცდომა
bank.withdraw("0108706032", 554)

# ბალანსის შემოწმება
print("ბალანსი:", bank.check_balance("0101406030"))
print("ბალანსი:", bank.check_balance("0195400620"))
print("ბალანსი:", bank.check_balance("0108706031"))

# მომხმარებლების სია
bank.get_clients()
