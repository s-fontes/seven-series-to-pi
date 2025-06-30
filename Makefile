CC = gcc
CFLAGS = -O2 -fPIC -std=c99
LDFLAGS = -shared
EPS ?= 1e-5
BUILD_DIR = build
OUT_DIR = out
SRCS := csrc/util.c csrc/leibniz.c csrc/nilakantha.c csrc/machin.c csrc/euler.c csrc/ramanujan.c csrc/chudnovsky.c csrc/bbp.c csrc/pi_series.c
OBJS := $(SRCS:.c=.o)
LIB = $(BUILD_DIR)/libpi_series.so

.PHONY: build run analysis test test-unit test-all test-coverage test-performance lint verify clean clean-out distclean

build: $(LIB)

$(LIB): $(OBJS)
	mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) $(OBJS) -o $@ $(LDFLAGS) -lm

csrc/%.o: csrc/%.c csrc/%.h csrc/pi_series.h
	$(CC) $(CFLAGS) -c $< -o $@

run: build
	python3 py/compute.py $(EPS)

analysis: run
	python3 py/convergence_analysis.py $(EPS)
test: test-unit

test-unit: build
	pytest py/tests/ -v -m "not slow"

test-all: build
	pytest py/tests/ -v

test-coverage: build
	pytest py/tests/ --cov=py --cov-report=html --cov-report=term

test-performance: build
	pytest py/tests/test_performance.py -v -s

lint:
	clang-format -i csrc/*.c csrc/*.h
	ruff check py --fix

verify: lint test

clean:
	        rm -rf $(BUILD_DIR)
	        find csrc -name '*.o' -delete

clean-out:
	        rm -rf $(OUT_DIR)

distclean: clean clean-out
