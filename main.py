import pygame

# start pygame modules
pygame.init()

# set the display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Feed The Dragon')

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# set game value: CONSTANT_NAME, value
''' 5 CONSTANTS 
PLAYER_STARTING_LIVES, 5 
PLAYER_VELOCITY, 10 
COIN_STARTING_VELOCITY, 10 
COIN ACCELERATION, 0.5
BUFFER_DISTANCE, 100
'''
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

# set game variables : Variable_name
''' 3 variables 
score, 0 
player_lives, PLAYER_STARTING_LIVES
coin_velocity, COIN_STARTING_VELOCITY
'''
score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set fonts
font = pygame.font.Font('AttackGraffiti.ttf')

# set text for score
'''
variable names: score_text, score_rect
render text: "Score: " + str(score)
antialias: True 
color: GREEN
background: DARKGREEN 
rect location : topleft = (10,10)
'''
score_text = font.render("Score" + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

# Set Text for Title (Similar to Score)
'''
variable names:  title_text , title_rect 
render text: "Feed the Dragon"
antialias: True
color: GREEN
background: WHITE
rect location: centerx = WINDOW_WIDTH//2
rect location: y = 10 
'''
title_text = font.render("Feed the Dragon", True, GREEN, WHITE, )
title_rect = title_text.get_rect()
title_rect.centerx = ((WINDOW_WIDTH // 2), 10)

# Set Text for Lives (Similar to Score)
'''
variable names:  lives_text, lives_rect
render text: "Lives: " + str(player_lives)
antialias: True
color: GREEN
background: DARKGREEN
rect location: y = 10  
'''
lives_text = font.render("lives" + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = y = 10

# Set Text for Game Over (Similar to Score)
'''
variable names:  game_over_text , game_over_rect 
render text: "GAMEOVER"
antialias: True
color: GREEN
background: DARKGREEN
rect location: center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) 
'''
game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Set Text for Continue (Similar to Score)
'''
variable names:  continue_text, continue_rect  
render text: "Press any key to play again"
antialias: True
color: GREEN
background: DARKGREEN
rect location: center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)
'''
continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

' We will write more code here '''

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_rect, title_text)
    ''' YOU DO; blit title_text and title_rect'''
    ''' YOU DO: blit lives_text and lives_rect'''

    # update display and tick th clock
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
