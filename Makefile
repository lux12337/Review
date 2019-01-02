out: main.o datalgo.o
	g++ -std=c++0x -Wall main.o datalgo.o -o out

main.o: main.cpp
	g++ -c main.cpp

datalgo.o: datalgo.cpp datalgo.hpp
	g++ -c datalgo.cpp

clean:
	rm *.o output
