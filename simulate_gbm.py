# This module reads the config file and send the variables to the rest of the program
import numpy as np
import pandas as pd
import os

dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class SimulationGbm(object):
    def read_gbm_parameters(self):

        file_name_vol_corr = os.path.join(dir_path, 'data_outputs', 'vol_corr.csv')
        # file_name_vc_chol_decompose_upper_triangle = os.path.join(dir_path, 'data_outputs',
        #                                                           'vc_chol_decompose_upper_triangle.csv')
        # file_name_matrix_correlation = os.path.join(dir_path, 'data_outputs', 'matrix_correlation.csv')

        matrix_vc = np.genfromtxt(file_name_vol_corr,  delimiter=',')
        print(df_vc)

    def read_upper_tringular_matrix(self):
        file_name_vc_chol_decompose_upper_triangle = os.path.join(dir_path, 'data_outputs',
                                                                  'correlation_chol_decompose_upper_triangle.csv')
        upper_triangular_matrix = np.genfromtxt(file_name_vc_chol_decompose_upper_triangle,  delimiter=',')
        return upper_triangular_matrix

    def generate_random_number_matrix_1_sample(self, risk_factor_count=3, simulation_count=10, tenor=46, fixed_seed=10):
        np.random.seed(fixed_seed)
        random_variables = np.random.normal(size=(tenor, risk_factor_count,simulation_count))
        random_variables_1_sample = np.random.normal(size=(tenor, risk_factor_count))
        # file_name_random_variables = os.path.join(dir_path, 'data_outputs', 'random_variables.csv')
        # np.save(file_name_random_variables, random_variables)
        return random_variables_1_sample

    def generate_correlated_random_variables_1_sim(self):
        # Here we define ONE price PATH starting from front period to the end of the period for ALL risk factors
        # 5,000 such simulations are required for asset valuation
        upper_triangular_matrix = self.read_upper_tringular_matrix()
        risk_factor_count = upper_triangular_matrix.shape[1]
        random_variables = self.generate_random_number_matrix_1_sample(risk_factor_count)
        correlated_random_returns = np.dot(random_variables,upper_triangular_matrix)
        file_name_correlated_random_returns = os.path.join(dir_path, 'data_outputs', 'correlated_random_returns.csv')
        # np.savetxt(file_name_correlated_random_returns, correlated_random_returns, delimiter=',')
        return correlated_random_returns





if __name__ == "__main__":
    print(SimulationGbm().generate_correlated_random_variables_1_sim())
    # SimulationGbm().generate_correlated_random_variables()
    # print(a)
