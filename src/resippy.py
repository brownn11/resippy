import numpy as np
import random
from resippy_data import recipes
import ipywidgets as widgets
from IPython.display import clear_output
from IPython.display import display

# Main function:
def select_recipes():
    r_names=[] # recipe name
    inp_a = []

    # Gather random recipes:
    r_indices = random.sample(range(0,len(recipes)),5)
    for index in r_indices:
        r_names.append(list(recipes.keys())[index])
        inp_a.append(widgets.Checkbox(description=list(recipes.keys())[index]))

    list_dict = {ii:r_names[ii] for ii in range(len(r_names))}

    def display_recipes(**inp_dict): 
        display(widgets.VBox(inp_a))
        for ii in range(len(inp_a)):
            if inp_a[ii].value: # get new recipe index if a printed recipe is checked
                new = random.sample(range(0,len(recipes)),1)[0]
                if new in r_indices:
                    while new in r_indices:
                        new = random.sample(range(0,len(recipes)),1)[0]
                r_indices.append(new)
                r_names[ii] = list(recipes.keys())[new]
                inp_a[ii] = widgets.Checkbox(description=list(recipes.keys())[new])
    
                clear_output()
    
                print('reshuffling...')
                list_dict = {jj:r_names[jj] for jj in range(len(r_names))}
                inp_dict = {list_dict[jj] : inp_a[jj] for jj in range(len(r_names))}  
                out = widgets.interactive_output(display_recipes, inp_dict) 
                display(out)
            
    print("Sounds good? (Select any recipes you don't want to keep):")
    inp_dict = {list_dict[ii] : inp_a[ii] for ii in range(len(r_names))} # call 
    out = widgets.interactive_output(display_recipes, inp_dict) 
    display(out)

def gather_ingredients():
    g_name=[]  # ingredient name
    g_amt=[]   # ingredient amt

    # Gather ingredients and amounts:
    print('Finalized meal list:')
    for r_name in r_names:
        print('-->',r_name)
        for item in recipes[r_name]:
            if item in g_name:
                index=np.where(np.array(g_name)==item)[0][0]
                g_amt[index]+=recipes[r_name][item]
            else:
                g_amt.append(recipes[r_name][item])
                g_name.append(item)

    print('\nIngredients:')
    # Print final list:
    for ii in range(len(g_name)):
        print(g_amt[ii],g_name[ii])
        
def select_ingredients():
    list_dict = {ii:str(g_amt[ii]) + ' ' + g_name[ii] for ii in range(len(g_amt))}
    inp_a = []
    for n in list_dict:
        inp_a.append(widgets.Checkbox(description=list_dict[n]))

    s_list=[]
    def f(**inp_dict): 
        for ii in range(len(inp_a)):
            if not inp_a[ii].value:
                if str(g_amt[ii]) + ' ' + g_name[ii] not in s_list:
                    s_list.append(str(g_amt[ii]) + ' ' + g_name[ii])
            else:
                if str(g_amt[ii]) + ' ' + g_name[ii] in s_list:
                    s_list.remove(str(g_amt[ii]) + ' ' + g_name[ii])
        print(s_list)

    inp_dict = {list_dict[ii] : inp_a[ii] for ii in range(len(g_amt))}
    print('Sounds good? (Select to remove  ingredients)')
    out = widgets.interactive_output(f, inp_dict) 
    widgets.VBox([widgets.VBox(inp_a), out])
