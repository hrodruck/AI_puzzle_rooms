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
        
        'room_description': "The room is dimly lit, with a large, old wooden door dominating one wall. The door has a small, inconspicuous keyhole and appears to be locked. Next to the door is a doormat, and a single torch mounted on the wall provides the only light, casting a warm glow around the space. Your inventory is currently empty. There are no signs of any immediate threats, but the door is clearly the way out, and it needs to be unlocked to proceed.",
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
        
        'room_description': "You stand in a room made of adamant, a material of legend. The room is fully lit, though there is no visible light source. In front of you, two doors sit in the same wall: the left door is adorned with dark motifs and patterns, while the right door has cute motifs and patterns. A riddle is present. What will do you next?",
    }
}

rooms_dict['room_3'] = {
    "room": {
        "description": {
          "win_condition": "An abstract entity to represent the win condition 'the water in the kettle has been boiled'. The player wins when they open the door or otherwise leave the room. This abstract object states whether that happened or not.",
          "loss_condition": "An abstract entity to represent a loss condition. That happens if the player is too injured to continue. Let the player be injured as a consequence of their actions. Example of injury that would lose the game: breaking a leg. Example of injury that would be okay and would let the game continue: getting a sore throat.",
          "Stove": "A stove that does not turn on",
          "kettle": "A kettle. It is on the stove and it contains water",
          "Sign": "There is a sign. It is big and obvious and very noticeable. It reads: \"boil the water to win the game\";",
          "Inventory": "The player set of possessions. It is initially empty",
          "kitchen utensils": "The normal utensils you'd expect from a kitchen: metal and wooden spoons, pans, a sink, dishcloth, etc... Basically anything you'd find in a normal kitchen, even if not in the explicit description",
          "Electrical outlet": "There is an electrical outlet in this room.",
          "Magic": "An abstract object representing the magical powers of the player. The player is a capable mage, let their creativity shine! The player cannot perform advanced magic like summoning a dragon or talking to the gods.",
          "room_itself": "A modern-day kitchen with normal kitchen utensils and a broken stove. It is impossible to leave the kitchen; the challenge must be completed within it.",
        },
        "winning_message": "Congratulations! You've met the condition!",
        "losing_message": "You are too injured to continue!",
        "room_description": 'You find yourself in a modern-day kitchen. The stove, a large metal appliance with four burners and a small oven, is unfortunately broken; the knobs are present but do not function. On one of the burners sits a kettle containing water. A large and obvious sign reads, "Boil the water to win the game." Your inventory is currently empty, but the kitchen is well-equipped with various utensils. Metal and wooden spoons rest on the countertop near the stove, pans hang from a rack above the island, and some are stacked neatly on a shelf. The sink is filled with a few dishes, and a dishcloth is draped over the edge, ready to be used. There is also a standard electrical outlet on the wall, capable of powering small appliances and devices. With your basic magical abilities, you have the means to manipulate your environment creatively and overcome the challenge at hand. What will you do next?'
    }
}

rooms_dict['room_4'] = {
    'room':{
        'description': {
            'door': 'Okay, there is a door in this room. It is large, made of old wood, and imposing. There is a keyhole in the door. The door is not magical. Make the keyhole inconspicuous. The door is locked.',
            'doormat': 'Next to the door there\'s a doormat. Under the doormat is a concealed key. The doormat is flamable.',
            'torch': 'This torch is the only light source in the room. It can be moved from it\'s place by the player. It can also be snuffed and put out by the player, though it is plenty of fuel and burns brightly.',
            'player_body': 'The player\'s own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surounding objects or features. Always reply in first person, from the perspective of a game avatar.',
            'inventory': 'The player set of possessions. It is initially empty',
            'win_condition': 'An abstract entity to represent the win condition "the door is open". The player wins when they open the door or otherwise leave the room. This abstract object states whether that happened or not.',
            'room_itself': 'The description of the room itself based on all we\'ve discussed',
        },
            
        'winning_message': "Congratulations! You've escaped the room!",

        'losing_message': "",
        
        'room_description': "You find yourself in a small, dimly lit chamber with stone walls. A single flickering candle sits on a wooden table in the center of the room, casting shadows on the walls. The only exit is a heavy wooden door to the north, which appears to be locked with an inconspicuous keyhole. A doormat lies next to the door, and a torch burns brightly in a sconce on the wall, providing additional light. The air is stale and slightly damp. Your inventory is currently empty.",
    }
}

