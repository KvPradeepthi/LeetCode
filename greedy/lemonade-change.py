class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten = 0, 0
        
        # Iterate through each bill in the list
        for bill in bills:
            if bill == 5:
                # Customer pays with a $5 bill, no change needed, just collect the $5 bill
                five += 1
            elif bill == 10:
                # Customer pays with a $10 bill, give $5 as change if possible
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                # Customer pays with a $20 bill
                if ten > 0 and five > 0:
                    # Prefer to give one $10 bill and one $5 bill as change
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    # If no $10 bill, give three $5 bills as change
                    five -= 3
                else:
                    # If neither option is available, return False
                    return False
        
        # If all customers received correct change, return True
        return True
        