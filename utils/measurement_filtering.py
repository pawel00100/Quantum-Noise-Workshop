from qiskit import QuantumRegister, assemble, transpile
from qiskit.ignis.mitigation.measurement import complete_meas_cal, CompleteMeasFitter
from .backends import BackendModel


def get_measurement_filter(n_qbits: int, backend_model: BackendModel):
    qr = QuantumRegister(n_qbits)
    meas_calibs, state_labels = complete_meas_cal(qr=qr, circlabel='mcal')  # returns array of 4 simple gates with X at 00, 01, 10, 11

    t_qc = transpile(meas_calibs, backend_model.backend, backend_model.basis_gates, coupling_map=backend_model.coupling_map)
    cal_results = backend_model.backend.run(assemble(t_qc, shots=10000), noise_model=backend_model.noise_model, shots=10000).result()

    meas_fitter = CompleteMeasFitter(cal_results, state_labels, circlabel='mcal')
    return meas_fitter.filter

