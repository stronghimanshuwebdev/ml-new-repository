import sys

class HousingException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        """
        Error message: Exception object
        """
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail):
        _, _, exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        return f"Error Occurred in the script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return self.__class__.__name__
