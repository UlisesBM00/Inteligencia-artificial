% -------------------------------
% Base de conocimientos
% -------------------------------

% juego(Nombre, MinJugadores, MaxJugadores, Duracion, Complejidad, Tematica).

juego(jaipur, 2, 2, corta, media, estrategia).
juego(pandemic, 2, 4, media, media, cooperativo).
juego(king_of_tokyo, 2, 6, media, baja, azar).
juego(ticket_to_ride, 2, 5, media, media, estrategia).
juego(scythe, 1, 5, larga, alta, estrategia).
juego(catan, 3, 4, media, media, familiar).
juego(seven_wonders_duel, 2, 2, media, media, estrategia).
juego(uno, 2, 10, corta, baja, azar).
juego(dixit, 3, 6, corta, baja, social).
juego(love_letter, 2, 4, corta, baja, azar).
juego(coup, 3, 6, media, media, bluff).
juego(mage_knight, 1, 1, larga, alta, estrategia).
juego(just_one, 4, 7, corta, baja, social).
juego(exploding_kittens, 3, 5, corta, baja, humor).
juego(mysterium, 2, 7, media, media, deduccion).
juego(avalon, 5, 10, media, media, traicion).
juego(terraforming_mars, 1, 5, larga, alta, ciencia_ficcion).
juego(dobble, 2, 8, corta, baja, familiar).
juego(star_realms, 2, 2, media, media, confrontacion).
juego(gloomhaven, 1, 4, larga, alta, fantasia).
juego(clue, 3, 6, corta, baja, misterio).
juego(splendor, 2, 4, media, media, economia).
juego(viral, 2, 5, media, media, virus).
juego(lost_cities, 2, 2, corta, baja, cartas).
juego(timeline, 2, 6, media, baja, historia).

% -------------------------------
% Regla de recomendación
% -------------------------------

% recomendar(Jugadores, Duracion, Complejidad, Tematica, JuegoRecomendado).
recomendar(Jugadores, Duracion, Complejidad, Tematica, Juego) :-
    juego(Juego, Min, Max, Duracion, Complejidad, Tematica),
    Jugadores >= Min,
    Jugadores =< Max.

% -------------------------------
% Interfaz interactiva
% -------------------------------

menu :-
    writeln('=========================================='),
    writeln('      Sistema Experto: Juegos de Mesa'),
    writeln('=========================================='),
    writeln('Ingresa los siguientes datos:'),
    
    write('Numero de jugadores: '), read(Jugadores),
    write('Duracion (corta, media, larga): '), read(Duracion),
    write('Complejidad (baja, media, alta): '), read(Complejidad),
    write('Tematica (estrategia, cooperativo, azar, familiar, social, bluff, deduccion, traicion, ciencia_ficcion, humor, fantasia, misterio, economia, virus, cartas, historia, confrontacion): '), read(Tematica),

    findall(Juego, recomendar(Jugadores, Duracion, Complejidad, Tematica, Juego), Lista),
    mostrar_resultados(Lista).

mostrar_resultados([]) :-
    writeln('No se encontraron juegos con esas características.').

mostrar_resultados([H|T]) :-
    writeln('Juegos recomendados:'),
    mostrar_lista([H|T]).

mostrar_lista([]).
mostrar_lista([H|T]) :-
    write('- '), writeln(H),
    mostrar_lista(T).
