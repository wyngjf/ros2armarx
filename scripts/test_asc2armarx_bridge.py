#!/usr/bin/env python
import sys
# license removed for brevity
import rospy
from imagine_common.msg import Affordance, AscPair, ActionParameters
from geometry_msgs.msg import Pose

def talker(action):
    print("Triggering action {}".format(action))
    pub = rospy.Publisher('/kit_gripper/action', Affordance, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    aff = Affordance()
    ap = ActionParameters()
    target = Pose()
    asc = AscPair()

    if action == "SuckingAction":
        target.position.x = 0.2
        target.position.y = 0.3
        target.position.z = 0.4
        target.orientation.w = 0.7070
        target.orientation.x = 0.7070
        target.orientation.y = 0.0
        target.orientation.z = 0.0

        asc.value_pose = target
        asc.value_double = 125.0
        aff.affordance_name = "SuckingAction"

    elif action == "TeachInAction":
        aff.affordance_name = "TeachInAction"
        asc.key = "TeachInAction"
        asc.value_type = 0
        asc.value_str = "TeachInAction"

    elif action == "UnscrewAction":
        pass

    ap.parameters.append(asc)
    aff.action_parameters_array.append(ap)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        test = "test ros2armarx action %s" % rospy.get_time()
        rospy.loginfo(test)
        pub.publish(aff)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker(sys.argv[1])
    except rospy.ROSInterruptException:
        pass
