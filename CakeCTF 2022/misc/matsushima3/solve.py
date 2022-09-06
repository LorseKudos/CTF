import enum
import json
import os
import random
import requests
import time

HOST = os.getenv("HOST", "misc.2022.cakectf.com")
PORT = os.getenv("PORT", 10011)


class GameState(enum.Enum):
    NONE = enum.auto()
    INIT = enum.auto()
    GAME = enum.auto()
    WIN = enum.auto()
    LOSE = enum.auto()
    DRAW = enum.auto()
    FLAG = enum.auto()


class GameAction(enum.Enum):
    HIT = enum.auto()
    STAND = enum.auto()
    SKIP = enum.auto()


class ServerConnection(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.session = None

    def request(self, endpoint, data=None):
        try:
            r = requests.get(f"http://{self.host}:{self.port}/{endpoint}",
                             params=data,
                             cookies=self.session)
        except requests.exceptions.RequestException as e:
            print("[ERROR]", e)
            print(f"Server '{self.host}:{self.port}' is down...?")
            exit(1)

        if self.session is None:
            self.session = r.cookies
        return json.loads(r.text)


class Game(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = GameState.INIT
        self.frame = 0
        self.player_score = 0
        self.dealer_score = 0
        self.player_hand = []
        self.dealer_hand = []
        self.num_dealer_cards = 0
        self.connection = ServerConnection(HOST, PORT)
        _response = self.connection.request('user/new')
        self.money = _response['money']
        self.user_id = _response['user_id']
        self.title_cards = random.sample(
            [(i // 13, i % 13) for i in range(4*13)], 5
        )

    def notify_action(self, act):
        """Player chose hit or stand"""
        if act == GameAction.HIT:
            # Hit
            response = self.connection.request('game/act', {'action': 'hit'})
            self.deck = self.deck[:-1]
            if self.num_dealer_cards < response['num_dealer_cards']:
                self.deck = self.deck[:-(response['num_dealer_cards'] -
                                         self.num_dealer_cards)]

        elif act == GameAction.STAND:
            # Stand
            response = self.connection.request('game/act', {'action': 'stand'})
            self.deck = self.deck[:-(response['num_dealer_cards'] -
                                     self.num_dealer_cards+1)]

        elif act == GameAction.SKIP:
            # Skip
            response = self.connection.request('game/act', {'action': 'skip'})
            self.deck = self.deck[:-(response['num_dealer_cards'] -
                                     self.num_dealer_cards+1)]

        self.player_score = response['player_score']
        self.dealer_score = response['dealer_score']
        self.player_hand = response['player_hand']
        self.dealer_hand = response['dealer_hand']
        self.num_dealer_cards = response['num_dealer_cards']
        self.money = response['money']

        # Update state
        if response['state'] == 'win':
            self.state = GameState.WIN
        elif response['state'] == 'lose':
            self.state = GameState.LOSE
        elif response['state'] == 'draw':
            self.state = GameState.DRAW
        elif response['state'] == 'flag':
            self.flag = response['flag']
            self.state = GameState.FLAG

    def init_game(self):
        """Start game"""
        response = self.connection.request('game/new')
        self.player_hand = response['player_hand']
        self.player_score = response['player_score']
        self.num_dealer_cards = response['num_dealer_cards']
        self.state = GameState.GAME

        sec = int(time.time())
        for _seed in range(sec-10, sec+10):
            deck = [[i // 13, i % 13] for i in range(4*13)]
            random.seed(_seed ^ self.user_id)
            random.shuffle(deck)
            if self.player_hand[0] == deck[-1] and self.player_hand[1] == deck[-3]:
                break
        self.deck = deck[:-4]


def calculate_score(cards):
    """Calculate current total of cards"""
    num_ace = 0
    score = 0
    for _, c in cards:
        if c == 0:
            num_ace += 1
        elif c < 10:
            score += c + 1
        else:
            score += 10

    while num_ace > 0:
        if 21 - score >= 10 + num_ace:
            score += 11
        else:
            score += 1
        num_ace -= 1

    return -1 if score > 21 else score


if __name__ == '__main__':
    game = Game()

    while game.state != GameState.FLAG:
        print(game.money)

        game.init_game()

        while game.player_score < 21 and game.state not in [GameState.WIN, GameState.DRAW]:
            if calculate_score(game.player_hand + [game.deck[-1]]) == -1:
                game.notify_action(GameAction.SKIP)
            else:
                game.notify_action(GameAction.HIT)

        if game.state not in [GameState.WIN, GameState.DRAW]:
            game.notify_action(GameAction.STAND)

    print(game.flag)
