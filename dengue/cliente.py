import flwr as fl
from modelo import criar_modelo_lstm

class UbsCliente(fl.client.NumPyClient):
    def __init__(self, nome_ubs, X_treino, y_treino, X_teste, y_teste):
        self.nome_ubs = nome_ubs
        self.model = criar_modelo_lstm(input_shape=(X_treino.shape[1], X_treino.shape[2]))
        self.X_treino = X_treino
        self.y_treino = y_treino
        self.X_teste = X_teste
        self.y_teste = y_teste

    def get_parameters(self, config):
        return self.model.get_weights()

    def fit(self, parameters, config):
        print(f" -> {self.nome_ubs} treinando com dados locais protegidos...")
        self.model.set_weights(parameters)
        self.model.fit(self.X_treino, self.y_treino, epochs=3, batch_size=8, verbose=0)
        return self.model.get_weights(), len(self.X_treino), {}

    def evaluate(self, parameters, config):
        self.model.set_weights(parameters)
        loss, mae = self.model.evaluate(self.X_teste, self.y_teste, verbose=0)
        return loss, len(self.X_teste), {"mae": mae}