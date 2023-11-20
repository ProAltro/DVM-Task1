class SectionService:
    def __init__(self, db) -> None:
        self.db = db

    def create_section(
        self,
        course_id: str,
        section_id: str,
        section_type: str,
        times: str,
        room: str,
        midsem: str,
        compre: str,
        instructors,
    ):
        query = f"""
            INSERT INTO sections
            VALUES (
                '{course_id}',
                '{section_id}',
                '{section_type}',
                '{times}',
                '{room}',
                '{midsem}',
                '{compre}',
                '{instructors}'
            );
        """
        return self.db.insert_data(query)

    def get_section(self, course_id: str, section_id: str):
        query = f"""
            SELECT 1
            FROM sections
            WHERE
                course_id = '{course_id}'
                AND section_id = '{section_id}';
        """
        return self.db.fetch_data(query)

    def edit_section(self, **kwargs):  # TODO
        query = f"""
            UPDATE sections
            SET
                section_type = '{kwargs['section_type']}',
                times = '{kwargs['times']}',
                room = '{kwargs['room']}',
                midsem = '{kwargs['midsem']}',
                compre = '{kwargs['compre']}',
                instructors = '{kwargs['instructors']}'
            WHERE
                course_id = '{kwargs['course_id']}'
                AND section_id = '{kwargs['section_id']}';
        """
        return self.db.insert_data(query)

    def delete_section(self, course_id: int, section_id: int):
        query = f"""
            DELETE FROM sections
            WHERE
                course_id = '{course_id}'
                AND section_id = '{section_id}';
        """
        return self.db.insert_data(query)

    def get_all_sections(self):
        query = f"""
            SELECT *
            FROM sections;
        """
        return self.db.fetch_data(query)

    def get_sections_by_course(self, course_id: str):
        query = f"""
            SELECT *
            FROM sections
            WHERE
                course_id = '{course_id}';
        """
        return self.db.fetch_data(query)
