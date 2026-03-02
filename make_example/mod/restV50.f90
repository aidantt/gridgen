module rest
  implicit none
  save
  integer :: inmax ! max number of grid points in x direction
  integer :: jnmax ! max number of grid points in y direction
  integer :: nle   ! grid node number at leading edge
  integer :: nte   ! grid node number at trailing edge
  integer :: icmax != inmax - 1 ! max number of cells in x dir
  integer :: jcmax != jnmax - 1 ! max number of cells in y dir

  integer :: nstep_s ! total number of iterations
  real(8) :: err(4)  ! averaged state variable error between time n and n+1
  logical :: messages
  logical :: debug
  logical :: interactive
  character(80) :: case_name, grid_name
  character(10) :: run_type ! new or restart
  logical :: riemannvar     ! flag for printing Riemann variables
  real(8) :: resallmax      ! geometric mean of max residual
  integer :: ioutbc         ! 1 for Riemann bcs, 2 for zero gradient
  real(8) :: epscon         ! criterion for convergence
  real(8) :: cfl            ! CFL number
  real(8) :: nu2    ! dissipation coefficient
  real(8) :: nu4    ! dissipation coefficient
  integer :: maxiter        ! Number maxim of iterations
  integer :: iterwr         ! Number of iterations b/w writing results
  integer :: itermovie      ! Number of iterations b/w saving snapshots for movie
  logical :: movie          ! if .true. saves snapshots for movies
end module rest

! icmax - max number of cells in i-direction
! jcmax - max number of cells in j-direction
! inmax - max number of nodes in i-direction
! jnmax - max number of nodes in j-direction	 

