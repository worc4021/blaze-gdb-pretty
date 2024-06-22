#include <cstdio>
#include "blaze/Math.h"

/* Note: The "MS" section flags are to remove duplicates.  */
#define DEFINE_GDB_PY_SCRIPT(script_name) \
  asm("\
.pushsection \".debug_gdb_scripts\", \"MS\",@progbits,1\n\
.byte 1 /* Python */\n\
.asciz \"" script_name "\"\n\
.popsection \n\
");

DEFINE_GDB_PY_SCRIPT("blazepretty.py")

using mat = blaze::DynamicMatrix<double>;
using vec = blaze::DynamicVector<double>;


int main() {
    vec a{1., 2., 3.};
    mat C{{7.,8.,9.},{10.,11.,12.}};

    vec x = C*a;
    return 0;
}
