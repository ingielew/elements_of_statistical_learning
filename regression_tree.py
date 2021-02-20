#import matplotlib.pyplot as plt

def regression_tree(x, y):
    # max 10000 observations
    # min 10 observations in the each leaf
    # max_deep = 3
    # x_tab = [1, 2, 3]
    # y_tab = [1, 1, 1]
    division_points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    results_tab = [0 for i in range(1, 20)]

    #To przekazać w funkcji
    #x_tab = [i * 2 for i in range(1, 20)]
    #y_tab = [0, 0, 0, 0, 5, 20, 100, 100, 100, 100, 70, 65, 50, 45, 40, 10, 0, 0, 0]


    print("x", len(x_tab), "y", len(y_tab))
    input1 = list(zip(x_tab, y_tab))
    print(input1)
    sse_min = float("Inf")
    division_point = 0
    division_counter = 0

    # print(len(x_tab))
    # print(x_tab[0])

    while division_counter < 4:
        for i in range(0, len(x_tab)):
            # m1 left mean
            m1 = 0
            for j in range(0, (i - 1)):
                m1 = m1 + y_tab[j]
            m1 = m1 / (i + 1)
            # m2 right mean
            m2 = 0
            for j in range(i, len(x_tab)):
                m2 = m2 + y_tab[j]
            m2 = m2 / (len(x_tab) - i)
            # sum of square
            sse = 0
            for k in range(0, (i - 1)):
                sse = sse + (y_tab[k] - m1) ** 2
            for k in range(i, len(x_tab)):
                sse = sse + (y_tab[k] - m2) ** 2
            results_tab[i] = sse
            if sse < sse_min:
                sse_min = sse
                division_point = i
        division_points[division_counter] = division_point

        # if len(x_tab) > (len(division_points[division_counter]))
        # print(results_tab, division_point)
        # plt.scatter(x_tab, results_tab)
        # plt.show()
        division_counter = division_counter + 1
        regression_tree() #new_tab

        # TODO: sprawdzenie podziałów -> warunek na koniec algorytmu
        # if XXX
        # break
    return([2])

#regression_tree([i * 2 for i in range(1, 20)], [0, 0, 0, 0, 5, 20, 100, 100, 100, 100, 70, 65, 50, 45, 40, 10, 0, 0, 0])

