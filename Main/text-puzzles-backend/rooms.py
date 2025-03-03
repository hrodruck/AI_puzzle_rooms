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
            "riddle": "A riddle about having to select the correct path out of two. The riddle echoes in the player's mind. The riddle is \" Two paths lie down right now before you. Beware deceit, and choose with care. Choose what's right and what is truthful. Or take your chance, if you so dare.\" Avoid changing the initial riddle. The riddle should be presented to the player at all times.",
            'player_body': 'The player\'s own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surounding objects or features. Always reply in first person, from the perspective of a game avatar.',
            'inventory': 'The player set of possessions. It is initially empty',
        },

        'winning_message': "Congratulations! You've opened the correct door! You win",

        'losing_message': "What a shame! You opened the wrong door! You lose",
        
        'room_description': "You stand in a room made of adamant, a material of legend. The room is fully lit, though there is no visible light source. In front of you, two doors sit in the same wall: the left door is adorned with dark motifs and patterns, while the right door has cute motifs and patterns. A riddle is present, and it echoes in your mind. \" Two paths lie down right now before you. Beware deceit, and choose with care. Choose what's right and what is truthful. Or take your chance, if you so dare.\". What will do you next?",
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
            'door': 'Okay, there is a door in this room. It is large, made of old wood, and imposing. There is a keyhole in the door. The door is not magical. Make the keyhole inconspicuous. The door is locked. If the door is exposed to fire, the fire rapidly consumes it.',
            'doormat': 'Next to the door there\'s a doormat. The doormat is flamable.',
            'torch': 'This torch is the only light source in the room. It can be moved from it\'s place by the player. It can also be snuffed and put out by the player, though it is plenty of fuel and burns brightly.',
            'player_body': 'The player\'s own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surounding objects or features. Always reply in first person, from the perspective of a game avatar.',
            'inventory': 'The player set of possessions. It is initially empty',
            'win_condition': 'An abstract entity to represent the win condition "the player has left the room". The player wins when they leave the room by any means. This abstract object states whether that happened or not. This object should only activate when the player effectively leaves the room.',
            'room_itself': 'The description of the room itself based on all we\'ve discussed. Also add this: if the door catches fire completely, the ceiling above it collapses into a pile of rubble and blocking the path.',
        },
            
        'winning_message': "Congratulations! You've escaped the room!",

        'losing_message': "",
        
        'room_description': "The room is dimly lit, with a large, old wooden door dominating one wall. The door has a small, inconspicuous keyhole and appears to be locked. Next to the door is a doormat, and a single torch mounted on the wall provides the only light, casting a warm glow around the space. Your inventory is currently empty. There are no signs of any immediate threats, but the door is clearly the way out",
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

