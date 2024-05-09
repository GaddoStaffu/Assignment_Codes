from threading import Thread
import time


def print_numbers(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(0.1)  

def main():

    starting = 1
    ending = 50


    thread1 = Thread(target=print_numbers, args=(starting, ending//2))
    thread2 = Thread(target=print_numbers, args=(ending//2 + 1, ending))


    thread1.start()
    thread2.start()


    print("all numbers are printed.")

if __name__ == "__main__":
    main()
