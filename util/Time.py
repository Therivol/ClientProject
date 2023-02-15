import math
import time


class Time:
    time_started = 0
    delta_time_ns = 0
    last_time = 0

    @staticmethod
    def awake():
        Time.time_started = time.time_ns()
        Time.last_time = time.time_ns()

    @staticmethod
    def start_frame():
        Time.last_time = time.time_ns()

    @staticmethod
    def calculate_dt():
        Time.delta_time_ns = (time.time_ns() - Time.last_time)

    @staticmethod
    def delta():
        return Time.delta_time_ns / 1000000000

    @staticmethod
    def elapsed():
        return (time.time_ns() - Time.time_started) / 1000000000