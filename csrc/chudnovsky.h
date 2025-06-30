#ifndef CHUDNOVSKY_H
#define CHUDNOVSKY_H

#ifdef __cplusplus
extern "C" {
#endif

#include "pi_series.h"

PiResult* run_chudnovsky_f(float eps, unsigned long* len);
PiResult* run_chudnovsky_d(double eps, unsigned long* len);

#ifdef __cplusplus
}
#endif

#endif  // CHUDNOVSKY_H
