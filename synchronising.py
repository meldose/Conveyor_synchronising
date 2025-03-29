import time # importing time module
from neurapy import move_robot_to_position, servo_j # form nuerapy import modules servo_j


conveyor_speed = 0.5  # settig the conveyor speed

def get_object_pose(): # defining function for getting the object pose
    """Simulated function to get object position from a vision system."""
    return {"x": 0.3, "y": 0.2, "z": 0.1, "qx": 0, "qy": 0, "qz": 0, "qw": 1}

def synchronize_robot(): # defining the function for synchronising the robot
    """Synchronizes robot with moving object on a conveyor belt."""
    object_pose = get_object_pose() # getting the object pose

    # Predict future position based on belt speed
    reaction_time = 1.0  # Delay compensation (seconds)
    future_x = object_pose["x"] + (conveyor_speed * reaction_time) # [X=X0+ velocity*time]

    # Move robot dynamically to the new position
    target_pose = [future_x, object_pose["y"], object_pose["z"], 
                   object_pose["qx"], object_pose["qy"], object_pose["qz"], object_pose["qw"]]

    servo_j(target_pose)  # Move robot in sync

    # Simulate gripping action
    print("Object picked successfully.")

# Run synchronization
synchronize_robot()
