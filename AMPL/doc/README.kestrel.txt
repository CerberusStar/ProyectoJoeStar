Kestrel client for AMPL modeling environment

A complete user's guide to Kestrel is available at
http://neos.mcs.anl.gov/neos/kestrel.html

USAGE
-----
Design your model as you normally would.  When choosing options, everything
should remain as usual with the following exceptions:

 - Choose
      ampl: option solver kestrel;
   instead of usual solver name.

 - Choose the solver you wish to use with
      ampl: option kestrel_options "solver=<solver_name>";
           (Do not actually type in '<' or '>')

   If you do not know what solvers are available via Kestrel, submitting a job
   (see below) without setting kestrel_options will return a list of
   possible solvers.

 - When kestrel_options is set, submit the job to NEOS by typing
      ampl: solve;

 - If you are somehow disconnected from the Kestrel server during your
   job execution, the job will still be running on a remote machine.
   To retrieve the results in this case:
      ampl: option kestrel_options "job=<job#> password=<password>";
      ampl: solve;
   Jobs may removed from the NEOS server after some length of time
   (no sooner than two days), so you may not be able to retrieve your
   job this way after that time.  To resume normal Kestrel solver operations
   type:
      ampl: option kestrel_options "solver=<solver_name>";
