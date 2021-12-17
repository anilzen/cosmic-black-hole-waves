# Black hole waves in Schwarzschild-de Sitter spacetime
A simple Python solver for scalar waves in a cosmological spacetime with a black hole.

The code uses horizon-penetrating hyperboloidal coordinates in the static patch of Schwarzschild-de Sitter (SdS) spacetime. The coordinates have two advantages:
- No boundary conditions need to be applied;
- Radiation leaves the numerical domain smoothly through the boundaries.

## Hyperboloidal coordinates in spherical symmetry
We can write any spherically symmetric metric as
<!-- $$
ds^2 = - f dt^2 + \frac{1}{f} dr^2 + r^2 d\omega^2.
$$ --> 
<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=ds%5E2%20%3D%20-%20f%20dt%5E2%20%2B%20%5Cfrac%7B1%7D%7Bf%7D%20dr%5E2%20%2B%20r%5E2%20d%5Comega%5E2."></div>
Introduce hyperboloidal time
<!-- $$ 
\tau = t - h(r)$$, \qquad H(r):= \frac{dh}{dr}.
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=%5Ctau%20%3D%20t%20-%20h(r)%24%24%2C%20%5Cqquad%20H(r)%3A%3D%20%5Cfrac%7Bdh%7D%7Bdr%7D."></div>
to get the metric
<!-- $$ 
ds^2 = - f d\tau^2 - 2 fH d\tau dr + \frac{1}{f}\left(1-f^2 H^2\right) dr^2 + r^2 d\omega^2.
$$ --> 
<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=ds%5E2%20%3D%20-%20f%20d%5Ctau%5E2%20-%202%20fH%20d%5Ctau%20dr%20%2B%20%5Cfrac%7B1%7D%7Bf%7D%5Cleft(1-f%5E2%20H%5E2%5Cright)%20dr%5E2%20%2B%20r%5E2%20d%5Comega%5E2."></div>

<!-- ## Horizion-penetrating hyperboloidal coordinates in SdS
In SdS, the metric is singular at three roots. We express 
\be\label{eq:f} f = \frac{1}{\ell^2 r} (r-r_e)(r_c-r)(r-r_0). \ee
The metric is singular at the roots of $f$. To remove the singularity, the boost function is chosen such that
\be\label{eq:fH} f H = 2 \frac{r-r_e}{r_c-r_e} - 1.\ee
We get the metric
\[ ds^2 = - f dt^2 - 2 \left(2 \frac{r-r_e}{r_c-r_e} - 1\right) d\tau dr + \frac{4 \ell^2 r}{(r_c-r_e)^2 (r-r_0)} dr^2 + r^2 d\omega^2. \]
This metric has two nice properties: (i) regular everywhere; (ii) outgoing with respect to both horizons $r_e$ and $r_c$. -->

## Scalar wave equation
The scalar wave equation reads
<!-- $$
\partial_{{t}}^{\,2}\psi  = f^2 \partial_r^2 \psi + f \left(\frac{2f}{r}+f'\right) \partial_r \psi - \frac{f k^2}{r^2}.
$$ --> 
<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cpartial_%7B%7Bt%7D%7D%5E%7B%5C%2C2%7D%5Cpsi%20%20%3D%20f%5E2%20%5Cpartial_r%5E2%20%5Cpsi%20%2B%20f%20%5Cleft(%5Cfrac%7B2f%7D%7Br%7D%2Bf'%5Cright)%20%5Cpartial_r%20%5Cpsi%20-%20%5Cfrac%7Bf%20k%5E2%7D%7Br%5E2%7D."></div>
We use a variable rescaled with radius to get
<!-- $$ 
\partial_{{t}}^{\,2}u  = f^2 \partial_r^2 u + f f' \partial_r \psi - \frac{f}{r^2} (r f' + k^2).
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cpartial_%7B%7Bt%7D%7D%5E%7B%5C%2C2%7Du%20%20%3D%20f%5E2%20%5Cpartial_r%5E2%20u%20%2B%20f%20f'%20%5Cpartial_r%20%5Cpsi%20-%20%5Cfrac%7Bf%7D%7Br%5E2%7D%20(r%20f'%20%2B%20k%5E2)."></div> 
We get after the time transformation
<!-- $$
\frac{1-f^2H^2}{f} \partial_\tau^2 u = - 2 fH \partial_r\partial_\tau u + f \partial_r^2 u - (f H)' \partial_\tau u + f'\partial_r u -\frac{1}{r^2} (r f' + k^2 ).
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cfrac%7B1-f%5E2H%5E2%7D%7Bf%7D%20%5Cpartial_%5Ctau%5E2%20u%20%3D%20-%202%20fH%20%5Cpartial_r%5Cpartial_%5Ctau%20u%20%2B%20f%20%5Cpartial_r%5E2%20u%20-%20(f%20H)'%20%5Cpartial_%5Ctau%20u%20%2B%20f'%5Cpartial_r%20u%20-%5Cfrac%7B1%7D%7Br%5E2%7D%20(r%20f'%20%2B%20k%5E2%20)."></div>
The code solves the above equation for Gaussian initial data.