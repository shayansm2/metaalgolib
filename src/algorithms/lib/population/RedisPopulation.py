from abc import ABC

from src.algorithms.lib.population.Population import Population
import redis


class RedisPopulation(Population, ABC):  # remove ABC later
    def __init__(self):
        self.redis = redis.Redis()
