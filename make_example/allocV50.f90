subroutine alloc
  use fluxes
  use rest, only: inmax, jnmax, icmax, jcmax
  
  implicit none
  integer :: status
  !------------------------------------------------------------------------
  !
  !     *** allocate node, x, y ***
  !
  allocate(x(inmax * jnmax), stat = status)
  if (status /= 0) stop 'failure to allocate x fluxes in alloc'
  allocate(y(inmax * jnmax), stat = status)
  if (status /= 0) stop 'failure to allocate y fluxes in alloc'
  !
  allocate(node(-1:icmax+2, -1:jcmax+2, 4), stat = status)
  if (status /= 0) stop 'failure to allocate node in alloc'
  allocate(a(icmax, jcmax), stat = status)
  if (status /= 0) stop 'failure to allocate area a in alloc'
  !
  allocate(u(-1:icmax+2,-1:jcmax+2,4), stat = status)
  if (status /= 0) stop 'failure to allocate u in alloc'
  !
  allocate(uold(-1:icmax+2,-1:jcmax+2,4), stat = status)
  if (status /= 0) stop 'failure to allocate uold in alloc'

  allocate(pv(-1:icmax+2,-1:jcmax+2), stat = status)
  if (status /= 0) stop 'failure to allocate pv in alloc'

  allocate(uv(-1:icmax+2,-1:jcmax+2), stat = status)
  if (status /= 0) stop 'failure to allocate uv in alloc'

  allocate(vv(-1:icmax+2,-1:jcmax+2), stat = status)
  if (status /= 0) stop 'failure to allocate vv in alloc'

  allocate(cv(-1:icmax+2,-1:jcmax+2), stat = status)
  if (status /= 0) stop 'failure to allocate cv in alloc'

  allocate(Ma(-1:icmax+2,-1:jcmax+2), stat = status)
  if (status /= 0) stop 'failure to allocate Ma in alloc'
  !
  !     *** allocate fluxes ***
  !
  allocate(f(-1:icmax+2, -1:jcmax+2, 4), stat = status)
  if (status /= 0) stop 'failure to allocate f fluxes in alloc'
  allocate(g(-1:icmax+2, -1:jcmax+2, 4), stat = status)
  if (status /= 0) stop 'failure to allocate g fluxes in alloc'
  !
  allocate(r(icmax, jcmax, 4), stat = status)
  if (status /= 0) stop 'failure to allocate r in alloc'
  !
  return
end subroutine alloc
