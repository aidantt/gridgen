subroutine initia
  !
  use gasprop,  only: gamma, gammam1
  use flowprop, only: mach, alpha, pratio, ptinf, pexit, rinf, uinf, vinf, &
       qinf, epsinf, cinf, pinf, htinf
  use fluxes,   only: u, uold, pv, uv, vv, cv, Ma
  use rest,     only: icmax, jcmax, messages

  implicit none
  !
  !-----------------------------------------------------------------------
  if (messages) write(*,*) 'calling initia'
  !
  ! *** values at infinity upstream, nondimensionalized as in L5.3 *** 
  !
  !
  return
end subroutine initia
