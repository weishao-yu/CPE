count = 0 
while True:
    try:
        text = input() 
        result = ""
        
        for char in text:
            if char == '"':
                if count % 2 == 0:
                    result += '``'  
                else:
                    result += "''"  
                count += 1
            else:
                result += char      
                
        print(result)
        
    except EOFError:
        break