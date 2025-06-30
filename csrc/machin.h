#ifndef MACHIN_H
#define MACHIN_H

#ifdef __cplusplus
extern "C" {
#endif

#include "pi_series.h"

PiResult* run_machin_f(float eps, unsigned long* len);
PiResult* run_machin_d(double eps, unsigned long* len);

#ifdef __cplusplus
}
#endif

#endif  // MACHIN_H
