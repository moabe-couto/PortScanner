import socket
from datetime import datetime
from colorama import Fore, Style, init

init()

def banner():
    print("""
=================================
  PORT SCANNER EDUCACIONAL
=================================
  Autor: Moabe Couto
  Linguagem: Python
  Uso: Estudos de Redes
=================================
   """)

servicos = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MYSQL",
    3389: "RDP"
}

portas_abertas = []
banners = []
    

banner()

VERDE_NEON = "\033[92m"
ROXO_NEON = "\033[95m"
RESET = "\033[0m"

def input_verde(texto):
    return input(f"{VERDE_NEON}{texto}{RESET}")

ip = input_verde("Digite o IP do alvo: ")
porta_inicial = int(input_verde("Digite a porta inicial: "))
porta_final = int(input_verde("Digite a porta final: "))

mostrar_fechadas = input("Mostrar portas fechadas? (s/n): ").lower()

print(f"\nIP informado: {ip}")
print(f"Porta inicial: {porta_inicial}")
print(f"Porta final: {porta_final}")

print("\nVerificando porta...")

for porta in range(porta_inicial, porta_final + 1):
     
    servico = servicos.get(porta, "Serviço Desconhecido")

for porta in range(porta_inicial, porta_final + 1):

    servico = servicos.get(porta, "Serviço Desconhecido")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    resultado = sock.connect_ex((ip, porta))

    if resultado == 0:
        print(f"{ROXO_NEON}[+] Porta {porta} encontrada aberta!{RESET}")
        print(f"[+] Serviço identificado: {servico}")

        portas_abertas.append((porta, servico))

    try:
        sock.settimeout(3)

        banner = sock.recv(1024).decode(errors="ignore")

        if banner:
            print("[+] Banner encontrado:")
            print(banner)

            banners.append((porta, banner))

    except:
        pass

    sock.close()

with open("relatorio.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write("========================\n")
    arquivo.write("RELATÓRIO DE SCAN\n")
    arquivo.write("========================\n\n")

    arquivo.write(f"IP: {ip}\n\n")
    arquivo.write(f"Data do scan: {datetime.now()}\n\n")

    arquivo.write("PORTAS ABERTAS:\n\n")
    
    arquivo.write(f"Total encontradas: {len(portas_abertas)}\n\n")

    for porta, servico in portas_abertas:
        arquivo.write(f"Porta {porta} - {servico}\n")

    arquivo.write("\nBANNERS ENCONTRADDOS:\n\n")

    for porta, banner in banners:
        arquivo.write(f"Porta {porta}\n")
        arquivo.write(f"{banner}\n")
        arquivo.write("----------------------\n")

print("\nRelatório salvo em relatorio.txt")