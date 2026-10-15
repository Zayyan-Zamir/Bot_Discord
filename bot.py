import discord
import random
from discord.ext import commands
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

saved_number = None

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def vibe(ctx):
    vibes = [
        "🔥 Bot lagi on fire hari ini!",
        "😎 Mood: santai tapi tetap kece!",
        "💪 Ayo semangat, kamu pasti bisa!",
        "🎉 Hari ini harus tetap positif!",
        "🌈 Kalau semangat, semuanya terasa ringan."
    ]
    await ctx.send(random.choice(vibes))

@bot.command()
async def roll(ctx):
    await ctx.send(f"🎲 Kamu mendapat angka: {random.randint(1, 6)}")

@bot.command()
async def pick(ctx, *choices):
    if not choices:
        await ctx.send("Contoh: $pick nasi mie ayam bakso")
        return
    await ctx.send(f"✨ Pilihan saya: {random.choice(choices)}")

@bot.command()
async def joke(ctx):
    jokes = [
        "Kenapa ayam naik motor? Karena mau jadi ayam-bermotor!",
        "Apa bedanya kopi dan aku? Kopi bikin semangat, aku bikin chat makin seru.",
        "Kenapa buku selalu tenang? Karena dia punya banyak isi.",
        "Apa nama robot yang suka tidur? Bot-ty!"
    ]
    await ctx.send(random.choice(jokes))

@bot.command()
async def fact(ctx):
    facts = [
        "🐱 Kucing bisa tidur sampai 16 jam sehari.",
        "🌍 Air mendominasi permukaan bumi.",
        "🧠 Otak manusia bisa memproses banyak informasi dalam satu detik.",
        "🌞 Matahari adalah bintang terdekat dengan bumi.",
        "🦋 Kupu-kupu memiliki rasa di kaki mereka.",
        "🐘 Gajah memiliki ingatan yang sangat baik dan bisa mengenali individu lain."
    ]
    await ctx.send(random.choice(facts))

@bot.command()
async def factabouttrash(ctx):
    trashfacts = [
        "🧴 Sampah plastik membutuhkan waktu puluhan hingga ratusan tahun untuk terurai.",
        "🍂 Sampah organik, seperti daun dan sisa makanan, dapat diolah menjadi kompos.",
        "🌊 Membuang sampah sembarangan dapat mencemari sungai dan laut.",
        "♻️ Sampah bisa didaur ulang menjadi barang baru yang bermanfaat.",
        "🚮 Mengurangi penggunaan plastik sekali pakai dapat membantu mengurangi jumlah sampah.",
        "🗑️ Sampah elektronik mengandung bahan berbahaya yang dapat mencemari lingkungan jika tidak dibuang dengan benar.",
        "🌍 Memilah sampah membantu menjaga lingkungan tetap bersih dan sehat."
    ]
    await ctx.send(random.choice(trashfacts))

@bot.command()
async def quote(ctx):
    quotes = [
        """"Kesuksesan bukan hasil dari kebetulan, tapi dari usaha.""",
        """"Mulai hari ini, jadilah versi terbaik dari dirimu.""",
        """"Konsisten lebih kuat daripada sekadar semangat sesaat.""",
        """"Kecil tapi terus bergerak, itu lebih baik daripada diam."""
    ]
    await ctx.send(random.choice(quotes))

@bot.command()
async def guess(ctx, start=1, end=10):
    global saved_number

    saved_number = random.randint(start, end)
    await ctx.send("Guess a number from " + str(start) + " until " + str(end))

@bot.command()
async def answer(ctx, number):
    if int(number) == saved_number:
        await ctx.send("Congrats!!! you win")
    else:
        if int(number) < saved_number:
            await ctx.send("The number is bigger")
        else:
            await ctx.send("The number is smaller")

@bot.command()
async def mem(ctx):
    file_list = os.listdir('images')
    image = random.choice(file_list)
    with open('images/' + image, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)


def get_duck_image_url():
    try:
        url = 'https://random-d.uk/api/random'
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        return data['url']
    except Exception as e:
        print('Gagal mengambil gambar bebek:', e)
        return None


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send('Gagal mengambil gambar bebek, coba lagi nanti.')

@bot.command('kirimvideo')
async def kirimvideo(ctx):
    url = "https://www.youtube.com/watch?v=t0k5iOtPyfI"
    await ctx.send(url)


bot.run("")