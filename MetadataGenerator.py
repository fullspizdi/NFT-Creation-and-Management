import json
import os

class MetadataGenerator:
    def __init__(self, collection_name, description):
        """
        Initialize the MetadataGenerator with collection details.
        
        :param collection_name: Name of the NFT collection
        :param description: Description of the NFT collection
        """
        self.collection_name = collection_name
        self.description = description

    def create_metadata_files(self, output_dir):
        """
        Create metadata files for each generated image in the specified output directory.
        
        :param output_dir: Directory where the generated images and metadata files will be stored
        """
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Load traits configuration
        with open('./traits.json', 'r') as file:
            traits = json.load(file)

        # Generate metadata for each image
        for i in range(1, 1001):  # Assuming 1000 images as per basic usage example
            metadata = {
                "name": f"{self.collection_name} #{i}",
                "description": self.description,
                "image": f"{output_dir}/image_{i}.png",
                "attributes": self.generate_attributes(traits)
            }

            # Write metadata to a JSON file
            with open(f"{output_dir}/metadata_{i}.json", 'w') as outfile:
                json.dump(metadata, outfile, indent=4)

    def generate_attributes(self, traits):
        """
        Randomly generate attributes for an NFT based on defined traits.
        
        :param traits: A dictionary containing trait types and their options
        :return: A list of attribute dictionaries
        """
        import random
        attributes = []
        for trait in traits['traits']:
            options = trait['options']
            probabilities = [option['probability'] for option in options]
            chosen_option = random.choices(options, weights=probabilities, k=1)[0]
            attributes.append({
                "trait_type": trait['trait_type'],
                "value": chosen_option['value']
            })
        return attributes
