#include "util.h"

#include <math.h>
#include <stdlib.h>

float calculate_error_float(float pi) { return (pi - (float)M_PI) * (pi - (float)M_PI); }

double calculate_error_double(double pi) { return (pi - M_PI) * (pi - M_PI); }

double erro2(double pi) { return (pi - M_PI) * (pi - M_PI); }
