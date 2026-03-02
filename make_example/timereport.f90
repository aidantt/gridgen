subroutine timereport(res_io)

  ! report CPU time and CPU per real time simulated

  ! pgc - 4.8g - 02/21/12 - first version

  implicit none
  ! input
  integer, intent(in) :: res_io    ! file number
  ! local
  real(4) :: tarray(2)             ! elapsed user and system time 
  real(4) :: etime                 ! U77 time function
  real(8) :: total
  ! --------------------------------------------------------------------
  total = dble(etime(tarray))
  write(*     ,*) 'Elapsed user time: ', tarray(1), 'seconds'
  write(*     ,*) 'Elapsed user + system time: ', total, 'seconds'
  write(res_io,*) 'Elapsed user time: ', tarray(1), 'seconds'
  write(res_io,'(A,F10.1,A,F10.2,A)') 'Elapsed user + system time: ', &
       total, 'seconds or', total/3600.0d0,' hours'

  return
end subroutine timereport
