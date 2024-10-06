import time

def input_simulation():
    while True:
        time.sleep(1)
        # Given sentence
        sentence = input("\nUser:\n")
        print(sentence)
import threading

simulation = threading.Thread(target=input_simulation)
simulation.start()


while True:
    print('hello')
    time.sleep(1)
