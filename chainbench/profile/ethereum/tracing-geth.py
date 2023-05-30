"""
Ethereum tracing profile Geth client
"""
from locust import task

from chainbench.user.evm import EVMBenchUser


class EthereumTracingGethProfile(EVMBenchUser):
    @task
    def trace_transaction_task(self):
        self.make_call(
            name="trace_transaction",
            method="debug_traceTransaction",
            params=[ "0xae2cdf10877ee7b2698acbe53f34f3ab7bac22b95902b7fdc5191a0f3c24921c",
    {
      "tracer": "callTracer"
    }],
        ),

    @task
    def block_task(self):
        self.make_call(
            name="trace_block",
            method="debug_traceBlockByNumber",
            params=["latest",
    {
      "tracer": "callTracer"
    }],
        ),
    
    @task
    def get_block_by_number_task(self):
        self.make_call(
            name="get_block_by_number",
            method="eth_getBlockByNumber",
            params=self._block_by_number_params_factory(),
        ),


