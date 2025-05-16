class Bank:
    bank_name = "Al habib"
    @classmethod
    def change_bank_name(cls,name):
         cls.bank_name = name

b1 = Bank()
print(f"bank name before : {b1.bank_name}")
b1.change_bank_name("Standard chartered")
print(f"Bank name after : {b1.bank_name}")