import discord
from discord.ext import commands
from flywithdsc import database, scraper, config

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}, ID:{client.user.id}')
    database.initialize_database(config.DATABASE_URL)


@client.command()
async def helpme(ctx: commands.Context):
    embeded = discord.Embed(title='🛠️Available commands:', colour=discord.Colour.dark_blue())
    embeded.add_field(name='!helpme - Shows this message', value='', inline=False)
    embeded.add_field(name='!refreshdb [Ryanair] [WMI] [PFO] [YES/NO](Roundtrip)- Refreshes the database for the flights',  value='', inline=False)
    await ctx.send(embed=embeded)

@client.command()
async def refreshdb(ctx: commands.Context, airline: str, from_code: str, to_code: str, roundtrip: str):
    if airline == 'Ryanair':
        
        total = 0

        download = scraper.scrape_flights(from_code, to_code)
        dwnl_count = int(len(download) / 7)
        total += dwnl_count
        for x in range(1, dwnl_count+1):
            database.save_flight(config.DATABASE_URL, download[(x-1)*7:x*7])
        
        if roundtrip.lower() == 'yes':
            download = scraper.scrape_flights(to_code, from_code)
            dwnl_count = int(len(download) / 7)
            total += dwnl_count
            for x in range(1, dwnl_count+1):
                database.save_flight(config.DATABASE_URL, download[(x-1)*7:x*7])

        embeded = discord.Embed(title='✅ Ryanair Database Updated',
                                description=f'Processed {total} flights',
                                colour=discord.Colour.green()
                                )
        await ctx.send(embed=embeded)
    else:
        await ctx.send(f'Wrong airline provided: {airline}!')

@client.command()
async def find(ctx: discord.Context):
    # TBD: Searching algorithm
    await ctx.send()