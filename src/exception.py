import sys

def error_message_detail(error ,error_details : sys):
   _,_,exc_tb =error_details.exc_info()
   file_name = exc_tb.tb_frame.f_code.co_filename
   error_message = f'Error occured in python script name {file_name} \n line number {exc_tb.tb_lineno} \n error message {str(error)} '
   return error_message


class CustomException(Exception):
    def __init__(self, error_message ,error_details : sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message , error_details=error_details)

    def __str__(self) -> str:
        return self.error_message


