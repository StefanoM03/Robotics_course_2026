import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from tf_transformations import quaternion_from_euler


class StaticFramePublisher(Node):

    def __init__(self, transformation):
        super().__init__('static_turtle_tf2_broadcaster')

        self._tf_publisher = StaticTransformBroadcaster(self)

        # Publish the static transform once at startup
        self.make_transforms(transformation)

    def make_transforms(self, transformation):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = transformation[1]    # parent frame
        t.child_frame_id  = transformation[2]    # child frame

        t.transform.translation.x = float(transformation[3])
        t.transform.translation.y = float(transformation[4])
        t.transform.translation.z = float(transformation[5])

        # Convert roll-pitch-yaw (radians) to quaternion
        quat = quaternion_from_euler(
            float(transformation[6]),   # roll
            float(transformation[7]),   # pitch
            float(transformation[8]))   # yaw

        t.transform.rotation.x = quat[0]
        t.transform.rotation.y = quat[1]
        t.transform.rotation.z = quat[2]
        t.transform.rotation.w = quat[3]

        self._tf_publisher.sendTransform(t)


def main():
    rclpy.init()
    node = StaticFramePublisher(sys.argv)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()