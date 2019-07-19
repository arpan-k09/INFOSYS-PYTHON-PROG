class Customer:
    def __init__(self,customer_id,customer_name,total_items,item=None,total_bill_amount=0):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.total_items = total_items
        self.item = item
        self.total_bill_amount = total_bill_amount

    def purchases(self):
        if self.item == 'item1':
            self.total_bill_amount = (self.total_items*150)*0.95
        elif self.item == 'item2':
            self.total_bill_amount = (self.total_items * 150) * 0.95
        elif self.item == 'item3':
            self.total_bill_amount = (self.total_items * 150) * 0.95
        print(self.customer_name+"have to pay "+str(self.total_bill_amount)+"for "+str(self.item))

    def pays_bill(self,amount):
        self.total_bill_amount = self.total_bill_amount - amount
        print(self.customer_name+"pays bill amount of "+str(amount))
        print(self.customer_name + "have change or due of " + str(self.total_bill_amount))


cust1 = Customer(1,"ak",5,'item1',0)
cust1.purchases()
cust1.pays_bill(1000)


