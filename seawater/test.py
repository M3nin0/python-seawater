import seawater.gibbs as gsw
import seawater.csiro as sw
import numpy as np

try:
    import cPickle as pickle
except:
    import pickle

""" load test data """
class Dict2Struc(object):
    """ all the variables from a dict in a "matlab-like-structure" """
    def __init__(self, adict):
        self.__dict__.update(adict)

data = pickle.load( open('gsw_cv.pkl','rb') )
gsw_cv = Dict2Struc(data) # then type dat.<tab> to navigate through your variables


""" SA_from_SP """
SA_chck_cast = gsw.SA_from_SP(gsw_cv.SP_chck_cast, gsw_cv.p_chck_cast, gsw_cv.long_chck_cast, gsw_cv.lat_chck_cast)[0]
ISA_from_SP = (gsw_cv.SA_from_SP - SA_chck_cast) >= gsw_cv.SA_from_SP_ca

if ISA_from_SP.any():
    print "SA_from_SP:   Failed. Note that this will cause many other programmes in the GSW toolbox to fail"
else:
    print "SA_from_SP:   Passed"

""" z_from_p """
z_from_p = gsw.z_from_p(gsw_cv.p_chck_cast, gsw_cv.lat_chck_cast)
Iz_from_p = (gsw_cv.z_from_p - z_from_p) >= gsw_cv.z_from_p_ca

if Iz_from_p.any():
    print "z_from_p:   Failed"
else:
    print "z_from_p:   Passed"

""" grav """
grav = gsw.grav(gsw_cv.lat_chck_cast, gsw_cv.p_chck_cast )
Igrav = (gsw_cv.grav - grav) >= gsw_cv.grav_ca

if Igrav.any():
    print "grav:   Failed"
else:
    print "grav:   Passed"


""" molality """
molality = gsw.molality(SA_chck_cast)
Imolality = (gsw_cv.molality - molality) >= gsw_cv.molality_ca

if Imolality.any():
    print "molality:   Failed"
else:
    print "molality:   Passed"


""" ionic_strength """
ionic_strength = gsw.ionic_strength(SA_chck_cast)
Iionic_strength = (gsw_cv.ionic_strength - ionic_strength) >= gsw_cv.ionic_strength_ca

if Iionic_strength.any():
    print "ionic_strength:   Failed"
else:
    print "ionic_strength:   Passed"


""" gsw/sw f """
f = sw.cor(gsw_cv.lat_chck_cast)

If = (gsw_cv.f - f) >= gsw_cv.f_ca

if If.any():
    print "f:   Failed"
else:
    print "f:   Passed"


""" CT_from_t """
CT_chck_cast = gsw.CT_from_t(SA_chck_cast, gsw_cv.t_chck_cast, gsw_cv.p_chck_cast)
ICT_from_t = (gsw_cv.CT_from_t - CT_chck_cast) >= gsw_cv.CT_from_t_ca
if ICT_from_t.any():
    print "CT_from_t:   Failed. Note that this will cause many other programmes in the GSW toolbox to fail."
else:
    print "CT_from_t:   Passed"



""" pt_from_t """
pt = gsw.pt_from_t(SA_chck_cast, gsw_cv.t_chck_cast, gsw_cv.p_chck_cast, gsw_cv.pr)
Ipt_from_t = (gsw_cv.pt_from_t - pt) >= gsw_cv.pt_from_t_ca

if Ipt_from_t.any():
    print "pt_from_t:   Failed"
else:
    print "pt_from_t:   Passed"


""" entropy_from_t 'pt' """ #FIXME: pass, but small float are detected, investigate further
entropy_from_pt =  gsw.entropy_from_t(SA_chck_cast, pt)
Ientropy_from_pt = (gsw_cv.entropy_from_pt - entropy_from_pt) >= gsw_cv.entropy_from_pt_ca

if Ientropy_from_pt.any():
    print "entropy_from_pt:   Failed"
else:
    print "entropy_from_pt:   Passed"


""" entropy_from_t 'CT'"""
entropy_from_CT =  gsw.entropy_from_t(SA_chck_cast, CT_chck_cast, t_type='CT')
Ientropy_from_CT = (gsw_cv.entropy_from_CT - entropy_from_CT) >= gsw_cv.entropy_from_CT_ca

if Ientropy_from_CT.any():
    print "entropy_from_CT:   Failed"
else:
    print "entropy_from_CT:   Passed"


