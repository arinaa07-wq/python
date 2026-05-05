class CalendarError(Exception):
    """Базовое исключение для всего календаря"""
    pass
class DateSelectionError(CalendarError):
    """Ошибка при выборе даты"""
    def __init__(self, message="Ошибка при выборе даты"):
        self.message = message
        super().__init__(self.message)

class DateFormatError(CalendarError):
    """Ошибка при формате даты"""
    def __init__(self, *args):
        super().__init__(*args)