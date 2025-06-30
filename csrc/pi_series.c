#include "pi_series.h"

#include <math.h>
#include <stdlib.h>
#include <string.h>

#include "bbp.h"
#include "chudnovsky.h"
#include "euler.h"
#include "leibniz.h"
#include "machin.h"
#include "nilakantha.h"
#include "ramanujan.h"

series_func_f resolve_series_f(const char* name) {
    if (strcmp(name, "leibniz") == 0) return run_leibniz_f;
    if (strcmp(name, "nilakantha") == 0) return run_nilakantha_f;
    if (strcmp(name, "machin") == 0) return run_machin_f;
    if (strcmp(name, "euler") == 0) return run_euler_f;
    if (strcmp(name, "ramanujan") == 0) return run_ramanujan_f;
    if (strcmp(name, "chudnovsky") == 0) return run_chudnovsky_f;
    if (strcmp(name, "bbp") == 0) return run_bbp_f;
    return NULL;
}

series_func_d resolve_series_d(const char* name) {
    if (strcmp(name, "leibniz") == 0) return run_leibniz_d;
    if (strcmp(name, "nilakantha") == 0) return run_nilakantha_d;
    if (strcmp(name, "machin") == 0) return run_machin_d;
    if (strcmp(name, "euler") == 0) return run_euler_d;
    if (strcmp(name, "ramanujan") == 0) return run_ramanujan_d;
    if (strcmp(name, "chudnovsky") == 0) return run_chudnovsky_d;
    if (strcmp(name, "bbp") == 0) return run_bbp_d;
    return NULL;
}

void free_results(PiResult* ptr) { free(ptr); }
