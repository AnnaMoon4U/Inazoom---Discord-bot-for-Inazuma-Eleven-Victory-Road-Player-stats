# Inazoom
Discord bot for Inazuma Eleven Victory Road Player stats and more!

Credit to User Xion (Xion14blade)'s dataset that can be found here: https://docs.google.com/spreadsheets/d/1N4h7z27Rxq3bvYuR9VyeQv3Ze-zwo-1XZQTd9rZa-Zs/edit?usp=sharing

# Public Release (Add to discord server):

Coming soon

# Current Features:

**All 5000+ (Current) Players searchable/filterable** via command with Kanji Name, Hiragana Name, Nickname, Position, Element, Playstyle, Stats and BST Values, including images, up to the Galaxy update.

## All commands support autofill input!

 ### **/player search**

Smart search feature - Searches with Kanji, Hiragana, Nickname, First name and even Last name! The search will also list players with a similar name to your (manual) input. Pages can be navigated by clicking on the arrow keys underneath the output image 

<img width="483" height="913" alt="image" src="https://github.com/user-attachments/assets/080e084a-2b2f-44ac-b900-666730352c66" />

### **/player translate**

Simple Translate Feature - Translates a player from any language to.. any language! (Supports Kanji/Hiragana as well)

<img width="547" height="242" alt="image" src="https://github.com/user-attachments/assets/b7017869-43f9-4134-acc2-26672505e6bc" />

 ### **/player filter**

Filter command - Filters players by position, role, element, playstyle, gender, stat in either ascending or a descending format!

Example input and result: 
/player filter gender: 女 (Female) sort_by_stat: physical

<img width="629" height="927" alt="image" src="https://github.com/user-attachments/assets/5dd9dc58-7891-4e1b-86cf-e0e708907825" />

 #### Also supports Coordinator/manager passives:

<img width="524" height="887" alt="image" src="https://github.com/user-attachments/assets/6d6cc3e5-b2a6-40b1-a978-a656991dc704" />

 ### **/player compare**

Example input and result:
/player compare player1:Tim Saunders (Ayumu Shorinji) player2:Jim Wraith (Jin Kageno)

<img width="437" height="876" alt="image" src="https://github.com/user-attachments/assets/7d0a225a-0faa-49f1-be06-faddb9105d98" />

### **/hissatsu search**

Searches Hissatsus and provides all values extracted from Xion's dataset (Including subtype: longshot/countershot), which shop, animation duration etc...

Example input and result:
/hissatsu search name: Disaster Strike

<img width="559" height="302" alt="image" src="https://github.com/user-attachments/assets/7405c674-2378-489a-a89a-0fcf1e89cd50" />

 ### **/hissatsu filter**

Searches hissatsus based on filters (all optional):  (type, subtype, min_power, max_cost)

Example command:

/hissatsu filter element: 山 (Mountain) type: Shot subtype: Long Shot

<img width="462" height="353" alt="image" src="https://github.com/user-attachments/assets/57650ada-409d-467a-8887-41e9c289ddb6" />

 ### **/item search**

Searches items based on filters (all optional) : (category kick control technique pressure physical intelligence agility shop), Sorts by descending (Highest value first sorted by tuple logic)

For stats such as kick, control etc... you need to input a number (int) to set as a minimum stat 

Can also search purely by name with autofill features

Example input and result:
/item search category: boots kick: 20 control: 20

<img width="309" height="483" alt="image" src="https://github.com/user-attachments/assets/5c80bd8f-c109-449b-aaef-0fbdacb56312" />

### **/player hero**

Searches hero players based on filters (all optional): (gender, position, element, moves)

Pagination support for multiple Playstyles

Can also search purely by name with autofill features

Example input 1 (Image 1):
/player hero gender:Female moves:Omega Assault position:FW element:風 (Wind)

Example input 2 (Image 2):
/player hero name: Alpha

<img width="465" height="905" alt="image" src="https://github.com/user-attachments/assets/5515c218-faca-4d02-a3bb-d57a2351cade" />
<img width="446" height="911" alt="image" src="https://github.com/user-attachments/assets/62168da0-0a21-4e2d-8317-64c4f5e114fe" />

### **/player basara**

Searches basara players based on filters (all optional): (gender, position, altpostion, element, moves)

Has pagination support for futureproofing's sake and for filter search

Lists first 3 passives based on sheet in output (Probably very useful)

Can also search purely by name with autofill features similar to the hero command

Example input 1 (Image 1):
/player basara gender: Female position: FW element: 風 (Wind)

Example input 2 (Image 2):
/player basara name: Alpha

<img width="436" height="936" alt="image" src="https://github.com/user-attachments/assets/912b9bd4-c97a-46ef-8a19-8103487e9660" />
<img width="437" height="919" alt="image" src="https://github.com/user-attachments/assets/1183dc1f-5f15-4495-8a36-0bb5060ee93a" />


