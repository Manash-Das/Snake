import pygame
from random import randrange

pygame.init()
BACKGROUND = pygame.image.load("background.jpg")
snakeTail = pygame.image.load("snake.png")
snakeHead = pygame.image.load("snake.png")
appleImage = pygame.image.load("apple.png")
pygame.display.set_caption("Snake Game")
movement = 28
SNAKES_LIST = []
DIRECTION = "LEFT"


class SNAKE:
    def __init__(self, RECENT_START_POS=None, END_POS=None, image=snakeTail,
                 screen=pygame.display.set_mode((1500, 800))):
        if RECENT_START_POS is None:
            RECENT_START_POS = [400, 400]
        if END_POS is None:
            END_POS = [32, 32]
        self.RECENT_START_POS = RECENT_START_POS
        self.EARLIER_START_POS = [RECENT_START_POS[0] + END_POS[0], RECENT_START_POS[1]]
        self.END_POS = END_POS
        self.image = image
        self.screen = screen

    def DISPLAY(self):
        self.screen.blit(self.image, self.RECENT_START_POS)

    def move(self):
        self.EARLIER_START_POS = [self.RECENT_START_POS[0], self.RECENT_START_POS[1]]
        if DIRECTION == "LEFT":
            self.RECENT_START_POS[0] -= movement
        elif DIRECTION == "RIGHT":
            self.RECENT_START_POS[0] += movement
        elif DIRECTION == "UP":
            self.RECENT_START_POS[1] -= movement
        elif DIRECTION == "DOWN":
            self.RECENT_START_POS[1] += movement
        self.condition()

    def condition(self):
        if self.RECENT_START_POS[0] < 10:
            self.RECENT_START_POS[0] = 1490
        elif self.RECENT_START_POS[0] > 1490:
            self.RECENT_START_POS[0] = 10
        elif self.RECENT_START_POS[1] < 10:
            self.RECENT_START_POS[1] = 770
        elif self.RECENT_START_POS[1] > 770:
            self.RECENT_START_POS[1] = 10

    @staticmethod
    def increment():
        try:
            snk = SNAKES_LIST[-1]
            snakeName = SNAKE([snk.EARLIER_START_POS[0], snk.EARLIER_START_POS[1]])
        except IndexError:
            snakeName = SNAKE(image=snakeHead)
        SNAKES_LIST.append(snakeName)


class Apple:
    def __init__(self, screen):
        self.position = [0, 0]
        self.apple = appleImage
        self.screen = screen

    def createApple(self):
        self.position = randrange(10, 1400), randrange(10, 700)
        self.drawApple()

    def drawApple(self):
        self.screen.blit(self.apple, self.position)

    def collision(self, snake):
        rect1 = self.apple.get_rect(topleft=self.position)
        rect2 = snakeHead.get_rect(topleft=SNAKES_LIST[0].RECENT_START_POS)
        if rect1.colliderect(rect2):
            self.createApple()
            snake.increment()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1500, 800))
        self.snake = SNAKE(screen=self.screen)
        self.snake.increment()
        self.apple = Apple(self.screen)

    def play(self):
        print("true")
        self.apple.createApple()
        clock = pygame.time.Clock()
        run = True
        global DIRECTION
        while run:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    run = False
                elif events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_LEFT:
                        DIRECTION = "LEFT"
                    elif events.key == pygame.K_RIGHT:
                        DIRECTION = "RIGHT"
                    elif events.key == pygame.K_UP:
                        DIRECTION = "UP"
                    elif events.key == pygame.K_DOWN:
                        DIRECTION = "DOWN"
            self.screen.blit(BACKGROUND, (0, 0))
            for index, snakePart in enumerate(SNAKES_LIST):
                if index == 0:
                    snakePart.move()
                else:
                    snakePart.EARLIER_START_POS = [snakePart.RECENT_START_POS[0], snakePart.RECENT_START_POS[1]]
                    snakePart.RECENT_START_POS = SNAKES_LIST[index - 1].EARLIER_START_POS
                self.apple.drawApple()
                self.apple.collision(self.snake)
                snakePart.DISPLAY()
            clock.tick(10)
            pygame.display.update()


def main():
    game = Game()
    game.play()


main()
