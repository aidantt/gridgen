module GASPROP
  implicit none
  save
  integer, PARAMETER :: DBLP = 8
  real(DBLP), PARAMETER  :: GAMMA = 1.4D0
  real(DBLP), PARAMETER  :: GAMMAM1 = GAMMA - 1.0D0
  real(DBLP), PARAMETER  :: ONEBYGAMMA = 1.0D0 / GAMMA
  real(DBLP), PARAMETER  :: ONEBYGAMMAM1 = 1.0D0 / GAMMAM1
end module GASPROP
