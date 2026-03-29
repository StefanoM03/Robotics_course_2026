#!/bin/bash
# Start script for Linux - ROS2 Humble + Gazebo Harmonic

echo "=========================================="
echo "ROS2 Humble + Gazebo Harmonic - Linux"
echo "=========================================="

# Allow X11 connections from Docker
echo "[1/4] Configuring X11 permissions..."
xhost +local:docker > /dev/null 2>&1

# Create workspace directory if it doesn't exist
echo "[2/4] Checking workspace directory..."
mkdir -p ./ros2_ws/src

# Build and start the container
echo "[3/4] Starting Docker container..."
docker-compose up -d

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to start container."
    echo "Check the Docker build logs above and ensure Docker is running."
    exit 1
fi

# Enter the container
echo "[4/4] Entering container..."
echo ""
echo "You are now inside the ROS2 container."
echo "Type 'exit' to leave the container."
echo "=========================================="
echo ""

docker exec -it ros2_course_container bash
