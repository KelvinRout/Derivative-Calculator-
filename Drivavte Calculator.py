import math, string
def dirvivatvecalc():
    print("Welcome to the derivative calculator!")
    print("Please enter what you want the derivative to be taken from")
    print("use: X as your varible,^ for squaring")
    print("And use: [/] for fractions EX: [1/2] or [1/2x^2] and to denoate a negative fraction [-1/2]")
    print("Be warned this is very unstable if something dosen't work try it a few other ways if it still dosent work it won't work")
    driv = input(":")
    driv = driv.lower()
    finalanswer = ("")
    counter = 0
    checker = 0
    valuechecker = 0
    signchecker = False
    lastdriv = 0
    term1 = "eighty" 
    #valuechecker tells where a new function to take der begins
    if driv[0] !="(":
        for i in driv[1:]:
            counter = counter + 1
            if i =="[" or driv[0]=="[":
                checker = checker + 1
                term1 = driv[valuechecker:driv.find("]")+1]
                partANSWER = fractions(term1)
                if signchecker == False:
                    if valuechecker == 0:
                        finalanswer = finalanswer + " " + partANSWER
                    else:
                        finalanswer = finalanswer + " + " + partANSWER
                    lastdriv = counter 
                else:
                    finalanswer = finalanswer + "-" + partANSWER
                valuechecker = counter + len(term1) 
                if len(driv) == len(term1):
                #checks if the fraction is the only term entered 
                    print(finalanswer)
                    return
            elif i == "+" or i == "-":
                checker = checker + 1
                if i in term1 in driv:
                    pass
                else:
                    #tells number of times this ran so can know if missing thing
                    term1 = driv[valuechecker:counter]
                    partANSWER = simplecase(term1)
                    if signchecker == False:
                        if valuechecker == 0:
                            finalanswer = finalanswer + " " + partANSWER
                        else:
                            finalanswer = finalanswer + " + " + partANSWER
                        lastdriv = counter 
                    else:
                        finalanswer = finalanswer + "-" + partANSWER
                        signchecker = False
                        lastdriv = counter
                    valuechecker = counter + 1
            if i == "-":
                signchecker = True
                
        
        if checker == 0:
            if driv[0] == "-":
                finalanswer = "-" + simplecase(driv[1:])
            else:
                finalanswer = simplecase(driv)
        else:
            partANSWER = simplecase(driv[lastdriv:])
            if driv[lastdriv-1] == "-":
                finalanswer = finalanswer + "-" + partANSWER
            else:
                finalanswer = finalanswer + " " + partANSWER
        print(finalanswer.upper())


def fractions(term):
    term = term[1:len(term)-1]
    startpoint = term.find("/")
    numerator = term[:startpoint]
    denominator =term[startpoint+1:]
    if "x" in term:
        if "x" in numerator and "x" in denominator:
            return ("This will not work")
        else:
            pass
            if "x" in numerator:
                driv = simplecase(numerator)
                return "[" + driv + "/" + denominator + "]"

            if "x" in denominator:
                driv = denominators(numerator,denominator)
                return driv
    else:
        return" "

    

def simplecase(term):
    if "x" in term:
        if "x^" in term:
            if term[term.rfind("^")+1] in string.ascii_lowercase:
                return term[term.rfind("^")+1] + term + "-1"
            else:
                number = int(term[term.rfind("^")+1:])
                number2 = str(number - 1)
                #find what are new ^ value will be 
                if number2 == "0":
                    return("1")
                else:
                    pass
                if term[:term.find("x")] not in string.ascii_lowercase:
                    value = number * int(term[:term.find("x")])
                    return( str(value) + "x^" + number2)
                else:
                    if term[0] == "x":
                        return( str(number)+ "x^" + number2)
                    else:
                        return( str(number)+ term[0] + "x^" + number2)
        else:
            if term == "x":
                return ("1")
            else:
                return term[:term.find("x")]
    else:
        return ""

def denominators(num,denom):
        if "x^" in denom:
            if denom[denom.rfind("^")+1] in string.ascii_lowercase:
                return "[" +"-" + denom[denom.rfind("^")+1] + num + "/" + denom + "+1"
            else:
                number = int(denom[denom.rfind("^")+1:])
                number2 = str(number + 1)
                #find what are new ^ value will be 
                if number2 == "0":
                    return "[" +"-"+ num + "/" + "1" + "]"
                else:
                    pass
                if denom[:denom.find("x")] not in string.ascii_lowercase:
                    return( "["+"-" + str(number) + "*" + num + "/"+str(number) + "x^" + number2 + "]")
                else:
                    if denom[0] == "x":
                        return( "[" "-" + str(number) + "*" + num + "/" + "x^" + number2 + "]")
                    else:
                        return "[" +"-"+ str(number)+ term[0]+ "*" + num + "/" + "x^" + number2 + "]"
        else:
            if denom == "x":
                return "["+"-" + num + "/" + "x^2" + "]"
            else:
                pass
