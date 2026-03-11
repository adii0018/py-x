person=("aditya",21,"india")
name,age,country=person
print(name)
print(age)
print(country)
#...................................
cricket=(
    ("virat",18,"100"),
    ("rohit",45,"50"),
    ("dhoni",7,"60")
)
print("cricket list...\n")

runs=0
player=""

for player in cricket:
    name,jno,runs=cricket
    print("player:", name)
    print("jursy no :",jno)
    print("Runs", runs)
    print("--------------")
    
    if runs> runs:
         runs = runs
         player = name

print("\n⭐ best player:", name)
print("⭐ normal:", runs)