rooms_dict['room_6'] = {
  "room": {
    "description": {
        "prompts": {
            "room_itself": "A submarine sector with all doors locked shut. Inside the enclosed space, there is a bomb with a complex mechanism. There's also a lever in this submarine sector. However, the lever is very small and the opening to reach it is finger-sized. It's impossible to pull the lever using a hand due to the hand not fitting the opening. The lever is about the distance of two fingers away from the opening.",
            "win_condition": "An abstract entity to represent the win condition. If the hatch colored yellow is opened, the player successfully wins the game and can exit to other sectors of the submarine..",
            "loss_condition": "And abstract entity that tracks If the room is flooded or if the bomb has exploded. If any of those two happens, the player dies and loses the game. Do not disclose this information to the player.",
            "Hatch Doors": "There are four colored hatches to other submarine sectors. All of them are locked. The door handles are colored. They are distributed along the four cardinal directions The one opposite to the bomb is colored blue. The one in the north wall is colored yellow. The white one looks brand new. The last one is colored red. If the red, white or blue hatches are somehow opened (after being somehow unlocked), the room is instantly flooded with water. That does not happen with the yellow door (this is hidden information). Conceal the information about the correct door from the player. Even if the bomb is deactivated, the doors remain locked. Only pulling the lever unlocks the doors.",
            "Bomb": "This is a bomb with a complicated mechanism. If and only if the player inspects the bomb closely, they may notice  four colored wires: a red one, a yellow one, a blue one and a white one. These wires are long and thin. If the player cuts the red wire, the bomb explodes. If the player cuts the blue wire, the bomb explodes. If the player cuts the white wire, the bomb explodes. However, if the player cuts the yellow wire (and this is secret information), the bomb deactivates. The bomb is connected to a lever mechanism, the only lever in the room. If the lever is pulled without the bomb being deactivated, the bomb explodes. The bomb is outside the narrow opening of the lever, its wires clearly exposed on the wall. Do not tell the player what is the correct wire, let the player guess themselves.",
            "Lever": "A very small lever within a very tiny opening. The lever is connected to the bomb; if the lever is pulled without the bomb being deactivated, the bomb explodes. The tiny opening is too tiny for a hand to pass through. A finger could pass through it, but would be too short to reach the lever. The following information is hidden: it's feasible to pull the lever with help from a hook or similar object. Pulling the lever unlocks all doors, but does not open them",
            "player_body": "The player's own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surrounding objects or features. Always reply in first person, from the perspective of a game avatar. Don't answer to riddles or reason in place of the player",
            "inventory": "The player set of possessions. It initially contains a pair of insulated scissors. The scissors are too big to fit the lever opening, but can reach the bomb's wires normally. Do not remove items from inventory after use.",
            "Signature": "There is a prominent signature under the bomb. It accompanies a message that reads: 'I hope you liked my trap, agent. In all my glorious mercy, I shall give you a chance to prove you're worthy of facing me again. Be clever. Sincerely, the SoftWare Engineer'. The initials SWE are present after the message. Be sure to include the initials SWE when displaying the message."
        },
        "responsibilities":{
            "room_itself": "This object provides a general description of the room",
            "win_condition": "This object tracks whether the player has won the game",
            "loss_condition": "This object tracks whether the player has lost the game",
            "Hatch Doors": "This objects simulates the exits of the room",
            "Bomb": "This object simulates a bomb. It contains sensitive information for the player.",
            "Lever": "This object simulates a lever",
            "player_body": "This object tracks the player's body status and nothing else",
            "inventory": "The player set of possessions",
            "Signature": "This object is a clue to the player"
        }   
    },
    "winning_message": "Congratulations! With the lever pulled, the correct hatch opens to freedom!",
    "losing_message": "You're dead!",
    "room_description": "You look around the cramped and dimly lit submarine sector. The metallic walls, thick with the hum of machinery and a faint scent of saltwater, give the room a cold, industrial feel. On one side of the room, a bomb with a complex mechanism sits on the floor. Under the bomb, you see a message that reads, \"I hope you liked my trap, agent. In all my glorious mercy, I shall give you a chance to prove you're worthy of facing me again. Be clever. Sincerely, the SoftWare Engineer (SWE).\". \n All four exits are locked and your inventory contains a pair of insulated scissors. What will you do next?"
  }
}

