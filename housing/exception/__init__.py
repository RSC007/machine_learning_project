import os
import sys


class HousingException(Exception):
    def __init__(self, error_message:  Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,error_detail=error_detail)


    # Use statictmethod: To call without assigning the object of this class
    @staticmethod
    def get_detailed_error_message(error_message:  Exception, error_detail: sys)->str:
        '''
        error_message: Exception object
        error_detail: object of sys module
        '''

        _,_, exec_tb = error_detail.exc_info()

        line_number=exec_tb.tb_frame.f_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in script: [{file_name}] at the line number: [{line_number}] error message: [{error_message}]"
        return error_message

    def __str__(self) -> str:
        # when you print the class then current error will display
        return self.error_message

    def __repr__(self) -> str:
        # we always write the code, how contructor call
        return HousingException.__name__.str()