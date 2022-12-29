from builders import TestingBuilder

from director import EnvDirector
from environment import Environment

environment_ = Environment()
testing_builder = TestingBuilder(environment_)
full_testing_env = EnvDirector.create_full_env(testing_builder)
print()
print(full_testing_env)

print()
testing_env_without_app = EnvDirector.create_env_without_app(testing_builder)
print()
print(testing_env_without_app)
