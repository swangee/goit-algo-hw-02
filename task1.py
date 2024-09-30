from queue import Queue
import sys

queue = Queue()
req_id = 0

def generate_request():
    global req_id, queue

    req_id = req_id + 1

    queue.put(req_id)

    print(f"Order {req_id} added to queue")

def process_request():
    global req_id, queue

    if queue.empty():
        print("Queue is empty")
        return

    print(f"Order {queue.get()} is being processed")

def main():
    while True:
        for line in sys.stdin:
            if 'exit' == line.rstrip().lower():
                print("good bye")
                return

            generate_request()
            process_request()
            print(f'Processing Message from sys.stdin *****{line}*****')

if __name__ == '__main__':
    main()