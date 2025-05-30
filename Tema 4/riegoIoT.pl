%Zonas
zona(edificio).
zona(campo).

%Tipo de zona
tipo_zona(edificio, interior).
tipo_zona(campo, exterior).

% Estado de sensores por zona
humedad_suelo(edificio, baja).
humedad_suelo(campo, media).

temperatura(edificio, 35).
temperatura(campo, 30).

hora(edificio, 12).
hora(campo, 12).

pronostico_lluvia(edificio, false).
pronostico_lluvia(campo, true).


%Reglas: ¿Es una hora adecuada para regar?
hora_adecuada(Z) :- hora(Z, H), (H < 10 ; H > 18).

%Regla principal: ¿Cuando se debe activar el sistema de riego?
activar_riego(Z) :-
    humedad_suelo(Z, baja),
    hora_adecuada(Z),
    (tipo_zona(Z, interior) ; (tipo_zona(Z, exterior), pronostico_lluvia(Z, false))).


%Diagnostico del sistema
estado_riego(Z, 'Activado') :-
    activar_riego(Z).
estado_riego(Z, 'No activado') :-
    \+ activar_riego(Z).
    
 %Regla para alerta de temperatura extrema
alerta_calor(Z) :-
    temperatura(Z, T),
    T >= 32.

%Mensaje de alerta si se activa el riego con calor extremo
recomendacion(Z) :-
    activar_riego(Z),
    alerta_calor(Z), 
    tipo_zona(Z, exterior), !,
    format('Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo en la Zona ~w.~n', [Z]).

recomendacion(Z) :-
    activar_riego(Z),
    alerta_calor(Z), 
    tipo_zona(Z, interior), !,
    format('Alerta: Riego activado con temperatura alta. Considere neutralizar o disminuir la temperatura en la Zona ~w.~n', [Z]).

recomendacion(Z) :-
    format('Sin recomendaciones especiales para el riego en la Zona ~w.~n', [Z]).


%Mensaje de alerta si se activa el riego con calor extremo
estatus_humedad(Z) :-
    humedad_suelo(Z, baja),
    tipo_zona(Z, exterior),
    format('Riego necesario en la Zona ~w.~n', [Z]).

estatus_humedad(Z) :-
    humedad_suelo(Z, baja),
    tipo_zona(Z, interior),
    format('Revisión recomendada en la Zona ~w.~n', [Z]).

estatus_humedad(Z) :-
    (humedad_suelo(Z, media) ;
    humedad_suelo(Z, alta)),
    format('Riego no necesario en la Zona ~w.~n', [Z]).
