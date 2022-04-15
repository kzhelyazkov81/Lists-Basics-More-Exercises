times = input().split(' ')
left_car_points = 0
right_car_points = 0
winner = ''

left_car_times = times[0:len(times)//2]
right_car_times = times[len(times)//2+1::]
right_car_times.reverse()

for left in left_car_times:
    left_car_points += int(left)
    if int(left) == 0:
        left_car_points *= 0.8

for right in right_car_times:
    right_car_points += int(right)
    if int(right) == 0:
        right_car_points *= 0.8

if left_car_points < right_car_points:
    winner = 'left'
    total_time = left_car_points
else:
    winner = 'right'
    total_time = right_car_points

print(f'The winner is {winner} with total time: {total_time:.1f}')
