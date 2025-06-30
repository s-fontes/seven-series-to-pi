#ifndef LEIBNIZ_H
#define LEIBNIZ_H

#ifdef __cplusplus
extern "C" {
#endif

#include "pi_series.h"

PiResult* run_leibniz_f(float eps, unsigned long* len);
PiResult* run_leibniz_d(double eps, unsigned long* len);

#ifdef __cplusplus
}
#endif

#endif  // LEIBNIZ_H
