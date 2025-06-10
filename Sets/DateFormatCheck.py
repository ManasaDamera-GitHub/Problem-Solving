date="29-02-2024"
days=[31,28,31,30,31,30,31,31,30,31,30,31]
# - validations
if (date[2]!="-" or date[2]!="-"):
    print("invalid format")
    # isdigit validation
if (not date[:2].isdigit() or not date[3:5].isdigit() or not date[6:10].isdigit()):
    print("invalid format")
    # months validation
if(int(date[3:5])<=0 or int(date[3:5])>12):
    print("invalid format")
    
month=int(date[3:5])
year=int(date[6:10])
day=days[month-1]

# leap year
if((year%4==0 or year%100==0) and month==2):
    day=day+1
if(int(date[:2])<=0 or int(date[:2])>day):
    print("invalid format")
else:
    print("valid format-true")

