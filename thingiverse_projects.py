import webbrowser
import sqlite3


class DB_Controller:
    def __init__(self, db_name: str) -> sqlite3.Cursor:
        """
        Initialize DB_Controller object

        Args:
            db_name (str): Name of the database file
        """

        self.db_name = db_name
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cur = self.conn.cursor()
            print('База данных успешно инициализирована')
            return self.cur
        except Exception as ex:
            raise sqlite3.DatabaseError('Во время инициализации базы данных возникла ошибка: {}'.format(ex))
        
    
    def __del__(self) -> None:
        """
        Clean up and close database resources upon deletion of the object.

        This destructor method ensures that the database cursor and connection
        are properly closed to release any held resources when the DB_Controller
        instance is deleted.
        """

        self.cur.close()
        self.conn.close()

    def create_table(self) -> None:
        """
        Create a table in the database if it doesn't exist

        This method creates a table in the database with the following structure:
        - id: INTEGER PRIMARY KEY
        - name: TEXT
        - url: TEXT
        - description: TEXT

        If the table already exists, the method does nothing.
        If an error occurs during the execution of the method, it raises a sqlite3.DatabaseError exception
        """
        
        try:
            self.cur.execute('CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name TEXT, url TEXT, description TEXT)')
            print('Таблица успешно создана')
        except Exception as ex:
            raise sqlite3.DatabaseError('Во время создания таблицы возникла ошибка: {}'.format(ex))
        
    def add_project(self, name: str, url: str, description: str) -> None:
        """
        Add a new project to the database.

        This method inserts a new project record into the projects table
        with the specified name, url, and description.

        Args:
            name (str): The name of the project.
            url (str): The URL associated with the project.
            description (str): A brief description of the project.

        Raises:
            sqlite3.DatabaseError: If an error occurs while adding the project to the database.
        """
        
        try:
            self.cur.execute('INSERT INTO projects (name, url, description) VALUES (?, ?, ?)', (name, url, description))
            self.conn.commit()
            print('Проект успешно добавлен')
        except Exception as ex:
            raise sqlite3.DatabaseError('Во время добавления проекта возникла ошибка: {}'.format(ex))
        
    def delete_project(self, project_id: int) -> None:
        """
        Delete a project from the database.

        This method removes a project record from the projects table
        based on the specified project ID.

        Args:
            project_id (int): The ID of the project to be deleted.

        Raises:
            sqlite3.DatabaseError: If an error occurs while deleting the project from the database.
        """
        
        try:
            self.cur.execute('DELETE FROM projects WHERE id = ?', (project_id,))
            self.conn.commit()
            print('Проект успешно удален')
        except Exception as ex:
            raise sqlite3.DatabaseError('Во время удаления проекта возникла ошибка: {}'.format(ex))
        
    def get_project(self, project_id: int) -> tuple:
        """
        Retrieve a project from the database by its ID.

        This method queries the projects table for a project
        with the specified ID and returns the corresponding
        project record as a tuple.

        Args:
            project_id (int): The ID of the project to retrieve.

        Returns:
            tuple: A tuple containing the project data, or None if no project with the specified ID exists.

        Raises:
            sqlite3.DatabaseError: If an error occurs while retrieving the project from the database.
        """
        
        try:
            self.cur.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
            return self.cur.fetchone()
        except Exception as ex:
            raise sqlite3.DatabaseError('Во время получения проекта возникла ошибка: {}'.format(ex))
        
    def get_all_projects(self) -> list:
        """
        Retrieve all projects from the database.

        This method queries the projects table and returns a list of all
        project records stored in the database.

        Returns:
            list: A list of tuples, each containing the data of a project.

        Raises:
            sqlite3.DatabaseError: If an error occurs while retrieving the projects
            from the database.
        """
        
        try:
            self.cur.execute('SELECT * FROM projects')
            return self.cur.fetchall()
        except Exception as ex:
            raise sqlite3.DatabaseError('Во время получения всех проектов возникла ошибка: {}'.format(ex))

class ThingiverseProjects:
    def __init__(self) -> None:  
        self.db_controller = DB_Controller('thingiverse_projects.db')

    def add_project(self, name: str, url: str, description: str) -> None:
        self.db_controller.add_project(name, url, description)

    def delete_project(self, project_id: int) -> None:
        self.db_controller.delete_project(project_id)

    def get_project(self, project_id: int) -> tuple:
        return self.db_controller.get_project(project_id)

    def get_all_projects(self) -> list:
        return self.db_controller.get_all_projects()
