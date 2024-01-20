import pygame as pg
from settings import *


class CutScene:
    all_scenes = [
        [(pg.image.load(cut_scene_presets[j][i][0]), cut_scene_presets[j][i][1]) for i in
         range(len(cut_scene_presets[j]))]
        for j in range(len(cut_scene_presets))]

    def __init__(self, scenes=None, number=None):
        if scenes is not None:
            self.scenes = [(pg.image.load(scenes[i][0]), scenes[i][1]) for i in range(len(scenes))]
        elif number is not None:
            self.scenes = CutScene.all_scenes[number]
        else:
            raise TypeError

    def save_scene(self):
        CutScene.all_scenes.append(self.scenes)

    def play_cut_scene(self, screen, virtual_surface, clock: pg.time.Clock):
        for scene, delay in self.scenes:
            flag = True
            for i in range(round(delay * 1000) // round(clock.get_fps())):
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        exit()
                    if event.type == pg.MOUSEBUTTONUP:
                        flag = False
                virtual_surface.blit(pg.transform.scale(scene, virtual_surface.get_size()), (0, 0))
                scaled_surface = pg.transform.scale(virtual_surface, screen.get_size())
                screen.blit(scaled_surface, (0, 0))
                clock.tick(fps)
                pg.display.update()
                if not flag:
                    break
