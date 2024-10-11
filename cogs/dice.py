from discord.ext import commands
import random
import re

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx, *, arg: str):
        # ตรวจสอบรูปแบบคำสั่ง 1d10
        match = re.match(r'(\d+)d(\d+)([+-]?\d+)?', arg)
        if match:
            num_dice = int(match.group(1))  # จำนวนลูกเต๋า
            dice_sides = int(match.group(2))  # จำนวนด้านของลูกเต๋า
            modifier = int(match.group(3)) if match.group(3) else 0  # ค่าปรับ (+/-)

            if num_dice <= 0 or dice_sides <= 0:
                await ctx.send("❌กรุณาใส่คำสั่งให้ถูกต้อง!")
                return

            # ทอยลูกเต๋า
            results = [random.randint(1, dice_sides) for _ in range(num_dice)]
            total = sum(results) + modifier

            # สร้างสตริงสำหรับค่าปรับ
            modifier_str = f' + {modifier}' if modifier > 0 else f' - {abs(modifier)}' if modifier < 0 else ''

            await ctx.send(f'**ผลลัพธ์ :** {results}{modifier_str}\n**รวม :** ` {total}{" " if modifier != 0 else ""}`')
        else:
            await ctx.send("❌รูปแบบคำสั่งไม่ถูกต้อง! เช่น 1d10")

async def setup(bot):
    await bot.add_cog(Dice(bot))
