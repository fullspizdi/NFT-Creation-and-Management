```python
# main.py

from autonft.generators import ImageGenerator
from autonft.metadata import MetadataGenerator
from autonft.minters import EthereumMinter

def main():
    # Configuration for image generation
    base_layers_dir = './layers'
    output_dir = './output'
    traits_config = './traits.json'
    num_images = 1000

    # Configuration for metadata generation
    collection_name = 'My NFT Collection'
    description = 'Amazing NFTs generated with AutoNFT'

    # Configuration for minting
    private_key = 'YOUR_PRIVATE_KEY'
    provider_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_ID'

    # Initialize the image generator
    image_generator = ImageGenerator(base_layers_dir, output_dir)
    print("Generating images...")
    image_generator.generate(num_images, traits_config)
    print("Images generated successfully.")

    # Initialize the metadata generator
    metadata_generator = MetadataGenerator(collection_name, description)
    print("Creating metadata files...")
    metadata_generator.create_metadata_files(output_dir)
    print("Metadata files created successfully.")

    # Initialize the Ethereum minter
    ethereum_minter = EthereumMinter(private_key, provider_url)
    print("Minting NFTs...")
    ethereum_minter.mint_collection(output_dir)
    print("NFTs minted successfully.")

if __name__ == '__main__':
    main()
```
