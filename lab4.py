import math 
  
key = "HACK"
  
# Шифрование 
def encryptMessage(msg): 
    cipher = "" 
  
    k_indx = 0
  
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 
  
    col = len(key) 
      
    row = int(math.ceil(msg_len / col)) 
  
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
  
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)] 
  
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return cipher 
  
# Расшифрока
def decryptMessage(cipher): 
    msg = "" 
  
    k_indx = 0
  
    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher) 
  
    col = len(key) 
      
    row = int(math.ceil(msg_len / col)) 
  
    key_lst = sorted(list(key)) 
  
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
  
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
  
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
  
    try: 
        msg = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.") 
  
    null_count = msg.count('_') 
  
    if null_count > 0: 
        return msg[: -null_count] 
  
    return msg

msg = input("Введите текст для шифрования/расшифрования методом двойной перестановки:")
  
cipher = encryptMessage(msg) 
print("Encrypted Message: {}". 
               format(cipher)) 
  
print("Decryped Message: {}". 
       format(decryptMessage(cipher)))


cryptMode = input("[E]ncrypt|[D]ecrypt методом Гронсфельда: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit

startMessage = msg
keyMessage = input("Write the keyNumber: ")

def encryptDecrypt(mode, message, key, final = ""):
	key *= len(message) // len(key) + 1
	for index, symbol in enumerate(message):
		if mode == 'E':
			temp = ord(symbol) + int(key[index]) -13
		else:
			temp = ord(symbol) - int(key[index]) -13
		final += chr(temp%26 + ord('A'))
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage, keyMessage))