""" CT_from_pt """
CT_from_pt = gsw.CT_from_pt(SA_chck_cast, pt) #FIXME: pass, but small float are detected, investigate further
ICT_from_pt = (gsw_cv.CT_from_pt - CT_from_pt) >= gsw_cv.CT_from_pt_ca

if ICT_from_pt.any():
    print "CT_from_pt:   Failed"
else:
    print "CT_from_pt:   Passed"


""" pt0_from_t """
pt0 = gsw.pt0_from_t(SA_chck_cast, gsw_cv.t_chck_cast, gsw_cv.p_chck_cast)
Ipt0 = (gsw_cv.pt0 - pt0) >= gsw_cv.pt0_ca

if Ipt0.any():
    print "pt0_from_t:   Failed"
else:
    print "pt0_from_t:   Passed"



""" pt_from_CT """
pt_from_CT = gsw.pt_from_CT(SA_chck_cast, CT_chck_cast)
Ipt_from_CT = (gsw_cv.pt - pt_from_CT) >= gsw_cv.pt_ca

if Ipt_from_CT.any():
    print "pt_from_CT:   Failed"
else:
    print "pt_from_CT:   Passed"




""" entropy """
entropy = gsw.entropy(SA_chck_cast, gsw_cv.t_chck_cast, gsw_cv.p_chck_cast)
Ientropy = (gsw_cv.entropy - entropy) >= gsw_cv.entropy_ca

if Ientropy.any():
    print "entropy:   Failed"
else:
    print "entropy:   Passed"



""" pt_from_entropy """ #FIXME: pass, but small float are detected, investigate further
pt_from_entropy =  gsw.t_from_entropy(SA_chck_cast, entropy)
Ipt_from_entropy = (gsw_cv.pt_from_entropy - pt_from_entropy) >= gsw_cv.pt_from_entropy_ca

if Ipt_from_entropy.any():
    print "pt_from_entropy:   Failed"
else:
    print "pt_from_entropy:   Passed"



""" CT_from_entropy """ #FIXME: pass, but small float are detected, investigate further
CT_from_entropy =  gsw.t_from_entropy(SA_chck_cast, entropy, 'CT')
ICT_from_entropy = (gsw_cv.CT_from_entropy - CT_from_entropy) >= gsw_cv.CT_from_entropy_ca

if ICT_from_entropy.any():
    print "CT_from_entropy:   Failed"
else:
    print "CT_from_entropy:   Passed"


""" sigma_CT """
sigma0_CT = gsw.sigma_CT(SA_chck_cast, CT_chck_cast)
Isigma_CT = (gsw_cv.sigma0_CT - sigma0_CT) >= gsw_cv.sigma0_CT_ca

if Isigma_CT.any():
    print "sigma_CT at 0 db:   Failed"
else:
    print "sigma_CT at 0 db:   Passed"

sigma1_CT = gsw.sigma_CT(SA_chck_cast, CT_chck_cast, 1000)
Isigma_CT = (gsw_cv.sigma1_CT - sigma1_CT) >= gsw_cv.sigma1_CT_ca

if Isigma_CT.any():
    print "sigma_CT at 1000 db:   Failed"
else:
    print "sigma_CT at 1000 db:   Passed"

sigma2_CT = gsw.sigma_CT(SA_chck_cast, CT_chck_cast, 2000)
Isigma_CT = (gsw_cv.sigma2_CT - sigma2_CT) >= gsw_cv.sigma2_CT_ca

if Isigma_CT.any():
    print "sigma_CT at 2000 db:   Failed"
else:
    print "sigma_CT at 2000 db:   Passed"

sigma3_CT = gsw.sigma_CT(SA_chck_cast, CT_chck_cast, 3000)
Isigma_CT = (gsw_cv.sigma3_CT - sigma3_CT) >= gsw_cv.sigma3_CT_ca

if Isigma_CT.any():
    print "sigma_CT at 3000 db:   Failed"
else:
    print "sigma_CT at 3000 db:   Passed"

sigma4_CT = gsw.sigma_CT(SA_chck_cast, CT_chck_cast, 4000)
Isigma_CT = (gsw_cv.sigma4_CT - sigma4_CT) >= gsw_cv.sigma4_CT_ca

if Isigma_CT.any():
    print "sigma_CT at 4000 db:   Failed"
else:
    print "sigma_CT at 4000 db:   Passed"

""" cp """
cp = gsw.cp(SA_chck_cast, gsw_cv.t_chck_cast, gsw_cv.p_chck_cast)
Icp = (gsw_cv.cp - cp) >= gsw_cv.cp_ca

if Icp.any():
    print "cp:   Failed"
else:
    print "cp:   Passed"