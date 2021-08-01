from tqdm import tqdm
import time
import retro

from stable_baselines.common.policies import MlpPolicy,MlpLstmPolicy, MlpLnLstmPolicy, CnnLnLstmPolicy, CnnPolicy, CnnLstmPolicy
from stable_baselines.common.vec_env import SubprocVecEnv, DummyVecEnv

from stable_baselines import PPO2, A2C
nomeJogo = 'StreetFighterIISpecialChampionEdition-Genesis'

nomeModelo = 'Fighter_treinado_a2c_pt2'


##inimigos = ['blanka', 'chunli', 'zangief', 'guile', 'ken', 'dahlism']
inimigos = ['dahlism']
inicio_treinamento_modelo = time.time()
for inimigo in tqdm(inimigos, desc='Main Loop'):
  print("\n" + inimigo)
  ambienteTreinamento = DummyVecEnv([lambda: retro.make(nomeJogo, state=inimigo, scenario='scenario')])
  modelo = A2C(CnnPolicy,ambienteTreinamento)
  modelo.set_env(ambienteTreinamento)
  modelo.learn(total_timesteps=7000)
  modelo.save(nomeModelo)
  ambienteTreinamento.close()
fim_treinamento = time.time() - inicio_treinamento_modelo
print(f'\n O treinamento durou {fim_treinamento} seconds')


ambienteTreinamento = DummyVecEnv([lambda: retro.make(nomeJogo,state='dahlism', record='.')])
modelo = A2C.load(nomeModelo)
modelo.set_env(ambienteTreinamento)
obs = ambienteTreinamento.reset()
finalizado = False
recompensaTotal = 0
while not finalizado:
  acoes, _ = modelo.predict(obs)
  obs, recompensa, finalizado, info = env.step(acoes)
  recompensaTotal += recompensa
print(recompensaTotal)



