#First lab program

def celsius_fahrenheit(temp_str, temp_num):
    """This function converts the temperature from
       to fahrenheit and vice-verse"""

    if temp_str == "celsius":
        f = ((9/5)*temp_num) + 32
        print(f)
        
    elif temp_str == "fahrenheit":
        c = (temp_num - 32)*(5/9)
        print(c)
                                
    else:
        print("Unknown string: ",temp_str)