from abstract_Class import AbstractPayment 
from service.checkout import Checkout
from Entity import googlepay,paytm


# pay amount using googlepay
googlepay =googlepay.GooglePay(1200)
Checkout.paymentOption(googlepay) 

# pay amount using paytm
paytm = paytm.Paytm(4000) 
Checkout.paymentOption(paytm)

