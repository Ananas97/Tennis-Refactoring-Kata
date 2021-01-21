# -*- coding: utf-8 -*-

class TennisGame1:
    DRAW_SCORES = {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
    }

    SCORES = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_points = 0
        self.player_two_points = 0

    def won_point(self, player_name):
        if player_name == self.player_one_name:
            self.player_one_points += 1
        else:
            self.player_two_points += 1

    def score(self):
        if self.player_one_points == self.player_two_points:
            return self.get_draw()
        elif self.player_one_points >= 4 or self.player_two_points >= 4:
            points_difference = abs(self.player_one_points - self.player_two_points)
            return self.get_message_by_difference(points_difference) + self.get_winning_player_name()
        else:
            result = self.get_player_score(self.player_one_points)
            result += "-"
            result += self.get_player_score(self.player_two_points)
            return result

    def get_draw(self):
        return self.DRAW_SCORES.get(self.player_one_points, "Deuce")

    def get_winning_player_name(self):
        return self.player_one_name if self.player_one_points > self.player_two_points else self.player_two_name

    def get_player_score(self, points):
        return self.SCORES[points]

    def get_message_by_difference(self, points_difference):
        if points_difference == 1:
            return "Advantage "
        else:
            return "Win for "


class TennisGame2:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_points = 0
        self.player_two_points = 0

    def won_point(self, player_name):
        if player_name == self.player_one_name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if (self.player_one_points == self.player_two_points and self.player_one_points < 3):
            if (self.player_one_points == 0):
                result = "Love"
            if (self.player_one_points == 1):
                result = "Fifteen"
            if (self.player_one_points == 2):
                result = "Thirty"
            result += "-All"
        if (self.player_one_points == self.player_two_points and self.player_one_points > 2):
            result = "Deuce"

        player_one_result = ""
        player_two_result = ""
        if (self.player_one_points > 0 and self.player_two_points == 0):
            if (self.player_one_points == 1):
                player_one_result = "Fifteen"
            if (self.player_one_points == 2):
                player_one_result = "Thirty"
            if (self.player_one_points == 3):
                player_one_result = "Forty"

            player_two_result = "Love"
            result = player_one_result + "-" + player_two_result
        if (self.player_two_points > 0 and self.player_one_points == 0):
            if (self.player_two_points == 1):
                player_two_result = "Fifteen"
            if (self.player_two_points == 2):
                player_two_result = "Thirty"
            if (self.player_two_points == 3):
                player_two_result = "Forty"

            player_one_result = "Love"
            result = player_one_result + "-" + player_two_result

        if (self.player_one_points > self.player_two_points and self.player_one_points < 4):
            if (self.player_one_points == 2):
                player_one_result = "Thirty"
            if (self.player_one_points == 3):
                player_one_result = "Forty"
            if (self.player_two_points == 1):
                player_two_result = "Fifteen"
            if (self.player_two_points == 2):
                player_two_result = "Thirty"
            result = player_one_result + "-" + player_two_result
        if (self.player_two_points > self.player_one_points and self.player_two_points < 4):
            if (self.player_two_points == 2):
                player_two_result = "Thirty"
            if (self.player_two_points == 3):
                player_two_result = "Forty"
            if (self.player_one_points == 1):
                player_one_result = "Fifteen"
            if (self.player_one_points == 2):
                player_one_result = "Thirty"
            result = player_one_result + "-" + player_two_result

        if (self.player_one_points > self.player_two_points and self.player_two_points >= 3):
            result = "Advantage " + self.player_one_name

        if (self.player_two_points > self.player_one_points and self.player_one_points >= 3):
            result = "Advantage " + self.player_two_name

        if (self.player_one_points >= 4 and self.player_two_points >= 0 and (self.player_one_points - self.player_two_points) >= 2):
            result = "Win for " + self.player_one_name
        if (self.player_two_points >= 4 and self.player_one_points >= 0 and (self.player_two_points - self.player_one_points) >= 2):
            result = "Win for " + self.player_two_name
        return result


    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1


class TennisGame3:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_points = 0
        self.player_two_points = 0

    def won_point(self, n):
        if n == self.player_one_name:
            self.player_one_points += 1
        else:
            self.player_two_points += 1

    def score(self):
        if (self.player_one_points < 4 and self.player_two_points < 4) \
                and (self.player_one_points + self.player_two_points < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.player_one_points]
            return s + "-All" if (self.player_one_points == self.player_two_points) \
                else s + "-" + p[self.player_two_points]
        else:
            if self.player_one_points == self.player_two_points:
                return "Deuce"
            s = self.player_one_name if self.player_one_points > self.player_two_points \
                else self.player_two_name
            return "Advantage " + s if ((self.player_one_points - self.player_two_points)
                                        * (self.player_one_points - self.player_two_points) == 1) \
                else "Win for " + s
