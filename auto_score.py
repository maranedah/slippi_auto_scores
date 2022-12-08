from slippi import Game
import json, os, time

color_port = {
	"Red": 1,
	"Blue": 2,
	"Yellow": 3,
	"Green": 4
}
port_color = {
	1: "Red",
	2: "Blue",
	3: "Yellow",
	4: "Green"
}

scoreinfo_path = "C:\\Users\\melee\\Desktop\\Mauro\\Stream\\Melee Stream Tool v1.1\\Stream Tool\\Resources\\Texts\\ScoreboardInfo.json"
charinfo_path ="C:\\Users\\melee\\Desktop\\Mauro\\Stream\\Melee Stream Tool v1.1\\Stream Tool\\Resources\\Texts\\Character Info\\"


def get_winner(g):
	last_frame = g.frames[-1]

	f = open(scoreinfo_path)
	scoreinfo = json.load(f)
	f.close()

	port1 = color_port[scoreinfo["p1Color"]]
	port2 = color_port[scoreinfo["p2Color"]]
	p1, p2 = last_frame.ports[port1 - 1], last_frame.ports[port2 - 1]
	player1, player2 = g.metadata.players[port1 - 1], g.metadata.players[port2 - 1]
	css1, css2 = g.start.players[port1 - 1], g.start.players[port2 - 1]

	stocks_winner = port1 if p1.leader.post.stocks > p2.leader.post.stocks else port2 if p1.leader.post.stocks < p2.leader.post.stocks else None
	percent_winner = port1 if p1.leader.post.damage < p2.leader.post.damage else port2 if p1.leader.post.damage > p2.leader.post.damage else None
	winner = stocks_winner if stocks_winner != None else percent_winner


	return winner


def get_skin(char, skin_id):
	path = os.path.join(charinfo_path, char + ".json")
	f = open(path)
	skin = json.load(f)["skinList"][skin_id]
	return skin
	

def updateScore(slp_path):
	g = Game(slp_path)

	winner = get_winner(g)
	winner_color = port_color[winner]
	
	f = open(scoreinfo_path)
	scoreinfo = json.load(f)
	f.close()
	
	if scoreinfo["p1Color"] == winner_color:
		scoreinfo["p1Score"] += 1
	elif scoreinfo["p2Color"] == winner_color:
		scoreinfo["p2Score"] += 1

	f = open(scoreinfo_path, 'w')
	json.dump(scoreinfo, f)
	f.close()

def updateChars(json_path):
	time.sleep(2)
	f = open(json_path)
	gameinfo = json.load(f)
	f.close()

	f = open("characters.json")
	characters = json.load(f)
	f.close()


	p1 = gameinfo["players"][0]
	p2 = gameinfo["players"][1]

	f = open(scoreinfo_path)
	scoreinfo = json.load(f)
	f.close()

	p1_char = characters[str(p1["characterId"])]["name"]
	p1_skin = characters[str(p1["characterId"])]["colors"][p1["characterColor"]]
	p2_char = characters[str(p2["characterId"])]["name"]
	p2_skin = characters[str(p2["characterId"])]["colors"][p2["characterColor"]]

	

	

	if scoreinfo["p1Color"] == port_color[p1["port"]]:
		if p1_char == "Zelda":
			p1_skin = "Sheik " + p1_skin
		scoreinfo["p1Character"] = p1_char
		scoreinfo["p1Skin"] = p1_skin
	else:
		if p2_char == "Zelda":
			p2_skin = "Sheik " + p2_skin
		scoreinfo["p2Character"] = p2_char
		scoreinfo["p2Skin"] = p2_skin
	
	if scoreinfo["p2Color"] == port_color[p2["port"]]:
		if p2_char == "Zelda":
			p2_skin = "Sheik " + p2_skin
		scoreinfo["p2Character"] = p2_char
		scoreinfo["p2Skin"] = p2_skin
	else:
		if p1_char == "Zelda":
			p1_skin = "Sheik " + p1_skin
		scoreinfo["p1Character"] = p1_char
		scoreinfo["p1Skin"] = p1_skin

	f = open(scoreinfo_path, 'w')
	json.dump(scoreinfo, f)
	f.close()

def resetScore():
	f = open(scoreinfo_path)
	scoreinfo = json.load(f)
	f.close()

	scoreinfo["p1Score"] = 0
	scoreinfo["p2Score"] = 0

	f = open(scoreinfo_path, 'w')
	json.dump(scoreinfo, f)
	f.close()
