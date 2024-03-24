import pygame
import os

# Initialize Pygame mixer
pygame.mixer.init()

# Initialize Pygame display (dummy window)
pygame.display.set_mode((400, 300))
pygame.display.set_caption('Music Player')

# Initialize font module
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)

# List of songs
songs = ['Pac.mp3', 'Cent.mp3', 'Aaron.mp3', 'Arash.mp3', 'Jason.mp3']

# Load the first song
pygame.mixer.music.load(songs[0])

# Current song index
current_song_index = 0

# Function to play the current song
def play_song():
    pygame.mixer.music.play()

# Function to stop the current song
def stop_song():
    pygame.mixer.music.stop()

# Function to play the next song
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

# Function to play the previous song
def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

# Function to draw the song list and current song
def draw_song_list(screen, current_song_index):
    screen.fill((0, 0, 0))  # Fill the screen with black
    y = 20
    for i, song in enumerate(songs):
        song_text = font.render(song, True, (255, 255, 255))
        if i == current_song_index:
            pygame.draw.rect(screen, (255, 255, 255), (10, y - 10, 380, 30), 1)
        screen.blit(song_text, (10, y))
        y += 30
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                play_song()
            elif event.key == pygame.K_s:  # Stop
                stop_song()
            elif event.key == pygame.K_n:  # Next
                next_song()
            elif event.key == pygame.K_b:  # Previous
                prev_song()

    # Draw the song list and current song
    draw_song_list(pygame.display.get_surface(), current_song_index)

# Quit Pygame
pygame.quit()