#!/usr/bin/env python
# license removed for brevity
import rospy
from iot_sensor.msg import IoTSensor
import random


def publisher():
    # Create a new publisher, specify topic name, message type, queue size
    iot_sensor_publisher = rospy.Publisher(
        'iot_sensor_topic', IoTSensor, queue_size=10)

    # Initialise node, anonymous = True tells ROS to use a unique name for node
    rospy.init_node('iot_sensor_publisher', anonymous=True)

    # Set loop rate
    rate = rospy.Rate(0.5)  # 10hz

    i = 0
    # Keep publishing until Ctrl+C is pressed
    while not rospy.is_shutdown():
        iot_sensor = IoTSensor()
        iot_sensor.id = random.random()
        iot_sensor.name = 'iot_parking_01'
        iot_sensor.temperature = 24.33 + (random.random() * 2)
        iot_sensor.humidity = 33.41 + (random.random() * 2)

        # Print string to terminal
        rospy.loginfo(iot_sensor)

        # Publish the message
        iot_sensor_publisher.publish(iot_sensor)

        # Sleep to enforce rate
        rate.sleep()
        i = i+1


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
