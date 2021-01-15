# -*- coding: utf-8 -*-
import json
import random

# the possibility for a player to drop his skull
# the value should be from 0.0 to 1.0
P = 0.2


def on_death_message(server, message):
	if random.random() <= P:
		player = message.split(' ')[0]
		api = server.get_plugin_instance('PlayerInfoAPI')
		x, y, z = api.getPlayerInfo(server, player, path='Pos')
		dim = api.getPlayerInfo(server, player, path='Dimension')
		dim_mapping = {
            0: 'minecraft:overworld',
            -1: 'minecraft:the_nether',
            1: 'minecraft:the_end',
            'minecraft:overworld': 'minecraft:overworld',
            'minecraft:the_nether': 'minecraft:the_nether',
            'minecraft:the_end': 'minecraft:the_end'
        }
		prefix = 'execute in {} run '.format(dim_mapping[dim])
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
