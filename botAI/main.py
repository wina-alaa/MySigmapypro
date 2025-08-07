import discord
from discord.ext import commands
import os, random
import requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''The duck command returns the photo of the duck'''
    print('hello')
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def classify(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'./{file_name}')
            await ctx.send(f'file berhasil disimpan dengan nama {file_name}')
            await ctx.send(f'dapat juga diakses melalui cloud discord di {file_url}')

            kelas, skor = get_class('keras_model.h5', 'labels.txt',f'./{file.filename}')

            # INFERENSI
            if kelas == 'pipit' and skor >= 0.75:
                await ctx.send('INI ADALAH BURUNG PIPIT')
                await ctx.send('PERSENTASE', 100*skor)
                await ctx.send('makanan burung pipit adalah biji-bijian, buah-buahan, dll')
                await ctx.send('burung pipit biasanya ditemukan di persawahan, perkebunan, dan bahkan di sekitar pemukiman seperti dekat rumah')

                # tambahkan inferensi
            elif kelas == 'merpati' and skor >= 0.75:
                await ctx.send('INI ADALAH BURUNG MERPATI')
                await ctx.send('PERSENTASE', 100*skor)
                await ctx.send('makanan burung merpati adalah biji-bijian, buah-buahan, sayur-sayuran, dll')
                await ctx.send('burung merpati biasanya ditemukan di persawahan, perkebunan, dan bahkan di sekitar pemukiman seperti dekat rumah')

            elif kelas == 'perkutut' and skor >= 0.75:
                await ctx.send('INI ADALAH BURUNG PERKUTUT')
                await ctx.send('PERSENTASE', 100*skor)
                await ctx.send('makanan burung perkutut adalah gabah, jewawut, ketan hitam, dan biji-bijian lainnya')
                await ctx.send('burung perkutut biasanya ditemukan di hutan, padang rumput, lahan pertanian dan bahkan di sekitar pemukiman seperti dekat rumah')

            elif kelas == 'burung hantu' and skor >= 0.75:
                await ctx.send('INI ADALAH BURUNG HANTU')
                await ctx.send('PERSENTASE', 100*skor)
                await ctx.send('makanan burung hantu adalah tikus, burung kecil, serangga seperti jangkrik dan ulat, dll')
                await ctx.send('burung hantu biasanya ditemukan di pohon berlubang, tebing, gua, lumbung, bangunan kosong, dll')

            elif kelas == 'elang' and skor >= 0.75:
                await ctx.send('INI ADALAH BURUNG ELANG')
                await ctx.send('PERSENTASE', 100*skor)
                await ctx.send('makanan burung elang adalah mamalia kecil seperti tikus, kelinci, tupai, reptil seperti kadal dan ular, dll')
                await ctx.send('burung elang biasanya ditemukan di hutan pegunungan, sungai atau pantai, kebun binatang, dll')

            elif kelas == 'beo' and skor >= 0.75:
                await ctx.send('INI ADALAH BURUNG BEO')
                await ctx.send('PERSENTASE', 100*skor)
                await ctx.send('makanan burung beo adalah biji-bijian, buah-buahan, sayuran, kacang-kacangan, dan serangga')
                await ctx.send('burung beo biasanya ditemukan di hutan, penangkaran, kebun binatang, dll')

                # tambahkan inferensi
            else:
                await ctx.send('aku tidak tahu itu apa')
    else:
        await ctx.send('kamu tidak melampirkan apa apa!')


bot.run('MTM0MjExNDM3NzM2ODYwNDcxMg.GzXJHA.7XiFlH3Y86WHe5jf9n_gOsbpGwwfRveP4sWygU')