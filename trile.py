import pygame, random
pygame.init()

DIMENSIONS = (1080, 770)
SCREEN = pygame.display.set_mode(DIMENSIONS)
CLOCK = pygame.time.Clock()
TARGET_FPS = 30

myfont = pygame.font.SysFont("URW Bookman L", 50)
label = myfont.render("Play", 1, (255,0,0))
death_counter = 0
counter = myfont.render("Deaths %s" % death_counter, 1, (255,255,255)) #death counter (called once)
splash_screen=pygame.image.load("splash_screen.png")
splash_screen_rect = splash_screen.get_rect()
pygame.display.set_caption("trip")


is_running = True

KEYS = {
	"d": False,
	"a": False,
	"s": False,
	"w": False
}

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
yelgre = (0, 255, 165)
green = (0, 235, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)

colors = [
	#red, 
	orange, 
	#yellow, 
	yelgre, 
	green, 
	blue, 
	purple
]

start_game = False
play_button = {
	"x": DIMENSIONS[0] - 415,
	"y": DIMENSIONS[1] - 190,
	"width": 350,
	"height": 125
}

spawn = (0,9)

def changeKeys(key, value):
	if key == pygame.K_d:
		KEYS['d'] = value
	if key == pygame.K_a:
		KEYS['a'] = value
	if key == pygame.K_s:
		KEYS['s'] = value
	if key == pygame.K_w:
		KEYS['w'] = value

def kill_player():
	global death_counter
	global counter
	player[0] = spawn[0]
	player[1] = spawn[1]
	death_counter += 1
	counter = myfont.render("Deaths %s" % death_counter, 1, (255,255,255)) #death counter update

def save_player():
	pass

def beat_level():
	global level_counter
	global level
	global grid
	global grid_overlay
	global first_turn
	player[0] = spawn[0]
	player[1] = spawn[1]
	level_counter += 1
	if level_counter < len(levels):
		grid = levels[level_counter]
		first_turn = levels[level_counter][len(levels[level_counter])-1].index(1)
	pygame.time.delay(1000)
	grid_overlay = []
	death_counter = 0
	level = myfont.render("Level %s" % (level_counter + 1), 1, (255,255,255)) #level counter update


tile_size = 77
player = [0, DIMENSIONS[1] / tile_size - 1]
speed = tile_size

tile = {
	"kill":0,
	"safe":1,
	"turn":2,
	"beat":3
}

tile1 = colors[random.randint(0, len(colors)-1)]
tile2 = colors[random.randint(0, len(colors)-1)]
tile3 = colors[random.randint(0, len(colors)-1)]
tile4 = colors[random.randint(0, len(colors)-1)]

