class Robot:
    def action(self):
        print("Il Robot sta processando i dati con i suoi circuiti.")

class Worker:
    def action(self):
        print("L'impiegato sta scrivendo un rapporto sulla scrivania.")

class Manager:
    def start_task(self, employee):
        print("Manager: 'Per favore, inizia il tuo lavoro...'")
        employee.action()

boss = Manager()

r2d2 = Robot()
mario = Worker()

boss.start_task(r2d2)
boss.start_task(mario)