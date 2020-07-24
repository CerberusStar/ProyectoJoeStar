The AMPL processor and solvers in this directory will operate without
restriction when used with a suitable license.  The license (file
ampl.lic) that is initially provided with this directory is a
"demonstration" license that restrict problem sizes (e.g., to 300
variables and 300 general constraints and objectives for nonlinear
problems and to 500 and 500 for lineear problems, or to 10 and 10 for
global solvers).  This "demo" license is intended for noncommercial
use.  For serious commercial use, you should (eventually) buy a
suitable academic or commercial license, even if your applications
never exceed the limits of the "demo" license.

See the AMPL web site

	http://www.ampl.com

for extensive information about AMPL, including descriptions of
extensions available in current versions and pointers to information
about other solvers.

File ampl.exe is the AMPL processor.  By default, it obtains table
handlers from ampltabl.dll.  For more details, see
http://ampl.com/resources/database-and-spreadsheet-table-handlers/ .

File baron.exe is the AMPL/BARON solver for global optimization of
nonconvex problems.  Currently it does not allow use of trigonometric
functions, but this restriction should eventually be lifted when the
underlying BARON software is suitably updated.  For more details, see
file doc\README.baron.txt.

File conopt.exe is the AMPL/CONOPT solver for nonlinear problems
involving continuous variables.  See file doc\README.conopt.txt for more
details.

File cplex.exe is the AMPL/CPLEX solver for linear or quadratic
objectives and constraints involving continuous or integer variables.
See file doc\README.cplex.txt for more details.

File gjh.exe is a "solver" that computes gradients, Jacobian matrices
and Hessians of nonlinear problems and makes them available to AMPL as
parameters.

File gurobi.exe is the AMPL/Gurobi solver for linear or quadratic
objectives and constraints involving continuous or integer variables.
See file doc\README.gurobi.txt for more details.

File ilogcp.exe is a constraint-programming solver based on the
CP Optimizer in IBM's ILOG CPLEX Studio.  See file doc\README.ilogcp.txt
for more details.

File knitro.exe is the AMPL/KNITRO solver for linear or nonlinear
objectives and constraints involving continuous or integer variables.
It does not work with a "demo" license.  See file doc\README.knitro.txt
for more details.

File lgo.exe is the AMPL/LGO solver for global optimization of
nonconvex functions.  It only uses function values.  See file
doc\README.lgo.txt for more details.

File locsol.exe is the AMPL/LocalSolver for finding "good" local
solutions to difficult integer and/or nonlinear programming problems.
Currently it lacks support for some trigonometric functions.  See
doc\README.locsol.exe for more details.

File minos.exe is the AMPL/MINOS solver for linear or nonlinear
objectives and constraints involving continuous variables.  See file
doc\README.minos.txt for more details.

File modinc is an AMPL include command for easy access to the models
and models/nlmodels subdirectories.  The models directory contains
examples from the AMPL book and and various papers on AMPL, and the
models/nlmodels subdirectory contains some nonlinear models
assembled by Elena Bobrovnikova.  For example, rather than giving
the AMPL statements
	model models/oil.mod;
	data models/oil.dat;
after "include modinc" you could equivalently use the simpler
statements
	model oil.mod;
	dat oil.dat;

File snopt.exe is the AMPL/SNOPT solver for linear or nonlinear
objectives and constraints involving continuous variables.  See file
doc\README.snopt.txt for more details.

File xpress.exe is the AMPL/XPRESS solver for linear or quadratic
objectives and constraints involving continuous or integer variables.
See file doc\README.xpress.txt for more details.
