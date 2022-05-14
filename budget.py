''' @uthor: Mohammareza Baghery '''

'''The Budget class instantiates objects based on different budget categories like food,
clothing, entertainment etc.. When objects are created, they are passed in the name of the category.
The class can handle different transcactions, including deposit, withdraw, tranfer to other budget 
categories and balance check.
'''

class Budget:

    def __init__(self, category):
        self.category = category
        # instance variable ledger (a collection of financial accounts)
        self.ledger = []

    def get_balance(self):
        ''' returns the current balance of the budget category 
        based on the deposits and withdrawals that have occurred.
        '''
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def deposit(self, amount, description=None):
        ''' Accepts an amount and description. If no description is given, 
        it should default to an empty string. The method should append 
        an object to the ledger list in the form of {"amount": amount, "description": description}
        '''
        if not description:
            description = ''
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self,  amount, description=None):
        ''' Similar to the deposit method, but the amount passed in should be stored in the ledger 
        as a negative number. If there are not enough funds, nothing should be added to the ledger. 
        This method should return True if the withdrawal took place, and False otherwise.
        '''
        if not description:
            description = ''
        if self.get_balance() >= amount: 
            self.ledger.append({"amount": -1 * amount, "description": description})
            return True
        else:
            return False
 
    def transfer(self, amount, new_category):
        ''' accepts an amount and another budget category as arguments. 
        The method adds a withdrawal with the amount to Destination Budget Category.
        The method then adds a deposit to the other budget category (Source Budget Category) 
        with the amount. If there are not enough funds, nothing should be added to either ledgers. 
        Returns True if the transfer took place, and False otherwise.
        '''

        if self.get_balance() >= amount: 
            withdrawal_description = "Transfer to {}".format(new_category.category)
            self.withdraw(amount, withdrawal_description)
            deposit_description = "Transfer from {}".format(self.category)
            new_category.deposit(amount, deposit_description)

            return True
        else: 
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        ''' When the budget object is printed, it shows
        a list of the transcctions in that category.
        '''
        first_line = self.category.center(30, "*")
        second_line = ''
        total = 0
        width_lst = []
        for item in self.ledger:
          width_lst.append(str(item['amount']))
        width = max(width_lst, key=len)
        
        for item in self.ledger:
            description = item['description']
            description = description[:23]
            amount = "{:.2f}".format(float(item['amount']))
            amount = str(amount)[:7]
            amount = amount.rjust(len(width) + (24 -len(description)))

            second_line += '{}{}\n'.format(description, amount)
            total += item['amount']

        third_line = 'Total: {:.2f}'.format(total)
        return '{}\n{}{}'.format(first_line, second_line, third_line)