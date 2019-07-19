wt_limit=30

def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt-wt_limit
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge

def update_baggage_limit(new_wt_limit):
    wt_limit=new_wt_limit
    print("This airline now allows baggage limit till",wt_limit,"kgs")

print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
update_baggage_limit(45)
print(wt_limit)
print("Pay the extra baggage charge of",baggage_check(25),"rupees")
