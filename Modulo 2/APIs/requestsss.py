import requests
response = requests.get('https://github.com/akiragh0sagt')
status = (response.status_code) #vê se a pagina está ativa, com erro ou não existente 

if status <=299:
    print(f"Pagina tá ON patrão, o status é {status}")
else:
    print(f"Tá dando errrado patrão, o status é {status}")