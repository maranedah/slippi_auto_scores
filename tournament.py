import json, glob, os, math, time
from auto_score import updateScore, resetScore, updateChars
from auto_stats import getStatsUrl
from obs_script import changeStats, changeToScoreBoard, startRecording, stopRecording, changeToVenueCam
import vlc
import os

scoreinfo_path = "C:\\Users\\melee\\Desktop\\Mauro\\Stream\\Melee Stream Tool v1.1\\Stream Tool\\Resources\\Texts\\ScoreboardInfo.json"
spectate_path = "C:\\Users\\melee\\Documents\\Slippi\\Training Arc\\test"
player = vlc.MediaPlayer("melee_menu.flac")
            
def tourney_match():

    f = open(scoreinfo_path)
    scoreinfo = json.load(f)
    f.close()

    bestOf = scoreinfo["bestOf"][-1] # "Bo3", "Bo5"
    max_score = math.ceil(int(bestOf)/2)
    print("max_score", max_score)
    p1_score = 0
    p2_score = 0

    n_files = len(os.listdir(spectate_path))

    set_files = []

    while p1_score < max_score and p2_score < max_score:
        
        new_n_files = len(os.listdir(spectate_path))
        print(new_n_files)

        # Revisar carpeta si hay archivos nuevos *y no esta cambiando el tamaño del archivo*
        # Si hay, hacer cosas
        if new_n_files > n_files:
            print("Found new file")
            player.stop()
            changeToScoreBoard()
            #startRecording()

            # Change Characters in ScoreBoard
            
            updateChars("game.json")
            
            # GetLatestFile
            list_of_files = glob.glob(f'{spectate_path}\\*.slp') 
            latest_file = max(list_of_files, key=os.path.getctime)


            # Wait while latest file still changing size
            curr_size = os.path.getsize(latest_file)
            time.sleep(2)
            while curr_size != os.path.getsize(latest_file):
                curr_size = os.path.getsize(latest_file)
                time.sleep(2)   

            # Añadir a lista de juegos del set
            set_files.append(latest_file)

            # Auto-Score
            updateScore(latest_file)
            player.play()
            changeToVenueCam()
            
            
        # Updatear puntaje de los jugadores
        f = open(scoreinfo_path)
        scoreinfo = json.load(f)
        p1_score = scoreinfo["p1Score"]
        p2_score = scoreinfo["p2Score"] 
        print("puntajes:", p1_score, p2_score)
        f.close()
        time.sleep(0.5)

        # Updatear numero de archivos en carpeta
        n_files = new_n_files

    # Calcular Estadisticas del Set
    url = getStatsUrl(set_files)
    print(url)
    # Cambiar estadisticas en el obs
    changeStats(url)
    resetScore()
    #stopRecording()
    changeToVenueCam()


if __name__ == "__main__":
    while True:
        try:
            tourney_match() 
        except KeyboardInterrupt:
            break