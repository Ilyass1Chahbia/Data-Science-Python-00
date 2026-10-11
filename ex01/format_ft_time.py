import time

def main():
    timestamp = time.time()
    date_struct = time.localtime(timestamp)
    date = time.strftime("%b %d %Y", date_struct)
    print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
    print(date)
    

if __name__ == "__main__":
    main()