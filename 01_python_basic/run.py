# run.py

import my_module #my module 실행

#my_packge 모듈안에있는 todo_module을 실행.(사용)
import my_package.todo_module as todo #as 별칭 ->my_packge.todo_module 대신 todo

r = my_module.plus(100, 200)
print(r)
r = my_module.minus(230, 100)
print(r)

#my_packge.todo_module.print_gugudan(5)
todo.print_gugudan(6)

#plus()
#python run.py

