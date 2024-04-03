import numpy as np
try:
    input_str = input("Enter 9 numbers separated by spaces: ")
    user_list = []
    for item in input_str.split():
        user_list.append(int(item))

    def calculate(user_list):
        sq = np.array(user_list).reshape(3,3)
        flatten_sq =np.array(sq).flatten()
        return {
                'mean' : [list(sq.mean(axis = 0 )),list(sq.mean(axis =1)),(flatten_sq.mean())],
                'variance' : [list(sq.var(axis = 0)),list(sq.var(axis = 1)),flatten_sq.var()],
                'standard deviation' : [list(sq.std(axis = 0)),list(sq.std(axis= 1)),flatten_sq.std()],
                'max' :[list(sq.max(axis = 0)) ,list(sq.max(axis =1)), flatten_sq.max()],
                'min' : [list(sq.min(axis = 0)) ,list(sq.min(axis =1)), flatten_sq.min()],
                'sum' : [list(sq.sum(axis = 0)) ,list(sq.sum(axis =1)),  flatten_sq.sum()]
                }
    print(calculate(user_list))

except ValueError as ve:
    print("List must contain nine numbers.",ve)