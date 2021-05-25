#!/usr/bin/env python
# license removed for brevity

import rospy
import speech_recognition as sr
from gtts import gTTS
import playsound
import urllib3

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client(x,y,w):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y	
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = w

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
urllib3.disable_warnings()


# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
	rate = rospy.Rate(10) # 10hz
    	while not rospy.is_shutdown():
		r = sr.Recognizer()
		speech = sr.Microphone()
		# for recognizing speech
		with speech as source:
    			print("Please say your next order")
			speak("Please say your next order")
    			audio = r.adjust_for_ambient_noise(source)
    			audio = r.listen(source)
		# Speech recognition using Google Speech Recognition
		try:
    			recog = r.recognize_google(audio, language = 'en-US')
    			print("You said: " + recog)
			if recog == "go to room" : 		
				print("going to room")
				speak("going to room")
				result = movebase_client(2.5,5,1)
        			if result:
            				rospy.loginfo("Goal room execution done!")
					speak("Goal room execution done")

			elif recog == "go to poster" : 		
				print("going to poster")
				speak("going to poster")
				result = movebase_client(-4.7,-2.7,-0.013)
        			if result:
            				rospy.loginfo("Goal poster execution done!")
					speak("Goal poster execution done")

			elif recog == "come to me" : 		
				print("going to you")
				speak("going to you")
				result = movebase_client(0,0,1)
        			if result:
            				rospy.loginfo("Goal poster execution done!")
					speak("Goal poster execution done")
			else:
				print("I do not understand... can you repeat again")
				speak("I do not understand... can you repeat again")
		except sr.UnknownValueError:
    			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
   			print("Could not request results from Google Speech Recognition service; {0}".format(e))

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
