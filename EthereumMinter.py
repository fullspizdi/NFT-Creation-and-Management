# EthereumMinter.py

import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from config import ETH_PRIVATE_KEY, ETH_PROVIDER_URL, OUTPUT_DIR

class EthereumMinter:
    def __init__(self, private_key, provider_url):
        self.private_key = private_key
        self.provider_url = provider_url
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.account = self.web3.eth.account.privateKeyToAccount(private_key)

    def mint_collection(self, output_dir):
        # Load the metadata files
        metadata_files = [f for f in os.listdir(output_dir) if f.endswith('.json')]
        for metadata_file in metadata_files:
            with open(os.path.join(output_dir, metadata_file), 'r') as file:
                metadata = json.load(file)
                self.mint_nft(metadata)

    def mint_nft(self, metadata):
        # Dummy function for minting an NFT
        # In a real scenario, this would interact with a smart contract
        print(f"Minting NFT with metadata: {metadata['name']}")

        # Example of sending a transaction
        nonce = self.web3.eth.getTransactionCount(self.account.address)
        transaction = {
            'nonce': nonce,
            'to': '',  # Address of the NFT contract
            'value': self.web3.toWei(0, 'ether'),  # No ether to send
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        }

        # Sign the transaction
        signed_txn = self.web3.eth.account.signTransaction(transaction, self.private_key)
        
        # Send the transaction
        tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction hash: {self.web3.toHex(tx_hash)}")

        # Wait for the transaction to be mined
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Transaction receipt: {tx_receipt}")

# Example usage
if __name__ == "__main__":
    minter = EthereumMinter(ETH_PRIVATE_KEY, ETH_PROVIDER_URL)
    minter.mint_collection(OUTPUT_DIR)
