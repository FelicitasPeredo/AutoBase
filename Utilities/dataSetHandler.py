class DataSetHandler():
    
    def dataSetHandler(file):
        tuples_list = []
        for a in file.keys():
            if (a != 'test'):
                iteration = ( a, file[a] )
                tuples_list.append(iteration)
        return tuples_list
    
    