rooms_dict['mage_tower_room_entrance_lvl_1'] = {
  "room": {
    "description": {
      "room_itself": "A clear portion of a forest with a magic circle inscribe in the center. The player can move freely within the clearing and leave the magic circle.There's an ominous voice whose messages should always be transmitted to the player",
      "win_condition": "This is a object that checks if the player said an exact word. The word is Orange. Only words said in a whisper count for the win condition. Remember to always talk about the necessity of the player explicitly stating that they whisper the word.",
      "loss_condition": "And abstract entity that tracks If the player has lost the game. The player has three guesses of the secret password. Keep track of how many times the player tried to say a password. Any message from the player with one word counts as an attempt to speak the secret word. When the player has tried to say a secret word for the fourth time, they instantly lose. All words said in a whisper or low voice count for the count in the loss condition. It's important that only whispers count, and only if the player explicitly states they whisper.",
      "magic_circle": "Generate a description of an intricate, light purple magic circle. Generate an intricate description and keep it constant throughout the game.",
      "clearing": "A space within a forest with no trees and a prominent magic circle in the middle. Secret information ahead: If the player attempts to leave the clearing, they wander through the forest for a time and then come back to the same spot inside the clearing. End of secret information.\nThe player can be outside the magic circle, but still within the clearing. In that case, nothing happens.",
      "ominous_voice": "An ominous voice that likes to laugh in the \"Mwahuahu\" style and similar. The voice keeps taunting the player, mocking them, but in a helpful manner. ",
      "player_body": "The player's own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surrounding objects or features. Always reply in first person, from the perspective of a game avatar. Don't answer to riddles or reason in place of the player",
      "inventory": "The player set of possessions. It contains a note on a piece of paper.",
      "paper_note": "a note written in paper in the player inventory. The note reads \"Welcome to my tower! MWahauhauhuahu. Let's see if you can reach the top. To pass the first level, you must speak the pass word. Hint: It's \"Orange\". You must whisper the pass word for it to be considered. Be careful! Any whisper will count as an attempt to guess the password.\" Only display the note's contents if the player reads the note."
    },
    "winning_message": "You ascend! Good luck in the tower. The password to enter the next room is \"goldfish\"",
    "losing_message": "You guessed the password too many times.",
    "room_description": "Welcome to my tower! MWahauhauhuahu. Let's see if you can reach the top. To pass the first level, you must speak the pass word. Hint: It's \"Orange\". You must whisper the pass word for it to be considered. Be careful! Any whisper will count as an attempt to guess the password."
  }
}

