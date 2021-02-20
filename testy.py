def test(x_tab, y_tab, divisions_tab, division_num, min_observations):
    #tab = [11, 12, 5, 2]
    #tab.insert(2, 1)
    #matrix = [[0 for x in range(0,10)] for y in range(0,10)]

    sse_min_local = float("Inf")
    chosen_point_local = float("Inf")
    sse_min_global = float("Inf")
    chosen_point_global = float("Inf")
    sse = 0.0
    for i in range(0, division_num+1):
        start_point = divisions_tab[i]
        end_point = divisions_tab[i+1]

        #print(start_point)
        #print(end_point)

        if end_point - start_point >= (2 * min_observations):
            for j in range(start_point + 1, end_point):
                if (end_point - j > min_observations - 1) and (j - start_point) > min_observations:
                    left_mean = sum(y_tab[start_point:j]) / (j - start_point)
                    right_mean = sum(y_tab[j:end_point]) / (end_point - j)
                    for k in range(start_point, j):
                        sse = sse + (y_tab[k] - left_mean)**2
                    for k in range(j, end_point):
                        sse = sse + (y_tab[k] - right_mean)**2
                    if sse < sse_min_local:
                        sse_min_local = sse
                        chosen_point_local = j

                    print(left_mean)
                    print(right_mean)##pamiętać, że tu nie dochodzi do końca tabeli i to jest ok1!!
        if sse_min_local < sse_min_global:
            sse_min_global = sse_min_local
            chosen_point_global = chosen_point_local
            #print(sse_min_local)

    if chosen_point_global < float("Inf"):
        #artofical value
        divisions_tab.insert((division_num + 2), chosen_point_global)


    #sse_min_local = 0
    #choosen_point = 0
    #print(sorted(divisions_tab), len(divisions_tab))
    return(sorted(divisions_tab), (len(divisions_tab) - 2))

#a = test([i * 2 for i in range(1, 20)], [0, 0, 0, 0, 5, 20, 100, 100, 100, 100, 70, 65, 50, 45, 40, 10, 0, 0, 0], [0,9, 19], 1, 4)
#print(a[1][1], a[1][0])

def regtree(x_tab, y_tab, divisions_tab, division_num, min_observations, num_leaf):
    counter = num_leaf
    while counter > 0:
        a = test([i * 2 for i in range(1, 20)], [0, 0, 0, 0, 5, 20, 100, 100, 100, 100, 70, 65, 50, 45, 40, 10, 0, 0, 0], divisions_tab, division_num, 4)
        divisions_tab = a[0]
        division_num = a[1]
        counter = counter - 1
    print(divisions_tab)



b = regtree([i * 2 for i in range(1, 20)], [0, 0, 0, 0, 5, 20, 100, 100, 100, 100, 70, 65, 50, 45, 40, 10, 0, 0, 0], [0, 19], 0, 5, 1)
