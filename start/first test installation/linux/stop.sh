#!/bin/bash
# Stop script for Linux - ROS2 Humble + Gazebo Harmonic

echo "Stopping ROS2 container..."
docker-compose down
echo "Container stopped."

# Optionally revoke X11 permissions
# xhost -local:docker
