from microbit import display, button_a, button_b
from time import sleep
from random import randint

running = True

snake = []
snake.append([1, 2])
snake.append([0, 2])

apple = [3, 2]

vel = [1, 0]

interval = 0.4
loops = 0
score = 0

x = 0
y = 1


while running:
    display.clear()
    display.set_pixel(apple[x], apple[y], 9)

    if button_a.was_pressed():
        if not vel[x] == 0:
            vel[y] = vel[x] * -1
            vel[x] = 0
        elif not vel[y] == 0:
            vel[x] = vel[y]
            vel[y] = 0

    if button_b.was_pressed():
        if not vel[x] == 0:
            vel[y] = vel[x]
            vel[x] = 0
        elif not vel[y] == 0:
            vel[x] = vel[y] * - 1
            vel[y] = 0

    index = len(snake) - 1
    for part in reversed(snake):
        if loops == 0:
            display.set_pixel(part[x], part[y], 9)
            continue

        if index == 0:
            part[x] += vel[x]
            part[y] += vel[y]

            if part[x] == apple[x] and part[y] == apple[y]:
                last = snake[-1]
                new_part = [last[x], last[y]]

                snake.append(new_part)

                apple[x] = randint(0, 4)
                apple[y] = randint(0, 4)

                score += 1
        else:

            next_part = snake[index - 1]
            part[x] = next_part[x]
            part[y] = next_part[y]

        if part[x] in range(5) and part[y] in range(5):
            display.set_pixel(part[x], part[y], 9)
        else:
            running = False

        index -= 1

    head = snake[0]
    for i, part in enumerate(snake):
        if i > 0 and part[x] == head[x] and part[y] == head[y]:
            running = False

            display.set_pixel(part[x], part[y], 4)
            sleep(0.2)
            display.set_pixel(part[x], part[y], 9)

    loops += 1
    sleep(interval)


for index in range(6):
    display.on()
    sleep(0.2)
    display.off()
    sleep(0.2)

display.on()
display.clear()
display.scroll("Score: {}".format(score))
