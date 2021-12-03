#!/usr/bin/python3

#pip3 install discord.py

########################### Дискорд
import os
import discord #pip3 install discord.py
import asyncio
from discord.ext import commands #pip3 install discord.py
############################
from multiprocessing import Process
from threading import Thread
put = os.path.dirname(os.path.realpath(__file__)) + "/"#Путь- (part-1)
from time import strftime, localtime, sleep #Для (Time)
import tic
############################ json модуль
import json
with open(f"{put}sonf.json", "r") as read_file:
    X_Pars = json.load(read_file)
############################
admin_list_id = X_Pars['admin_list_id']

TOKEN = X_Pars['token']
#bot = commands.Bot(command_prefix=X_Pars['prefix'])
bot = commands.Bot(command_prefix = X_Pars['prefix'], intents = discord.Intents.all())
client = discord.Client()
bot.remove_command("help")

import calendar
import bd_module
################################################
### Старт бота.
@bot.event
async def on_ready():
    print("Бот онлайн!!!")

    variable = Thread(target=tis)
    variable.start()

    print("УСПЕХ!!!")


async def D_API(guild, role, ls):
    user = await guild.fetch_member(ls)
    print(f"СНЯТЬ У {user.name}")
    print(f"guild {guild}")
    print(f"role {role.id}")
    await user.remove_roles(role)
    bd_module.rm_mut(user.id, role.id)
    #print(f"СНЯТ")

    #print(role.name)
    #print(role.members)

def tis():
    while True: # Не оптимально когда людей дахера!
        #time.sleep(5*60)
        print("ДА")
        #sleep(30)
        sleep(60*5)
        for ls in bd_module.ls_mut():
            ls = ls[0]
            Date, Time, guild_id = bd_module.read_mut(ls)
            print(guild_id)

            if tic.test(Date, Time):
                guild = bot.get_guild(guild_id) # получаем объект сервера*
                #user = await guild.fetch_member(ls)

                role = guild.get_role(bd_module.role_read_mut(guild_id))
                print("НУ?")
                bot.loop.create_task(D_API(guild, role, ls))



@bot.command(pass_context=True, aliases=['help']) #разрешаем передавать агрументы
async def h(ctx): #создаем асинхронную фунцию бота
    for admin_id in admin_list_id:
        if admin_id == ctx.author.id:
            await ctx.send("```/w <ID> # Выдать/повысить варнинг\n/unw <ID> # Понизить/убрать варнинг\n/mut <ВРЕМЯ_В_ЧАСАХ> <ID> # Выдать мут на (Дробные работают.)```")
            exit()



@bot.command(pass_context=True) #разрешаем передавать агрументы
async def w(ctx, u_id): #создаем асинхронную фунцию бота
    for admin_id in admin_list_id:
        if admin_id == ctx.author.id:
            u_id = u_id.replace('<', '')
            u_id = u_id.replace('>', '')
            u_id = u_id.replace('@', '')
            u_id = u_id.replace('!', '')
            u_id = int(u_id)
            print(u_id)


            guild_id = ctx.message.guild.id
            print(f"guild_id - {guild_id}")
            guild = bot.get_guild(guild_id) # получаем объект сервера*
            X_Roleid = bd_module.role_read_w(guild_id)
            user = await guild.fetch_member(u_id)

            a = 0

            for sss in user.roles:
                print(sss.id)
                if X_Roleid[0] == sss.id:
                    a = a + 100
                if X_Roleid[1] == sss.id:
                    a = a + 10
                if X_Roleid[2] == sss.id:
                    a = a + 1
            if a == 0:
                role = guild.get_role(X_Roleid[0])
                await user.add_roles(role)
                await ctx.send("w0 ➡️ w1 ✅") #отправляем обратно аргумент
                print("w0 ➡️ w1 ✅")
                bd_module.add_w(user.id, user.name, role.id, role.name)
            elif a == 100:
                role = guild.get_role(X_Roleid[1])
                await user.add_roles(role)
                await ctx.send("w1 ➡️ w2 ✅") #отправляем обратно аргумент
                print("w1 ➡️ w2 ✅")
                bd_module.add_w(user.id, user.name, role.id, role.name)
            elif a == 110:
                role = guild.get_role(X_Roleid[2])
                await user.add_roles(role)
                await ctx.send("w2 ➡️ w3 ✅") #отправляем обратно аргумент
                print("w2 ➡️ w3 ✅")
                bd_module.add_w(user.id, user.name, role.id, role.name)
        exit()


