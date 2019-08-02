import pygame
import pickle

num_pixels = int(input('Num Pixels> '))
honk = pygame.image.load(input('File> '))

meh = []
for x in range(num_pixels * 2):
    buffer = []
    for y in range(num_pixels * 2):
            buffer.append(honk.get_at((x, y))[:3])
    meh.append(buffer)

with open('pattern.pkl', 'wb') as file:
    pickle.dump(meh, file)
