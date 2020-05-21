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


    if action == "SuckingAction":
        aff.affordance_name = "SuckingAction"

        asc = AscPair()
        asc.key = "SuckingPose"
        asc.value_type = 2
        print("test me")
        target.position.x = 0.240
        target.position.y = 0.045
        target.position.z = 0.000
        target.orientation.w = 0.7070
        target.orientation.x = 0.7070
        target.orientation.y = 0.0
        target.orientation.z = 0.0
        asc.value_pose = target
        ap.parameters.append(asc)

        asc1 = AscPair()
        asc1.key = "SuckingPower"
        asc1.value_type = 1
        asc1.value_double = 5.0
        ap.parameters.append(asc1)


    elif action == "TeachInAction":
        aff.affordance_name = "TeachInAction"

        asc = AscPair()
        asc.key = "TeachInAction"
        asc.value_type = 0
        asc.value_str = "TeachInAction"
        ap.parameters.append(asc)

    elif action == "UnscrewAction":
        pass

    aff.action_parameters_array.append(ap)


#    test = "test ros2armarx action %s" % rospy.get_time()
#    rospy.loginfo(test)
#    pub.publish(aff)
#    rospy.spin()

    rate = rospy.Rate(1)
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
