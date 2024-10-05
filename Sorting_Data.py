def getUserData():
    elements = []
    n = int(input("Enter the number of transactions: "))

    for i in range(n):
        print(f"\nEnter details for transaction {i + 1}:")
        name = input("Name: ")
        bank_name = input("Bank Name: ")
        transaction_amount = int(input("Transaction Amount: "))
        payment_method = input("Payment Method: ")

        elements.append({
                'name': name,
                'bank_name': bank_name,
                'transaction_amount': transaction_amount,
                'payment_method': payment_method
            })

    return elements

elements = getUserData()


def sortData(elements, key=None):
    n=len(elements)

    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
            
        if not swapped:
            break
        
    return elements

sortData(elements, key='transaction_amount')
print("Transaction Details by Amount : ",elements )