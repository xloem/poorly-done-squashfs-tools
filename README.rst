
##########################
poorly done squashfs-tools
##########################


poorly done squashfs-tools
--------------------------
| Package builds squashfs-tools as a python c extension and provides for calling the tools as functions.
| The arguments to the functions are passed directly to the tools.
| Due to use of static variables, only the first call works. Further calls crash.
| This could be resolved by using CFFI and reloading the .so, by appropriately
| rewriting the top-level functionality of the tools, or by integrating a python
| interface or library into the codebase upstream.
