            
        if gameState == 'options':
            font3 = pygame.font.SysFont("georgia", 26)
        if gameState == 'options': #screen is set to options
            font3 = pygame.font.SysFont("georgia", 26) #set fonts and sizes
            font4 = pygame.font.SysFont("georgia", 100)
            font5 = pygame.font.SysFont("georgia", 20)
            mainSurface.blit(backl, (-200, -200))
            mouse_position = pygame.mouse.get_pos()
            blindinglights = pygame.draw.rect(mainSurface, 'Purple', pygame.Rect(400, 50, 250, 50), border_radius =10)
            mainSurface.blit(backl, (-200, -200)) #display the background
            mouse_position = pygame.mouse.get_pos() #get mouse positions
            blindinglights = pygame.draw.rect(mainSurface, 'Purple', pygame.Rect(400, 50, 250, 50), border_radius =10) #make boxes for all the songs
            badhabits = pygame.draw.rect(mainSurface, 'Purple', pygame.Rect(50, 50, 250, 50), border_radius =10)
            industrybaby = pygame.draw.rect(mainSurface, 'Purple', pygame.Rect(400, 150, 250, 50), border_radius =10)
            stay = pygame.draw.rect(mainSurface, 'Purple', pygame.Rect(50, 150, 250, 50), border_radius =10)
            lol = pygame.draw.rect(mainSurface, 'Purple', pygame.Rect(230, 250, 250, 50), border_radius =10)
            backs = pygame.draw.rect(mainSurface, RED, pygame.Rect(50, 620, 250, 50), border_radius =20)
            mutes = pygame.draw.rect(mainSurface, 'Grey' , pygame.Rect(325, 530, 100, 50), border_radius =10)
            volumelow = pygame.draw.rect(mainSurface, 'Grey', pygame.Rect(100, 450, 100, 50), border_radius =10)
            volumemid = pygame.draw.rect(mainSurface, 'Grey', pygame.Rect(250, 450, 100, 50), border_radius =10)
            volumehigh = pygame.draw.rect(mainSurface, 'Grey', pygame.Rect(400, 450, 100, 50), border_radius =10)
            volumemax = pygame.draw.rect(mainSurface, 'Grey', pygame.Rect(550, 450, 100, 50), border_radius =10)
            volume = pygame.draw.rect(mainSurface, 'Purple', pygame.Rect(550, 550, 100, 100), border_radius =10)
            volumewords1 = "VOLUME:"
            backs = pygame.draw.rect(mainSurface, RED, pygame.Rect(50, 620, 250, 50), border_radius =20) #make the "back" box
            mutes = pygame.draw.rect(mainSurface, 'Grey' , pygame.Rect(325, 530, 100, 50), border_radius =10) #make the volume boxes
            volumelow = pygame.draw.rect(mainSurface, 'Grey', pygame.Rect(100, 450, 100, 50), border_radius =10) #%25
            volumemid = pygame.draw.rect(mainSurface, 'Grey', pygame.Rect(250, 450, 100, 50), border_radius =10) #%50
            volumehigh = pygame.draw.rect(mainSurface, 'Grey', pygame.Rect(400, 450, 100, 50), border_radius =10) #%75
            volumemax = pygame.draw.rect(mainSurface, 'Grey', pygame.Rect(550, 450, 100, 50), border_radius =10) #%100
            volume = pygame.draw.rect(mainSurface, 'Purple', pygame.Rect(550, 550, 100, 100), border_radius =10) #draw the volume display box
            volumewords1 = "VOLUME:" #set all the words to fill in the boxes
            renderedText = font5.render(volumewords1, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (555,570))
            textSurfacevol = font3.render (str(volumewords), True, 'Black')
            mainSurface.blit(renderedText, (555,570)) #display the words
            textSurfacevol = font3.render (str(volumewords), True, 'Black') #set all the words to fill in the boxes
            mainSurface.blit(textSurfacevol, (560,600))
            mute = "Mute"
            renderedText = font3.render(mute, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (345,540))
            mute = "Mute" #set the words in the volume box
            renderedText = font3.render(mute, 1, pygame.Color("Black")) #set all the words to fill in the boxes
            mainSurface.blit(renderedText, (345,540)) #display the words
            
            low = "%25"
            renderedText = font3.render(low, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (125,460))
            low = "%25" 
            renderedText = font3.render(low, 1, pygame.Color("Black")) #set all the words to fill in the boxes
            mainSurface.blit(renderedText, (125,460)) #display the words
            
            mid = "%50"
            renderedText = font3.render(mid, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (275,460))
            renderedText = font3.render(mid, 1, pygame.Color("Black")) #set all the words to fill in the boxes
            mainSurface.blit(renderedText, (275,460)) #display the words
            
            high = "%75"
            renderedText = font3.render(high, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (425,460))
            renderedText = font3.render(high, 1, pygame.Color("Black")) #set all the words to fill in the boxes
            mainSurface.blit(renderedText, (425,460)) #display the words
            
            maxvol = "%100"
            renderedText = font3.render(maxvol, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (570,460))
            renderedText = font3.render(maxvol, 1, pygame.Color("Black")) #set all the words to fill in the boxes
            mainSurface.blit(renderedText, (570,460)) #display the words
            
            word = "BLINDING LIGHTS"
            renderedText = font3.render(word, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (410,60))
            renderedText = font3.render(word, 1, pygame.Color("Black"))#set all the words to fill in the boxes
            mainSurface.blit(renderedText, (410,60)) #display the words
            word = "BAD HABITS"
            renderedText = font3.render(word, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (100,60))
            renderedText = font3.render(word, 1, pygame.Color("Black"))#set all the words to fill in the boxes
            mainSurface.blit(renderedText, (100,60)) #display the words
            word = "INDUSTRY BABY"
            renderedText = font3.render(word, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (420,160))
            renderedText = font3.render(word, 1, pygame.Color("Black"))#set all the words to fill in the boxes
            mainSurface.blit(renderedText, (420,160)) #display the words
            word = "STAY"
            renderedText = font3.render(word, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (130,160))
            renderedText = font3.render(word, 1, pygame.Color("Black"))#set all the words to fill in the boxes
            mainSurface.blit(renderedText, (130,160)) #display the words
            word = "???"
            renderedText = font2.render(word, 1, pygame.Color("Black"))
            mainSurface.blit(renderedText, (335,260))
            renderedText = font2.render(word, 1, pygame.Color("Black"))#set all the words to fill in the boxes
            mainSurface.blit(renderedText, (335,260)) #display the words
            word = "BACK"
            renderedText = font2.render(word, 1, pygame.Color("Black"))
            renderedText = font2.render(word, 1, pygame.Color("Black"))#set all the words to fill in the boxes
            mainSurface.blit(renderedText, (140,630))
            if pygame.mouse.get_pressed()[0] == True:
                if badhabits.collidepoint(( mouse_position)):
                    musicLoaded = True
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/badhabits.WAV")
                if badhabits.collidepoint(( mouse_position)): #if any boxes are clicked and collided with do the following
                    musicLoaded = True #set to true so the game knows music is loaded
                    pygame.mixer.music.unload() #unload any previous songs
                    pygame.mixer.music.load("music/badhabits.WAV") #load bad habits
                if blindinglights.collidepoint(( mouse_position)):
                    musicLoaded = True
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/blindinglights.WAV")
                    print(pygame.mixer.music.load)
                    musicLoaded = True#set to true so the game knows music is loaded
                    pygame.mixer.music.unload()#unload any previous songs
                    pygame.mixer.music.load("music/blindinglights.WAV")#load blinding lights
                if industrybaby.collidepoint(( mouse_position)):
                    musicLoaded = True
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/industrybaby.WAV")
                    musicLoaded = True#set to true so the game knows music is loaded
                    pygame.mixer.music.unload()#unload any previous songs
                    pygame.mixer.music.load("music/industrybaby.WAV")#load industry baby
                if stay.collidepoint(( mouse_position)):
                    musicLoaded = True
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/stay.WAV")
                    musicLoaded = True#set to true so the game knows music is loaded
                    pygame.mixer.music.unload()#unload any previous songs
                    pygame.mixer.music.load("music/stay.WAV") #load stay
                if lol.collidepoint(( mouse_position)):
                    musicLoaded = True
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/rick.WAV")
                if mutes.collidepoint(( mouse_position)):
                    volumemixer = 0
                    volumewords = "%0"
                    musicLoaded = True#set to true so the game knows music is loaded
                    pygame.mixer.music.unload()#unload any previous songs
                    pygame.mixer.music.load("music/rick.WAV") #load rick roll
                if mutes.collidepoint(( mouse_position)): #if the following boxes were clicked...
                    volumemixer = 0 #set volume to 0
                    volumewords = "%0" #set words in the "volume:" box
                if volumelow.collidepoint(( mouse_position)):
                    volumemixer = 0.25
                    volumewords = "%25"
                    volumemixer = 0.25 #set volume to %25
                    volumewords = "%25" #set words in the "volume:" box
                if volumemid.collidepoint(( mouse_position)):
                    volumemixer = 0.50
                    volumewords = "%50"
                    volumemixer = 0.50 #set volume to %50
                    volumewords = "%50" #set words in the "volume:" box
                if volumehigh.collidepoint(( mouse_position)):
                    volumemixer = 0.75
                    volumewords = "%75"
                    volumemixer = 0.75 #set volume to %75
                    volumewords = "%75" #set words in the "volume:" box
                if volumemax.collidepoint(( mouse_position)):
                    volumemixer = 1.0
                    volumewords = "%100"
                if backs.collidepoint(( mouse_position)):
                    gameState = "startScreen"
                    time.sleep(0.1)
                print(volumemixer)
                    volumemixer = 1.0 #set volume to %100
                    volumewords = "%100" #set words in the "volume:" box
                if backs.collidepoint(( mouse_position)): #if the back button collides with mouse
                    gameState = "startScreen" #go to start screen
                    time.sleep(0.1) #delay for any bugs 