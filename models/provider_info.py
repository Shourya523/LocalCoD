class ProviderInfo:
    def __init__(self, name, loadedModels,installedModels):
        self.name = name
        self.loadedModels = loadedModels
        self.installedModels=installedModels

    def __repr__(self):
        return f"ProviderInfo(name={self.name}, installedmodels={self.installedModels}), loadedModels={self.loadedModels} "