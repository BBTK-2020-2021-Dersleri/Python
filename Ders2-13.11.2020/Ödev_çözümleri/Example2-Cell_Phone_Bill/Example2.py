minute=float(input("How many minute: "))
text=float(input("How many text: "))
cost=15
minute_difference=0
text_difference=0
additional_minute_charge=0
additional_text_charge=0
call_center_charge=0.44
print("Base charge: 15.00$")
if(minute>50):
    minute_difference=minute-50
    additional_minute_charge=(minute_difference*(0.25))
    print("--------------------------")
    print("Additional minute charge: ",additional_minute_charge)
if(text>50):
    text_differencet=text-50
    additional_text_charge=(text_differencet*(0.15))
    print("--------------------------")
    print("Additional text charge: ",additional_text_charge)
    
cost=cost+additional_minute_charge+additional_text_charge+call_center_charge
cost=cost+(cost*(5))/100
print("**************************")
print("Minute you spend:",minute)
print("Text you spend: ",text)
print("911 fee:",call_center_charge)
print("%5 tax and 911 fee added......")
print("Total:",cost)
