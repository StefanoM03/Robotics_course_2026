# ROS2 Humble + Gazebo Harmonic - Linux Setup

## Prerequisites

1. **Docker Engine** installed:
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install docker.io docker-compose
   sudo usermod -aG docker $USER
   # Log out and back in for group changes to take effect
   ```

2. **(Optional) NVIDIA GPU Support:**
   ```bash
   # Install nvidia-container-toolkit
   distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
   curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
   curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   sudo apt-get update
   sudo apt-get install nvidia-container-toolkit
   sudo systemctl restart docker
   ```

## Quick Start

### Option 1: Using the start script (Recommended)
```bash
chmod +x start.sh stop.sh
./start.sh
```

### Option 2: Manual commands
```bash
# Allow X11 forwarding
xhost +local:docker

# Create workspace
mkdir -p ros2_ws/src

# Build and start
docker-compose build
docker-compose up -d

# Enter the container
docker exec -it ros2_course_container bash
```

## Testing the Installation

Inside the container:
```bash
# Test ROS2
ros2 topic list

# Test GUI (should open a window with eyes)
ros2 run rviz2 rviz2

# Test Gazebo
gz sim shapes.sdf
```

## NVIDIA GPU Support

If you have an NVIDIA GPU:

1. Install nvidia-container-toolkit (see Prerequisites)
2. Edit `docker-compose.yml`:
   - Comment out the `ros2-gazebo` service
   - Uncomment the `ros2-gazebo-nvidia` service
3. Rebuild: `docker-compose build`

## Helpful Aliases

Inside the container:
- `cb` - Build workspace (`colcon build --symlink-install`)
- `sw` - Source workspace (`source install/setup.bash`)
- `cbsw` - Build and source combined

## Stopping the Container

```bash
./stop.sh
# or
docker-compose down
```

## Troubleshooting

### GUI not showing
```bash
# Make sure X11 is allowed
xhost +local:docker

# Check DISPLAY variable
echo $DISPLAY
```

### Permission denied on workspace
```bash
# Inside container
sudo chown -R ros2user:ros2user ~/ros2_ws
```

### No GPU acceleration
Verify NVIDIA setup:
```bash
nvidia-smi  # Should show your GPU
docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```
