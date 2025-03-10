"""
Ethereum profile (heavy mode).
"""
from locust import constant_pacing, tag, task

from chainbench.user.evm import EVMBenchUser


class EthereumHeavyProfile(EVMBenchUser):
    wait_time = constant_pacing(10)

    @task
    def trace_transaction_task(self):
        self.make_call(
            name="trace_transaction",
            method="debug_traceTransaction",
            params=[],
        ),

    @task
    def block_task(self):
        self.make_call(
            name="block",
            method="trace_block",
            params=self._block_by_number_params_factory(),
        ),
        
    @task
    def get_block_by_number_task(self):
        self.make_call(
            name="get_block_by_number",
            method="eth_getBlockByNumber",
            params=self._block_by_number_params_factory(),
        ),
        
    @task
    def get_block_receipts(self):
        self.make_call(
            name="get_block_receipts",
            method="eth_getBlockReceipts",
            params=self._block_receipts_params_factory(),
        ),   
