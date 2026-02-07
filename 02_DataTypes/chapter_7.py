masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# membership testing

print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")


t = (1,2,3,4,5,3,2) 
print(t) 

print(f"{t.count(2)} and {t.index(2)}") 

t = 1,2,1
print(t)

a,b,c = t 
print(f"{a}, {b}, {c}")