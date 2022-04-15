class AlgorithmSettings:
    # todo make the names better
    stopCriteriaNumberOfGeneration = 'number_of_generation'
    stopCriteriaCompleteConvergence = 'complete_convergence'
    stopCriteriaNoProgress = 'no_progress'

    all_stop_criteria = [
        stopCriteriaNoProgress,
        stopCriteriaCompleteConvergence,
        stopCriteriaNumberOfGeneration,
    ]

    initialSelectionRandom = 'random'
    initialSelectionGreedy = 'greedy'

    all_initial_selections = [
        initialSelectionGreedy,
        initialSelectionRandom,
    ]

    parentSelectionRandom = 'random'
    parentSelectionTop = 'top'
    parentSelectionRouletteWheel = 'roulette_wheel'
    parentSelectionTournament = 'tournament'

    all_parent_selections = [
        parentSelectionTournament,
        parentSelectionRouletteWheel,
        parentSelectionTop,
        parentSelectionRandom,
    ]

    generationSelectionTop = 'top'
    generationSelectionTopShare = 'top_share'
    generationSelectionRandom = 'random'

    all_generation_selections = [
        generationSelectionTop,
        generationSelectionRandom,
        generationSelectionTopShare,
    ]
