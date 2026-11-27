from database.database_connection import database_connect as connection
from main.player import Player
from functions.gameLoop import game_loop
from flask import Flask, request
app = Flask(__name__)

@app.route('/new_game', methods=['POST'])
def new_game():
    connect = connection()
    cursor = connect.cursor()

    screen_name = request.form["screen_name"]
    # screen_name = input("Anna pelaajanimesi: ")

    if not screen_name:
        return "Virhe: pelaajanimi ei voi olla tyhjä."

    check_sql = "SELECT screen_name FROM game WHERE screen_name = %s"
    cursor.execute(check_sql, (screen_name,))
    result = cursor.fetchone()

    if result:
        return "Käyttäjänimi on jo varattu"

    insert_sql = "INSERT INTO game (screen_name) VALUES (%s)"
    cursor.execute(insert_sql, (screen_name,))
    connect.commit()

    player_id = cursor.lastrowid

    cursor.close()
    connect.close()

    Player.current_player = Player(screen_name, player_id)

    # print("Kuulet kuulutuksen: lentosi lähtee pian. Valitse oikea lento lentotaulusta. Kello on 7.32, ja kone nousee ilmaan jo 13 minuutin kuluttua!")

    game_loop()