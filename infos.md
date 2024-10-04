List of All Possible Commands and Their Options in Speeder

1. Configuration Settings (config.txt Lines 1-33)
You can adjust these settings in the config.txt file. Each line corresponds to a specific setting:

Line 1: Disable/Enable Hacks Key

Option: Virtual key code to disable or re-enable all hacks.
Example: 113 (F2 key).
Line 2: Movement Speed Increase

Option: Decimal value representing the multiplier.
1.5 for a 50% increase.
2.0 for a 100% increase.
Note: Due to server checks, actual increase is less.
Line 3: Driver Name

Option: String with your driver's name.
Note: Leave blank to enter it manually each time.
Line 4: Zoom Distance

Option: Number representing zoom distance.
Default: 1800.
Disable: Set to 0.
Line 5: Macro File Name

Option: File name of your macro file (including extension).
Example: macros.ini.
Line 6: Movement Keys

Option: Virtual key codes for movement keys.
Format: [forward key][left key]|[backward key]|[right key].
Example: 87|65|83|68 (WASD keys).
Line 7: Record Current Location Key

Option: Virtual key code to activate the -cl command.
Example: 113 (F2 key).
Line 8: Teleport Hop Distance

Option: Number representing distance per teleport hop.
Default: 100.
Line 9: Teleport Hop Delay

Option: Milliseconds to wait between teleport hops.
Default: 30.
Line 10: Arrival Threshold

Option: Distance before Speeder assumes arrival at destination.
Default: 100.
Line 11: Waymark Sleep Randomization

Option: Decimal between 0 and 1 for sleep time variation.
Example: 0.05 for ±5% variation.
Line 12: Pause/Resume Waymarks Key

Option: Virtual key code to pause/resume waymarks.
Also Terminates: mt (move to) command.
Line 13: Allow Injected Keys

Option: 1 to enable, 0 to disable.
Note: For controller inputs mapped to keyboard keys.
Line 14: Random Keys During Macros/Waymarks

Option: [chance]|[max duration]|[key1]|[key2]|...
Example: 50|1000|97|98|99 (50% chance, max 1000ms, keys 97, 98, 99).
Line 15: Auto-Load Macros

Option: Virtual key codes of macros to auto-load, separated by |.
Example: 100|101.
Line 16: Re-enable Hacks Delay

Option: Milliseconds to wait after an address problem.
Default: As per your preference.
Line 17: Keys Before Waymarks

Option: Virtual key codes pressed before moving to next waymark, separated by |.
Example: 160|87 (Shift + W for sprint).
Line 18: Keys After Waymarks

Option: Virtual key codes pressed or released after reaching a waymark, separated by |.
Line 19: Entities to Ignore

Option: Entity names separated by |.
Example: Resistance Soldier|Practice Dummy.
Line 20: Entities to Consider as Mobs

Option: Entity names separated by |.
Line 21: Use Device Input

Option:
1 or 2: Enable device input.
0: Disable.
Advanced: 1|keyboard_device_number|mouse_device_number.
Line 22: Exclusive Mobs List

Option: Entity names separated by |.
Note: Only these entities are considered mobs.
Line 23: Targetable Mobs Only

Option: 1 to enable, 0 to disable.
Line 24: Allied Players

Option: Player names considered allies, separated by |.
Line 25: Ignore Players

Option: Player names to ignore, separated by |.
Line 26: Targeting Method

Option:
0: Use TAB key for targeting.
1: Write directly to game's memory.
Advanced: 0|[key code]|[delay]|[timeout].
Line 27: Key Press Speed Threshold

Option: Milliseconds to warn for pressing keys too quickly.
Default: 100.
Line 28: Radar Settings

Option: Values separated by | in order:
X position|Y position|Width|Height|ID|Total entities|Font size|Background color|Mob color|Player color|Ally player color|Object color|Center indicator|Show mobs|Show players|Show objects|Transparent|Always on top|Distance multiplier|Refresh rate
Example: 0|0|960|540|1|100|35|3618615|255|16711680|65280|16777215|*|1|1|1|0|0|0.05|200.
Line 29: Custom Radar/ESP Colors

Option: [Entity Name],[Color]|...
Example: Violent Harvester,65280|Beehive,65535.
Line 30: ESP Settings

