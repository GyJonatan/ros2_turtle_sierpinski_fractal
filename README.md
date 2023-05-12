# ros2_turtle_sierpinski_fractal

This is a simple turtle sim project that draws a Sierpinski Triangle fractal based on the size given by the ros2 launch param. 

to start the listener node:
```
ros2 run ros2_course listener
```

to start giving it commands:
```
ros2 topic pub /sierpinski_size std_msgs/msg/Int32 "data: <size>"
```
where size should be an integer number of your choice. 

keep in mind that the bigger the number the longer it takes to draw, for quick demo i suggest '25'.
