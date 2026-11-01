from collections import deque

# Campus locations and their connections (Adjacency List)

campus = {
    "Entry Plaza": ["Innovation Hub", "Knowledge Centre"],
    "Innovation Hub": ["Entry Plaza", "Computing Lab", "Convention Hall"],
    "Knowledge Centre": ["Entry Plaza", "Food Court"],
    "Computing Lab": ["Innovation Hub", "Food Court", "Sports Arena"],
    "Food Court": ["Knowledge Centre", "Computing Lab", "Sports Arena"],
    "Sports Arena": ["Computing Lab", "Food Court", "Convention Hall"],
    "Convention Hall": ["Innovation Hub", "Sports Arena"],
    "Orion Hostel": []
}


# BFS - Find shortest route
def bfs(start, end):
    queue = deque([start])
    visited = [start]
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            break

        for place in campus[current]:
            if place not in visited:
                visited.append(place)
                parent[place] = current
                queue.append(place)

    if end not in visited:
        return None

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


# DFS - Find reachable locations
def dfs(start):
    stack = [start]
    visited = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            for place in campus[current]:
                if place not in visited:
                    stack.append(place)

    return visited


# Display all locations
def show_locations():
    print("\nCampus Locations:")

    for place in campus:
        print("-", place)


# Main menu
while True:
    print("\n--- CAMPUS NAVIGATOR ---")
    print("1. Show locations")
    print("2. Find shortest route (BFS)")
    print("3. Show reachable and disconnected locations (DFS)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_locations()

    elif choice == "2":
        show_locations()
        start = input("\nEnter starting location: ")
        end = input("Enter destination: ")

        if start not in campus or end not in campus:
            print("Invalid location!")

        else:
            path = bfs(start, end)

            if path is None:
                print("No route exists between these locations.")

            else:
                print("\nShortest route:")
                print(" -> ".join(path))
                print("Number of edges:", len(path) - 1)

    elif choice == "3":
        show_locations()
        start = input("\nEnter starting location: ")

        if start not in campus:
            print("Invalid location!")

        else:
            reachable = dfs(start)
            disconnected = []

            for place in campus:
                if place not in reachable:
                    disconnected.append(place)

            print("\nReachable locations:")
            for place in reachable:
                print("-", place)

            if disconnected:
                print("\nDisconnected locations:")
                for place in disconnected:
                    print("-", place)
            else:
                print("\nNo disconnected locations.")

    elif choice == "4":
        print("Thank you for using Campus Navigator!")
        break

    else:
        print("Invalid choice! Please try again.")
