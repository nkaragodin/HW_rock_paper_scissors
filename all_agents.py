import random
#0 - rock
#1 - paper
#2 - scissors

def rock_agent(observation, configuration):
    return 0

def not_rock_agent(observation, configuration):
    return random.randrange(1, configuration.signs)

def paper_agent(observation, configuration):
    return 1

def not_paper_agent(observation, configuration):
    return random.randrange(0, configuration.signs, 2)

def scissors_agent(observation, configuration):
    return 2

def not_scissors_agent(observation, configuration):
    return random.randrange(0, configuration.signs - 1)

def opponent_agent(observation, configuration):
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        return random.randrange(0, configuration.signs)

def random_agent(observation, configuration):
    return random.randrange(random.randrange(0,2), configuration.signs)

def copynext_opponent_agent(observation, configuration):
    if observation.step > 0:
        return (observation.lastOpponentAction + 1) % configuration.signs
    else:
        return random.randrange(0, configuration.signs)

def copyprevious_opponent_agent(observation, configuration):
    if observation.step > 0:
        return (observation.lastOpponentAction + 2) % configuration.signs
    else:
        return random.randrange(0, configuration.signs)

last_change_lose_action = None
def change_if_lose_agent(observation, configuration):
    global last_change_lose_action
    if observation.step == 0:
        last_change_lose_action = random.randrange(0, configuration.signs)
    elif (observation.lastOpponentAction - last_change_lose_action) in [-2, 0, 1]:
        last_change_lose_action = (observation.lastOpponentAction + 1) % configuration.signs
    return last_change_lose_action

last_change_win_action = None
def change_if_win_agent(observation, configuration):
    global last_change_win_action
    if observation.step == 0:
        last_change_win_action = random.randrange(0, configuration.signs)
    elif (observation.lastOpponentAction - last_change_win_action) in [-1, 2]:
        last_change_win_action = (observation.lastOpponentAction + 1) % configuration.signs
    return last_change_win_action

counter = 0
def queue_agent (observation, configuration):
    global counter
    counter += 1
    if counter % 3 == 0:
        return 0
    elif counter % 3 == 1:
        return 1
    else:
        return 2

agents = {
    "rock_agent": rock_agent,
    "not_rock_agent": not_rock_agent,
    "paper_agent": paper_agent,
    "not_paper_agent": not_paper_agent,
    "scissors_agent": scissors_agent,
    "not_scissors_agent": not_scissors_agent,
    "opponent_agent": opponent_agent,
    "random_agent": random_agent,
    "copynext_opponent_agent": copynext_opponent_agent,
    "copyprevious_opponent_agent": copyprevious_opponent_agent,
    "change_if_lose_agent": change_if_lose_agent,
    "change_if_win_agent": change_if_win_agent,
    "queue_agent": queue_agent
}
