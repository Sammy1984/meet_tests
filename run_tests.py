from multiprocessing import Process
import pytest
from Constants import BOTS_COUNT

flag = True


def start():
    pytest.main(["-s", "-v", "-k", "TestCallPageCreate"])
    global flag
    while flag:
        with open("Constants.py", "r") as file:
            x = file.readlines()
            if x[-1] == "REF_URL = None":
                continue
            else:
                flag = False
    pytest.main(["-s", "-v", "-k", "TestSecond", "-n", f"{BOTS_COUNT}", "--dist", "each"])


process = Process(target=start)

if __name__ == "__main__":
    process.start()

