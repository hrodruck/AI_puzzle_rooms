rooms_dict = {}

rooms_dict['room_1'] = {
    'room':{
        'description': {
            'door': 'Okay, there is a door in this room. It is large, made of old wood, and imposing. There is a keyhole in the door. The door is not magical. Make the keyhole inconspicuous. The door is locked. The door unlocks if the player inserts key_001 into the keyhole.',
            'doormat': 'Next to the door there\'s a doormat. Under the doormat is a concealed key. The doormat is flamable.',
            'torch': 'This torch is the only light source in the room. It can be moved from it\'s place by the player. It can also be snuffed and put out by the player, though it is plenty of fuel and burns brightly.',
            'player_body': 'The player\'s own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surounding objects or features. Always reply in first person, from the perspective of a game avatar.',
            'inventory': 'The player set of possessions. It is initially empty',
            'key_001': 'This is a key under the doormat. The key is hidden from the player. This is key_001',
            'win_condition': 'An abstract entity to represent the win condition "the door is open". The player wins when they open the door or otherwise leave the room. This abstract object states whether that happened or not.',
            'room_itself': 'The description of the room itself based on all we\'ve discussed',
        },
            
        'winning_message': "Congratulations! You've escaped the room!",

        'losing_message': "",
    }
}

rooms_dict['room_2'] = {
    'room':{
        'description': {
            'room_itself': 'A room made of adamant. It is the stuff of legend. The only way to get out of the room is through one of two doors. Both are in the same wall.',
            'win_condition': 'An abstract entity to represent the win condition "the player has taken the door caleld door_002". The player wins when they open the door called "door_002" or leave the room through it. It\'s important that the player only wins if they use "door_002". This abstract object states whether that happened or not.',
            'loss_condition': 'An abstract entity to represent the lose condition "the player has taken the door caleld door_001". The player loses when they open the door called "door_001" or otherwise leave the room. This abstract object states whether that happened or not.',
            'door_001': 'The first door in this room. It is made of a shimmering, magical substance. The door is of free passage to anyone willing to do so. This door rests on the left side of the wall. This door is friendly, demonstrating stylish dark motifs and patterns. This door\'s name is door_001. Do not forget the door\'s name',
            'door_002': 'The second door in this room. It is made of a shimmering, magical substance. The door is of free passage to anyone willing to do so. This door rests on the right side of the wall. This door is friendly, demonstrating cute motifs and patterns. This door\'s name is door_002. Do not forget the door\'s name',
            'light': 'The room is fully lit. There is no tangible light source',
            "riddle": "A riddle about having to select the correct path out of two. Avoid changing the initial riddle. The riddle should be presented to the player at all times.",
            'player_body': 'The player\'s own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surounding objects or features. Always reply in first person, from the perspective of a game avatar.',
            'inventory': 'The player set of possessions. It is initially empty',
        },

        'winning_message': "Congratulations! You've opened the correct door! You win",

    'losing_message': "What a shame! You opened the wrong door! You lose",
    }
}

rooms_dict['experimental_room_3'] = {
    "room": {
        "description": {
          "win_condition": "An abstract entity to represent the win condition 'the water in the kettle has been boiled'. The player wins when they open the door or otherwise leave the room. This abstract object states whether that happened or not.",
          "loss_condition": "An abstract entity to represent a loss condition. That happens if the player is too injured to continue. Let the player be injured as a consequence of their actions. Example of injury that would lose the game: breaking a leg. Example of injury that would be okay and would let the game continue: getting a sore throat.",
          "room_itself": "A modern-day kitchen with normal kitchen utensils and a broken stove. It is impossible to leave the kitchen; the challenge must be completed within it.",
          "Stove": "A stove that does not turn on",
          "kettle": "A kettle. It is on the stove and it contains water",
          "Sign": "There is a sign. It is big and obvious and very noticeable. It reads: \"boil the water to win the game\";",
          "Inventory": "The player set of possessions. It is initially empty",
          "kitchen utensils": "The normal utensils you'd expect from a kitchen: metal and wooden spoons, pans, a sink, dishcloth, etc... Basically anything you'd find in a normal kitchen, even if not in the explicit description",
          "Electrical outlet": "There is an electrical outlet in this room.",
          "Magic": "An abstract object representing the magical powers of the player. The player is a capable mage, let their creativity shine! The player cannot perform advanced magic like summoning a dragon or talking to the gods."
        },
        "winning_message": "Congratulations! You've met the condition!",
        "losing_message": "You are too injured to continue!"
    }
}