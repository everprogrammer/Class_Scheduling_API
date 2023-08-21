import sys
import os
import django

sys.path.append("C:\\Users\\Asus\\Documents\\GitHub\\Class_Scheduling_API\\schedule")

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'schedule.settings'

django.setup()

def main():

  from timetable.models import Course, Professor, Classroom, TimeSlot
  # define the data lists
  import random
  from deap import base, creator, tools, algorithms
  import numpy as np
  import seaborn as sns
  import matplotlib.pyplot as plt
  from tabulate import tabulate

  # classrooms = ["Room 1","Room 2", "Room 3", 
  #               "Room 4", "Room 5"]
  # courses = ["Math", "History", "English", "Literature", "Spanish", "French", "Italian",
  #            "Phisics", "Chemistry", "Programming", "Art", "Algorithms", "Sport"]
  # professors = ["Professor X","Professor Y", "Professor Z", "Professor W", 
  #               "Professor T", ] # "Professor E"
  # timeslots = ["9:00-10:30", "10:30-12:00", "13:00-14:30", 
  #              "14:30-16:00", ] #  "13:00-14:30", "14:30-16:00" "17:00-18:30"

  courses = list(Course.objects.all())
  professors = list(Professor.objects.all())
  classrooms = list(Classroom.objects.all())
  timeslots = list(TimeSlot.objects.all())


  POPULATION_SIZE = 200
  P_CROSSOVER = 0.9
  P_MUTATION = 0.1
  MAX_GENERATIONS = 50
  HALL_OF_FAME_SIZE = 1

  random.seed(42)

  toolbox = base.Toolbox()


  # define the number of courses
  num_courses = len(courses)

  # create the custom fitness and individual classes
  creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
  creator.create("Individual", list, fitness=creator.FitnessMin)

  # create the toolbox object
  toolbox = base.Toolbox()

  # define a function to return a random course
  def randomCourse():
    return random.choice(courses)

  # define a function to return a random professor
  def randomProfessor():
    return random.choice(professors)

  # define a function to return a random classroom
  def randomClassroom():
    return random.choice(classrooms)

  # define a function to return a random timeslot
  def randomTimeslot():
    return random.choice(timeslots)

  # register the functions to the toolbox
  toolbox.register("randomCourse", randomCourse)
  toolbox.register("randomProfessor", randomProfessor)
  toolbox.register("randomClassroom", randomClassroom)
  toolbox.register("randomTimeslot", randomTimeslot)

  def individualCreator():
    # use tools.initRepeat to generate num_courses elements from the four functions
    individual = tools.initRepeat(creator.Individual, 
          lambda: [toolbox.randomCourse(), toolbox.randomProfessor(), 
                  toolbox.randomClassroom(), toolbox.randomTimeslot()], n=num_courses)  # return the individual
    return individual

  # register the function to the toolbox
  toolbox.register("IndividualCreator", individualCreator)

  # toolbox.register('IndividualCreator', tools.initRepeat, creator.Individual, toolbox.zeroOrOne, len(knapsack))

  toolbox.register("populationCreator", tools.initRepeat, list, toolbox.IndividualCreator)

  def evaluate(individual):
    # initialize the number of violations for each constraint
    violations_0 = 0
    violations_1 = 0
    violations_2 = 0
    violations_3 = 0
    violations_4 = 0

    professor_specializations = {}
    for professor in Professor.objects.all():
        professor_specializations[professor] = set(professor.courses_taught.all())

    # loop through the courses in the individual
    for i in range(0, len(individual)):
      # get the course, professor, classroom and timeslot
      course = individual[i][0]
      professor = individual[i][1]
      classroom = individual[i][2]
      timeslot = individual[i][3]

      if course not in professor_specializations.get(professor,set()):
         violations_0 += 500
      # loop through the other courses in the individual
      for j in range(i+1, len(individual)):
        # get the other course, professor, classroom and timeslot
        other_course = individual[j][0]
        other_professor = individual[j][1]
        other_classroom = individual[j][2]
        other_timeslot = individual[j][3]
        # check if the first and second constraint are violated
        if professor == other_professor and timeslot == other_timeslot:
          violations_1 += 1000
        if classroom == other_classroom and timeslot == other_timeslot:
          violations_2 += 1000
          
        # check if the third constraint is violated
        if course == other_course:
          violations_3 += 100

        # if timeslot == other_timeslot:
        #   violations_4 += 20      
    # calculate the weighted sum of violations
    fitness = violations_0 + violations_1 + violations_2 + violations_3 + violations_4
    return (fitness,)

  toolbox.register("evaluate", evaluate)

  toolbox.register("select", tools.selTournament, tournsize=3)

  toolbox.register("mate", tools.cxTwoPoint)

  # toolbox.register("mutate", tools.mutFlipBit, indpb=1/num_courses)

  def mutate_individual(individual, indpb):
      for i in range(0, len(individual)):
          if random.random() < indpb:
              individual[i][0] = toolbox.randomCourse()
          if random.random() < indpb:
              individual[i][1] = toolbox.randomProfessor()
          if random.random() < indpb:
              individual[i][2] = toolbox.randomClassroom()
          if random.random() < indpb:
              individual[i][3] = toolbox.randomTimeslot()
      return individual,

  toolbox.register("mutate", mutate_individual, indpb=0.1)  # Adjust indpb as needed

  population = toolbox.populationCreator(n=POPULATION_SIZE)

  stats = tools.Statistics(lambda ind: ind.fitness.values)
  # Register various functions that can be applied to these values
  stats.register('min', np.min)
  stats.register('avg', np.mean)

  hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

  generationCounter = 0


  population, logbook = algorithms.eaSimple(population, toolbox,
                                              cxpb=P_CROSSOVER,
                                              mutpb=P_MUTATION,
                                              ngen=MAX_GENERATIONS,
                                              stats=stats, 
                                              halloffame = hof,
                                              verbose=True)


  best = hof.items[0]
  # print("-- Best Ever Individual = ", best)
  table_headers = ["Course", "Professor", "Classroom", "Timeslot"]
  table_data = [[course, professor, classroom, timeslot] for course, professor, classroom, timeslot in best]
  print(tabulate(table_data, headers=table_headers, tablefmt='grid'))
  print("-- Best Ever Fitness = ", best.fitness.values[0])


  # minFitnessValues, meanFitnessValues = logbook.select("min", "avg")


  # sns.set_style("whitegrid")
  # plt.plot(minFitnessValues, color='red')
  # plt.plot(meanFitnessValues, color='green')
  # plt.xlabel('Generation')
  # plt.ylabel('Max / Average Fitness')
  # plt.title('Average and Min fitness over Generations')
  # plt.show()

if __name__ == '__main__':
  main()
