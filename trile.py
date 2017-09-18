import pygame, random

pygame.init()

DIMENSIONS = (1080, 770)
SCREEN = pygame.display.set_mode(DIMENSIONS)
CLOCK = pygame.time.Clock()
TARGET_FPS = 30

pygame.display.set_caption("trile")

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
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)

colors = [
	red, 
	orange, 
	yellow, 
	yelgre, 
	green, 
	blue, 
	purple
	]

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
	player[0] = spawn[0]
	player[1] = spawn[1]
	print "You stepped on a deadly tile!"

def save_player():
	pass

tile_size = 77
player = [0, DIMENSIONS[1] / tile_size - 1]
print player[1]
speed = tile_size

tile = {
	"kill":0,
	"safe":1
}

tile1 = colors[random.randint(0, len(colors)-1)]
tile2 = colors[random.randint(0, len(colors)-1)]
tile3 = colors[random.randint(0, len(colors)-1)]
tile4 = colors[random.randint(0, len(colors)-1)]

grid = [
	[0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 1, 1, 1, 0, 1],
	[1, 1, 1, 1, 0, 1, 1, 1],
	[1, 0, 0, 0, 0, 0, 0, 0],
	[1, 0, 0, 1, 1, 1, 1, 1],
	[1, 0, 0, 1, 0, 0, 0, 1],
	[1, 1, 1, 1, 0, 0, 1, 1],
	[0, 0, 0, 0, 0, 0, 1, 0]
	]

grid_overlay = []

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
	if KEYS['w'] and player[1] > 0:
		player[1] -= 1
		KEYS['w'] = False

while is_running:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			changeKeys(event.key, True)
			if event.key == pygame.K_ESCAPE:
				is_running = False
		if event.type == pygame.KEYUP:
			changeKeys(event.key, False)
		if event.type == pygame.QUIT:
			is_running = False
	
	SCREEN.fill((1,1,1))
	
	pygame.draw.rect(SCREEN, (200, 200, 200), (232, 0, 616, 770))
	pygame.draw.rect(SCREEN, (200, 200, 200), (232, 693, 616, 77))
	pygame.draw.rect(SCREEN, (200, 200, 200), (232, 0, 616, 77))

	for x in range(0, 25):
		pygame.draw.rect(SCREEN, (255, 255, 255), (random.randint(2, 230), random.randint(2, 768), random.randint(2, 3), random.randint(2, 3)))
		pygame.draw.rect(SCREEN, (255, 255, 255), (random.randint(850, 1078), random.randint(2, 768), random.randint(2, 3), random.randint(2, 3)))
	
	color = colors[random.randint(0, len(colors)-1)]
	for y in range(0, len(grid)):
		for x in range(0, len(grid[y])):
			n=grid[y][x]
			color = colors[random.randint(0, len(colors)-1)]
			pygame.draw.rect(SCREEN, (color), (tile_size*x + 232, tile_size*y + tile_size, tile_size, tile_size))
			if player[0] == x and player[1] - 1 == y and n == tile['kill']:
				kill_player()
			elif player[0] == x and player[1] -1 == y and n == tile['safe']:
				grid_overlay.append({'val': n, 'x': x, 'y': y})

	for i in range(0, len(grid_overlay)):
		square = grid_overlay[i]
		if square['val'] == tile['safe']:
			pygame.draw.rect(SCREEN, (200, 200, 200), (tile_size * square['x'] + 232, \
				tile_size * square['y'] + tile_size, tile_size, tile_size))

	
	player_x, player_y = player[0] * tile_size + 232, player[1] * tile_size
	pygame.draw.circle(SCREEN, (0, 0, 0), (player_x + tile_size / 2, player_y + tile_size / 2), 15)

	pygame.display.update()

	movement()

	CLOCK.tick(TARGET_FPS)

pygame.quit()
print 
