from time import sleep
import nime
import play

print("*"*20)
print()
print("  ---- SCRIPT BOT ----  ")
print()
print("*"*20)
sleep(1)

bot = "Frow"
nome = input(" Qual Seu Nome : ")

sleep(1)
print()
print(f"{bot}: Lindo Nome ")
print()
sleep(1)
print("_________________________________________")
print()
print('''    1 - Playlist De Musicas
             2 - Sites De Animes 
             3 - Musicas Recomendadas 
             4 - Estou Triste Preciso De Ajuda ''')
print()
print("_________________________________________")

sleep(1)

escolha = int(input(" Qual Opção Deseja : "))

if escolha == 1:
    print()
    play.playlist1()

elif escolha == 2:
    print()
    nime.anime()
