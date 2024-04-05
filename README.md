# First Game Development project

Working with pygame:
- you have to define the screen aspects
- init pygame instance
- add a name for the project
- you have to loop until you arrive to a break condition

```python
run = True
while run:
    # draw background
    draw_bg(bg_image)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
```