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

# 05_function 
 *Scopes and Name Resolution 
  - Local -> inside a function 
  - Enclosing from outer function if nested 
  - global - Top level script 
  - Built in

 ** 
   - global chai_type - ye variable ko globally change kr dega
   - nonlocal chai_type - ye sirf outer function wale variable ko update krega

# git command 
git status 
git add . 
git commit -m "message" 
git push -u origin main