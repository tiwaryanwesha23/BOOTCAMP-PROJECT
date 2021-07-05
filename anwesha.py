import hashlib 
variable = input('enter string')
result = hashlib.md5(variable.encode()) 

print(result.hexdigest())