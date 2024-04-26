import os
import json
import random
from PIL import Image

class ImageGenerator:
    def __init__(self, base_layers_dir, output_dir):
        """
        Initialize the ImageGenerator with the directory containing base layers and the output directory.
        :param base_layers_dir: str, path to the directory containing image layers
        :param output_dir: str, path to the directory where generated images will be saved
        """
        self.base_layers_dir = base_layers_dir
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def load_traits(self, traits_config):
        """
        Load traits configuration from a JSON file.
        :param traits_config: str, path to the JSON file containing traits configuration
        :return: dict, loaded traits configuration
        """
        with open(traits_config, 'r') as file:
            return json.load(file)

    def select_trait(self, options):
        """
        Randomly select a trait based on the defined probabilities.
        :param options: list of dicts, each containing 'value' and 'probability'
        :return: str, selected trait value
        """
        population = [option['value'] for option in options]
        weights = [option['probability'] for option in options]
        return random.choices(population, weights=weights, k=1)[0]

    def generate_image(self, traits):
        """
        Generate a single image based on the selected traits.
        :param traits: dict, selected traits for the image
        :return: PIL.Image, generated image
        """
        layers = []
        for trait_type, value in traits.items():
            layer_path = os.path.join(self.base_layers_dir, trait_type, f"{value}.png")
            if os.path.exists(layer_path):
                layer = Image.open(layer_path)
                layers.append(layer)

        if not layers:
            raise ValueError("No layers found for the given traits.")

        base_image = layers[0]
        for layer in layers[1:]:
            base_image.paste(layer, (0, 0), layer)

        return base_image

    def generate(self, num_images, traits_config):
        """
        Generate multiple images based on the traits configuration.
        :param num_images: int, number of images to generate
        :param traits_config: str, path to the JSON file containing traits configuration
        """
        traits_data = self.load_traits(traits_config)
        for i in range(num_images):
            selected_traits = {trait['trait_type']: self.select_trait(trait['options']) for trait in traits_data['traits']}
            image = self.generate_image(selected_traits)
            image.save(os.path.join(self.output_dir, f"image_{i+1}.png"))
            print(f"Generated image {i+1}/{num_images}")

# Example usage:
# generator = ImageGenerator(base_layers_dir='./layers', output_dir='./output')
# generator.generate(num_images=1000, traits_config='./traits.json')
