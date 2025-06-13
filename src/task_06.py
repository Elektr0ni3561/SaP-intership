# Разработать методы для программы Камень-Ножницы-Бумага. При реализации
# обработки исключений важно не использовать встроенные классы ошибок с
# передачей им сообщения, а разработать классы с представленными ниже
# названиями.
#
# Метод rps_game_winner должен принимать на вход массив следующей структуры
# [ ["player1", "P"], ["player2", "S"] ], где P — бумага, S — ножницы, R — камень,
# и функционировать следующим образом:
#
#     • если количество игроков больше 2 необходимо вызывать исключение
#     WrongNumberOfPlayersError
#     • если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
#     исключение NoSuchStrategyError
#     • в иных случаях необходимо вернуть имя и ход победителя, если оба
#     игрока походили одинаково - выигрывает первый игрок.

class WrongNumberOfPlayersError(Exception):
    def __init__(self, *args, **kwargs):
        pass

class NoSuchStrategyError(Exception):
    def __init__(self, *args, **kwargs):
        pass

def rps_game_winner(psr: list):
    # В задании указано, вызывать исключение только, когда больше 2 игроков, но очевидно нельзя играть одному или вообще без игроков.
    if len(psr) != 2:
        raise WrongNumberOfPlayersError("There must be 2 players in the game.")
    player_turn_1 = psr[0]
    player_turn_2 = psr[1]
    if player_turn_1[1] not in "PSR" or player_turn_2[1] not in "PSR":
        raise NoSuchStrategyError("No such strategy. Expected P, S or R.")
    if player_turn_1[1] + player_turn_2[1] == "PS" or "RP" or "SR":
        return player_turn_2
    return player_turn_1

if __name__ == "__main__":
    try:
        print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))  # => WrongNumberOfPlayersError
    except Exception as e:
        print(e)
    try:
        print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))                    # => NoSuchStrategyError
    except Exception as e:
        print(e)
    print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))                        # => 'player2 S'
    print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))                        # => 'player1 P'