from discord.ext import commands
import random
import discord

class Do(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.inventory = {}  # ดิกชันนารีสำหรับเก็บข้อมูลกระเป๋า

    @commands.command()
    async def do(self, ctx, *, action: str):
        # แปลง action เป็นตัวพิมพ์เล็กเพื่อตรวจสอบ
        action = action.lower()
        user_id = ctx.author.id  # ใช้ ID ของผู้ใช้เป็นกุญแจ
        user_mention = ctx.author.mention  # ดึงแท็กผู้ใช้

        # สร้างกระเป๋าใหม่ให้กับผู้ใช้ถ้ายังไม่มี
        if user_id not in self.inventory:
            self.inventory[user_id] = {'ไม้': 0, 'หิน': 0, 'เนื้อ': 0, 'หนังสัตว์': 0}

        # กำหนด Embed
        embed = discord.Embed(title="🔍ระบบหาทรัพยากร", color=discord.Color.green())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)

        # สุ่มผลลัพธ์ตาม action ที่ผู้ใช้ระบุ
        if action == "ตัดไม้":
            wood_count = random.randint(1, 3)
            self.inventory[user_id]['ไม้'] += wood_count
            embed.description = (f'{user_mention} 🪓ทำการตัดไม้\n'
                                 f'🌲ได้รับท่อนไม้ ` {wood_count} ` ea')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1293942978439680093/1293951696791404635/latest.png?ex=67093dec&is=6707ec6c&hm=93ecef5f56e149e0ae64e96c7edf48137e345f4ffc6c24721b97e9ea40db0062&')
            embed.color = discord.Color.green()  # สีเขียวสำหรับตัดไม้

        elif action == "ขุดหิน":
            stone_count = random.randint(1, 3)
            self.inventory[user_id]['หิน'] += stone_count
            embed.description = (f'{user_mention} ⛏️ทำการขุดหิน\n'
                                 f'🪨ได้รับก้อนหิน ` {stone_count} ` ea')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1293942978439680093/1293952030141841532/latest.png?ex=67093e3c&is=6707ecbc&hm=e4e3c80e45420c8c7dc3d0fd80a5c8e61226542df301c0e1bbd2ebbaa31c6e24&')
            embed.color = discord.Color.from_rgb(128, 128, 128)  # สีเทาสำหรับขุดหิน

        elif action == "ล่าสัตว์":
            meat_count = random.randint(1, 3)
            self.inventory[user_id]['เนื้อ'] += meat_count

            # ระบบสุ่มหนังสัตว์
            chance_of_hide = random.randint(1, 100)  # สุ่มเลข 1-100

            # เปลี่ยนให้ skin_count สามารถเป็น 0 หรือ 1
            skin_count = 0
            if chance_of_hide <= 50:  # กำหนดเปอร์เซ็นต์ที่ได้หนังสัตว์ (50%)
                skin_count = 1  # ได้รับหนังสัตว์ 1 ชิ้น
                self.inventory[user_id]['หนังสัตว์'] += skin_count
                embed.description = (f'{user_mention} 🏹ทำการล่าสัตว์\n'
                                     f'🥩ได้รับเนื้อ ` {meat_count} ` ea\n'
                                     f'🦌และหนังสัตว์ ` {skin_count} ` ea! 🎉')
            else:
                embed.description = (f'{user_mention} 🏹ทำการล่าสัตว์\n'
                                     f'🥩ได้รับเนื้อ ` {meat_count} ` ea\n'
                                     f'🦌แต่ไม่ได้หนังสัตว์ 🥺')

            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1293942978439680093/1293951758053281882/latest.png?ex=67093dfb&is=6707ec7b&hm=d526168d33ac62e3667ea4bf83197cd940ead67a6f2112b33dc2df1630c127f4&')
            embed.color = discord.Color.red()  # สีแดงเข้มสำหรับล่าสัตว์

        else:
            embed.description = "❌ รูปแบบคำสั่งไม่ถูกต้อง! ใช้: .do ตัดไม้, .do ขุดหิน หรือ .do ล่าสัตว์"
            embed.color = discord.Color.red()  # สีแดงสำหรับคำสั่งที่ไม่ถูกต้อง

        await ctx.send(embed=embed)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Do(bot))
