class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the account identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def _set_balance(self, amount):
        self._balance += amount

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        # ensure that the caller sends a number as a parameter
        if not isinstance(price, (int, float)):
            raise TypeError('price must be numeric')

        if price + self.get_balance() > self._limit:
            return False
        else:
            self._set_balance(price)
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""

        if not isinstance(amount, (int, float)):
            raise TypeError('payment amount must be numeric')

        if amount < 0:
            raise ValueError('payment amount must be positive')

        self._set_balance(-amount)


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    NUMBER_OF_CHARGES = 0

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the account identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed;
        Return False and assess $5 fee if charge was denied.
        """
        success = super().charge(price)
        if success:
            PredatoryCreditCard.NUMBER_OF_CHARGES += 1
            return True
        else:
            self._set_balance(5)  # assess penalty
            return False

    def process_month(self):
        """Assess monthly interest on outstanding balance."""

        if PredatoryCreditCard.NUMBER_OF_CHARGES > 10:
            self._set_balance(1 * (PredatoryCreditCard.NUMBER_OF_CHARGES - 10))

        if self.get_balance() > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._set_balance(self.get_balance() * (monthly_factor - 1))


# testing CreditCard class
if __name__ == '__main__':
    wallet = [CreditCard('John Bowman', 'California Savings',
                         '5391 0375 9387 5309', 2500),
              CreditCard('John Bowman', 'California Federal',
                         '3485 0399 3395 1954', 3500),
              CreditCard('John Bowman', 'California Finance',
                         '5391 0375 9387 5309', 5000)]

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()

    pc = PredatoryCreditCard('John Bowman', 'California Savings',
                             '5391 0375 9387 5309', 2000, 0.05)
    print("Balance: ", pc.get_balance())
    print("Make 11 charges ...")
    for i in range(11):
        pc.charge(10)
    print("Balance: ", pc.get_balance())
    print("Monthly processing ...")
    pc.process_month()
    print("After processed: ", pc.get_balance())
