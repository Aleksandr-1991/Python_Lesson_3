import Lesson_3_Task_3_MODUL   # Импорт всего модуля.
print(Lesson_3_Task_3_MODUL.max1(19, 20))

from Lesson_3_Task_3_MODUL import max1  # Импорт одной f-ции из модуля.
print(max1(19, 20))

from Lesson_3_Task_3_MODUL import *  # Импорт Всех f-ций из модуля.
print(max1(19, 20))

import Lesson_3_Task_3_MODUL as m1   # Импорт всего модуля c временным сокращением его имени до указанного "m1".
print(m1.max1(19, 20))