module flowprop
  implicit none
  save
  integer, PARAMETER :: DBLP = 8
  real(DBLP) :: mach  ! Mach number @ inf
  real(DBLP) :: alpha ! incidence @ inf
  real(DBLP) :: tinf  ! static temperature @ inf
  real(DBLP) :: pratio! ratio of exit static pressure by inlet stagnation pres.
  real(DBLP) :: ptinf ! stagnation pressure @ inf
  !
  real(DBLP) :: pexit
  !
  real(DBLP) :: rinf  ! density @ inf
  real(DBLP) :: uinf  ! x-velocity @ inf
  real(DBLP) :: vinf  ! y-velocity @ inf
  real(DBLP) :: qinf  ! velocity @ inf
  real(DBLP) :: epsinf! rhoE_inf
  real(DBLP) :: cinf  ! speed of sound @ inf
  real(DBLP) :: pinf  ! pressure @ inf
  real(DBLP) :: htinf ! stagnation enthalpy @ inf
end module flowprop
