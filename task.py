import typer
from rich import print as rprint
import subprocess
from questionary import Style
import questionary
from prompt_toolkit import print_formatted_text, ANSI
import time
import sys
import itertools
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()
tasks = []
time_2 = []
category_2 = []
priority_2 = []

@app.command()
def main():
    global tasks
    global times 
    global priority
    global category

    answers = questionary.form(
          #first = questionary.confirm("Would you like to add a Task",default=True),
          second = questionary.select("Select Item",choices=["Add","Help","Exit"]),
          
    ).ask()

    selected_item = answers["second"] 

    confirm = questionary.confirm(f"Are you sure you want to select {selected_item}?",default=True).ask()

    if confirm:
     rprint(f"[yellow bold]You selected[/yellow bold] [green bold]{selected_item}[/green bold]")
    else:
        app()
    
    if selected_item == "Add":
        task = questionary.text(
            "Write a task you want to add:",
            
        ).ask()

        
        tasks.append(task)

        rprint(f"Task added: [green bold]{tasks} [/green bold]")
        
        time_q = questionary.text(
            "Write the time you want to do the task:",


        ).ask()

        time_2.append(time_q)
        rprint(f"Task added: [green bold]{time_q}[/green bold]")


        priority = questionary.select(
               "Set the priority for the task:",
               choices=["High","Medium","Low"]
       ).ask()
        priority_2.append(priority)
        
        rprint(f"Task priority: [green bold]{priority}[/green bold]")
       
        category = questionary.select(
            "Select the category for the task:",
             choices=["Work","Personal",]
       ).ask()
        category_2.append(category)
        loading_animation()
        rprint(f"Task category: [green bold]{category}[/green bold]")

        
         
        
        task_table()

        
        #user = input("Press Enter for more... ")
        
        adding_task()
        #task_view()
    elif selected_item == "Help":
        view_help()

def task_view():
    global tasks
    global times 
    global priority
    global category


    loading_animation()

    task_table()

    user = input("Press Enter for more... ")

    adding_task()

def task_table():
    table_task = Table(title="Task View")
    table_task.add_column("Task",style="blue",no_wrap=True)
    table_task.add_column("Time",style="yellow")
    table_task.add_column("Category",style="yellow")
    table_task.add_column("Priority",style="yellow")

    for i in range(len(tasks)):
        table_task.add_row(tasks[i],time_2[i],category_2[i],priority_2[i])

    console.print(table_task)

    

def adding_task():
    global tasks,task
    add_rm = questionary.select(
            "What do you want to do?",
            choices=["Add","Remove","Help","Exit"]
            
         ).ask()

    if add_rm == "Add":
            task_add = questionary.select(
                "What do you want to add?",
                choices=["Task"]
            ).ask()

            task_ = questionary.text(
                    "Write a task you want to add:"
            ).ask()

            time_add = questionary.text(
                "Add a Time for your new Task",

            ).ask()
            priority_add = questionary.text(
                "Add a Priority for your new Task",

            ).ask()
            category_add = questionary.text(
                "Add a category for your new Task",

            ).ask()





            
            time_2.append(time_add)
            category_2.append(category_add)
            priority_2.append(priority_add)
            tasks.append(task_)
            rprint(f"Task added: [green bold]{task_}[/green bold]")

            task_view()
    if add_rm == "Remove":
        selecting_rm = questionary.select(
            "What do you want to remove?",
            choices=["A task"]

        ).ask()

        if selecting_rm == "A task":
            del_task = questionary.text(
                "Write the name of the task you want to delete: "
            ).ask()
            
            if del_task in tasks:
               tasks.remove(del_task)
               task_view()
    if add_rm == "Help":
        view_help()
    if add_rm == "Exit":
        sys.exit(0)

def view_help():
    
    table = Table(title="Available Commands")
    table.add_column("Command",style="cyan",no_wrap=True)
    table.add_column("Description",style="magenta")

    table.add_row("add", "Add a new task to the list")
    table.add_row("remove", "Remove a task from a list")
    table.add_row("help", "Show this help message")

    
    #main()

    console.print(table)
    input("Press Enter to go back ")
    main()
    

def loading_animation(duration=2):
    spinner = itertools.cycle(["-","\\","|","/"])

    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f'\rLoading... {next(spinner)}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!          \n')

if __name__ == "__main__":
     while True:
          app()


