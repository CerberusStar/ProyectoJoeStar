# This script writes the solution to the current problem to the file
# __sol_filename and row and column names to the files with the same
# basename and extensions '.row' and '.col' respectively. The solution
# file has extra data but is compatible with AMPL meaning that it can
# be loaded with the solution command.

param __col_filename symbolic =
    substr(__sol_filename, 0, length(__sol_filename) - 3) & 'col';
param __row_filename symbolic =
    substr(__sol_filename, 0, length(__sol_filename) - 3) & 'row';

print 'objective', _obj[1] > (__sol_filename);
print >> (__sol_filename);
print 'Options' >> (__sol_filename);
print 3 >> (__sol_filename);
print 10 >> (__sol_filename);
print 1 >> (__sol_filename);
print 0 >> (__sol_filename);

param __temp;

let __temp := sum {i in 1.._ncons: _con[i].astatus == 'in'} 1;
print __temp >> (__sol_filename);
print __temp >> (__sol_filename);

let __temp := sum {i in 1.._nvars: _var[i].astatus == 'in'} 1;
print __temp >> (__sol_filename);
print __temp >> (__sol_filename);

printf '' > (__row_filename);
for {i in 1.._ncons: _con[i].astatus == 'in'} {
    print _con[i], _con[i].body, _con[i].slack >> (__sol_filename);
    print _conname[i] >> (__row_filename);
}
print _objname[1] >> (__row_filename);
close (__row_filename);

printf '' > (__col_filename);
for {i in 1.._nvars: _var[i].astatus == 'in'} {
    print _var[i], _var[i].rc, _var[i].slack >> (__sol_filename);
    print _varname[i] >> (__col_filename);
}
close (__col_filename);

print 'objno 0', solve_result_num >> (__sol_filename);

close (__sol_filename);
