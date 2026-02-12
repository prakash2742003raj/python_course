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
  
  * Function types 
  - Pure and impure function
  - Recursive function 
  - lambda and Anonymous Function 
  
# 11_Exception handling 
 - Handle the Excepton or error 
        - IndexError -> Index out of range 
        - KeyError -> Key is missing in Dict
        - ZeroDivisionError -> divide by zero
        - TypeError -> Incompitable types of variables
        - NameError -> variable is not define and try to use

  1️⃣ What is Exception?
👉 Exception = Runtime error (program chalate waqt error)
Example:
print(10/0)
Output:
ZeroDivisionError

🟢 2️⃣ Why Exception Handling?
- Program crash hone se bachata hai
- Error ko gracefully handle karta hai
- User-friendly message deta hai

🟢 3️⃣ try – except (Basic Syntax)
try:
    risky_code
except ErrorType:
    handling_code

Example:
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")

🟢 4️⃣ Multiple except
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Invalid conversion")
except ZeroDivisionError:
    print("Cannot divide by zero")

🟢 5️⃣ Generic Exception
try:
    risky_code
except Exception as e:
    print("Error:", e)

👉 Exception sab errors ko catch karega
👉 e me error ka message milta hai

🟢 6️⃣ else Block
👉 Jab error nahi aata tab chalta hai

try:
    x = 10/2
except ZeroDivisionError:
    print("Error")
else:
    print("No error")

🟢 7️⃣ finally Block

👉 Hamesha chalega (error aaye ya na aaye)

try:
    x = 10/0
except:
    print("Error")
finally:
    print("Done")

*Use case:
-File close karna
-Database connection close karna

🟢 8️⃣ raise Keyword
👉 Manually error generate karna
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

🟢 9️⃣ Custom Exception
class MyError(Exception):
    pass

raise MyError("Something went wrong")

🟢 🔟 Common Built-in Exceptions
Exception	Meaning
ZeroDivisionError	10/0
ValueError	Wrong value type
TypeError	Wrong data type
KeyError	Dictionary key missing
IndexError	List index out of range
FileNotFoundError	File not found
🟢 1️⃣1️⃣ Full Structure (Best Practice)
try:
    risky_code
except SpecificError:
    handle_specific
except Exception as e:
    handle_other
else:
    no_error_case
finally:
    always_execute

🟢 Quick Revision Summary

- try → risky code
- except → error handle
- else → no error case
- finally → always run
- raise → manually error

Custom exception → apna error class
# git command 
git status 
git add . 
git commit -m "message" 
git push -u origin main