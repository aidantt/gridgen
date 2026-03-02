module fluxes
  implicit none
  save
  real(8), allocatable :: x(:), y(:)  ! x, y grid coordinates
  real(8), allocatable :: a(:,:)      ! cell area
  integer, allocatable :: node(:,:,:) ! pointer from cell to node
  real(8), allocatable :: f(:,:,:)    ! f fluxes at cell center
  real(8), allocatable :: g(:,:,:)    ! g fluxes at cell center
  real(8), allocatable :: r(:,:,:)    ! residual
  real(8), allocatable :: xghost(:,:) ! x grid that includes ghost cells nodes
  real(8), allocatable :: yghost(:,:) ! y grid that includes ghost cells nodes
  real(8), allocatable :: u(:,:,:)    ! state vector at cell center
  real(8), allocatable :: uold(:,:,:) ! state vector at cell center, old
  real(8), allocatable :: pv(:,:)     ! pressure at cell center
  real(8), allocatable :: uv(:,:)     ! u velocity at cell center
  real(8), allocatable :: vv(:,:)     ! v velocity at cell center
  real(8), allocatable :: cv(:,:)     ! speed of sound at cell center
  real(8), allocatable :: Ma(:,:)     ! Mach number at cell center
end module fluxes
