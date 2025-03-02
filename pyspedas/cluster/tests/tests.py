import os
import unittest
from pytplot import data_exists
import pyspedas
from pyspedas.cluster.load_csa import load_csa, cl_master_probes, cl_master_datatypes


class LoadTestCases(unittest.TestCase):
    def test_csa(self):
        dtypes = cl_master_datatypes()
        probes = cl_master_probes()
        self.assertTrue('CP_FGM_SPIN' in dtypes)
        self.assertTrue('C1' in probes)

    def test_load_fgm_data_csa(self):
        mag_vars = load_csa(datatypes=['CP_FGM_SPIN'], probes=None)  # returns empty list
        mag_vars = load_csa(datatypes=None)  # returns empty list
        mag_vars = load_csa(datatypes='CP_FGM_SPIN', probes='*')
        mag_vars = load_csa(datatypes=['CP_FGM_SPIN'], notplot=True)
        self.assertTrue(data_exists('B_vec_xyz_gse__C1_CP_FGM_SPIN'))
        self.assertTrue(data_exists('B_mag__C1_CP_FGM_SPIN'))
        self.assertTrue(data_exists('sc_pos_xyz_gse__C1_CP_FGM_SPIN'))

    def test_load_fgm_data(self):
        mag_vars = pyspedas.cluster.fgm(time_clip=True)
        self.assertTrue(data_exists('B_xyz_gse__C1_UP_FGM'))

    def test_load_fgm_cp_data(self):
        files = pyspedas.cluster.fgm(datatype='cp', trange=['2003-12-15', '2003-12-16'], downloadonly=True)
        self.assertTrue(os.path.exists(files[0]))

    def test_load_asp_data(self):
        asp_vars = pyspedas.cluster.aspoc(trange=['2004-04-05', '2004-04-06'])
        self.assertTrue(data_exists('I_ion__C1_PP_ASP'))

    def test_load_cis_data(self):
        cis_vars = pyspedas.cluster.cis()
        self.assertTrue(data_exists('N_p__C1_PP_CIS'))
        
    def test_load_dwp_data(self):
        dwp_vars = pyspedas.cluster.dwp()
        self.assertTrue(data_exists('Correl_freq__C1_PP_DWP'))

    def test_load_edi_data(self):
        edi_vars = pyspedas.cluster.edi(downloadonly=True)
        self.assertTrue(isinstance(edi_vars, list))
        
    def test_load_efw_data(self):
        efw_vars = pyspedas.cluster.efw()
        self.assertTrue(data_exists('E_pow_f1__C1_PP_EFW'))
        
    def test_load_peace_data(self):
        p_vars = pyspedas.cluster.peace()
        self.assertTrue(data_exists('T_e_par__C1_PP_PEA'))
        
    def test_load_rap_data(self):
        r_vars = pyspedas.cluster.rapid()
        self.assertTrue(data_exists('J_e_lo__C1_PP_RAP'))
        
    def test_load_sta_data(self):
        sta_vars = pyspedas.cluster.staff()
        self.assertTrue(data_exists('E_pow_f2__C1_PP_STA'))

    def test_load_wbd_data(self):
        wbd_vars = pyspedas.cluster.wbd(trange=['2012-11-6/02:10', '2012-11-6/02:15'], notplot=True)
        self.assertTrue('WBD_Elec' in wbd_vars)
        
    def test_load_whi_data(self):
        whi_vars = pyspedas.cluster.whi()
        self.assertTrue(data_exists('E_pow_f5__C1_PP_WHI'))

        
if __name__ == '__main__':
    unittest.main()
