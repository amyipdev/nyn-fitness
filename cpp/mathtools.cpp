// SPDX-License-Identifier: AGPL-3.0-or-later
//
// nyn-fitness: the dynamic recommendation fitness app
// Copyright (C) 2023 Amy Parker <amy@amyip.net>
//   				  Kevin Ramirez <thekevinramirez@csu.fullerton.edu>
//   				  Nicholas Goulart <nick.goulart@csu.fullerton.edu>
//   				  Theresa Nguyen <ttnguyen1011@csu.fullerton.edu>
//   				  Dat Lam <Dlam42@csu.fullerton.edu>
//   				  Srinidhi Chevvuri <srinidhi.chevvuri@csu.fullerton.edu>
//
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU Affero General Public License as published by
// the Free Software Foundation; either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// See the GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA or visit the
// GNU Project at https://gnu.org/licenses. The GNU Affero General Public
// License version 3 is available at, for your convenience,
// https://www.gnu.org/licenses/agpl-3.0.en.html.

#include "mathtools.h"
#include <cmath>
#include "common.h"

// All functions in this file should be able to compile
// to the highest SIMD (SSE2-AVX512) available on the
// platform.

f64 dotProduct(f64 v1[], f64 v2[], u64 len) {
    f64 ax = 0;
    for (u64 i = 0; i < len; ++i) {
        ax += v1[i] * v2[i];
    }
    return ax;
}

f64 vectorMagnitude(f64 v[], u64 len) {
    f64 magsq = 0;
    for (u64 i = 0; i < len; ++i) {
        f64 stack = v[i];
        magsq += stack*stack;
    }
    return std::sqrt(magsq);
}

void makeVectorUnitInPlace(f64 v[], u64 len) {
    f64 mag = vectorMagnitude(v, len);
    // if |v| = 0, v = vec(0), score will be 0
    // no division will affect it, but we are
    // going to accidentally DBZ, causing segv
    // to fix this, we just don't touch it if
    // it's zero, because it doesn't matter
    if (mag == 0) [[unlikely]]
        return;
    for (u64 i = 0; i < len; ++i) {
        v[i] /= mag;  
    }
}