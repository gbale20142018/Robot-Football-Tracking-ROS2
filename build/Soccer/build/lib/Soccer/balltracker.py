import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class MinimalPublisherSubscriber(Node):
    def __init__(self):
        super().__init__('Image_Subscriber')
        self.subscription = self.create_subscription(
            Image, 'camera_color_frame/image_raw', self.listener_callback, 10)
        self.subscription
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.move = Twist()
        self.br = CvBridge()

    def listener_callback(self, data):
        # Define the gain factor for the angular velocity
        gain = 0.01
        value = Twist()

        self.get_logger().info('Receiving Video Frame')
        img = self.br.imgmsg_to_cv2(data, 'bgr8')
        img = cv2.resize(img, None, 1, 0.5, 0.5, cv2.INTER_CUBIC)

        # Area of Interest
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img2 = cv2.inRange(img_hsv, np.array(
            [23, 144, 17]), np.array([29, 255, 255]))
        rows = img2.shape[0]
        cols = img2.shape[1]

        # Finding Centroid
        M4 = cv2.moments(img2)
        cx4 = 0
        cy4 = 0
        if M4['m00'] > 0:
            cx4 = int(M4['m10']/M4['m00'])
            cy4 = int(M4['m01']/M4['m00'])
        cv2.circle(img2, (cx4, cy4), 5, (0, 255, 0), 2)

        # Line Following

        centroid_pos_x = cx4
        desired_centroid_pos_x = cols/2
        ang_vel = gain * (desired_centroid_pos_x - centroid_pos_x)
        # Set the linear velocity to a fixed value to keep the robot moving forward
        lin_vel = 0.4
        value.linear.x = lin_vel
        value.angular.z = ang_vel
        self.publisher.publish(value)
        cv2.imshow('Center', img)
        cv2.imshow('HSV Image', img2)
        cv2.waitKey(2)

def main(args=None):
    rclpy.init(args=args)
    robotcontrol = MinimalPublisherSubscriber()
    rclpy.spin(robotcontrol)
    robotcontrol.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
