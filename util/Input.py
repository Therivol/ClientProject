import pygame as p
from util.Window import Window
from util.Globals import Globals


class Input:
    # Dictionary to hold the action states
    actions = {}
    # Dictionary to hold the key bindings
    key_bindings = {}
    # Dictionary to hold the mouse bindings
    mouse_bindings = {}
    # Dictionary to hold the key down states
    key_down = {}
    # Dictionary to hold the mouse button down states
    mouse_down = {}

    raw_keys = []
    
    mouse_dx, mouse_dy = 0, 0
    
    mouse_x, mouse_y = 0, 0

    @staticmethod
    def add_action(action_name, default_key=None, default_mouse=None):
        Input.actions[action_name] = 0
        Input.key_bindings[action_name] = default_key
        Input.mouse_bindings[action_name] = default_mouse
        Input.key_down[action_name] = False
        Input.mouse_down[action_name] = False

    @staticmethod
    def bind_key(action_name, key):
        Input.key_bindings[action_name] = key

    @staticmethod
    def bind_mouse(action_name, button):
        Input.mouse_bindings[action_name] = button

    @staticmethod
    def update():

        # Update mouse position and mouse movement
        mouse_pos = p.mouse.get_pos()

        Input.mouse_dx = mouse_pos[0] - Input.mouse_x
        Input.mouse_dy = mouse_pos[1] - Input.mouse_y

        Input.mouse_x = mouse_pos[0]
        Input.mouse_y = mouse_pos[1]
        
        # Reset all action states
        for action_name in Input.actions:
            Input.actions[action_name] = 0
            Input.key_down[action_name] = False
            Input.mouse_down[action_name] = False

        Input.raw_keys = p.key.get_pressed()
        # Update action states based on keyboard input
        keys = p.key.get_pressed()
        for action_name, key in Input.key_bindings.items():
            if key is not None and keys[key]:
                if not Input.key_down[action_name]:
                    Input.actions[action_name] = 1
                    Input.key_down[action_name] = True

        # Update action states based on mouse input
        mouse_buttons = p.mouse.get_pressed()
        for action_name, button in Input.mouse_bindings.items():
            if button is not None and mouse_buttons[button]:
                if not Input.mouse_down[action_name]:
                    Input.actions[action_name] = 1
                    Input.mouse_down[action_name] = True

    @staticmethod
    def get_key(key):
        return Input.raw_keys[key]

    @staticmethod
    def get_button(button):
        mouse_buttons = p.mouse.get_pressed()
        return mouse_buttons[button]

    @staticmethod
    def get_key_down(key):
        keys = p.key.get_pressed()
        if keys[key] and not Input.key_down[key]:
            Input.key_down[key] = True
            return True
        elif not keys[key]:
            Input.key_down[key] = False
        return False

    @staticmethod
    def get_button_down(button):
        mouse_buttons = p.mouse.get_pressed()
        if mouse_buttons[button] and not Input.mouse_down[button]:
            Input.mouse_down[button] = True
            return True
        elif not mouse_buttons[button]:
            Input.mouse_down[button] = False
        return False

    @staticmethod
    def get_mouse_pos():
        res_x, res_y = Globals.resolution
        win_x = Window.view.get_width()
        win_y = Window.view.get_height()
        x, y = p.mouse.get_pos()
        start_x, start_y = Window.view_destination

        return res_x * ((x - start_x) / win_x), res_y * ((y - start_y) / win_y)
