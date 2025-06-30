#ifndef PI_SERIES_H
#define PI_SERIES_H

#include <stdio.h>
#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

typedef struct {
    unsigned long k;
    double pi;
} PiResult;

typedef PiResult* (*series_func_f)(float, unsigned long*);
typedef PiResult* (*series_func_d)(double, unsigned long*);

series_func_f resolve_series_f(const char* name);
series_func_d resolve_series_d(const char* name);

void free_results(PiResult* ptr);


#ifdef __cplusplus
}
#endif

#endif  // PI_SERIES_H
