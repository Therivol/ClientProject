import pygame as p


class Assets:

    images = {}

    @staticmethod
    def get_image(path, alpha=False):

        if path in Assets.images:
            return Assets.images[path]
        else:
            if alpha:
                Assets.images[path] = p.image.load(path).convert_alpha()
            else:
                Assets.images[path] = p.image.load(path).convert()

        return Assets.images[path]

    @staticmethod
    def clear_images():
        Assets.images.clear()
