CC := gcc
CXX := g++

LIBS += $(shell pkg-config --cflags --libs python3)
CFLAGS += -Wall -Werror -O3 -fPIC -march=native

CXXSRCS=$(wildcard *.cpp)

all: $(CXXSRCS)
	g++ -shared -o nyn_recommender.so $^ $(CFLAGS) $(LIBS)
	
clean:
	rm -f *.o *.so