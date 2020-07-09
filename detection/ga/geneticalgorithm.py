
import pygad
import numpy
from fis import fuzzification
last_fitness = 0


    
def Run2(testset_size,test_weight):
    print("GA run\n")
    
def Run(testset_size,test_weight):
    
    desired_output = 100 

    def fitness_func(solution, solution_idx):
        
        output = fuzzification.Run(solution,testset_size,test_weight)
        fitness = 1.0 / numpy.abs(output - desired_output)
        return fitness

    fitness_function = fitness_func

    num_generations = 100 
    num_parents_mating = 7 

    
    sol_per_pop = 50 
    num_genes = 8 

    init_range_low = -2
    init_range_high = 40

    parent_selection_type = "sss" 
    keep_parents = 7 

    crossover_type = "single_point" 

    
    mutation_type = "random" 
    mutation_percent_genes = 10 

    
    def callback_generation(ga_instance):
        global last_fitness
        print("Generation = {generation}".format(generation=ga_instance.generations_completed))
        print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))
        print("Change     = {change}".format(change=ga_instance.best_solution()[1] - last_fitness))

    
    ga_instance = pygad.GA(num_generations=num_generations,
                           num_parents_mating=num_parents_mating, 
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop, 
                           num_genes=num_genes,
                           init_range_low=init_range_low,
                           init_range_high=init_range_high,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           callback_generation=callback_generation)

    
    ga_instance.run()

   
    ga_instance.plot_result()

   
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

    #prediction = numpy.sum(numpy.array(function_inputs)*solution)
    #print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

    if ga_instance.best_solution_generation != -1:
        print("Best fitness value reached after {best_solution_generation} generations.".format(best_solution_generation=ga_instance.best_solution_generation))

    
    filename = 'genetic' 
    ga_instance.save(filename=filename)

    
    loaded_ga_instance = pygad.load(filename=filename)
    loaded_ga_instance.plot_result()
