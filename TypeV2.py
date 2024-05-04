import pygame as p
from pygame.locals import *
from random import choice, randint
gameOver = False

timeWaitedforWordSpawn = 3000

#Initializations
p.init()
p.font.init()
p.time.set_timer(p.USEREVENT, timeWaitedforWordSpawn)

#Clock
clock = p.time.Clock()

#Screen
screenRes = (800, 600)
screen = p.display.set_mode(screenRes)

#Game Font
Font = p.font.SysFont('Comic Sans MS', 20)

#Keys
keyList = {97 : 'a', 98 : 'b', 99 : 'c', 100 : 'd', 101 : 'e', 102 : 'f',
           103 : 'g', 104 : 'h', 105: 'i', 106 : 'j', 107 : 'k', 108 : 'l',
           109 : 'm', 110 : 'n', 111 : 'o', 112 : 'p', 113 : 'q', 114 : 'r',
           115 : 's', 116 : 't', 117 : 'u', 118 : 'v', 119 : 'w', 120 : 'x',
           121 : 'y', 122 : 'z', K_MINUS : '-', 39 : '\'', 46 : '.'}

#Color
bg = (255, 255 ,255)  
color = (27, 65, 89)

#Game Lists
words = ['']
points = [[0,0]]
wordTyped = []
typedWordPos = (10, 570)

def textTuple(text):
	return Font.size(text)

def textBlit(text, pos, color):
	textSurface = Font.render(text, True, color)
	screen.blit(textSurface, pos)

def wordGen():
	file = open('words.txt', 'r')
	wordGn = choice(file.readlines()).replace('\n', '')
	return wordGn.lower()
	file.close()

def randomPoint(text):
	return [-textTuple(text)[0], randint(0, typedWordPos[1] - 10)]

def spawnMoveDelete():
	for i in range(len(words)):
		textGenerated = words[i]
		textBlit(textGenerated, points[i], color)

	for j in points:
		j[0] += 1

	try:
		if points[0][0] == 800:
			del(points[0])
			del(words[0])
	except:
		pass

def redrawTypedWord():
	textBlit(''.join(wordTyped), typedWordPos, color)

def OnUservent():
	tempWord = wordGen()
	words.append(tempWord)
	points.append(randomPoint(tempWord))

def deleteWordOnSpace():
	global wordTyped
	indexPos = words.index(''.join(wordTyped))
	del(words[indexPos])
	del(points[indexPos])
	wordTyped = []

while not gameOver:
	clock.tick(60)
	screen.fill(bg)
	for event in p.event.get():
		if event.type == QUIT:
			gameOver = True
		if event.type == USEREVENT:
			OnUservent()
		if event.type == KEYDOWN:
			for keys in keyList:
				if event.key == keys:
					letter = keyList[keys]
					wordTyped.append(letter)
					letterPos = [textTuple(''.join(wordTyped))[0], typedWordPos[1]]
					textBlit(letter, letterPos, color)
			if event.key == K_SPACE:
				if ''.join(wordTyped) in words:
					deleteWordOnSpace()
				else:
					wordTyped = []
			if event.key == K_BACKSPACE:
				try:
					del(wordTyped[-1])
				except:
					pass

	spawnMoveDelete()			
	redrawTypedWord()
	p.display.update()
p.quit()
