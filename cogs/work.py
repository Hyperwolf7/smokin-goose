import discord
import json
from discord.ext import commands


class WorkCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def jobs(self, ctx):
      with open("./json/jobs.json", "r") as f:
        jobslist = json.load(f)

      embed = discord.Embed(title="Jobs")

      for job in jobslist:
        embed.add_field(name=f"{(jobslist[job]['emoji'])} {job.title()}:", value=f"{jobslist[job]['description']}\n**Salary** - {jobslist[job]['salary']:,}\n**Work Hours Required** - {jobslist[job]['work_hours_required']}")

      await ctx.reply(embed=embed)
      



def setup(bot):
  bot.add_cog(WorkCommand(bot))
