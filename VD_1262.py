#!/usr/bin/env python
#Importing the required Python libraries
import rospy 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
PI = 3.1415926535897

#Initializing the ROS node
rospy.init_node('node_turtle_revolve', anonymous=True)
	
#Initializing the publisher and the message
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

pose_msg = Pose()

def pose_callback(pose_msg):
	data = pose_msg.x	

def main(): 	
	vel_msg = Twist()

	angle = 2*PI

	vel_msg.linear.y=0
	vel_msg.linear.z=0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0.2

	# Setting the current time for distance calculation
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

	rate = rospy.Rate(10)

	while(current_angle <= angle):
		t1 = rospy.Time.now().to_sec()
		current_angle = 0.2*(t1-t0)
		print(current_angle)
		vel_msg.linear.x= 1
		velocity_publisher.publish(vel_msg)
		rospy.loginfo("Moving in a circle")
		rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

		rate.sleep()

	if (pose_msg.x <= 5.544447):
		vel_msg.linear.x= 0.2
		velocity_publisher.publish(vel_msg)
		print(current_angle)
		rospy.loginfo("Goal reached")


#Python Main
if __name__ == '__main__':
    try:
         main()
    except rospy.ROSInterruptException:
        pass
