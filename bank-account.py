from datetime import datetime

class BankAccount:
    #دالة البنائ وتصفير الرصيد 
 def __init__(self):
        self.balance = 0
        
    #دالة الإيداع مع طباعة الوقت والتاريخ
 def deposit(self, amount):
    if amount > 0:
     self.balance += amount
     current_time = datetime.now().strftime("%Y-%m-%d %H;%M;%S")
     print(f"تم ايداع مع التاريخ والوقت")
    else:
        print("عذرا يجب أن يكون مبلغ الايداع اكبر من الصفر")
        
        #دالة السحب مع شرط التحقق وطباعة الوقت والتاريخ
        withdraw(self, amount)
    if self.balance >= amount:
         print(f"تم السحب مع التاريخ والوقت")
    else:
        print ("عذرا الرصيد غير كاف")
        #دالة الاستعلام عن الرصيد الحالي 
    def get_balance(self):
     print(f"رصيدك الحالي")
    return self.balance
