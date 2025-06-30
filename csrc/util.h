#ifndef UTIL_H
#define UTIL_H

#include <math.h>
#include <stdio.h>

#include "pi_series.h"

#define MAX_ITER 100000

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    float pi_value;
    int iterations;
    float final_error;
} pi_result_float_t;

typedef struct {
    double pi_value;
    int iterations;
    double final_error;
} pi_result_double_t;

double calculate_error_double(double pi);
float calculate_error_float(float pi);
double erro2(double pi);

#ifdef __cplusplus
}
#endif

#endif  // UTIL_H
