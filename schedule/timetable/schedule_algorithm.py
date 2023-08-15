import random
from datetime import datetime, timedelta
from deap import base, creator, tools, algorithms

# Define the classes
class Course:
    def __init__(self, name):
        self.name = name

class Professor:
    def __init__(self, name):
        self.name = name
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

class TimeSlot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other):
        return self.start_time < other.end_time and other.start_time < self.end_time

class Room:
    def __init__(self, name, capacity, is_lab):
        self.name = name
        self.capacity = capacity
        self.is_lab = is_lab

# Generate random data for the classes
course_names = ['Math', 'Science', 'History', 'English', 'Art']
professor_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
time_slots = [TimeSlot(datetime(2023, 8, 15, 8, 0), datetime(2023, 8, 15, 9, 30)),
              TimeSlot(datetime(2023, 8, 15, 9, 45), datetime(2023, 8, 15, 11, 15)),
              TimeSlot(datetime(2023, 8, 15, 11, 30), datetime(2023, 8, 15, 13, 0))]
rooms = [Room('Room A', 30, False), Room('Lab 101', 20, True), Room('Room B', 25, False)]

courses = [Course(name) for name in course_names]
professors = [Professor(name) for name in professor_names]

# Assign each course to a unique professor
for course, professor in zip(courses, professors):
    professor.assign_course(course)

# Genetic algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("professor", random.choice, professors)
toolbox.register("time_slot", random.choice, time_slots)
toolbox.register("room", random.choice, rooms)

def initialize_individual():
    individual = [(professor, course, toolbox.time_slot(), toolbox.room()) for course, professor in zip(courses, professors)]
    return creator.Individual(individual)

def evaluate_individual(individual):
    conflicts = 0

    time_slot_assignments = {}

    for professor, course, time_slot, room in individual:
        if time_slot in time_slot_assignments:
            conflicts += 1

        time_slot_assignments[time_slot] = course

    fitness = 1 / (1 + conflicts)
    return fitness,

toolbox.register("evaluate", evaluate_individual)
toolbox.register("individual", initialize_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

population_size = 10
crossover_probability = 0.7
mutation_probability = 0.2
generations = 50

population = toolbox.population(n=population_size)

algorithms.eaSimple(population, toolbox, cxpb=crossover_probability, mutpb=mutation_probability, ngen=generations)

best_individual = tools.selBest(population, k=1)[0]

for professor, course, time_slot, room in best_individual:
    print(f"Professor: {professor.name}, Course: {course.name}, Time Slot: {time_slot.start_time} - {time_slot.end_time}, Room: {room.name}")
