from database.database_connection import database_connect as connection
from main.player import Player
from functions.gameLoop import game_loop
from flask import request

def new_game():

    if request.method == 'POST':

        screen_name = request.form["screen_name"]
        # screen_name = input("Anna pelaajanimesi: ")

        if not screen_name:
            return "Virhe: pelaajanimi ei voi olla tyhjä."

        connect = connection()
        cursor = connect.cursor()

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

    return "Pelaaja tallennettu!"