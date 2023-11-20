class CourseService:
    def __init__(self, db) -> None:
        self.db = db

    def create_course(self, course_id: str, title: str, credits: dict):
        query = f"""
            INSERT INTO courses
            VALUES (
                '{course_id}',
                '{title}',
                '{credits['L']}',
                '{credits['P']}',
                '{credits['U']}'
            );
        """
        return self.db.insert_data(query)

    def get_course(self, course_id: str):
        query = f"""
            SELECT 1
            FROM courses
            WHERE
                course_id = '{course_id}';
        """
        return self.db.fetch_data(query)

    def edit_course(self, **kwargs):
        query = f"""
            UPDATE courses
            SET
                title = '{kwargs['title']}',
                credits_L = '{kwargs['credits']['L']}',
                credits_P = '{kwargs['credits']['P']}',
                credits_U = '{kwargs['credits']['U']}'
            WHERE
                course_id = '{kwargs['course_id']}';
        """
        return self.db.insert_data(query)

    def delete_course(self, course_id: str):
        query = f"""
            DELETE FROM courses
            WHERE
                course_id = '{course_id}';
        """
        return self.db.insert_data(query)

    def get_all_courses(self):
        query = f"""
            SELECT *
            FROM courses;
        """
        return self.db.fetch_data(query)
