from MDF.discretizacoes.crank_nicolson_dirichlet import CrankNicolsonDirichlet
from MDF.discretizacoes.crank_nicolson_von_neumann import CrankNicolsonVonNeumann
from MDF.discretizacoes.explicito_dirichlet import ExplicitoDirichlet
from MDF.discretizacoes.implicito_dirichlet import ImplicitoDirichlet
from MDF.discretizacoes.implicito_von_neumann import ImplicitoVonNeumann

L0 = 0
Ln = 3
T = 1
nx = 100
nt = 2200
a = 1

# exp_dir = ExplicitoDirichlet(L0, Ln, T, nx, nt, a)
# imp_dir = ImplicitoDirichlet(L0, Ln, T, nx, nt, a)
# crn_dir = CrankNicolsonDirichlet(L0, Ln, T, nx, nt, a)
# imp_neu = ImplicitoVonNeumann(L0, Ln, T, nx, nt, a)
# crn_neu = CrankNicolsonVonNeumann(L0, Ln, T, nx, nt, a)

# exp_dir.plota_2D(6)
# exp_dir.plota_3D()

# imp_dir.plota_2D(6)
# imp_dir.plota_3D()

# crn_dir.plota_2D(6)
# crn_dir.plota_3D()

# imp_neu.plota_2D(6)
# imp_neu.plota_3D()

# crn_neu.plota_2D(6)
# crn_neu.plota_3D()