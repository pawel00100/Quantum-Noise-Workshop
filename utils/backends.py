from qiskit.providers.aer.noise import pauli_error, NoiseModel
from qiskit import QuantumCircuit, assemble, transpile, Aer, IBMQ
from qiskit.providers.ibmq import least_busy


class BackendModel:
    def __init__(self, backend, noise_model, basis_gates, coupling_map) -> None:
        super().__init__()
        self.backend = backend
        self.noise_model = noise_model
        self.basis_gates = basis_gates
        self.coupling_map = coupling_map


def get_noise(p):
    error_meas = pauli_error([('X', p), ('I', 1 - p)])
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(error_meas, "measure")  # measurement error is applied to measurements
    return noise_model


def real_machine():
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    n = 2
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits > n and
                                                             not x.configuration().simulator and x.status().operational == True))
    return backend


def get_real_noise():
    noise_model = NoiseModel.from_backend(real_machine())
    return noise_model


def aer_simulator():
    return Aer.get_backend('aer_simulator')


def qasm_simulator():
    return Aer.get_backend('qasm_simulator')


aer_simulator_clean = BackendModel(aer_simulator(), None, None, None)
qasm_simulator_clean = BackendModel(qasm_simulator(), None, None, None)
aer_simulator_noise = BackendModel(aer_simulator(), get_noise(0.01), None, None)
qasm_simulator_noise = BackendModel(aer_simulator(), get_noise(0.01), None, None)
real_machine_backend_model = BackendModel(real_machine(), None, None, None)

# def real_machine_backend_model():
#     return BackendModel(real_machine(), None, None, None)

def get_aer_real_noise(real_backend):
    real_noise_model = NoiseModel.from_backend(real_backend)
    return BackendModel(aer_simulator(), real_noise_model, real_noise_model.basis_gates, real_backend.configuration().coupling_map)

aer_real_noise = get_aer_real_noise(real_machine_backend_model.backend)