Option: Values separated by | in order:
Total entities|Font size|Mob color|Player color|Object color|Show mobs|Show players|Show objects|Field of view|Refresh rate
Example: 100|35|255|60000|16777215|1|1|1|50|50.
Line 31: Weapon ESP Settings

Option: [Active weapon],[Inactive weapon],[Color]|...
Example: 40463328,40438765,120000|40438765,40463328,120000.
Line 32: ESP/Radar Text Erase Expansion

Option: Number of pixels to expand the text rectangle for erasure.
Default: 1.
Line 33: Fishing Bot Settings

Option: [key]|[max keypress duration]|[resting time]
Example: 96|1500|1000 (NUMPAD0 key).
2. Speeder Console Commands
These commands can be typed into the Speeder console or used within macros/waymarks using cc % [command]:

-d: Disables all hacks.
-e: Enables all hacks (use only after -d).
-cf [configfilename.txt]: Changes the active config file.
-t x, y, z: Gradually teleport to coordinates (x, y, z).
Options: Coordinates as numbers.
-t* x, y, z: Instantly teleport to coordinates (x, y, z).
-twrepeat* [filename.ini][|index]: Repeats waymarks in a loop from the specified file.
Options:
[filename.ini]: Waymark file name.
[|index] (optional): Start at specific index or |? for the closest waymark.
-tw* [filename.ini][|index]: Runs waymarks once from the specified file.
-tw** and -twrepeat**: Adjust waymarks based on current position.
-wmark reset: Resets offsets from -tw** or -twrepeat**.
-twresume: Resumes -twrepeat from the next waymark.
-record [distance],[wait time],[initial camera sleep]: Starts/stops recording waymarks.
Options:
[distance]: Distance to create waymarks.
[wait time]: Time to wait at each waymark.
[initial camera sleep] (optional): Time before adjusting the camera.
-cl: Displays current location and camera position.
-displayaid [p]: Outputs attack IDs.
Option: p to show only attacks involving you.
-allentities: Displays data for all entities.
-allmobs: Displays data for all mobs.
-allplayers: Displays data for all players.
-target: Displays data for your current target.
-hotbar: Displays ability IDs on your hotbar.
-status: Displays your status effects.
-mp: Displays mouse position.
-gpc: Displays pixel color at cursor position.
-gpc [x] [y]: Displays pixel color at specified screen coordinates.
-dump [entity] [data type] [filename]: Dumps entity data to a file.
Options:
[entity]: t for current target.
[data type]: 4 (4 bytes) or 1 (1 byte).
[filename]: Output file name.
-settings: Opens config.txt.
-macro: Opens your macro file.
-esp: Toggles the ESP display.
-cmd [commands]: Executes macro/waymark commands directly.
-scan: Scans game's memory for addresses.
-output: Toggles console output except for dbg % messages.
3. Waymark & Macro Commands
These commands are used within the keys= sections of macros and waymarks. Separate commands with the | character.

Keyboard & Mouse Commands

[key code]: Presses the key once.
Example: 49 to press the 1 key.
[key code]d: Holds down the key.
Example: 87d to hold down the W key.
[key code]u: Releases the key.
Example: 87u to release the W key.
m[x],[y]: Moves mouse cursor to (x, y).
rm[x1],[y1];[x2],[y2];...: Randomly moves mouse to one of the specified positions.
rkd[key1],[key2],...: Holds down a random key from the list.
rku: Releases the key held by the last rkd command.
kd[key]: If the key is pressed, processes the rest of the line.
kd*[key]: Checks if the physical key is pressed.
Timers & Delays

s[milliseconds]: Waits for specified milliseconds.
rs[min],[max]: Waits for a random time between min and max milliseconds.
st % [timername],[delay]: Sets a timer.
ct % [timername]: Checks if the timer has expired.
Targeting Commands