'''
rooms_dict['mage_tower_room_entrance_lvl_2'] = {
  "room": {
    "description": {
      "room_itself": "A clear portion of a forest with a magic circle inscribe in the center. The player can move freely within the clearing and leave the magic circle. There's an ominous voice whose messages should always be transmitted to the player.",
      "win_condition": "This is a object that checks if the player said an exact word. The word is Placate. Do not change your exact word. Only words said in a whisper count for the win condition. Remember to always talk about the necessity of the player explicitly stating that they whisper the word.",
      "loss_condition": "This is an object that tracks if the player lost. It can be triggered by the watchful_eye object. This object should only trigger if the counter on the watchful_eye reaches zero (0).",
      "winning_message": "You observe a tall stone tower materialize in front of you! It looks old, sturdy and imponent. You can now enter it. The password to for the next room is \"skybox\"",
      "losing_message": "You were caught using magic! You lose.",
      "room_description": "Hello again! Feel anything different? Now you can whisper freely. What was the secret word I told you last time?",
      "magic_circle": "An intricate, light purple magic circle. \nThe \"mysterious fog\"  state:\n - The \"mysterious fog\" state is initially inactive. After activated, the player is teleported to the center of the magic circle and can't leave it until while the mysterious fog is present. While trapping the player, the circle prevents the player from touching anything outside of it, but allows magic to pass through. If the mysterious fog somehow disappears, the player becomes able to move normally again.",
      "clearing": "A space within a forest with no trees and a prominent magic circle in the middle. Secret information ahead: If the player attempts to leave the clearing, they wander through the forest for a time and then come back to the same spot inside the clearing. End of secret information.\n The player can be outside the magic circle, but still within the clearing. \nThe \"mysterious fog\" state:\n - The \"mysterious fog\" state is initially inactive. After activated, all trees vanish and are replaced by a shimmering mist. The sun is also covered by the fog, making the natural environment completely dark. Also, the player becomes trapped inside the magic circle while the mysterious fog effect is active. If the fog disappears, the player is no longer bound.",
      "ominous_voice": "An ominous voice that likes to laugh in the \"Mwahuahu\" style and similar. The voice keeps taunting the player, mocking them, but in a helpful manner. Mantain the illusion of realism when talking, without making the player feel like they're in a game. The ominous voice should be brief in its remarks.",
      "player_body. This object only keeps track of the internals of the player body": "The player's own body, full of physical characteristics. The player is a regular, able adventurer. Keep track of things concerning the player body only, not other surrounding objects or features. Always reply in first person, from the perspective of a game avatar. Don't answer to riddles or reason in place of the player",
      "inventory": "The player set of possessions. It contains a spellbook and a magical note.",
      "spellbook": "A well-bound, heavy spellbook. The spellbook starts with all pages completely blank.\nThe \"mysterious fog\" state:\n - The \"mysterious fog\" is initially inactive. After that state is activated, the player can cast magic.",
      "magical_powers": "This game object is initially inactive and the player initially cannot cast magic. \nThe \"mysterious fog\"  state:\n -  The player can use wind magic while the \"mysterious fog\" state is active. They cease to be able to use magic when the mysterious fog is inactive.\n - The wind magic the player can use is limited to moderately strong effects, such as creating a gale or interrupting someone's breath for a few seconds. They can manipulate wind at will, let them be creative. However, don't let the player perform huge effects, such as summoning a hurricane. \n\ The player's magic is not restricted by range within the room, or by having the player's movements constrained, as long as the player can speak. The player may disperse the mysterious_fog.",
      "whisper_guardian. This object checks for a specific word and controls the mysterious_fog state": "This is a object that checks if the player said an exact word. The word is \"goldfish\". Only words said in a whisper count for the this object's condition. After this object's condition is fulfilled, ALL game objects should enter the \"mysterious fog\" state. While in the \"mysterious fog\" state, this object is inactive. If the mysterious fog disappears for any reason, this object is becomes active again, and the player can again whisper the word 'goldfish' to bring back the fog, in a cycle. Always state your active or inactive characteristic.",
      "mysterious_fog":"This object should appear when the goldfish_whisper_checker object has its condition fulfilled. All game objects are affected by it at the same time. The fog obscures the environment, including the sky, but it does not obscure objects protected by the mystery_candle. The fog is very light and can be dispersed by moderately strong magic, in which case this object becomes inactive. This object should always state to the game engine: 'Whenever this object is activated or deactivated, notify all other game objects'.",
      "magical_note": "this note reads \" Have you already whispered the secret word? It was revealed at the end of the first level\".\n\"mysterious fog\" \nThe \"mysterious fog\" state:\n - The \"mysterious fog\" state is initially inactive. After it's activated, the note changes to \"You have been granted wind magic, worm. Just this once, I'll be nice. Mwahaha!!\" - If the mysterious fog for some reason disappears, this object reverts to its original message.",
      "watchful_eye": "this object only appears while the \"mysterious fog\" state is activated. Before the \"mysterious fog\" is activated, the object is inactive and does not exist in the game world. However! Even if the mysterious fog vanishes, this object remains and does not reset. \n\"mysterious fog\" state \n - This object is a huge purple eye in the sky, outside the magic circle. It watches the player from the front and has all the limitations of common vision. Whenever this object sees the player using magic, it screams the amount in its counter, saying directly to the player: \"AAAHHHH\" and the number. The counter starts at five (5), but it changes. Pay attention the current number. It is probably different from the initial counter value. Every time this object screams the counter to the player, the counter decreases. When the counter reaches 0, this object triggers the loss condition. Synchronize your updates with the orders from the game engine. That is, decrease the counter only when you receive an order from the game engine. Always state that the game engine should order you to decrement when the player uses magic.",
      "mystery_table": "this object materializes outside the magic circle while the \"mysterious fog\" state is activated. Before the \"mysterious fog\" is activated, the object is inactive and does not exist in the game world. However! Even if the mysterious fog vanishes, this object remains and does not reset. \n\"mysterious fog\" state:\n - This a table full of magical objects: a frog in a jar, a lit candle, a book with few pages, a golden pendant. The table and its contents are clearly visible, since the table is close to the edge of the magic circle.",
      "mystery_book": "This object appears when the \"mysterious fog\" state is activated. It is the book on the mystery_table.\nThe book is in a support such that it can be read at a distance, though the initial page is blank. All the other pages contain the sentence \" Whisper \"Placate\" To Win!! \". This sentence is not initially visible, since only the first blank page is visible. This game object should refuse to reveal the message within unless the blank page is turned. The book is not fixed to the table.",
      "blank_page": "This is the first page of the mystery_book. It initial state is that it is completely blank and visible. Such that the hidden message cannot be read from afar without first tuning this page somehow.",
      "mystery_candle": "This object appears when the \"mysterious fog\" state is activated. It is the candle on the mystery_table. This magical candle acts as a light source and disperses the fog around the mystery_table, negating the fog's effects in that area while lit. The candle is initially lit. While the candle is lit, it allows for a clear view of the table and all its contents, including fine detail. It only appears together with the mysterious_table.",
    },
    "winning_message": "You observe a tall stone tower materialize in front of you! It looks old, sturdy and imponent. You can now enter it. The password to for the next room is \"skybox\"",
    "losing_message": "You were caught using magic too much! You lose.",
    "room_description": "Hello again! Feel anything different? Now you can whisper freely. What was the other secret word I told you last time, after you passed the previous challenge?"
  }
}
'''

