from time import sleep

def playlist1():
	print("_"*48)
	print()
	print("   ---- PLAYLIST DE MUSICAS --- ")
	print()
	print("_"*48)
	sleep(1)
	
	# Bot
	
	bot = "Frow"
	
	# PlayLists
	
	Rock_Classico =  "https://www.youtube.com/playlist?list=PLBD5pRttJ7N0vCfh4NpEg7Vw47hfeCxuE"
	
	DeathCore = "https://www.youtube.com/playlist?list=PLILR4eXFByn1eYRh33yF8bEP56Ocd4T8j"
	
	Indie = "https://www.youtube.com/playlist?list=PLrpga-n1MvA-4PrNGdmhteNu4Lkp_09vk"
	
	sad_music = "https://www.youtube.com/playlist?list=PLZ6tAXaQNfdloGAzrJAwcl_noQ_uD0DhT"
	
	funk = "https://www.youtube.com/playlist?list=PLA6B239361CC92D14"
	
	print()
	print(" Generos : ")
	print()
	print("OBS : PARA ESCOLHER A PLAYLIST BASTA DIGITAR O NÚMERO DELA ")
	print()
	sleep(1)
	print("  1 - Rock Classico")
	print("  2 - DeathCore")
	print("  3 - Indie ")
	print("  4 - Sad Musics ")
	print("  5 - Funk ")
	print()
	sleep(1)
	
	playlist = int(input(" Numero Da Playlist : "))
	
	if playlist == 1:
		print()
		print(f"{bot}: Playlist Rock Classico -> {Rock_Classico}")
		print()
	
	elif playlist == 2:
		print()
		print(f"{bot}: Playlist Deathacore -> ,{DeathCore}")
		print()
		
	elif playlist == 3:
		print()
		print(f"{bot}: Playlist Indie -> {Indie}")
		print()
	
	elif playlist == 4:
		print()
		print(f"{bot}: Playlist Sad Musics/Musicas Sad -> {sad_music}")
		print()
	
	elif playlist == 5:
		print()
		print(f"{bot}: Playlist Funk -> {funk}")
		print()

if(__name__ == "__main__"):
	playlist1()