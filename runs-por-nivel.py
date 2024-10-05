import discord
from utils import niveis
import math
import os



# Criar a instância do cliente Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = os.environ["bot-key"]

@client.event
async def on_ready():
    print(f'Bot {client.user} está pronto!')

# Função para executar quando uma mensagem for enviada
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Comando para calcular o XP do Digimon
    if message.content.startswith('!calcular'):
        try:
            # Extrair o nível do comando
            nivel = message.content.split()[1]

            # Validar se o nível é um número e se está no intervalo dos níveis
            if nivel in niveis:
                xp_por_ch = 14947386124
                nivel_xp = niveis[nivel]
                ch_por_nivel = math.ceil(nivel_xp / xp_por_ch)
                
                # Responder no chat com o resultado
                await message.channel.send(f"Você precisa fazer {ch_por_nivel} CH's da run para upar pro nível {int(nivel) + 1}.")
                await message.channel.send(f"Os cálculos foram feitos tendo como base 4250% de XP contando com o 500% padrão.")
            else:
                await message.channel.send("Digite um nível entre 150 e 170")
        
        except Exception:
            await message.channel.send("Digite um nível entre 150 e 170, ou a informação ainda não está disponível entre em contato com aowys no discord.")
        
    elif message.content.startswith('!me mama'):
        await message.channel.send(f"glub glub!!")
        await message.channel.send(f"só pros brother eim glub glub!!")

# Rodar o bot
client.run(TOKEN)





