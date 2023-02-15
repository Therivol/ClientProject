import pygame as p

from util.Debug import Debug
from util.Settings import Settings
from clue.scene.Scene import Scene


class Scenes:
    # Dictionary to hold the scenes
    scenes = {}
    # Current scene
    current_scene = None

    @staticmethod
    def add_scene(scene):
        Scenes.scenes[scene.name] = scene
        scene.start()
        scene.awake()

    @staticmethod
    def set_scene(name):
        if Scenes.current_scene:
            Scenes.current_scene.exit()
        Scenes.current_scene = Scenes.scenes[name.upper()]
        Scenes.current_scene.enter()
        Debug.log(f"{name.upper()}")

    @staticmethod
    def get_scene(name):
        return Scenes.scenes[name.upper()]

    @staticmethod
    def early_update():
        if Scenes.current_scene:
            Scenes.current_scene.early_update()

    @staticmethod
    def update():
        if Scenes.current_scene:
            Scenes.current_scene.update()

    @staticmethod
    def late_update():
        if Scenes.current_scene:
            Scenes.current_scene.late_update()

    @staticmethod
    def get_surface(scene=None):
        if scene:
            return Scenes.scenes[scene.upper()].get_surface()
        elif Scenes.current_scene:
            return Scenes.current_scene.get_surface()
        else:
            surf = p.Surface((Settings.get("RESOLUTION")))
            surf.fill((255, 0, 0))
            return surf
