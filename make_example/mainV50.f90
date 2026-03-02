program euler
  !
  !     2D Euler Solver
  !     Jameson's scheme
  !      
  implicit none
  !
  real(4) :: total              ! time 
  real(4) :: tarray(2)          ! elapsed user and system time 
  real(4) :: etime              ! U77 time function
  !
  !----------------------------------------------------------------------
  total = etime(tarray); if (.false.) print *, total, 'for forchk'
  call strtup
  call initia
  call control
  call output

  ! CPU time
  call timereport(2) ! write CPU time to file w/ io=2

end program euler
