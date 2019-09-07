import json
from helper import setup_exp, setup_run, parser, pretty, scale
from Environment import OmnetLinkweightEnv
with open('DDPG.json') as jconfig:
	DDPG_config = json.load(jconfig)
	DDPG_config['EXPERIMENT'] = 'runs/'

	folder = setup_run(DDPG_config)
	env = OmnetLinkweightEnv(DDPG_config, folder)
	s_t = env.reset()
	env.step([0.5 for _ in range(21)])


