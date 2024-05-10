from threading import Thread
import time


def print_numbers(starting, ending):
    for x in range(starting, ending+1):
        print(x)
        time.sleep(0.1)  

def main():



    thread1 = Thread(target=print_numbers, args=(1, 25))
    thread2 = Thread(target=print_numbers, args=(26, 50))


    thread1.start()
    thread2.start()


    print("all numbers are printed.")

if __name__ == "__main__":
    main()
