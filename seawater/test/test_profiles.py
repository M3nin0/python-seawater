# -*- coding: utf-8 -*-

"""Unit check for standard profiles for the 
   Gibbs Sea Water python package

   Functionality similar to matlab_test.py
   without the nice output
"""

# Bjørn Ådlandsvik <bjorn@imr.no>
# 2011-03-03

import os
import sys
import unittest
import functools   # require python 2.5
import numpy as np
import seawater.gibbs as gsw
from seawater.gibbs.library import Dict2Struc

# ------------------------------------
# Table of functions with arguments
# ------------------------------------

# Codes for non-tested functions
# 
# TI  : Returning a tuple, tested individually
# LIB : Library routine,
# NI: Not Implemented
# NV: No test value
# NA: Don't fit the testing scheme
# ERR: Gives error

# Could perhaps be auto-generated
function_arguments = {

#TI    'CT_first_derivatives' : ('SA', 'pt')
    'CT_derivative_SA' : ('SA', 'pt'),
    'CT_derivative_pt' : ('SA', 'pt'),
    'CT_from_entropy'  : ('SA', 'entropy'),
    'CT_from_pt'       : ('SA', 'pt'),
    'CT_from_t'        : ('SA', 't', 'p'),
    'CT_maxdensity'    : ('SA', 'p'),
#NI    'CT_second_derivatives' : ('SA', 'pt'),

    'Helmholtz_energy' : ('SA', 't', 'p'),

    'IPV_vs_fNsquared_ratio_CT25' : ('SA', 'CT', 'p', 'pr'),

    'Nsquared_CT25' : ('SA', 'CT', 'p', 'lat'),

    'Rsubrho_CT25' : ('SA', 'CT', 'p'),

#TI    'SA_Sstar_from_SP' : ('SP', 'p', 'long', 'lat'),
    'SA_from_SP' : ('SP', 'p', 'long', 'lat'),
#LIB    'SA_from_SP_Baltic' : ('SP', 'long', 'lat'),
    'SA_from_Sstar' : ('Sstar', 'p', 'long', 'lat'),
    'SA_from_rho' : ('rho', 't', 'p'),
    'SP_from_SA'  : ('SA', 'p', 'long', 'lat'),
#LIB    'SP_from_SA_Baltic' : ('SA', 'long', 'lat'),
    'SP_from_Sstar' : ('Sstar', 'p', 'long', 'lat'),
    'SP_from_cndr'  : ('R', 't', 'p'),
    'Sstar_from_SA' : ('SA', 'p', 'long', 'lat'),
    'Sstar_from_SP' : ('SP', 'p', 'long', 'lat'),
    
#TI    'Turner_Rsubrho_CT25' : ('SA', 'CT', 'p'),
    'Turner_CT25' : ('SA', 'CT', 'p'),

    'adiabatic_lapse_rate' : ('SA', 't', 'p'),
    'alpha_CT'             : ('SA', 'CT', 'p'),
    'alpha_CT25'           : ('SA', 'CT', 'p'),
    'alpha_wrt_CT'         : ('SA', 't', 'p'),
    'alpha_wrt_pt'         : ('SA', 't', 'p'),
    'alpha_wrt_t'          : ('SA', 't', 'p'),
    
    'beta_CT'       : ('SA', 'CT', 'p'),
    'beta_CT25'     : ('SA', 'CT', 'p'),
    'beta_const_CT' : ('SA', 't', 'p'),
    'beta_const_pt' : ('SA', 't', 'p'),
    'beta_const_t'  : ('SA', 't', 'p'),
    
#BUG in profile values on file
#    'cabbeling_CT25'   : ('SA', 't', 'p'),
    'chem_potential_relative' : ('SA', 't', 'p'),
    'chem_potential_salt'     : ('SA', 't', 'p'),
    'chem_potential_water'    : ('SA', 't', 'p'),
    'cp'                      : ('SA', 't', 'p'),
    
#LIB    'delta_SA' : ('p', 'long', 'lat'),
    'distance' : ('long', 'lat', 'p'),

    'enthalpy'        : ('SA', 't', 'p'),
    'enthalpy_CT'     : ('SA', 'CT', 'p'),
    'enthalpy_CT25'   : ('SA', 'CT', 'p'),
#NI    'enthalpy_SSO_0_CT25' : ('p',),
#NI    'enthalpy_diff_CT' : ('SA', 'CT', 'p0', 'p1'),
    'enthalpy_diff_CT25' : ('SA', 'CT', 'p0', 'p1'),
#NI    'enthalpy_first_derivatives' : ('SA', 'CT', 'p'),
#NI    'enthalpy_second_derivatives' : ('SA', 'CT', 'p'),
    'entropy' : ('SA', 't', 'p'),
#TI    'entropy_first_derivatives' : ('SA', 'CT'),
    'entropy_derivative_SA'    : ('SA', 'CT'),
    'entropy_derivative_CT'    : ('SA', 'CT'),
    'entropy_from_CT' : ('SA', 'CT'),
    'entropy_from_pt' : ('SA', 'pt'),
#?    'entropy_part' : ?
#?    'entropy_part_zerop' : ?
#TI    'entropy_second_derivatives' : ('SA', 'pt'),
    'entropy_derivative_CT_CT' : ('SA', 'CT'),
    'entropy_derivative_SA_CT' : ('SA', 'CT'),
    'entropy_derivative_SA_SA' : ('SA', 'CT'),
    
    'f' : ('lat',),

#NI    'geo_strf_Cunningham' :
#NI    'geo_strf_McD_Klocker' :
#NI    'geo_strf_McD_Klocker_pc' :
#NI    'geo_strf_Montgomery' :
#NI    'geo_strf_dyn_height' :
#NI    'geo_strf_dyn_height_pc' :
#NI    'geostrophic_velocity' :
#LIB    'gibbs' :
#?   'gibbs_pt0_pt0' :
    'grav' : ('lat', 'p'),

    'internal_energy'    : ('SA', 't', 'p'),
#NI    'interp_McD_Klocker' :
#NI    'interp_SA_CT' :
    'ionic_strength'     : ('SA',),
    'isochoric_heat_cap' : ('SA', 't', 'p'),
#NI    'isopycnal_slope_ratio_CT25' :
#NI    'isopycnal_vs_ntp_CT_ratio_CT25' :

    'kappa'         : ('SA', 't', 'p'),
    'kappa_const_t' : ('SA', 't', 'p'),
    
    'molality'      : ('SA',),

#NI    'ntp_pt_vs_CT_ratio_CT25' : ('SA', 't', 'p'),

    'osmotic_coefficient' : ('SA', 't', 'p'),

    'p_from_z'             : ('z', 'lat'),
    'pot_enthalpy_from_pt' : ('SA', 'pt'),
    'pot_rho'              : ('SA', 't', 'p', 'pr'),
    'pt0_from_t'           : ('SA', 't', 'p'),
#NI    'pt_first_derivatives' :
    'pt_from_CT'           : ('SA', 'CT'),
    'pt_from_entropy'      : ('SA', 'entropy'),
    'pt_from_t'            : ('SA', 't', 'p', 'pr'),
    'pt_maxdensity'        : ('SA', 'p'),
#NI    'pt_second_derivatives' :

    'rho'      : ('SA', 't', 'p'),
    'rho_CT'   : ('SA', 'CT', 'p'),
    'rho_CT25' : ('SA', 'CT', 'p'),
#TI    'rho_alpha_beta_CT' : ('SA', 'CT', 'p'),  # Tested individually
#TI    'rho_alpha_beta_CT25' : ('SA', 'CT', 'p'), # Tested individually
    
    'sigma0_CT'         : ('SA', 'CT'),
#NI    'sigma0_pt' : ('SA', 'pt0'),
    'sigma1_CT'         : ('SA', 'CT'),
    'sigma2_CT'         : ('SA', 'CT'),
    'sigma3_CT'         : ('SA', 'CT'),
    'sigma4_CT'         : ('SA', 'CT'),
    'sound_speed'       : ('SA', 't', 'p'),
    'specvol'           : ('SA', 't', 'p'),
    'specvol_CT'        : ('SA', 'CT', 'p'),
    'specvol_CT25'      : ('SA', 'CT', 'p'),
#?    '_specvol_SSO_0_CT25' : ('p',),
    'specvol_anom' : ('SA', 't', 'p'),
#NI    'specvol_anom_CT' : ('SA', 'CT', 'p'),
    'specvol_anom_CT25' : ('SA', 'CT', 'p'),

    't90_from_t48' : ('t',),
    't90_from_t68' : ('t',),
    't_from_CT'        : ('SA', 'CT', 'p'),
#TI    'temps_maxdensity' : ('SA', 'p'),   # Tested individually
    't_maxdensity'  : ('SA', 'p'),
    'thermobaric_CT25' : ('SA', 'CT', 'p'),

    'z_from_p' : ('p', 'lat'),

    
            }


