:- dynamic tarea/3.

% Hecho: tarea(Titulo, Prioridad, Estado)

% 1. Agregar tarea (se guarda dinámicamente en la base de conocimientos)
agregar_tarea(Titulo, Prioridad) :-
    assertz(tarea(Titulo, Prioridad, pendiente)).

% 2. Completar tarea (se elimina la pendiente y se inserta la completada)
completar_tarea(Titulo) :-
    retract(tarea(Titulo, Prioridad, pendiente)),
    assertz(tarea(Titulo, Prioridad, completada)).

% 3. Mostrar pendientes (recorre y hace backtracking con fail)
mostrar_pendientes :-
    tarea(Titulo, Prioridad, pendiente),
    write('- '), write(Titulo), write(' | Prioridad: '), write(Prioridad), nl,
    fail.
mostrar_pendientes. % Caso base para terminar el backtracking sin falso
