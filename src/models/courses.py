class Course:
    def __init__(self):
        self.course_id = None
        self.title = None
        self.credits = {"L": 0, "P": 0, "U": 0}

    def __str__(self) -> str:
        pass

    ## Functions to be implemented by an interface for the model

    def __create_course(self, course_id: str, title: str, credits: dict):
        pass

    def __get_course(self):
        pass

    def __edit_course(self, **kwargs):
        pass

    def __delete_course(self):
        pass

    def __get_all_courses(self):
        pass