@bot.command(pass_context=True) #разрешаем передавать агрументы
async def unw(ctx, u_id): #создаем асинхронную фунцию бота
    for admin_id in admin_list_id:
        if admin_id == ctx.author.id:
            u_id = u_id.replace('<', '')
            u_id = u_id.replace('>', '')
            u_id = u_id.replace('@', '')
            u_id = u_id.replace('!', '')
            guild_id = ctx.message.guild.id
            print(f"guild_id - {guild_id}")
            guild = bot.get_guild(guild_id) # получаем объект сервера*
            X_Roleid = bd_module.role_read_w(guild_id)
            user = await guild.fetch_member(u_id)

            a = 0

            for sss in user.roles:
                print(sss.id)
                if X_Roleid[0] == sss.id:
                    a = a + 100
                if X_Roleid[1] == sss.id:
                    a = a + 10
                if X_Roleid[2] == sss.id:
                    a = a + 1
            if a == 100:
                role = guild.get_role(X_Roleid[0])
                print(role.id)
                await user.remove_roles(role)
                await ctx.send("w1 ➡️ w0 ✅") #отправляем обратно аргумент
                print("w1 ➡️ w0 ✅")
                bd_module.rm_w(user.id, role.id)
            elif a == 110:
                role = guild.get_role(X_Roleid[1])
                await user.remove_roles(role)
                await ctx.send("w2 ➡️ w1 ✅") #отправляем обратно аргумент
                print("w2 ➡️ w1 ✅")
                bd_module.rm_w(user.id, role.id)
            elif a == 111:
                role = guild.get_role(X_Roleid[2])
                await user.remove_roles(role)
                await ctx.send("w3 ➡️ w2 ✅") #отправляем обратно аргумент
                print("w3 ➡️ w2 ✅")
                bd_module.rm_w(user.id, role.id)
        exit()

@bot.command(pass_context=True) #разрешаем передавать агрументы
async def mut(ctx, time, u_id): #создаем асинхронную фунцию бота
    for admin_id in admin_list_id:
        if admin_id == ctx.author.id:
            u_id = u_id.replace('<', '')
            u_id = u_id.replace('>', '')
            u_id = u_id.replace('@', '')
            u_id = u_id.replace('!', '')
            guild_id = ctx.message.guild.id
            print(f"guild_id - {guild_id}")
            guild = bot.get_guild(guild_id) # получаем объект сервера*
            Roleid = bd_module.role_read_mut(guild_id)

            user = await guild.fetch_member(u_id)
            role = guild.get_role(Roleid)
            # 10080
            m = int(strftime("%M"))
            ch = int(strftime("%H"))
            ch2 = 0 # Финальная
            G = int(strftime("%Y")) # Год
            M = int(strftime("%m")) # Месяц
            D = int(strftime("%d")) # День
            time = float(time) + ch
            print (ch)
            print(time)
            TUL = True
            while TUL == True:

                if M == 13:
                    M = 1
                    G = G + 1
                print(f"{time} - Время")
                if float(time) > 24:
                    print("!")
                    if float(time) > ((calendar.monthrange(G, M)[1]) - D + 1) * 24:
                        time = (float(time) - ((calendar.monthrange(G, M)[1]) - D) * 24)
                        M = M + 1
                        D = 0
                    else:
                        print("!!!")
                        time = float(time) - 24
                        D = D + 1
                        #print(time)

                else:
                    if float(time) < 1:
                        print(f"{time} - Время")
                        print(f"{ch} - Часы")
                        m2 = float(time) * 60
                        m = m + m2
                        if m > 60:
                            m = m - 60
                            ch = ch + 1
                            if ch > 24:
                                ch = 0
                                D = D + 1
                                if D > (calendar.monthrange(G, M)[1]):
                                    D = 1
                                    M = M + 1
                                    if M > 12:
                                        M = 1
                                        G = G + 1
                        TUL = False
                    else:
                        time = float(time) - 1
                        ch2 = ch2 + 1

            print(f"{G}:{M}:{D} - {ch2}:{int(m)}" )
            unaim = user.name
            bd_module.add_mut(u_id, unaim, role.id, role.name, f"{G}:{M}:{D}", f"{ch2}:{int(m)}")
            await user.add_roles(role)
            await ctx.send(f"Мут выдан пользователю <@{user.id}> или {unaim} до {G}:{M}:{D} - {ch2}:{int(m)}")
        exit()

@bot.event
async def on_member_join(member):
    guild_id = member.guild.id
    print(f"guild_id - {guild_id}")
    guild = bot.get_guild(guild_id) # получаем объект сервера*
    user = await guild.fetch_member(member.id)
    hi = bd_module.role_read_hi(guild_id)
    if hi != 0:
        role = guild.get_role(hi)
        await user.add_roles(role)
        print(f"Выдона роли {role.name} пользователю {member.name}")

    #print(member.id)
    #print(bd_module.cek_mut(member.id))
    if bd_module.cek_mut(member.id):
        role = guild.get_role(bd_module.role_read_mut(guild_id))
        await user.add_roles(role)
        print(f"Восстановление роли {role.name} у {member.name}")
    for A in bd_module.read_w(member.id):
        A = A[0]
        print(A)
        guild = bot.get_guild(guild_id)
        role = guild.get_role(A)
        await user.add_roles(role)
        print(f"Восстановление роли {role.name} у {member.name}")



bot.run(TOKEN)
