from clue.Clue import Clue


if __name__ == "__main__":

    clue = Clue()
    clue.start()
    clue.set_frame_rate(75)

    while not clue.should_close:
        clue.poll_events()
        clue.start_frame()
        clue.update()
        clue.draw()
        clue.calculate_dt()
        clue.end_frame()

    clue.quit()

