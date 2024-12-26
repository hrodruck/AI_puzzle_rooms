rooms_dict = {}

rooms_dict['room_1'] = {
    'description': {
        'door': 'Okay, there is a door in this room. It is large, made of old wood, and imposing. There is a keyhole in the door. The door is not magical. Make the keyhole inconspicuous. The door is locked. The door unlocks if the player inserts key_001 into the keyhole.',
        'doormat': 'Next to the door there\'s a doormat. Under the doormat is a concealed key. The doormat is flamable.',
        'torch': 'This torch is the only light source in the room. It can be moved and can be put out, though it is plenty of fuel.',
        'player_body': 'The player\'s own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surounding objects or features. Always reply in first person, from the perspective of a game avatar.',
        'inventory': 'The player set of possessions. It is initially empty',
        'key_001': 'This is a key under the doormat. The key is hidden from the player. This is key_001',
        'win_condition': 'An abstract entity to represent the win condition "the door is open". The player wins when they open the door or otherwise leave the room. This abstract object states whether that happened or not.',
        'room': 'The description of the room itself based on all we\'ve discussed',
    },
        
    'winning_message': "Congratulations! You've escaped the room!",

    'losing_message': "",
}

rooms_dict['room_2'] = {
    'description': {
        'room_itself': 'A room made of adamant. It is the stuff of legend. The only way to get out of the room is through one of two doors. Both are in the same wall.',
        'win_condition': 'An abstract entity to represent the win condition "the player has taken the door caleld door_002". The player wins when they open the door called "door_002" or leave the room through it. It\'s important that the player only wins if they use "door_002". This abstract object states whether that happened or not.',
        'loss_condition': 'An abstract entity to represent the lose condition "the player has taken the door caleld door_001". The player loses when they open the door called "door_001" or otherwise leave the room. This abstract object states whether that happened or not.',
        'door_001': 'The first door in this room. It is made of a shimmering, magical substance. The door is of free passage to anyone willing to do so. This door rests on the left side of the wall. This door is friendly, demonstrating stylish dark motifs and patterns. This door\'s name is door_001. Do not forget the door\'s name',
        'riddle': 'A riddle about having to select the correct path out of two. Avoid changing the initial riddle.',
        'door_002': 'The second door in this room. It is made of a shimmering, magical substance. The door is of free passage to anyone willing to do so. This door rests on the right side of the wall. This door is friendly, demonstrating cute motifs and patterns. This door\'s name is door_002. Do not forget the door\'s name',
        'light': 'The room is fully lit. There is no tangible light source',
        'player_body': 'The player\'s own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surounding objects or features. Always reply in first person, from the perspective of a game avatar.',
    },

    'winning_message': "Congratulations! You've opened the correct door! You win",

    'losing_message': "What a shame! You opened the wrong door! You lose",
}

