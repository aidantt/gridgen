subroutine control
  !
  !     *** controls iterations ***
  !
  use constants, only: dblp
  use fluxes,    only: x, y, a, f, g, r, u, uold
  use gasprop,   only: gamma, gammam1
  use rest,      only: icmax, jcmax, inmax, jnmax, nstep_s, debug, case_name, &
       riemannvar, messages, epscon, cfl, nu2, nu4, maxiter, iterwr, itermovie, &
       movie

  implicit none
  !
  ! local
  integer io, iter
  real(dblp) :: obya, dt
  real(dblp) :: d(icmax,jcmax,4) ! damping terms
  logical :: convrgd
  !
  integer ic, jc, i, nstages
  real(dblp) :: c(4)
  data c/ 0.25d0, 0.33333333333333333d0, 0.5d0, 1.d0/
  character peno*3
  !----------------------------------------------------------------------
  if (messages) write(*,*) 'calling control'
  !
  !
  return
end subroutine control
