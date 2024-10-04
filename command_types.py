
command_types = {
    "Check Spell Use": {
        "format": "!eq % shouldUseSpell{},true",
        "params": ["Slot Number"],
        "description": "Checks if a spell should be used",
        "example": "!eq %  shouldUseSpell1,true"
    },
    "Check Hotbar": {
        "format": "ch{}, {}",
        "params": ["Slot Number", "Delay Variable"],
        "description": "Checks if a hotbar slot is ready to use",
        "example": "ch1, queueDelay"
    },
    "Check Range": {
        "format": " {}",
        "params": ["Range Variable"],
        "description": "Checks a range condition",
        "example": " inRangedAttackRange"
    },
    "Press Key": {
        "format": " spell{}d",
        "params": ["Spell Number"],
        "description": "Presses a key to cast a spell",
        "example": " spell1d"
    },
    "Store Key": {
        "format": "store % key, spell{}",
        "params": ["Spell Number"],
        "description": "Stores the key of a spell",
        "example": "store % key, spell1"
    },
    "Go To": {
        "format": "gt{}",
        "params": ["Line Number"],
        "description": "Jumps to a specific line in the macro",
        "example": "gt16"
    },
    "Equal To": {
        "format": "eq % {},{}",
        "params": ["Variable (prefix with VAR if needed", "Value"],
        "description": "Checks if a variable is equal to a value",
        "example": "eq %  mobCount,5"
    },
    "Not Equal To": {
        "format": "!eq % {},{}",
        "params": ["Variable (prefix with VAR if needed", "Value"],
        "description": "Checks if a variable is not equal to a value",
        "example": "!eq %  mobCount,0"
    },
    "Less Than": {
        "format": "cmp % {},{}",
        "params": ["Value1 (prefix with VAR if needed", "Value2 (prefix with VAR if needed"],
        "description": "Checks if Value1 is less than Value2",
        "example": "cmp %  playerHP,0.5"
    },
    "Greater Than or Equal": {
        "format": "!cmp % {},{}",
        "params": ["Value1 (prefix with VAR if needed", "Value2 (prefix with VAR if needed"],
        "description": "Checks if Value1 is greater than or equal to Value2",
        "example": "!cmp %  playerMP,0.7"
    },
    "Set Release Timer": {
        "format": "ct % releaseTimer",
        "params": [],
        "description": "Checks the release timer",
        "example": "ct % releaseTimer"
    },
    "Store Release Timer": {
        "format": "store % releaseTimer,{}",
        "params": ["Value"],
        "description": "Stores a value in releaseTimer",
        "example": "store % releaseTimer,0"
    },
    "Random Range": {
        "format": "rand{},{}",
        "params": ["Min", "Max"],
        "description": "Generates a random number between Min and Max",
        "example": "rand100,500"
    },
    "Multiply Random": {
        "format": "mul % RAND,{}",
        "params": ["Multiplier"],
        "description": "Multiplies RAND by Multiplier",
        "example": "mul % RAND,0.001"
    },
    "Store Queue Delay": {
        "format": "store % queueDelay, RAND",
        "params": [],
        "description": "Stores RAND into queueDelay",
        "example": "store % queueDelay, RAND"
    },
    "Custom Command": {
        "format": "{}",
        "params": ["Command Text"],
        "description": "Enter a custom command",
        "example": "your custom command here"
    },
    "Hold Key Down": {
        "format": "[key code]d",
        "params": ["Key Code"],
        "description": "Holds down the key",
        "example": "87d"
    },
    "Release Key": {
        "format": "[key code]u",
        "params": ["Key Code"],
        "description": "Releases the key",
        "example": "87u"
    },
    "Move Mouse": {
        "format": "m{},{}",
        "params": ["X", "Y"],
        "description": "Moves mouse cursor to (X, Y",
        "example": "m100,200"
    },
    "Random Move Mouse": {
        "format": "rm{}",
        "params": ["[x1],[y1];[x2],[y2];..."],
        "description": "Randomly moves mouse to one of the specified positions",
        "example": "rm100,200;150,250"
    },
    "Random Key Down": {
        "format": "rkd{},{}",
        "params": ["Key1", "Key2"],
        "description": "Holds down a random key from the list",
        "example": "rkd87,65,83"
    },
    "Random Key Up": {
        "format": "rku",
        "params": [],
        "description": "Releases the key held by the last rkd command",
        "example": "rku"
    },
    "Key Down Conditional": {
        "format": "kd{}",
        "params": ["Key Code"],
        "description": "If the key is pressed, processes the rest of the line",
        "example": "kd87|87d|s1000|87u"
    },
    "Key Down Physical": {
        "format": "kd*{}",
        "params": ["Key Code"],
        "description": "Checks if the physical key is pressed",
        "example": "kd*87|87d|s1000|87u"
    },
    "Sleep": {
        "format": "s{}",
        "params": ["Milliseconds"],
        "description": "Waits for specified milliseconds",
        "example": "s1000"
    },
    "Random Sleep": {
        "format": "rs{},{}",
        "params": ["Min Milliseconds", "Max Milliseconds"],
        "description": "Waits for a random time between min and max milliseconds",
        "example": "rs500,1000"
    },
    "Set Timer": {
        "format": "st % {},{}",
        "params": ["Timer Name", "Delay"],
        "description": "Sets a timer",
        "example": "st % releaseTimer,5000"
    },
    "Check Timer": {
        "format": "ct % {}",
        "params": ["Timer Name"],
        "description": "Checks if the timer has expired",
        "example": "ct % releaseTimer"
    },
    "Camera Angle": {
        "format": "c{}",
        "params": ["Angle"],
        "description": "Adjusts camera horizontal angle (-180 to 180 degrees",
        "example": "c90"
    },
    "Camera Vertical Angle": {
        "format": "cy{}",
        "params": ["Angle"],
        "description": "Adjusts camera vertical angle",
        "example": "cy45"
    },
    "If Target is Mob": {
        "format": "it",
        "params": [],
        "description": "If targeting a mob, processes the rest of the line",
        "example": "it|87d|s1000|87u"
    },
    "If Being Targeted": {
        "format": "ibt{},{}",
        "params": ["Type", "Distance"],
        "description": "If being targeted by an entity of type within distance",
        "example": "ibt1,100"
    },
    "Target": {
        "format": "tar",
        "params": [],
        "description": "Populates TN (target name and TID (target ID",
        "example": "tar"
    },
    "Target Distance": {
        "format": "td{}",
        "params": ["Distance"],
        "description": "If current target is within distance",
        "example": "td100"
    },
    "Target Entity": {
        "format": "te{}{}",
        "params": ["*", "Entity ID"],
        "description": "Targets the entity by ID. Use '*' to also rotate camera toward the entity",
        "example": "te*12345"
    },
    "Target Closest Mob": {
        "format": "tcm{}{},{}",
        "params": ["*", "Max Distance", "Max Height"],
        "description": "Targets closest mob. Use '*' to rotate camera",
        "example": "tcm*100,50"
    },
    "Target Closest Player": {
        "format": "tcp{}{},{}",
        "params": ["*", "Max Distance", "Max Height", "Type"],
        "description": "Targets closest player. Type: 0 any, 1 enemy, 2 friendly",
        "example": "tcp*100,50,1"
    },
    "Target Mob with Lowest HP": {
        "format": "tmhp{}{},{}",
        "params": ["*", "Distance", "Max Height"],
        "description": "Targets mob with lowest HP. Use '*' to rotate camera",
        "example": "tmhp*100,50"
    },
    "Target Player with Lowest HP": {
        "format": "tphp{}{},{}",
        "params": ["*", "Distance", "Max Height"],
        "description": "Targets player with lowest HP. Use '*' to rotate camera",
        "example": "tphp*100,50"
    },
    "Target Player with Weapon": {
        "format": "tcpw{}{},{}",
        "params": ["*", "Distance", "Weapon ID"],
        "description": "Targets player with specified weapon. Use '*' to rotate camera",
        "example": "tcpw*100,40438765"
    },
    "Target Entity by Name": {
        "format": "tce % {},{},{}",
        "params": ["*", "Entity Name", "Distance", "Max Height"],
        "description": "Targets entity by name. Use '*' to rotate camera",
        "example": "tce % *Enemy Name,100,50"
    },
    "Lock Target": {
        "format": "lt",
        "params": [],
        "description": "Locks camera to current target",
        "example": "lt"
    },
    "Unlock Target": {
        "format": "lt-",
        "params": [],
        "description": "Unlocks camera",
        "example": "lt-"
    },
    "Ignore Players": {
        "format": "ign{}{}",
        "params": ["-", "Distance"],
        "description": "Sets nearby players as allies or resets the list. Use '-' to reset",
        "example": "ign100"
    },
    "Rotate Camera to Target": {
        "format": "tct",
        "params": [],
        "description": "Rotates camera toward current target",
        "example": "tct"
    },
    "Target Previous Target": {
        "format": "tpt{}",
        "params": ["*"],
        "description": "Targets previous target if none selected. Use '*' to rotate camera",
        "example": "tpt*"
    },
    "Health Percentage": {
        "format": "hp{}",
        "params": ["Percent"],
        "description": "If HP ≤ percent (0 to 1",
        "example": "hp0.5"
    },
    "Mana Percentage": {
        "format": "mp{}",
        "params": ["Percent"],
        "description": "If MP ≤ percent (0 to 1",
        "example": "mp0.3"
    },
    "Stamina Percentage": {
        "format": "sta{}",
        "params": ["Percent"],
        "description": "If stamina ≤ percent (0 to 1",
        "example": "sta0.8"
    },
    "Player Status Effect": {
        "format": "pse{},{}",
        "params": ["Status Effect ID", "Stacks"],
        "description": "If status effect is active",
        "example": "pse123,1"
    },
    "Is Attacking": {
        "format": "ia",
        "params": [],
        "description": "If currently attacking",
        "example": "ia"
    },
    "Current Attack": {
        "format": "att{}",
        "params": ["Attack ID"],
        "description": "If current attack matches attack ID",
        "example": "att456"
    },
    "Check Hotbar Slot": {
        "format": "ch{},{}",
        "params": ["Hotbar Slot", "Timer"],
        "description": "If ability is ready or near ready",
        "example": "ch1,500"
    },
    "Wait for Hotbar Slot": {
        "format": "ch*{},{}",
        "params": ["Hotbar Slot", "Timeout"],
        "description": "Waits until ability is on cooldown or times out",
        "example": "ch*1,5000"
    },
    "Check Hotbar ID": {
        "format": "chid{},{}",
        "params": ["Hotbar Slot", "Ability ID"],
        "description": "Checks if ability ID matches",
        "example": "chid1,789"
    },
    "Weapon Number": {
        "format": "wpn{}",
        "params": ["Weapon Number"],
        "description": "If active weapon is 1 or 2",
        "example": "wpn1"
    },
    "Weapon ID": {
        "format": "wpn*{}",
        "params": ["Weapon ID"],
        "description": "If equipped weapon matches ID",
        "example": "wpn*40438765"
    },
    "Move To Coordinates": {
        "format": "mt{},{},{}",
        "params": ["X", "Y", "Z"],
        "description": "Moves character to coordinates",
        "example": "mt1000,2000,300"
    },
    "Move Toward Mob": {
        "format": "mtm % {},{},{}",
        "params": ["Name", "Distance", "Angle", "How Far"],
        "description": "Moves toward mob",
        "example": "mtm % Goblin,100,90,50"
    },
    "Movement Speed": {
        "format": "ms{}",
        "params": ["Movement Speed"],
        "description": "Sets movement speed increase",
        "example": "ms1.5"
    },
    "Load Waymark File": {
        "format": "lwf % {}",
        "params": ["Filename.ini"],
        "description": "Loads waymark file",
        "example": "lwf % waymarks.ini"
    },
    "Check Nearby Mobs": {
        "format": "cnm{},{}{},{}",
        "params": ["Number", "Distance", "Max Height", "(X,(Y,(Z"],
        "description": "Checks for nearby mobs",
        "example": "cnm5,100,50"
    },
    "Check Mobs Around Target": {
        "format": "ctnm{},{}",
        "params": ["Number", "Distance"],
        "description": "Checks mobs around the target",
        "example": "ctnm5,100"
    },
    "Check Mobs with HP": {
        "format": "cmhp{},{}",
        "params": ["Percent", "Distance"],
        "description": "Checks mobs with HP ≤ percent",
        "example": "cmhp0.5,100"
    },
    "Check Players with HP": {
        "format": "cphp{},{}",
        "params": ["Percent", "Distance"],
        "description": "Checks players with HP ≤ percent",
        "example": "cphp0.5,100"
    },
    "Check Target HP": {
        "format": "cthp{}",
        "params": ["Percent"],
        "description": "Checks if target's HP ≤ percent",
        "example": "cthp0.5"
    },
    "Check Players with Weapon": {
        "format": "cnpw{},{}",
        "params": ["Number", "Distance", "Weapon ID"],
        "description": "Checks for players with weapon ID",
        "example": "cnpw5,100,40438765"
    },
    "Check Target's Status Effects": {
        "format": "cts{},{}{},{}",
        "params": ["Status Effect ID", "Stacks", "Remaining Duration"],
        "description": "Checks target's status effects",
        "example": "cts123,1,5000"
    },
    "Check Target's Weapon": {
        "format": "ctw{}{}",
        "params": ["*", "Weapon ID"],
        "description": "Checks target's weapon. Use '*' to rotate camera",
        "example": "ctw*40438765"
    },
    "Check Entity by Name": {
        "format": "cne % {},{},{}",
        "params": ["Entity Name", "Distance", "Max Height"],
        "description": "Checks for entity by name",
        "example": "cne % Goblin,100,50"
    },
    "Call Function": {
        "format": "call % {}",
        "params": ["Function Name"],
        "description": "Calls a defined function",
        "example": "call % myFunction"
    },
    "Go To Line": {
        "format": "gt{}",
        "params": ["Line Number"],
        "description": "Jumps to waymark index or macro keys section",
        "example": "gt16"
    },
    "Toggle Macro Key": {
        "format": "to{}",
        "params": ["Macro Key"],
        "description": "Toggles a macro",
        "example": "toF3"
    },
    "Random Number": {
        "format": "rand{},{}",
        "params": ["Min", "Max"],
        "description": "Generates a random number into RAND",
        "example": "rand1,100"
    },
    "Compare Less Than": {
        "format": "cmp{},{}",
        "params": ["Value1", "Value2"],
        "description": "If Value1 < Value2",
        "example": "cmp playerHP,0.5"
    },
    "Store Variable": {
        "format": "store % {},{}",
        "params": ["Variable", "Value"],
        "description": "Stores value in a variable",
        "example": "store % queueDelay,500"
    },
    "Retrieve Variable": {
        "format": " {}",
        "params": ["Variable"],
        "description": "Retrieves variable's value",
        "example": " queueDelay"
    },
    "Equal To": {
        "format": "eq % {},{}",
        "params": ["Variable", "Value"],
        "description": "If variable equals value",
        "example": "eq %  mobCount,5"
    },
    "Logical OR": {
        "format": "or % ({}({}...",
        "params": ["Command1", "Command2"],
        "description": "Logical OR between commands",
        "example": "or % (eq %  mobCount,5(eq %  mobCount,10"
    },
    "Add": {
        "format": "add % {},{}",
        "params": ["Variable", "Value"],
        "description": "Adds value to variable",
        "example": "add % mobCount,1"
    },
    "Subtract": {
        "format": "sub % {},{}",
        "params": ["Variable", "Value"],
        "description": "Subtracts value from variable",
        "example": "sub % mobCount,1"
    },
    "Multiply": {
        "format": "mul % {},{}",
        "params": ["Variable", "Value"],
        "description": "Multiplies variable by value",
        "example": "mul % RAND,0.001"
    },
    "Divide": {
        "format": "div % {},{}",
        "params": ["Variable", "Value"],
        "description": "Divides variable by value",
        "example": "div % totalDamage,2"
    },
    "Debug Message": {
        "format": "dbg % {}",
        "params": ["Text"],
        "description": "Outputs text to console",
        "example": "dbg % 'Debug message here'"
    },
    "Console Command": {
        "format": "cc % {}",
        "params": ["Console Command"],
        "description": "Executes a console command",
        "example": "cc % -cl"
    },
    "Get Pixel Color": {
        "format": "gp{},{}{},{}",
        "params": ["X", "Y", "Color", "Precision"],
        "description": "Checks pixel color at coordinates",
        "example": "gp100,200,16777215,0"
    },
    "No Operation": {
        "format": "nop",
        "params": [],
        "description": "No operation (placeholder",
        "example": "nop"
    },
    "Config Line": {
        "format": "conf % {},{}",
        "params": ["Line", "Text"],
        "description": "Writes text to a line in config.txt",
        "example": "conf % 1,113"
    }
}