# ------------------------------------------
# Read data file with check value profiles
# ------------------------------------------

datadir = os.path.join(os.path.dirname(gsw.__file__), 'data')
fname = 'gsw_cv.npz'
cv = Dict2Struc(np.load(os.path.join(datadir, fname)))

# ---------------------------
# Aliases in the cv struct
# ---------------------------

# Make aliases for some values to be used as arguments

# Note: there seems to be a bug in the dataset
# The arrays cv.SA_from_Sstar is wrong
# The error is also in mat-file
#
# cv.SA_from_Sstar != cv.SA_from_SP
# cv.SA_from_Sstar != gsw.SA_from_Sstar(Sstar, p, lon, lat)
# cv.SA_from_Sstar == gsw.SA_from_Sstar(SA, p, lon, lat)
#
# cv.specvol_ST == cv.specvol_ST25
# cv.specvol_ST != cv.specvol
# cv.specvol_ST != 1/cv.rho_ST
# Correction: set cv.specvol_ST = cv.specvol

# Bug work-around
cv.SA_from_Sstar = cv.SA_from_SP
cv.specvol_CT = cv.specvol

cv.SA_chck_cast      = cv.SA_from_SP
cv.CT_chck_cast      = cv.CT_from_t
cv.pt_chck_cast      = cv.pt_from_t
cv.Sstar_chck_cast   = cv.Sstar_from_SA 
##cv.Sstar_chck_cast   = cv.SA_chck_cast    
cv.entropy_chck_cast = cv.entropy
cv.z_chck_cast       = cv.z_from_p
cv.rho_chck_cast     = cv.rho
cv.R_chck_cast       = cv.cndr
cv.pr_chck_cast      = cv.pr
cv.p0_chck_cast      = cv.p_chck_cast_shallow
cv.p1_chck_cast      = cv.p_chck_cast_deep