level_counter = 0
level = myfont.render("Level %s" % (level_counter + 1), 1, (255,255,255)) #level counter (called once)
levels = [
	[
		[2, 1, 1, 1, 1, 1, 1, 2],  #level 1
		[1, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 2, 1, 1, 2, 0, 1],
		[1, 0, 1, 0, 0, 1, 0, 1],
		[1, 0, 1, 0, 3, 2, 0, 1],
		[1, 0, 1, 0, 0, 0, 0, 1],
		[1, 0, 2, 1, 1, 1, 1, 2],
		[1, 0, 0, 0, 0, 0, 0, 0]
	],
	[
		[0, 3, 0, 0, 0, 0, 0, 0],  #level 2
		[0, 1, 0, 0, 2, 1, 2, 0],
		[0, 2, 1, 1, 2, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 1, 0],
		[2, 1, 1, 1, 1, 1, 2, 0],
		[1, 0, 0, 0, 0, 0, 0, 0],
		[2, 1, 1, 1, 1, 1, 1, 2],
		[0, 0, 0, 0, 0, 0, 0, 1]
	],
	[
		[0, 0, 0, 0, 0, 0, 0, 3],  #level 3
		[0, 0, 0, 0, 0, 0, 2, 2],
		[0, 0, 0, 0, 0, 2, 2, 0],
		[0, 0, 0, 2, 1, 2, 0, 0],
		[0, 0, 2, 2, 0, 0, 0, 0],
		[0, 2, 2, 0, 0, 0, 0, 0],
		[2, 2, 0, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 0]
	],
	[
		[3, 0, 0, 0, 0, 0, 0, 0],  #level 4
		[1, 0, 2, 1, 1, 1, 1, 2],
		[1, 0, 1, 0, 0, 0, 0, 1],
		[2, 1, 2, 0, 0, 0, 2, 2],
		[0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 2, 1, 1, 1, 2, 0],
		[0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0]
	],
	[
		[2, 1, 1, 1, 1, 1, 1, 3],  #level 5
		[1, 0, 0, 0, 0, 0, 0, 0],
		[2, 1, 2, 0, 2, 1, 2, 0],
		[0, 0, 1, 0, 1, 0, 1, 0],
		[0, 0, 2, 1, 2, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 1, 0],
		[2, 1, 1, 1, 1, 1, 2, 0],
		[1, 0, 0, 0, 0, 0, 0, 0]
	],
	[
		[0, 0, 0, 0, 0, 0, 0, 3],  #level 6
		[0, 0, 0, 2, 1, 2, 0, 1],
		[2, 1, 1, 2, 0, 2, 1, 2],
		[1, 0, 0, 0, 0, 0, 0, 0],
		[1, 0, 0, 2, 1, 1, 1, 2],
		[1, 0, 0, 1, 0, 0, 0, 1],
		[2, 1, 1, 2, 0, 0, 2, 2],
		[0, 0, 0, 0, 0, 0, 1, 0]
	],
	[
		[0, 0, 0, 0, 0, 0, 0, 3],  #level 7
		[2, 1, 1, 2, 0, 0, 0, 1],
		[1, 0, 0, 1, 0, 2, 1, 2],
		[2, 2, 0, 1, 0, 1, 0, 0],
		[0, 1, 0, 1, 0, 2, 1, 2],
		[0, 1, 0, 1, 0, 0, 0, 1],
		[0, 1, 0, 2, 1, 1, 1, 2],
		[0, 1, 0, 0, 0, 0, 0, 0]
	],
	[
		[2, 1, 2, 0, 0, 0, 0, 3],  #level 8
		[1, 0, 1, 0, 0, 0, 0, 1],
		[1, 0, 2, 1, 2, 0, 2, 2],
		[1, 0, 0, 0, 1, 0, 1, 0],
		[2, 1, 2, 0, 1, 0, 2, 2],
		[0, 0, 1, 0, 1, 0, 0, 1],
		[2, 1, 2, 0, 2, 1, 1, 2],
		[1, 0, 0, 0, 0, 0, 0, 0]
	],
	[
		[0, 3, 0, 2, 1, 2, 0, 0],  #level 9
		[0, 1, 0, 1, 0, 2, 1, 2],
		[0, 2, 1, 2, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 1],
		[0, 2, 1, 2, 0, 0, 2, 2],
		[0, 1, 0, 1, 0, 0, 1, 0],
		[0, 1, 0, 2, 1, 1, 2, 0],
		[0, 1, 0, 0, 0, 0, 0, 0]
	],
	[
		[2, 1, 1, 1, 2, 0, 0, 3],  #level 10
		[1, 0, 0, 0, 1, 0, 2, 2],
		[1, 0, 2, 1, 2, 0, 1, 0],
		[1, 0, 1, 0, 0, 2, 2, 0],
		[1, 0, 1, 0, 2, 2, 0, 0],
		[1, 0, 1, 0, 1, 0, 0, 0],
		[1, 0, 2, 1, 2, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 0]
	],
	[
		[2, 1, 1, 1, 2, 0, 0, 3],  #level 11
		[1, 0, 0, 0, 1, 0, 0, 1],
		[2, 1, 2, 0, 2, 2, 0, 1],
		[0, 0, 1, 0, 0, 2, 1, 2],
		[0, 0, 2, 1, 2, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 2, 1, 1, 2],
		[0, 0, 0, 0, 0, 0, 0, 1]
	],
	[
		[0, 2, 1, 2, 0, 0, 0, 3],  #level 12
		[0, 1, 0, 1, 0, 2, 1, 2],
		[0, 1, 0, 1, 0, 1, 0, 0],
		[2, 2, 0, 1, 0, 2, 1, 2],
		[1, 0, 0, 2, 2, 0, 0, 1],
		[2, 1, 2, 0, 1, 0, 0, 1],
		[0, 0, 1, 0, 2, 1, 1, 2],
		[0, 0, 1, 0, 0, 0, 0, 0]
	],
	[
		[2, 1, 1, 2, 0, 2, 1, 2],  #level 13
		[1, 0, 0, 1, 0, 1, 0, 1],
		[1, 0, 0, 2, 1, 2, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 2, 1, 1, 2],
		[2, 1, 2, 0, 1, 0, 0, 0],
		[0, 0, 1, 0, 2, 1, 1, 3],
		[0, 0, 1, 0, 0, 0, 0, 0]
	],
	[
		[2, 1, 2, 0, 0, 0, 0, 0],  #level 14
		[1, 0, 1, 0, 2, 1, 2, 0],
		[1, 0, 2, 1, 2, 0, 2, 2],
		[1, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 2, 1, 1, 2, 0, 1],
		[1, 0, 1, 0, 0, 1, 0, 1],
		[2, 1, 2, 0, 2, 2, 0, 3],
		[0, 0, 0, 0, 1, 0, 0, 0]
	],
	[
		[0, 0, 0, 2, 1, 2, 0, 0],  #level 15
		[0, 0, 0, 1, 0, 1, 0, 0],
		[0, 0, 0, 1, 0, 2, 1, 2],
		[2, 1, 1, 2, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 2, 2],
		[2, 1, 2, 0, 3, 0, 1, 0],
		[0, 0, 1, 0, 2, 1, 2, 0],
		[0, 0, 1, 0, 0, 0, 0, 0]
	],
	[
		[0, 0, 2, 1, 1, 1, 1, 3],  #level 16
		[2, 1, 2, 0, 0, 0, 0, 0],
		[1, 0, 0, 2, 1, 2, 0, 0],
		[2, 2, 0, 1, 0, 2, 2, 0],
		[0, 1, 0, 2, 2, 0, 1, 0],
		[0, 2, 2, 0, 1, 0, 2, 2],
		[0, 0, 2, 1, 2, 0, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 1]
	],
	[
		[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1]
	]
]
grid = levels[level_counter]

