from pyscript import display, document

nometal = {"Hydrogen": ('H', 1, 1.0080), "Carbon": ('C', 6, 12.011), "Nitrogen": ('N', 7, 14.007), "Oxygen": ('O', 8, 16.00), "Phosphorus": ('P', 15, 30.9737), "Sulfur": ('S', 16, 32.07), "Selenium": ('Se', 34, 78.97)} #the 7 nonmetals

def yooo(e):
    nokmetal = document.getElementById("nometa").value #gets value of input
    resulting = nometal.get(nokmetal, ("Not a Non-metal", "N/A", "N/A")) #makes sure that if the elemenet entered wasnt a non metal, it would display not a non-metal
    document.getElementById("codes").innerText = nokmetal #puts result for element codde
    document.getElementById("namess").innerText = resulting[0] #puts result for element symbol
    document.getElementById("whereha").innerText = resulting[1] #puts result for atomicnumber
    document.getElementById("heavy").innerText = resulting[2] #puts in the result for mass