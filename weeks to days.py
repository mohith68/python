days=int(input("number of days="))
years=days//365
months=days-years*365
weeks=(days%365)//7
print("years=",years)
print("months=",months)
print("weeks=",weeks)
