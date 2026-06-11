# Bank hisobvaraqlarini boshqaruvchi dastur
# Kurs: Dasturlash / IT
# Mavzu: 1-mavzu: Python va dasturlashga kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
accounts = {}
for i in range(n):
    account, balance = input().split()
    accounts[account] = int(balance)
print("Hisobvaraqlar:")
for account, balance in accaunt.items():
    print(f"{accounts} - {balance}")