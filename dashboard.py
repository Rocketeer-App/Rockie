import inquirer
import pyfiglet
import colorama

title = pyfiglet.Figlet(font='big')
print(colorama.Fore.GREEN + title.renderText('Dashboard'))

questions = [
    inquirer.Text('devId', message="What is your RDI Number?")
]

print(inquirer.prompt(questions))