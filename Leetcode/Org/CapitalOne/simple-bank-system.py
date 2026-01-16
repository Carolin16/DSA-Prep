"""
  Q.2043 https://leetcode.com/problems/simple-bank-system/

   Time complexity: transfer: O(1)
                    deposit: O(1)
                    withdraw: O(1)

  Space complexity: Initialize: O(n)
                      transfer: O(1)
                      deposit: O(1)
                      withdraw: O(1)
"""
class Bank:
    """
        valid transaction conditions
            1. if account is valid - account number shud be betweeen 1 and n
            2. amount withdrawn or transferred is less than or equal to balance
    """
    def __init__(self, balance: List[int]):
        self.balance = balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # valid account number
        if(account1 > len(self.balance) 
            or account2 > len(self.balance)
            #if account has enough balance
            or self.balance[account1 - 1] < money):
                return False
        
        #update balances
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        #validate account number
        if(account > len(self.balance)):
            return False

        self.balance[account - 1] += money

        return True

    def withdraw(self, account: int, money: int) -> bool:
        if(account > len(self.balance) or money > self.balance[account - 1]):
            return False
        
        self.balance[account - 1] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
