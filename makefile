
include userconfig.mk

PACKET=bin/$(NAME).sh
MAIN=src/$(NAME).py
DISTNAME=$(NAME)_dist.tgz
SRCS=$(wildcard src/*.py)
OBJS=$(SRCS:.py=.notabs)

$(PACKET): $(MAIN)
	@mkdir -p bin/
	npyck $(MAIN) $(SRCS) $(INCLUDE) -o $(PACKET)

all: $(PACKET)

.PHONY: clean git-clean run packet expand dist

git-clean: clean
#	rm -f *~ */*~
	@find . -name \*~
	find . -name \*~ -exec rm "{}" ";"
	@find . -name \*.pyc
	find . -name \*.pyc -exec rm "{}" ";"

%.notabs : %.py
	expand --tabs=4 $< > $@
	cp $@ $<

expand: $(OBJS)

clean:
	rm -fr ./bin/
	rm -f ./src/*.pyc ./src/*.notabs
	rm -f $(DISTNAME)

run:
	python $(MAIN) $(ARGS)

packet: $(PACKET)
	sh $(PACKET)

dist: $(PACKET)
	tar cz  --directory=bin/ $(NAME).sh >$(DISTNAME)
