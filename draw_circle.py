#!/usr/bin/env python3

from geometry_msgs.msg import Twist
import rospy


def turn(radius):
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started !!!")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(1)
    msg = Twist()

    for j in range(0, 10):
        msg.linear.x = radius
        msg.angular.z = 2
        rospy.loginfo("Radius of circle is %f", radius)
        pub.publish(msg)
        rate.sleep()


if __name__ == "__main__":
    for i in range(2, 5, 1):
        turn(i)