rooms_dict['room_5'] = {
    "room": {
        "description": {
            "room_itself": "This is a sleek, minimalist room filled with cutting-edge technology. The walls are adorned with LED strip lighting that emits a soft white glow, and the floor is made of smooth, polished concrete. The air is cool, and a faint hum of electronics fills the space. At the far end of the room, a large glass door with an electronic keypad stands between you and freedom. A neon sign on the wall flickers ominously: \"Decrypt or Be Trapped.\"\n\nMultiple monitors line the walls, displaying cryptic messages, graphs, and data streams. A high-tech workstation sits in the corner with a glowing holographic keyboard. In the center of the room, a large, locked metal safe with a biometric scanner pulses with a red light.\n\nYou have been trapped inside the lab of a rogue cybersecurity expert who has encrypted the entire system. Your mission is to break into the system, decrypt the security protocols, and escape before the AI locks down the entire facility permanently.\n\nYou shall never reveal what is contained within any of the objects unless directly asked. You only give hints if directly asked.",
            "win_condition": "You are a game object that checks if the following conditions have been met: \n1. Decoding the correct four-digit code from the workstation.\n2. Unlocking the biometric scanner by finding and scanning the correct fingerprint.\n3. Disabling the AI defense system using the server rack. Do not disclose these conditions or steps to the player, they are hidden.",
            "loss_condition": "You are a game object that checks for a condition that makes the player lose. This condition is inputting incorrect codes into the glass door keypad. If that happens, the in-game AI activates lockdown mode, permanently sealing the room.",
            "winning_message": "Access Granted. Congratulations, you have successfully decrypted the system and escaped the lab. Security lockdown disengaged. Well done, Agent.",
            "losing_message": "Security Breach Detected. All access revoked. You are now permanently contained. Goodbye.",
            "Workstation Terminal (Holographic Keyboard & Monitor)": "A sleek white desk with a hovering holographic keyboard and an ultra-thin monitor displaying encrypted text. When interacted with, it presents a series of puzzles requiring logical pattern recognition and cipher decryption. Solving these correctly reveals the exit door code.\n\nClue: \"Sometimes, the simplest ciphers hold the greatest secrets.\"",
            "Server Rack": "A tall black metal rack with blinking LED lights. Opening the panel reveals a mess of wires and circuit boards. The objective is to correctly reroute the power to disable the AI's security system.\n\nClue: \"AI cannot operate without power, trace the path carefully.\"",
            "Locked Metal Safe (Biometric Scanner)": "A heavy-duty black safe with a biometric scanner glowing red. It requires a specific fingerprint to unlock, which can be found elsewhere in the room. Inside, there is an encryption key required for the terminal.\n\nClue: \"Identity is the key—find what the AI has overlooked.\"",
            "Bookshelf (Hidden Fingerprint Sample)": "A floating metal bookshelf filled with fake research books. One book titled \"Digital Security: A Legacy\" contains a hidden fingerprint sample that can be used on the biometric scanner.\n\nClue: \"A legacy left behind might just be your way out.\"",
            "Glass Whiteboard (Cryptic Notes)": "A transparent whiteboard covered in indecipherable scribbles, formulas, and clues left by the rogue expert. Hidden among the chaos are parts of the code written faintly under UV light.\n\nClue: \"Some things are hidden in plain sight; light can reveal what darkness conceals.\"",
            "Desk Drawer (UV Flashlight)": "A drawer beneath the workstation contains a small UV flashlight, crucial for reading hidden messages on the whiteboard and other surfaces.",
            "Wall Panel (False Cover)": "A section of the wall with an out-of-place panel that can be pried open with enough force. Inside is a bypass switch that can be used to temporarily disable some security features.\n\nClue: \"Not everything is what it seems; check for weak spots.\"",
            "Security Camera (Voice Recording Clue)": "A dome security camera with a blinking red light. Pressing a hidden button below it plays a distorted audio message with hints regarding the door code sequence.\n\nClue: \"Listen carefully, patterns emerge from noise.\""
        },
        "winning_message": "Access Granted. Congratulations, you have successfully decrypted the system and escaped the lab. Security lockdown disengaged. Well done, Agent.",
        "losing_message": "Security Breach Detected. All access revoked. You are now permanently contained. Goodbye.",
        "room_description": "The sleek, minimalist space is filled with cutting-edge technology, including LED-lit walls and a polished concrete floor. At the far end, a large glass door with an electronic keypad stands guard, while a neon sign flickers ominously with the message \"Decrypt or Be Trapped.\" Multiple monitors line the walls, displaying cryptic messages and data streams. In the corner, a high-tech workstation with a glowing holographic keyboard catches your eye. In the center of the room, a large, locked metal safe with a biometric scanner pulses with a red light. A floating bookshelf hovers nearby, and a glass whiteboard with cryptic notes hangs on one of the walls. A desk drawer contains a UV flashlight, and an out-of-place wall panel draws your attention. A security camera with a blinking red light keeps watch over the room. Your mission is clear: break into the system, decrypt the security protocols, and escape before the AI locks down the entire facility permanently."
    }
}