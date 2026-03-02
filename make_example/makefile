# #GFORTRAN OS X ###
# FC = gfortran
# FFLAGS = -m64 -fdefault-real-8
# #FFLAGS = -m64 -O3 -fdefault-real-8 -fbounds-check
# TARGET_ARCH =
# LDFLAGS = -m64
# LIBS = 

# # FC      = f90 
# # FFLAGS  = -YEXT_NAMES=LCS -s -YEXT_SFX=_
# # LDFLAGS  = 
# # LIBS    = /usr/lib/libgrafic.a -L/usr/X11R6/lib -lX11 $(ABSOFT)/lib/libU77.a 
##################
# Absoft OS X Mac Intel
FC      = f95
FFLAGS  = -m64 -O3 -N113
#FFLAGS  = -m64 -g -N113 -Rb -Rc #-TENV:simd_imask=off -TENV:simd_zmask=off #-TENV:simd_dmask=off #-Rb -Rc #-Rs -Rp -s -safefp
LDFLAGS = -m64 -O3
#LDFLAGS = -m64 -g
TARGET_ARCH =
LIBS = -lU77
##################
EXE   = euler
VPATH = mod

.SUFFIXES:      
.SUFFIXES: .f90 .o

GRAFIC_HEADER =

SRCMOD =                \
	constants.f90	\
	flowprop.f90	\
	fluxes.f90	\
	gasprop.f90     \
	restV50.f90

SRCMAIN =      			\
	allocV50.f90      	\
	controlV50.f90   	\
	initiaV50.f90    	\
	mainV50.f90      	\
	outputV50.f90    	\
	strtupV50.f90   	\
	timereport.f90   	\

OBJMAIN = ${SRCMAIN:.f90=.o}

OBJMOD = ${SRCMOD:.f90=.o}

OBJ = $(OBJMOD) $(OBJMAIN)

$(EXE): $(OBJ)
	$(FC) $(LDFLAGS) $(OBJ) $(LIBS) -o $(EXE)

%.o  : %.f90 
	$(FC) $(FFLAGS) -c $<

# Define dependencies for modules
$(OBJMAIN): $(OBJMOD)



