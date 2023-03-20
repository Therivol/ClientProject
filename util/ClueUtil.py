class ClueUtil:

    @staticmethod
    def characters():
        return ["MISS SCARLET", "MRS PEACOCK", "MRS WHITE", "COLONEL MUSTARD", "MR GREEN", "PROFESSOR PLUM"]

    @staticmethod
    def weapons():
        return ["REVOLVER", "KNIFE", "LEAD PIPE", "ROPE", "CANDLESTICK", "WRENCH"]

    @staticmethod
    def rooms():
        return ["STUDY", "HALL", "LOUNGE", "LIBRARY", "DINING ROOM", "BILLIARD ROOM", "CONSERVATORY", "BALLROOM",
                "KITCHEN"]

    room_doors = {(6, 3): "STUDY", (9, 4): "HALL", (11, 6): "HALL", (12, 6): "HALL", (17, 5): "LOUNGE",
                  (6, 8): "LIBRARY", (3, 10): "LIBRARY", (17, 9): "DINING ROOM", (16, 12): "DINING ROOM",
                  (1, 12): "BILLIARD ROOM", (5, 15): "BILLIARD ROOM", (4, 19): "CONSERVATORY", (8, 19): "BALLROOM",
                  (9, 17): "BALLROOM", (14, 17): "BALLROOM", (15, 19): "BALLROOM", (19, 18): "KITCHEN"}

    door_rooms = {"STUDY": [(6, 3)], "HALL": [(9, 4), (11, 6), (12, 6)], "LOUNGE": [(17, 5)],
                  "LIBRARY": [(6, 8), (3, 10)], "DINING ROOM": [(17, 9), (16, 12)], "BILLIARD ROOM": [(1, 12), (5, 15)],
                  "CONSERVATORY": [(4, 19)], "BALLROOM": [(8, 19), (9, 17), (14, 17), (15, 19)], "KITCHEN": [(19, 18)]}

    tunnels = {"STUDY": (0, 3), "LOUNGE": (23, 5), "CONSERVATORY": (1, 19), "KITCHEN": (18, 23)}

    tunnels_2 = {(0, 3): "KITCHEN", (23, 5): "CONSERVATORY", (1, 19): "LOUNGE", (18, 23): "STUDY"}

    room_centers = {"STUDY": (3, 1), "HALL": (12, 3), "LOUNGE": (20, 2), "LIBRARY": (3, 8), "DINING ROOM": (20, 12),
                    "BILLIARD ROOM": (2, 14), "CONSERVATORY": (2, 21), "BALLROOM": (11, 20), "KITCHEN": (20, 20)}
