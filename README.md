hiii

01-virtual
-----------
- python -m  venv .venv  (Create virtual Environment) 
- .venv\Scripts\activate (Activate the virtual Environment) 
- deactivate (Deactivate the virutal environment)


# Organize your python code 
  
  chai_shop/
    run.py -> starts the app       ---module
    chai.py                        --module
    processing/                    --folder
    utils/                         --packages
      __init__.py
# 4_loops 

* enumerate
 menu = ['Green', 'Lemon', 'Spiced', 'Mint'] 

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")

*zip 
names = ["Nishant", "Ankit", "Prakash", "Rachana", "Karina"]
bills = [50, 70, 80, 43, 28]

for name, amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")

* walrus 
value = 13 

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


# git command 
git status 
git add . 
git commit -m "message" 
git push -u origin main