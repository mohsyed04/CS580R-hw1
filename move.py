#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist



def rotate():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
    vel_msg = Twist()

    rospy.sleep(20)

    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    rospy.sleep(15)


    vel_msg.linear.x= 0
    vel_msg.angular.z = 2
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 0
    vel_msg.angular.z = 2
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 2
    vel_msg.angular.z = 0
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 2
    vel_msg.angular.z = 0
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 0
    vel_msg.angular.z = -2
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 2
    vel_msg.angular.z = 0
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 2
    vel_msg.angular.z = 0
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 0
    vel_msg.angular.z = -2
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 2
    vel_msg.angular.z = 0
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 0
    vel_msg.angular.z = 2
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 2
    vel_msg.angular.z = 0
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 0
    vel_msg.angular.z = -2
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 2
    vel_msg.angular.z = 0
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 2
    vel_msg.angular.z = 0
    #M done
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 4
    vel_msg.angular.z = 4
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 4
    vel_msg.angular.z = -4
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 0
    vel_msg.angular.z = 2
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x= 0
    vel_msg.angular.z = -2
    rospy.sleep(15)
    velocity_publisher.publish(vel_msg)
    


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()


if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptException:
        pass




    

