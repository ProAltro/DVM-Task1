class Section:
    def __init__(self):
        self.course_id = None
        self.id = None
        self.type = None  # Either L,P or T
        self.times = None
        self.room = None
        self.midsem = None
        self.compre = None
        self.instructors = []

    def parse(self, details):
        try:
            self.course_id = details["course_id"]
            self.id = details["id"]
            self.type = details["type"]
            self.times = details["times"]
            self.room = details["room"]
            self.midsem = details["midsem"]
            self.compre = details["compre"]
            self.instructors = details["instructors"]
            return True
        except KeyError:
            return False

    def pretty_time(self):
        days = {
            "M": "Monday",
            "T": "Tuesday",
            "W": "Wednesday",
            "Th": "Thursday",
            "F": "Friday",
            "S": "Saturday",
        }
        am_pm = lambda hour: "AM" if (hour + 7) < 12 else "PM"
        num = lambda hour: (hour + 7) if (hour + 7) < 12 else (hour + 7) - 12
        hour = lambda hour: f"{num(hour)}{am_pm(hour)}"

        time = self.times.split(" ")
        i = 0
        while not time[i].isnumeric():
            i += 1

        return f"{', '.join([days[i] for i in time[:i]])}: {hour(int(time[i]))} - {hour(int(time[-1]))}"

    def __str__(self) -> str:
        return f"""
Course ID: {self.course_id}
Section ID: {self.id}
Section Type: {self.type}
Times: {self.pretty_time()}
Room: {self.room}
Midsem: {self.midsem}
Compre: {self.compre}
Instructors: {', '.join(self.instructors)}
"""

    # Functions to be implemented by an interface for the model
    def __get_section(self):
        pass

    def __create_section(
        self,
        course_id,
        section_id,
        section_type,
        times,
        room,
        midsem,
        compre,
        instructors,
    ):
        pass

    def __edit_section(self, **kwargs):
        pass

    def __delete_section(self):
        pass

    def __get_all_sections(self):
        pass

    def __get_all_sections_for_course(self):
        pass
