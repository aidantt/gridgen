subroutine output
  !
  use rest,   only: messages
  implicit none
  !----------------------------------------------------------------------
  if (messages) write(*,*) 'calling output'
  !
  !  restart file
  !
  return
end subroutine output

