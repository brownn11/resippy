import numpy as np
import random
from resippy_data import recipes
import ipywidgets as widgets
from IPython.display import clear_output
from IPython.display import display
from tkinter import *
from tkinter import ttk

# Main function:
def select_recipes():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Sounds good? Select an item to replace it:").grid(column=0, row=0)

    # Copy all recipe names:
    r_names = list(recipes.keys())
    r_sample = ['','','','','']

    def replace1():
        new_meal = ttk.Button(frm, text=random.choice(r_names))
        new_meal.configure(command=replace1)
        new_meal.grid(column=0, row=1)
        r_sample[0] = (new_meal['text'])
        r_names.remove(new_meal['text'])
        print(new_meal['command'])
        if len(r_names) == 0:
            print('all out!')
            root.destroy()
    def replace2():
        new_meal = ttk.Button(frm, text=random.choice(r_names))
        new_meal.configure(command=replace2)
        new_meal.grid(column=0, row=2)
        r_sample[1] = (new_meal['text'])
        r_names.remove(new_meal['text'])
        if len(r_names) == 0:
            print('all out!')
            root.destroy()
    def replace3():
        new_meal = ttk.Button(frm, text=random.choice(r_names))
        new_meal.configure(command=replace3)
        new_meal.grid(column=0, row=3)
        r_sample[2] = (new_meal['text'])
        r_names.remove(new_meal['text'])
        if len(r_names) == 0:
            print('all out!')
            root.destroy()
    def replace4():
        new_meal = ttk.Button(frm, text=random.choice(r_names))
        new_meal.configure(command=replace4)
        new_meal.grid(column=0, row=4)
        r_sample[3] = (new_meal['text'])
        r_names.remove(new_meal['text'])
        if len(r_names) == 0:
            print('all out!')
            root.destroy()
    def replace5():
        new_meal = ttk.Button(frm, text=random.choice(r_names))
        new_meal.configure(command=replace5)
        new_meal.grid(column=0, row=5)
        r_sample[4] = (new_meal['text'])
        r_names.remove(new_meal['text'])
        if len(r_names) == 0:
            print('All out! Lower your standards...')
            root.destroy()

    meal1 =  ttk.Button(frm, text=random.choice(r_names))
    meal1.configure(command=replace1)
    meal1.grid(column=0, row=1)
    r_sample[0] = (meal1['text'])
    r_names.remove(meal1['text'])

    meal2 =  ttk.Button(frm, text=random.choice(r_names))
    meal2.configure(command=replace2)
    meal2.grid(column=0, row=2)
    r_sample[1] = (meal2['text'])
    r_names.remove(meal2['text'])

    meal3 =  ttk.Button(frm, text=random.choice(r_names))
    meal3.configure(command=replace3)
    meal3.grid(column=0, row=3)
    r_sample[2] = (meal3['text'])
    r_names.remove(meal3['text'])

    meal4 =  ttk.Button(frm, text=random.choice(r_names))
    meal4.configure(command=replace4)
    meal4.grid(column=0, row=4)
    r_sample[3] = (meal4['text'])
    r_names.remove(meal4['text'])

    meal5 =  ttk.Button(frm, text=random.choice(r_names))
    meal5.configure(command=replace5)
    meal5.grid(column=0, row=5)
    r_sample[4] = (meal5['text'])
    r_names.remove(meal5['text'])

    opt_quit = ttk.Button(frm, text="Sounds good!", command=root.destroy).grid(column=0, row=6)
    root.mainloop()

    return r_sample

def gather_ingredients():
    g_name=[]  # ingredient name
    g_amt=[]   # ingredient amt

    r_sample = select_recipes()

    # Gather ingredients and amounts:
    print('Finalized meal list:')
    for r_name in r_sample:
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

    return (g_amt, g_name)
        
def select_ingredients():
    g_amt, g_name = gather_ingredients()
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
