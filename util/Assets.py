import pygame as p


class Assets:

    images = {}
    working_directory = "assets/"

    @staticmethod
    def get_image(path, alpha=False):

        path = Assets.working_directory + path

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

    @staticmethod
    def set_working_directory(path):
        Assets.working_directory = path

    @staticmethod
    def position_by_percent(size, back_size, percent, center=True):
        x, y = 0, 0

        if center:
            x = back_size[0] * percent[0] - size[0] / 2
            y = back_size[1] * percent[1] - size[1] / 2

        else:
            x = back_size[0] * percent[0]
            y = back_size[1] * percent[1]

        return x, y
