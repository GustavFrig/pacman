from constants import *
from pathlib import Path
import pygame as pg

class Spokelse: 
    IMAGE_FILE = Path(__file__).parent / "sprites" / "pacman2.png"

    def getImageSpriteList(self, x_start, y_start, num_frames) -> list[pg.Surface]:
        full_image = pg.image.load(self.IMAGE_FILE)
        frame_width = 16
        
        # Dele opp bildet i frames, som lagres i en liste:
        frames = []
        for i in range(num_frames):
            # Bildene er kvadratiske - bruker frame widht både som høye og bredde:
            frame = full_image.subsurface(pg.Rect(x_start + i * frame_width, y_start, frame_width, frame_width))
            frames.append(frame)
        return frames
    

    def __init__(self, row, col):
        self.row = row
        self.col = col

        # Om vi vil speile bildet:
        self.retning = 0        # 0 = Høyre, 1 = Venstre, 2 = Opp, 3 = Ned
        self.frames_idle = self.getImageSpriteList(self.retning*32, 64, 2)
        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.frames_idle
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0


        self.bilde_timer = 0
        self.skiftbilde_timer = 150  # millisekunder per frame



    def draw(self, surface):

        # Få bildet fra en liste av bilder (om du vil bruke animasjon/sprites):
        current_frame_image = self.frames[self.current_frame]
        
        # Speiler bildet hvis det trengs:
        # if self.retning == 0:
        #    current_frame_image = pg.transform.flip(current_frame_image, True, False)

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        rect = current_frame_image.get_rect()
        rect.center = (self.col * TILE_SIZE + mid , self.row * TILE_SIZE + mid)

        # Blit images på skjermen (der self.rect befinner seg):
        surface.blit(current_frame_image, rect)
    
    def update(self, dt):
        """Oppdater animasjonen. Kall denne fra game loop med millisekunder siden forrige frame."""
        self.bilde_timer += dt
        if self.bilde_timer >= self.skiftbilde_timer:
            self.bilde_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

        
        