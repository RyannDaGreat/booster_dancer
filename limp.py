from booster_robotics_sdk_python import ChannelFactory, B1LowCmdPublisher, LowCmd, LowCmdType, MotorCmd, B1JointCnt, B1JointIndex
from booster_robotics_sdk_python import (
    ChannelFactory,
    B1LocoClient,
    B1LowCmdPublisher,
    B1LowStateSubscriber,
    LowCmd,
    LowState,
    B1JointCnt,
    RobotMode,
    GetModeResponse
)

import pickle

def set_global(name,value):
    globals()[name]=value

@globalize_locals
def _init_communication() -> None:
    ChannelFactory.Instance().Init(0)
    
    handler=partial(set_global,'low_state') #Low Level State
    low_state_subscriber = B1LowStateSubscriber(handler)
    low_state_subscriber.InitChannel()

    # low_cmd_publisher = B1LowCmdPublisher()
    # low_cmd_publisher.InitChannel()
    # low_cmd = LowCmd()

    client = B1LocoClient()
    client.Init()

@globalize_locals
def _init_custom_mode():
    #prepare_low_cmd(
        #low_cmd,
        #q=dof_init_pose,
        #stiffness=low_stiffness,
        #damping=high_damping
    #)
    #low_cmd_publisher.Write(low_cmd)

    client.ChangeMode(RobotMode.kCustom)

    # Wait until near target_q.
    #_get_state()
    #while np.linalg.norm(q - dof_init_pose) > 1.0:
        #time.sleep(0.01)
        #_get_state()

_init_communication()
_init_custom_mode()
while True:
    try:
        mystery_list = low_state.motor_state_serial
        #print(len(mystery_list))
        if len(mystery_list):
            mystery_element=mystery_list[0]
            value=mystery_element.q
            value=iblend(value,-1,1)
            print()
        sleep(.01)
    except Exception:
        pass
    
