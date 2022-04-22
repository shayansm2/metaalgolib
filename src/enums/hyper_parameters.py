class HyperParameterNames:
    numberOfIteration = 'number_of_iteration'  # todo move to algo settings
    numberOfPopulation = 'number_of_population'

    # genetic hyper-parameters
    geneticCrossoverPercentage = 'crossover_percentage'
    geneticMutationPercentage = 'mutation_percentage'
    geneticNumberOfCrossover = 'number_of_crossover'
    geneticNumberOfMutation = 'number_of_mutation'

    # PSO hyper-parameters
    psoInertiaWeight = 'inertia_weight'  # w
    psoCognitiveCoefficient = 'cognitive_coefficient'  # c1
    psoSocialCoefficient = 'social_coefficient'  # c2
