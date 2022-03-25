from src.algorithms.lib.population.Population import Population
import redis


class RedisPopulation(Population):
    def __init__(self):
        self.redis = redis.Redis()
