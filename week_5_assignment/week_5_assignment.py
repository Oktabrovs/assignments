def find_account_index(account_ids, account_id):
    i = 0
    while i < len(account_ids):
        if account_ids[i] == account_id: return i
        i += 1
    return -1
def process_ledger(initial_accounts, initial_balances, transactions):
    final_account_ids_list = initial_accounts.copy()
    final_account_balances_list = initial_balances.copy()
    for i in transactions:
        index = find_account_index(final_account_ids_list, i[1])
        if i[0] == "OPEN":
            if index == -1:
                final_account_ids_list.append(i[1])
                final_account_balances_list.append(i[2])
        elif i[0] == "WITHDRAW":
            if index != -1 and final_account_balances_list[index] >= i[2]: final_account_balances_list[index] -= i[2]
        else:
            if index != -1: final_account_balances_list[index] += i[2]
    return final_account_ids_list, final_account_balances_list

accounts = ["ACC-001", "ACC-002", "ACC-003"]
balances = [500.00, 1200.00, 250.00]
daily_transactions = [
    ["DEPOSIT", "ACC-001", 150.00],
    ["WITHDRAW", "ACC-002", 250.00],
    ["WITHDRAW", "ACC-003", 300.00], # This should fail (insufficient funds)
    ["OPEN", "ACC-004", 1000.00],
    ["DEPOSIT", "ACC-002", 50.00]
    
]

final_accounts, final_balances = process_ledger(accounts, balances, daily_transactions)
print(f"\n\nFinal Accounts: {final_accounts}")
print(f"Final Balances: {final_balances}\n\n")
