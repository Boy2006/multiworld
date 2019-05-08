from multiworld.envs.mujoco.sawyer_xyz.sawyer_pick_and_place import (
    SawyerPickAndPlaceEnv,
    SawyerPickAndPlaceEnvYZ,
)
from multiworld.core.image_env import ImageEnv
from multiworld.envs.mujoco.cameras import sawyer_pick_and_place_camera
import numpy as np

env = SawyerPickAndPlaceEnvYZ(
    hand_low=(-0.1, 0.48, 0.05),
    hand_high=(0.0, 0.72, 0.15),
    action_scale=0.02,
    hide_goal_markers=True,
    num_goals_presampled=50,
    p_obj_in_hand=1,
)

while True:
    env.reset()
    env.set_to_goal(
        {'state_desired_goal': env.generate_uncorrected_env_goals(1)['state_desired_goal'][0]}
    )
    action = np.array([-1, 0, -1])
    for _ in range(20):
        env.step(action)
        env.render()
    action = np.array([0, -1, -1])
    for _ in range(20):
        env.step(action)
        env.render()
    action = np.array([0, -1, 1])
    for _ in range(20):
        env.step(action)
        env.render()
    action = np.array([0, 1, 1])
    for _ in range(100):
        env.step(action)
        env.render()

    # for _ in range(100):
        # # action = np.array([0, 0, 1])
        # action = env.action_space.sample()
        # for _ in range(10):
            # obs, _, _, _ = env.step(action)
            # print(env.get_obj_pos())
            # env.render()
        # # obs, _, _, _ = image_env.step(np.zeros(3))
        # # render_cv2(obs)
