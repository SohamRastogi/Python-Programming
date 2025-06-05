class Payment_Gateway :

    def money_transfer (self , input_money) :
        print("input money of amount : {input_money}, to the payment gateway from the user")

    def money_refund(self , refund_money) :
        print("refunded money of amount : {refund_money}, to the user from the payment gateway")
        


p1 = Payment_Gateway()
p1.money_transfer(100)
p1.money_refund(100)