# Make aliases for check values whose names
# does not match the function
not_match = {'pt0_from_t' : 'pt0',
             'pt_from_CT' : 'pt',
             'pot_enthalpy_from_pt' : 'pot_enthalpy',
             'Nsquared_CT25' : 'n2',
             'IPV_vs_fNsquared_ratio_CT25' : 'IPVfN2',
             'Turner_CT25' : 'Tu',
             'Rsubrho_CT25' : 'Rsubrho',
             'CT_derivative_SA' : 'CT_SA',
             'CT_derivative_pt' : 'CT_pt',
             'entropy_derivative_SA'    : 'eta_SA',
             'entropy_derivative_CT'    : 'eta_CT',
             'entropy_derivative_CT_CT' : 'eta_CT_CT',
             'entropy_derivative_SA_CT' : 'eta_SA_CT',
             'entropy_derivative_SA_SA' : 'eta_SA_SA',
             'alpha_CT'   : 'alpha_CTrab',
             'alpha_CT25' : 'alpha_CT25rab',
             'beta_CT'    : 'beta_CTrab',
             'beta_CT25'  : 'beta_CT25rab',
             't_maxdensity' : 't_maxden',
             'pt_maxdensity' : 'pt_maxden',
             'CT_maxdensity' : 'CT_maxden',
             'chem_potential_relative' : 'chem_potential',
            }

for f in not_match:
    setattr(cv, f, getattr(cv, not_match[f]))
    setattr(cv, f+'_ca', getattr(cv, not_match[f]+'_ca'))

# ---------------------
# Generic test method
# ---------------------

def generic_test(self, func=None, argnames=None):
    """Generic test function, to be spesialized by functools.partial"""
    # Transform argument names to name convention in cv dataset
    args = [getattr(cv, a+'_chck_cast') for a in argnames]
    # Perform the function call
    out = getattr(gsw, func)(*args)
    # Check that the maximal error is less than the given tolerance
    maxdiff = np.nanmax(abs(out - getattr(cv, func)))
    #print maxdiff, getattr(cv, func+'_ca')
    self.assertTrue(maxdiff < getattr(cv, func+'_ca'))


# --------------------------------------------------------
# Dictionary of functions with corresponding test methods
# --------------------------------------------------------

function_test = {}
for f in function_arguments:
    function_test[f] = functools.partial(generic_test, 
                      func=f, argnames=function_arguments[f])

# ---------------------------
# Auto-generated TestCase 
# ---------------------------

class Test_profiles(unittest.TestCase):

    for f in function_test:
        method_def = ( "test_" + f + 
            " = lambda self: function_test['" + f + "'](self)" )
        #print method_def
        exec(method_def)


if __name__ == '__main__':
    # A more verbose output
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_profiles)
    a = unittest.TextTestRunner(verbosity=2).run(suite)
    if a.errors or a.failures: sys.exit(256)
    #unittest.main()

