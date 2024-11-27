import re

def validador_senha(senha):
    
    if len(senha) < 8:
        return False

   
    if not re.search(r'[a-z]', senha): 
        return False
    if not re.search(r'[A-Z]', senha):  
        return False

    
    if not re.search(r'\d', senha):  
        return False

  
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha): 
        return False


    return True


print(validador_senha("Abc12345@"))  # True
print(validador_senha("abc12345"))   # False, não tem letra maiúscula
print(validador_senha("ABC12345@"))  # False, não tem letra minúscula
print(validador_senha("Abcde@"))     # False, menos de 8 caracteres
