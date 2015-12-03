import  platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"
import game_framework

import start_state
import main_state2

game_framework.run((start_state))
#game_framework.run((main_state2))
