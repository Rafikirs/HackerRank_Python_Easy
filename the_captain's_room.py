def find_captains_room(k, room_numbers):
    room_count = {}
    for room in room_numbers:
        if room in room_count:
            room_count[room] += 1
        else:
            room_count[room] = 1
            
    for room, count in room_count.items():
        if count != k:
            return room

k = int(input())
room_numbers = list(map(int, input().split()))

print(find_captains_room(k, room_numbers))
