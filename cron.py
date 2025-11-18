from threading import Thread
from time import sleep
import logging
from subprocess import run, PIPE
import json

class Task:
    '''Класс-прототип, в котором будут содержаться методы, которые используют задачи, а также их свойства'''
    def __init__(self, name: str, cmd: str, delay: int) -> None:
        self.name = name
        self.cmd = cmd
        self.delay = delay
        self.active = False

    def _task_func(self):
        while True:
            proc = run(self.cmd, shell=True, stdout=PIPE, stderr=PIPE)
            ecode = proc.returncode
            sleep(self.delay)


class TaskManager:
    '''Менеджер заданий, который содержит методы, с помощью которых происходит управление задачами'''
    def __init__(self, name) -> None:
        self.name = name
        self.tasks_list = []
        self.threads = []
    # Описание state-машины: Задания могут быть в двух состояниях: Запущено и остановлено. Как переходят из одного состояния в другое: методом start_task будет создаваться новый поток, который будет дрочить команду, прописанную в таске по delay.
    # Остановка задачи будет выполняться методом stop_task, который будет убивать поток.
    
    def start_task(self, name: str) -> tuple[str, bool]:
        '''Запуск задачи. Тут вообще планируется внедрение мультипоточной штуки, которая будет контролить таски и время задержки. Каждая задача - отдельный поток'''
        pass
        return name, True

    def stop_task(self, name: str) -> tuple[str, bool]:
        '''Остановка задачи'''
        pass
        return name, True

    def get_tasks_list(self) -> dict[str, bool]:
        '''Метод, позволяющий получить словарь задач и их состояний'''
        pass

    def get_task_state(self, name) -> tuple[str, str]:
        for task in self.tasks_list:
            if task.name == name:
                return name, task.state
            else:
                return name, 'Ошибка: задачи с таким именем не найдено'
            

    def add_task(self, name: str, cmd: str, delay: int) -> Task:
        '''Метод, создающий таску и добавляющий её к исполнению'''
        self.tasks_list.append(Task(name=name, cmd=cmd, delay=delay))


    def remove_task(self, name: str) -> tuple[str, bool]:
        '''Метод, удаляющий задачу из пула выполняемых'''
        pass
        return name, True
            

class Cron:

    # Короче на моменте инициализации объекта класса Cron хочу сделать так, чтобы он сразу парсил файл с задачами, сразу создавал нужные таски и добавлял их в TaskManager

    '''Крон парсит файл с задачами, создаёт нужные задачи и заполняет очередь в TaskManager'''

    def __init__(self, tasks_file: str) -> None:
        '''Инициализация получает на вход экземпляр класса менеджера задач, через который крон будет управлять задачами'''
        self.task_manager = TaskManager('main')
        for task in self._parse_tasks_file(tasks_file):
            self.task_manager.tasks_list.append(Task(name=task.name, cmd=task.cmd, delay=task.delay))


    def start_cron(self) -> bool:
        '''Метод, запускающий выполнение всех задач из пула.'''
        pass
        return True


    def stop_cron(self) -> bool:
        '''Метод, останавливающий выполнение всех задач из пула.'''
        pass
        return True


    def _parse_tasks_file(self, tasks_file) -> dict[str, int]:
        '''Метод, отвечающий за парсиг файла с задачами.
        
           Формат задач будет в виде json
           {
            'name': 'test_task1,
            'cmd': 'ip a',
            'delay': 300
            }'''
        pass