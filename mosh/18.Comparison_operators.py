#if temperature is greater than 30
#    it's a hot day
#otherwirse if it's less than 10
#    it's a cold day
#otherwise
#    it's neither hot nor cold

name = "Jake smith"

if len(name) < 3 :
    print("Name must be at least 3 character")
elif len(name) > 50:
    print("Name must be a maximum of 50 character")
else:
    print("Name looks good!")