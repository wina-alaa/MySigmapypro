import discord
from discord.ext import commands
import random, os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

organik = ['daun', 'kulit buah', 'makanan sisa', 
           'kotoran hewan', 'ampas kopi', 'kulit telur', 
           'cangkang udang', 'sayur busuk', 'nasi basi', 
           'tulang ikan', 'batang pisang', 'ranting kayu', 
           'serbuk kayu', 'rumput', 'teh celup bekas', 
           'tisu bekas', 'jerami', 'sabut kelapa', 
           'biji buah', 'cangkang kepiting'
]

anorganik = ['plastik', 'botol plastik', 'kaca', 'kaleng', 
             'besi', 'aluminium', 'styrofoam', 'kardus bekas', 
             'baterai', 'kertas aluminium', 'sedotan', 'bungkus makanan', 
             'tutup botol', 'helm rusak', 'ban bekas', 'elektronik bekas', 
             'lampu neon', 'cd bekas', 'dvd bekas', 'kabel', 
             'paku', 'baut', 'pipa pvc'
]

b3 =  ['oli bekas', 'aki bekas', 'obat kadaluarsa', 
       'cat tembok', 'deterjen', 'pestisida', 'baterai bekas'
]

@bot.command()
async def sampah(ctx, *, item : str=None):
    #peringatan jika user tidak menyebut nama sampah
    if item is None:
        await ctx.send('⚠️ Tolong sebut nama sampah setelah command ⚠️')
        await ctx.send('misal: $sampah plastik')

    #klasifikasi sampah
    if item.lower() in organik:
        await ctx.send(f'🪴 {item} adalah **Sampah Organik 🍃**')
        await ctx.send(f'Cara menyikapi sampah {item} adalah:')
        await ctx.send('✅ Cara Penanganan = '
        '~ Daur ulang menjadi kompos menggunakan metode komposter takakura atau lubang biopori.'
        '~ Pakan ternak untuk sisa makanan tertentu yang bisa dikonsumsi hewan.'
        '~ Eco-enzyme dengan cara difermentasi menjadi cairan pembersih alami.')
    elif item.lower() in anorganik:
        await ctx.send(f'♻️ {item} adalah **Sampah Anorganik 🔄**')
        await ctx.send(f'Cara menyikapi sampah {item} adalah:')
        await ctx.send('✅ Cara Penanganan = '
        '~ Pisahkan berdasarkan jenisnya (plastik, kertas, logam, kaca).'
        '~ Daur ulang atau jual ke bank sampah untuk barang bernilai ekonomi.'
        '~ Gunakan kembali (reuse) barang yang masih bisa dimanfaatkan, seperti botol plastik atau tas belanja.')
    elif item.lower() in b3:
        await ctx.send(f'{item} adalah **Sampah B3 🆘**')
        await ctx.send(f'Cara menyikapi sampah {item} adalah:')
        await ctx.send('❌ Jangan dibuang sembarangan!')
        await ctx.send('✅ Cara Penanganan ='
        '~ Kumpulkan dalam wadah tertutup dan beri label.'
        '~ Serahkan ke tempat pengolahan limbah B3 seperti bank sampah khusus, fasilitas daur ulang elektronik, atau dinas lingkungan hidup setempat.'
        '~ Gunakan produk ramah lingkungan untuk mengurangi limbah B3, misalnya beralih ke baterai isi ulang.')

    else:
        await ctx.send(f'❓ `{item}` tidak ditemukan dalam daftar sampah.')
