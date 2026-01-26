import sys

def solve():
    try:
        input_data = sys.stdin.read().splitlines()
        if not input_data:
            return
        
        n = int(input_data[0])
        my_list = []
        for i in range(1, n + 1):
            parts = input_data[i].split()
            command = parts[0]
            
            if command == "insert":
                my_list.insert(int(parts[1]), int(parts[2]))
            elif command == "print":
                print(my_list)
            elif command == "remove":
                my_list.remove(int(parts[1]))
            elif command == "append":
                my_list.append(int(parts[1]))
            elif command == "sort":
                my_list.sort()
            elif command == "pop":
                my_list.pop()
            elif command == "reverse":
                my_list.reverse()
                
    except EOFError:
        pass

if __name__ == "__main__":
    solve()