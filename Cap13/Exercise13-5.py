'''
Created on 9 de ago de 2018

@author: Romulo
'''
def choose_from_hist(list_of_hist):
    hist_dict = {}
    for item in list_of_hist:
        if item not in hist_dict:
            hist_dict[item] = 1
        else:
            hist_dict[item] += 1
    probly_dict = {}
    total_items = len(list_of_hist)
    for key, value in hist_dict.items():
        probly_dict[key] = str(value) + "/" + str(total_items)
    return(probly_dict)
        
    
        
if __name__ == '__main__':
    print(choose_from_hist(['a','b','b','c']))