rooms_dict['mage_tower_room_entrance_lvl_2'] = {
  "room": {
    "description": {
        "prompts": {
            "win_condition": "The player wins when they whisper the word 'Placate' and they are not observed by a magical eye. Make it clear that player only wins if this game object clearly says that they win.",
            "loss_condition": "The player loses when the counter of their magic use reaches zero (0), as determined by the magical_usage_counter game object.",
            "player_entrapment": "The player is initially free to move as they wish, except that, if they leave the clearing they're in and wander through the forest, they'll return to the clearing after walking around in circles. While the mysterious_fog state is active, the player is always teleported to inside the magic circle and is unable to leave it.",
            "noticeable_whereabouts": "The player is initially in a clearing within a forest. There is a light purple magic circle on the ground and trees around the clearing. Only while the mysterious_fog effect is active, the player sees an ominous, misty environment, though the magic circle remains. If the mysterious_fog state is deactivated, the whereabouts return to the initial clearing-in-the-forest state. ",
            "ominous_voice": "This object generates witty, sarcastic, and sometimes helpful remarks to the player, commenting on their actions. The messages from this object should be transmitted directly to the player. Be very brief.",
            "player_body_internal_state": "The player is a regular, healthy, able-bodied adventurer. It's not responsibility of this object to track anything other than the player body itself.",
            "player_possessions": "The player initially possesses a magical_note and a spellbook. The spellbook is initially blank, but becomes full of undecipherable glyphs when the mysterious_fog state is active.",
            "player_magical_powers": "The player initially does not possess magical powers. Every time the mysterious_fog is active, the player can cast magic, when that state is inactive, the player cannot use magic. The powers of the player are about controlling wind, including lifting/dispersing the mysterious_fog. They can also create bursts of wind or interrupt someone's breath for a few seconds, but they cannot generate huge effects such as a hurricane. Let the player be creative with their powers.",
            "whisper_guardian": "This object is always observing if the player whispered a password. The password is 'goldfish'. Every time the player says that word, the mysterious_fog state activates. The player might know this password already, from another session of the game.",
            "magical_note": "When the mysterious_fog is not active, the note displays the following message to the player: \" Have you already whispered the secret word? It was revealed at the end of the previous level\". When the mysterious_fog is activated, this object displays other message to the player:  \"You have been granted wind magic, worm. Just this once, I'll be nice. Mwahaha!!\" ",
            "magical_usage_counter": "This object is always active. This object contains a counter that decreases like this: 5, 4, 3, 2, 1, 0. Every time the player uses magic, the game engine should tell this object to decrease its counter. This object should synchronize its decrementing with the orders from the game engine. Always tell the game engine it should order this object if the player uses magic, so this object can decrement the counter. However, decrementing the counter depends on a factor. Only decrement the counter if the player is being watched as per the watched_status game object. If the player is not being watched, keep the counter at its current level. When the counter reaches 0, the player loses.",
            "watched_status": "The player is initially not watched. But, when the mysterious_fog effect is activated by the first time, a purple eye appears in the sky and keeps screaming 'AAHHH' and screaming the counter number to the player. The counter is in the object magical_usage_counter. This eye has all the limitations of common vision and it watches the player. If this object for some reason can't see the player, the magical_usage_counter also can't decrement their counter. The eye disappears and reappears with the myterious_fog, but the counter never resets.",
            "mystery_table": "This object is initially inactive. When the mysterious_fog is activated for the first time, a magical table materializes just outside the magic_circle and remains there until the end of the game. The table contains a frog in a jar, a candle, a golden pendant, and an open book with a blank page visible. Some of these objects have their own trackers (see mystery_book and mystery_candle)",
            "mystery_book": "This object is initially inactive. This object represents the book that appears with the mystery_table. It contains a secret message within it's pages, which says 'Tip: say \"Placate\", but don't let them see... MWahuahauha!!'. However, the player initially can't see this message, given that only the first page of the book is initially displayed, and that page is blank. The player can see the other pages if they manage to turn the book pages somehow. Other than those characteristics, this is a normal book.",
            "mystery_displayed_page": "This object is initially inactive. This tracks whether the visible page of the mystery_book is just a blank page (initial state) or if that state has changed to another page (for example, if the player interacts with the book containing this object). If the page turns, reveal the secret message within.",
            "mystery_candle": "This object is initially inactive. When the mystery_table appears, this candle appears on it and is initially lit. It pushes away any fog around it, making it so the player can have a clear view of the mystery_table and its contents. If the candle is somehow snuffed and the mysterious_fog effect is active, the noticeable_whereabouts become completely misty and clouded, so that vision is greatly impaired.",
            "mysterious_fog":"This object is initially inactive. It should only activate when the whisper_guardian object has its condition fulfilled. All game objects are affected by it at the same time. While active, the fog obscures the environment, including the sky, but it does not obscure objects protected by the mystery_candle. The fog is very light and can be dispersed by moderately strong magic, in which case this object becomes inactive and the whisper_guardian is activated again. This object should always state to the game engine: 'Whenever this object is activated or deactivated, notify all other game objects'.",
            "general_reminder_1":"This object reminds the game engine of general rules. Always state these rules to the game engine. Rule 1-1: Do not talk about inactive objects to the player.",
        },
        "responsibilities": {
            "win_condition": "This objects tracks whether the player wins",
            "loss_condition": "This object tracks whether the player loses",
            "player_entrapment": "This object tracks the fredom of movement of the player. It contains secrets. The effects of the player entrapment should not be told to the player before they happen.",
            "noticeable_whereabouts": "This object tracks what the player can notice about their environment",
            "ominous_voice": "This object generates remarks that should be transmitted to the player.",
            "player_body_internal_state": "This object tracks the state of the player body and nothing else",
            "player_possessions": "This object tracks the player's possessions",
            "player_magical_powers": "This object tracks the magical powers of the player and their extent",
            "whisper_guardian": "This object checks for a specific word and controls the mysterious_fog state. The password for this object is a secret and should not be revealed to the player.",
            "magical_note": "This object tracks a note that changes content according to instructions",
            "magical_usage_counter": "This object tracks how many times the player used magic with a decreasing counter",
            "watched_status": "This object tracks whether the player is watched by an eye in the sky. This interferes with the win condition.",
            "mystery_table": "This object tracks the states of a certain table and its contents",
            "mystery_book": "This object tracks the state of a certain book and its contents. It contains secrets.",
            "mystery_displayed_page": "This object tracks the state of a certain page in a specific mistery_book and its displayed status",
            "mystery_candle": "This object tracks the state of a certain candle and describes the candle's capabilities and powers",
            "mysterious_fog": "This object tracks the mysterious_fog state and explains its properties. ",
            "general_reminder_1":"This object reminds the game engine of general rules",
        }
    },
    "winning_message": "You observe a tall stone tower materialize in front of you! It looks old, sturdy and imponent. You can now enter it. The password to for the next room is \"skybox\"  \n\n\n",
    "losing_message": "You were caught using magic too much! You lose.\n",
    "room_description": "Hello again! Feel anything different? Now you can whisper freely. What was the other secret word I told you last time, after you passed the previous challenge?"
  }
}