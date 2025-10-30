import os
import json

class AssetsLoader:
    def __init__(self, asset_paths):
        self.asset_paths = asset_paths
        self.assets = {}

    def load_models(self):
        for model_type in ['characters', 'weapons', 'environment']:
            self.assets[model_type] = {}
            for category in os.listdir(os.path.join(self.asset_paths['models'], model_type)):
                self.assets[model_type][category] = []
                category_path = os.path.join(self.asset_paths['models'], model_type, category)
                for model_file in os.listdir(category_path):
                    if model_file.endswith(('.obj', '.fbx', '.gltf')):
                        self.assets[model_type][category].append(model_file)

    def load_textures(self):
        self.assets['textures'] = {}
        for texture_type in ['characters', 'weapons', 'ui']:
            self.assets['textures'][texture_type] = []
            texture_path = os.path.join(self.asset_paths['textures'], texture_type)
            for texture_file in os.listdir(texture_path):
                if texture_file.endswith(('.png', '.jpg', '.jpeg')):
                    self.assets['textures'][texture_type].append(texture_file)

    def load_audio(self):
        self.assets['audio'] = []
        audio_path = self.asset_paths['audio']
        for audio_file in os.listdir(audio_path):
            if audio_file.endswith(('.wav', '.mp3')):
                self.assets['audio'].append(audio_file)

    def load_all_assets(self):
        self.load_models()
        self.load_textures()
        self.load_audio()
        return self.assets

if __name__ == "__main__":
    asset_paths = {
        'models': 'assets/models',
        'textures': 'assets/textures',
        'audio': 'assets/audio'
    }
    loader = AssetsLoader(asset_paths)
    all_assets = loader.load_all_assets()
    print(json.dumps(all_assets, indent=4))