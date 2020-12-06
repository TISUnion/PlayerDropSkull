# -*- coding: utf-8 -*-
import json
import random

# the possibility for a player to drop his skull
# the value should be from 0.0 to 1.0
P = 0.5


def on_death_message(server, message):
    if random.random() <= P:
        player = message.split(' ')[0]

        PlayerInfoAPI = server.get_plugin_instance('PlayerInfoAPI')
        pos = PlayerInfoAPI.getPlayerInfo(server, player, path='Pos')
        x = int(pos[0])
        y = int(pos[1]) + 1
        z = int(pos[2])
        dim = PlayerInfoAPI.getPlayerInfo(server, player, path='Dimension')
        dim_tran = {
            0: 'minecraft:overworld',
            -1: 'minecraft:the_nether',
            1: 'minecraft:the_end',
        }

        prefix = 'execute in {} run '.format(dim_tran.get(dim, dim))
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
