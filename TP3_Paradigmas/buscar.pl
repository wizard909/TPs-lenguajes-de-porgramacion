% Paradigma Lógico (Prolog)
% Definiendo una regla de pertenencia, el lenguaje se hace cargo de buscar
% si se cumple la lógica gracias a su motor de inferencia (backtracking).

pertenece(X, [X|_]).
pertenece(X, [_|Cola]) :- pertenece(X, Cola).

% Consulta para ejecutar:
% ?- pertenece(7, [3, 7, 2, 9]).
