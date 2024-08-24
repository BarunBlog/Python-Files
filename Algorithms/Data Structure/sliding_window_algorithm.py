import time

def main():
    window_size = 5

    request_time = int(time.time())

    request_times = [request_time + 2, request_time + 3, request_time + 4, request_time + 5, request_time + 6, request_time + 7, request_time + 8]

    print(request_times)

    window_list = []

    for request_time in request_times:
        current_time = request_time

        window_start = current_time // window_size * window_size
        
        window_list.append(window_start)

    print(window_list)

if __name__ == "__main__":
    main()