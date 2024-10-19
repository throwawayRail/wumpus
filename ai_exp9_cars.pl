% Define cars
car(ferrari).
car(jaguar).
car(bmw) .
car(mercedes) .
car(tesla_model_s).

% Define car features
feature(ferrari, speed).
feature(jaguar, luxury) .
feature(bmw, technology) .
feature(mercedes, comfort).
feature(tesla_model_s, efficiency).

% Define car preferences
preference(speed, pravin).
preference(luxury, nilam) .
preference(technology, chirag).
preference(comfort, manasi).
preference(efficiency, abhishek).
% Define a rule for finding a person's preferred car
preferred_car(Person, Car) :-
 preference(Feature, Person), % Get the person's preferred feature
 feature(Car, Feature). % Find a car that has that feature
