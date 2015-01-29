"""    @author:            Guang Yang
       @mktime:            1/26/2015
       @description:       Utility functions for encoding/decoding avro files
"""
import json


def read_json(fname):
    """ Open json file puts it into dictionary """

    with open(fname, 'r') as my_json:
        my_dict = json.load(my_json)
    return my_dict


def get_num_snapshot(extended_match_json, player0_id):
    """ Get the number of snapshots taken in the match """

    return len(extended_match_json['WorkersActiveCount'][player0_id])


def get_snapshot_output(file_name, snapshot)
    """ get new target file name based on snapshot number
    """

    snapshot_output = "{}_snapshot{}.{}".format(
        os.path.splitext(match_name)[0],
        snapshot,
        os.path.splitext(match_name)[1])

    return snapshot_output


def get_player_id(extended_match_json, player):
    """ Get the player_id as a **STRING** for player 0 and 1 """

    return extended_match_json['WorkersActiveCount'][player]
