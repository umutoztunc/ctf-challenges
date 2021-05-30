# ELVM is needed to compile this.
# https://github.com/umutoztunc/elvm
ELC := $(ELVM)/out/elc
CC := $(ELVM)/out/8cc
CFLAGS := -S -I$(ELVM)/libc

SRC_DIR := src
BUILD_DIR := build
RELEASE_DIR := release

$(RELEASE_DIR)/spaceship.ws: $(BUILD_DIR)/spaceship.eir
	mkdir -p $(dir $@)
	$(ELC) -ws $< > $@

$(BUILD_DIR)/spaceship.eir: $(SRC_DIR)/spaceship.c $(SRC_DIR)/spaceship.h
	mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -o $@ $<

$(SRC_DIR)/spaceship.h:
	python3 generate_conditions.py

.PHONY: clean
clean:
	$(RM) -r $(BUILD_DIR) $(RELEASE_DIR)