first_turn = levels[level_counter][len(levels[level_counter])-1].index(1)

grid_overlay = []
beat__current_level = False

def movement():
	if KEYS['d'] and player[0] < len(grid[0]) - 1:
		player[0] += 1
		KEYS['d'] = False
	elif KEYS['a'] and player[0] > 0:
		player[0] -= 1
		KEYS['a'] = False
	if KEYS['s'] and player[1] < len(grid) + 1:
		player[1] += 1
		KEYS['s'] = False
	if KEYS['w'] and player[1] > 1:
		player[1] -= 1
		KEYS['w'] = False

while is_running:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1 and event.pos[0] > play_button["x"] and \
			event.pos[0] < play_button["x"] + play_button["width"] and \
			event.pos[1] > play_button["y"] and \
			event.pos[1] < play_button["y"] + play_button["height"]:
				start_game = True
		if start_game:	
			if event.type == pygame.KEYDOWN:
				changeKeys(event.key, True)
				if event.key == pygame.K_ESCAPE:
					is_running = False
			if event.type == pygame.KEYUP:
				changeKeys(event.key, False)
		if event.type == pygame.QUIT:
			is_running = False

	# UPDATE GAME/PATH

	if start_game:
		for y in range(0, len(grid)):
			for x in range(0, len(grid[y])):
				n=grid[y][x]

				if player[0] == x and player[1] -1 == y and n == tile['kill']:
					kill_player()
				elif player[0] == x and player[1] -1 == y and n == tile['safe']:
					grid_overlay.append( {
						'val': n,
						'x': x,
						'y': y
					} )
					grid[y][x] = -1
				elif player[0] == x and player[1] -1 == y and n == tile['turn']:
					grid_overlay.append({'val': n, 'x': x, 'y': y})
					grid[y][x] = -1
				elif player[0] == x and player[1] -1 == y and n == tile['beat']:
					grid_overlay.append({'val': n, 'x': x, 'y': y})
					grid[y][x] = -1
					beat__current_level = True
					

	
	movement()

	# DRAW GAME
	
	SCREEN.fill((1,1,1))
	
	if start_game:
		
		pygame.draw.rect(SCREEN, (128, 128, 128), (232, 693, 616, 77)) #start row
		
		if level_counter + 1 < len(levels):
			SCREEN.blit(counter, (0,35)) #death counter display
			SCREEN.blit(level, (0,0)) #level counter display

		if level_counter >= len(levels) - 1:
			win = myfont.render("YOU WIN", 1, (255,255,255))
			for y in xrange(70, 770, 35):
				SCREEN.blit(win, (40, y))
				SCREEN.blit(win, (890, y))
			for x in xrange(40, 1000, 170):
				SCREEN.blit(win, (x, 35))
				SCREEN.blit(win, (x, 0))

		#STARS
		for x in range(0, 25):
			pygame.draw.rect(SCREEN, (255, 255, 255), (random.randint(2, 232), random.randint(2, 768), random.randint(2, 3), random.randint(2, 3)))
			pygame.draw.rect(SCREEN, (255, 255, 255), (random.randint(850, 1078), random.randint(2, 768), random.randint(2, 3), random.randint(2, 3)))
			pygame.draw.rect(SCREEN, (255, 255, 255), (random.randint(232, 1002), random.randint(2, 68), random.randint(2, 3), random.randint(2, 3)))

		#TILES
		color = colors[random.randint(0, len(colors)-1)]
		for y in range(0, len(grid)):
			for x in range(0, len(grid[y])):
				n=grid[y][x]
				color = colors[random.randint(0, len(colors)-1)]
				pygame.draw.rect(SCREEN, (color), (tile_size*x + 232, tile_size*y + tile_size, tile_size, tile_size))

		#PATH
		for i in range(0, len(grid_overlay)):
			square = grid_overlay[i]
			if square['val'] == tile['safe']:
				pygame.draw.rect(SCREEN, (128, 128, 128), (tile_size * square['x'] + 232, \
					tile_size * square['y'] + tile_size, tile_size, tile_size))
			if square['val'] == tile['turn']:
				pygame.draw.rect(SCREEN, (78,78,78), (tile_size * square['x'] + 232, \
					tile_size * square['y'] + tile_size, tile_size, tile_size))
			if square['val'] == tile['beat']:
				pygame.draw.rect(SCREEN, (255, 255, 255), (tile_size * square['x'] + 232, \
					tile_size * square['y'] + tile_size, tile_size, tile_size))

		pygame.draw.rect(SCREEN, (78,78,78), (tile_size * first_turn + 232, tile_size * 9, tile_size, tile_size))
		
		player_x, player_y = player[0] * tile_size + 232, player[1] * tile_size
		pygame.draw.circle(SCREEN, (0, 0, 0), (player_x + tile_size / 2, player_y + tile_size / 2), 15)

	else:
		SCREEN.blit(splash_screen, splash_screen_rect)
		pygame.draw.rect(SCREEN, (105,105,105), (play_button["x"], play_button["y"], play_button["width"], \
			play_button["height"]))
		pygame.draw.rect(SCREEN, (255,255,255), (play_button["x"] + 20, play_button["y"] + 20, play_button["width"] - 40, \
			play_button["height"] - 40))
		SCREEN.blit(label, (play_button["x"] + 140, play_button["y"] + 45))

	pygame.display.update()

	if beat__current_level:
		beat__current_level = False
		beat_level()

	
	if len(grid_overlay) >= 64:
	 	break

	CLOCK.tick(TARGET_FPS)

pygame.quit()