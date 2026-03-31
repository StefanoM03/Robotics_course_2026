Nella virtual machine NoVNC.

Per ogni terminale aperto:

    $ cd ~/github/racademy_ws
    $ colcon build --symlink-install   # --symlink-install speeds up Python edits
    $ source install/setup.bash

## 1 Running the Publisher

1. **Terminal 1 – Run the node**

   ```bash
   $ ros2 run racademy_py_examples simple_publisher
   [INFO] [simple_publisher]: Publishing at 1 Hz
   [INFO] [simple_publisher]: Sending: "Hello World 0"
   …
   ```

2. **Terminal 2 – Inspect topics**

   ```bash
   $ ros2 topic list
   /chatter
   /parameter_events
   /rosout

   $ ros2 topic echo /chatter
   data: Hello World 0
   data: Hello World 1
   …
   ```

Congratulations! You have written and launched your first ROS 2 publisher.

## 2 Testing the Full Pipeline

1. **Terminal 1 – Publisher**

   ```bash
   $ ros2 run racademy_py_examples simple_publisher
   ```

2. **Terminal 2 – Subscriber**

   ```bash
   $ ros2 run racademy_py_examples simple_subscriber
   [INFO] [simple_subscriber]: I heard: Hello World 0
   [INFO] [simple_subscriber]: I heard: Hello World 1
   …
   ```

3. **Terminal 3 – Inject a manual message** (optional)

   ```bash
   $ ros2 topic pub /chatter std_msgs/msg/String "data: 'Manual hello'"
   ```

   Watch Terminal 2 print the injected string.

— **End of Chapter 1**

---
