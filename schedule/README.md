# Class Scheduling Application README

Welcome to the Class Scheduling Application! This application is designed to help educational institutions efficiently create class schedules by utilizing a Genetic Algorithm powered by the DEAP library. Below, you'll find step-by-step instructions on how to install, use, and optimize the application.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Course Definition and Entry](#course-definition-and-entry)
  - [Professor Assignment](#professor-assignment)
  - [Classroom Allocation](#classroom-allocation)
  - [Timeslot Assignment](#timeslot-assignment)
  - [Genetic Algorithm Implementation](#genetic-algorithm-implementation)
  - [Optimization and Evaluation](#optimization-and-evaluation)
  - [Final Schedule Generation](#final-schedule-generation)
  - [Optimizing the Algorithm](#optimizing-the-algorithm)
  - [Troubleshooting](#troubleshooting)
  - [Donation](#donation)

## [Installation](#installation)

To get started, follow these installation steps:

```bash
git clone https://github.com/everprogrammer/Class_Scheduling_API.git
cd your-repo-name
pip install -r requirements.txt
```
## [Usage](#usage)
Follow these steps to use the application effectively:

### [Course Definition and Entry](#course-definition-and-entry)
- Launch the application.
- Use the intuitive interface to define courses offered by the institution.
- Enter the course name, required duration, and any associated constraints (prerequisites, preferred timeslots).
### [Professor Assignment](#professor-assignment)
- Input the list of professors along with their availability, preferences, and specialization areas.
- The Genetic Algorithm will allocate professors to courses, optimizing teaching load and respecting preferences.
### [Classroom Allocation](#classroom-allocation)
- Add classrooms to the system, specifying seating capacity and facilities.
- The application will efficiently allocate courses to classrooms, considering capacity and requirements.
### [Timeslot Assignment](#timeslot-assignment)
- Define available timeslots for each day.
- The Genetic Algorithm assigns timeslots to courses, professors, and classrooms, minimizing conflicts.
### [Genetic Algorithm Implementation](#genetic-algorithm-implementation)
The core of the application uses the Genetic Algorithm from the DEAP library.

. Documentation for the DEAP library: [DEAP Documentation](https://deap.readthedocs.io/en/master/)
. The algorithm evolves schedules through selection, crossover, and mutation operations.
###  [Optimization and Evaluation](#optimization-and-evaluation)
- The Genetic Algorithm iteratively improves schedules over generations.
- Tools are provided to visualize and evaluate schedules, assessing fitness, class distribution, and conflicts.
### [Final Schedule Generation](#final-schedule-generation)
- Once an optimal schedule is achieved, generate the final timetable.
- The application presents scheduled courses, professors, classrooms, and timeslots in a user-friendly format.
### [Optimizing the Algorithm](#optimizing-the-algorithm)
1. The Genetic Algorithm's efficiency can be influenced by hyperparameters:

`POPULATION_SIZE`
`P_CROSSOVER`
`P_MUTATION`
`MAX_GENERATIONS`
Selection method
Mutation method
Mutation probability

2.Default values are set to:

`Population size`: [default value=500]
`Crossover probability`: [default value=0.9]
`Mutation probability`: [default value=0.1]
`Max generations`: [default value=50]
`Selection method`: Tournament (size = 3)
`Mutation method`: TwoPoint
`Mutation probability`: 10%

Adjust these hyperparameters as needed for better results.

### [Troubleshooting](#troubleshooting)
1. The algorithm may not always generate the best result due to data entry or hyperparameters.
2. If desired results aren't achieved, consider:
        - Reviewing data entry for courses, professors, classrooms, and timeslots.
        - Modifying hyperparameters to fine-tune the algorithm's behavior.
        - Iterating the algorithm multiple times to explore different solutions.
    `Note`: This is a basic class scheduling application. If satisfied, use the generated schedule; otherwise, you can run the algorithm multiple times for better results. Keep in mind that the Genetic Algorithm's effectiveness depends on the problem's nature, so adjusting hyperparameters might be necessary.

    For any inquiries or support, please contact amir.tavakolian68@gmail.com

### [Donation](#donation)
Buy us a coffee if you like!

Bitcoin Address: bc1qtx4wmyyv8rptyw0khm8vxacxly2v4f82pc6lad
USDT Address: TJ9FPugsuvGh8xzcDqhKZvGKz6jbPmwvvo

Your support is greatly appreciated!