c[angle]: Adjusts camera horizontal angle (-180 to 180 degrees).
cy[angle]: Adjusts camera vertical angle.
it: If targeting a mob, processes the rest of the line.
ibt[type],[distance]: If being targeted by an entity of type within distance.
type: 1 for mobs, 2 for players.
tar: Populates TN (target name) and TID (target ID).
td[distance]: If current target is within distance.
te[*][entity ID]: Targets the entity by ID.
*: Also rotates camera toward the entity.
tcm[*][max distance],[max height][,(x),(y),(z)]: Targets closest mob.
*: Rotates camera.
(x),(y),(z): Origin coordinates (optional).
tcp[*][max distance],[max height],[type]: Targets closest player.
type: 0 any, 1 enemy, 2 friendly.
tmhp[*][distance],[max height]: Targets mob with lowest HP.
tphp[*][distance],[max height]: Targets player with lowest HP.
tcpw[*][distance],[weapon ID]: Targets player with specified weapon.
tce % [entity name],[distance],[max height]: Targets entity by name.
lt: Locks camera to current target.
lt-: Unlocks camera.
ign[-][distance]: Sets nearby players as allies or resets the list.
tct: Rotates camera toward current target.
tpt[*]: Targets previous target if none selected.
Auto-Block Commands

tatt[attack ID],[is fury],[time],[direction],[check target]: Triggers action on attack detection.
matt[attack ID],[is fury],[time],[distance],[direction],[check target]: For any mob.
patt[attack ID],[is fury],[time],[distance],[direction],[is enemy]: For any player.
eatt[attack ID],[is fury],[time],[distance],[direction],[check target]: For any entity.
Player Status & Hotbar Commands

hp[percent]: If HP ≤ percent (0 to 1).
mp[percent]: If MP ≤ percent.
sta[percent]: If stamina ≤ percent.
pse[status effect ID],[stacks]: If status effect is active.
ia: If currently attacking.
att[attack ID]: If current attack matches attack ID.
ch[hotbar slot],[timer]: If ability is ready or near ready.
ch*[hotbar slot],[timeout]: Waits until ability is on cooldown or times out.
chid[hotbar slot],[ability id]: Checks if ability ID matches.
wpn[weapon number]: If active weapon is 1 or 2.
wpn*[weapon ID]: If equipped weapon matches ID.
Movement & Waymark Commands

mt[x],[y],[z]: Moves character to coordinates.
mtm % [name],[distance],[angle],[how far]: Moves toward mob.
ms[movement speed]: Sets movement speed increase.
lwf % [filename.ini]: Loads waymark file.
Entity Commands

cnm[number],[distance],[max height][,(x),(y),(z)]: Checks for nearby mobs.
ctnm[number],[distance]: Checks mobs around the target.
cmhp[percent],[distance]: Checks mobs with HP ≤ percent.
cphp[percent],[distance]: Checks players with HP ≤ percent.
cthp[percent]: Checks if target's HP ≤ percent.
cnpw[number],[distance],[weapon ID]: Checks for players with weapon ID.
cts[status effect ID],[stacks],[remaining duration]: Checks target's status effects.
ctw[*][weapon ID]: Checks target's weapon.
cne % [entity name],[distance],[max height]: Checks for entity by name.
General Scripting & Variable Commands

call % [function name]: Calls a defined function.
gt[#]: Jumps to waymark index or macro keys section.
to[macro key]: Toggles a macro.
rand[min],[max]: Generates a random number into RAND.
cmp[value1],[value2]: If value1 < value2.
store % [variable],[value]: Stores value in a variable.
(VAR % [variable]): Retrieves variable's value.
eq % [variable],[value]: If variable equals value.
or % ([cmd1])([cmd2])...: Logical OR between commands.
add % [variable],[value]: Adds value to variable.
sub % [variable],[value]: Subtracts value from variable.
mul % [variable],[value]: Multiplies variable by value.
div % [variable],[value]: Divides variable by value.
dbg % [text]: Outputs text to console.
Miscellaneous Commands

cc % [console command]: Executes a console command.
gp[x],[y],[color],[precision]: Checks pixel color at coordinates.
nop: No operation (placeholder).
conf % [line],[text]: Writes text to a line in config.txt.
Reserved Global Variables

ADDRESS: 0 if addresses cannot be read, 1 if they can.
PX, PY, PZ: Player coordinates after -cl command.
WX, WY, WZ: Coordinates of last waymark.
TN: Name of current target (after tar command).
TID: ID of current target (after tar command).
RAND: Random number from rand command.
IBT: ID of entity targeting you (after ibt command).
Note: All virtual key codes can be found here: Virtual-Key Codes