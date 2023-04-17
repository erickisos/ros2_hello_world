# Simple Test for ROS 2 Humble

This package contains a simple test for ROS 2 Humble.
The content of this repo was initialized using the following command:

```bash
ros2 pkg create --build-type ament_cmake simple_test
```

## Build

To build this package, run the following commands from the root of this repository:

```bash
colcon build --packages-select simple_test
```

## Run

To run this package, run the following commands from the root of this repository:

```bash
source install/setup.bash
ros2 run simple_test talker
```

## Develop

If you want to add a new executable to this package, you can add a script into the simple_test directory and the following lines to the setup.py file:

```python
...
entry_points={
    'console_scripts': [
        ... # Other nodes
        'my_new_node = simple_test.my_new_node:main'
    ],
},
...
```

## Test

To test this package, run the following commands from the root of this repository:

```bash
colcon test --packages-select simple_test
```
