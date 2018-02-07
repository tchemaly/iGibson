from gibson.envs.husky_env import HuskyNavigateEnv, HuskyClimbEnv
from gibson.utils.play import play
import argparse
import os

timestep = 1.0/(4 * 22)
frame_skip = 4

config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'configs', 'husky_sensors.yaml')
print(config_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default=config_file)
    args = parser.parse_args()

    env = HuskyNavigateEnv(human=True, timestep=timestep, frame_skip=frame_skip, mode="SENSOR", is_discrete = True, resolution="MID", config = args.config)
    #env = HuskyClimbEnv(human=True, timestep=timestep, frame_skip=frame_skip, mode="SENSOR", is_discrete = True, resolution="MID")
    print(env.config)
    play(env, zoom=4, fps=int( 1.0/(timestep * frame_skip)))