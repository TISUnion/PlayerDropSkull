# -*- coding: utf-8 -*-
import json
import random

# the possibility for a player to drop his skull
# the value should be from 0.0 to 1.0
P = 0.5


def on_death_message(server, message):
	if random.random() <= P:
		player = message.split(' ')[0]
		api = server.get_plugin_instance('PlayerInfoAPI')
		data = api.getPlayerInfo(server, player)
		x, y, z = data['Pos']
		dim = data['Dimension']
		dim_mapping = {
			0: 'overworld',
			-1: 'the_nether',
			1: 'the_end'
		}
		prefix = 'execute in minecraft:{} run '.format(dim_mapping[dim])
		nbt = json.dumps({
			'Item': {
				'id': 'minecraft:player_head',
				'Count': 1,
				'tag': {
					'SkullOwner': {
						'Name': player
					}
				}
			}
		})
		command = prefix + 'summon item {} {} {} {}'.format(x, y, z, nbt)
		server.execute(command)
