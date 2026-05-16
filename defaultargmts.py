def net_bal(price,discount=0.01,tax=0.05):
    return price*(1-discount)*(1+tax)

x=net_bal(5000,0.1,0.05)
print(f"total bill with argmts={x}")

x=net_bal(5000)
print(f"total bill with default argmts={x}")

x=net_bal(5000,0.6)
print(f"total bill with partitial argmnts={x}")

