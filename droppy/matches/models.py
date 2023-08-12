from django.db import models


class Season(models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"Season {self.number}"


class Team(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Match(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name="home_team", on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name="away_team", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.home_team}-{self.away_team}"
