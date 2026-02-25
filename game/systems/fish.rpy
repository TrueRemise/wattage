

default fish_list = [
    {"name":"Phish",  "rarity":1, "toughness":1, "weight":3, "effect":"nothing", "desc":"The classic fish in the sea"},
    {"name":"Offish Worker",  "rarity":1, "toughness":1, "weight":4, "effect":"nothing", "desc":"They are kelping up with the deadline"},
    {"name":"Shr7mple",  "rarity":1, "toughness":2, "weight":4, "effect":"nothing", "desc":"He forgot to crabture the moment"},
    {"name":"The Pacifish",  "rarity":1, "toughness":3, "weight":4, "effect":"nothing", "desc":"Eel don't want to sea his angler"},
    {"name":"Fi",  "rarity":1, "toughness":1, "weight":3, "effect":"nothing", "desc":"Perfishly deformed"},
    {"name":"The Fishter",  "rarity":1, "toughness":4, "weight":4, "effect":"nothing", "desc":"He wants to taste defish"},
    {"name":"Bufferfish",  "rarity":1, "toughness":3, "weight":4, "effect":"effect_1_try", "desc":"Still in quill"},
    {"name":"Number Fishteen",  "rarity":1, "toughness":6, "weight":14, "effect":"effect_5_sol", "desc":"Barb Gar Krill Fugu Lake Trout"},
    {"name":"Gar of Char",  "rarity":1, "toughness":4, "weight":14, "effect":"effect_neg_5_sol", "desc":"He ate a lot that night"},
    {"name":"Sunfish", "rarity":2, "toughness":5, "weight":21, "effect":"effect_neg_10_sol", "desc":"Holy carp!"},
    {"name":"Snow Tuna", "rarity":2, "toughness":4, "weight":24, "effect":"effect_2_try", "desc":"The emoceanal"},
    {"name":"ManHake", "rarity":2, "toughness":4, "weight":25, "effect":"effect_nemu_1", "desc":"Heard you like fish girl me too"},
    {"name":"Fish and Hungar", "rarity":2, "toughness":7, "weight":25, "effect":"effect_neg_1_try", "desc":"He's getting hungry"},
    {"name":"Clownfish", "rarity":2, "toughness":5, "weight":26, "effect":"effect_10_sol", "desc":"Turn into female when it's the time"},
    {"name":"Sacabambaspis", "rarity":2, "toughness":6, "weight":26, "effect":"effect_1_weight", "desc":"The ancient fish!"},
    {"name":"Blahaj", "rarity":2, "toughness":6, "weight":26, "effect":"effect_20_sol", "desc":"The IKEA fish!"},
    {"name":"Fitus",  "rarity":2, "toughness":5, "weight":34, "effect":"effect_neg_20_sol", "desc":"prawn.ogg"},
    {"name":"South Fish", "rarity":2, "toughness":6, "weight":36, "effect":"effect_sari", "desc":"Can be made into good sauce"},
    {"name":"Dollar Chums", "rarity":2, "toughness":8, "weight":36, "effect":"effect_1_luck", "desc":"A little taste to your baits"},
    {"name":"Jumbo Fish", "rarity":3, "toughness":15, "weight":50, "effect":"effect_toko_1", "desc":"I think his fish looks delicious"},
    {"name":"Dried Fish", "rarity":3, "toughness":22, "weight":44, "effect":"nothing", "desc":"Caught this in a Pool, What?"},
    {"name":"Hallucirenia", "rarity":3, "toughness":8, "weight":75, "effect":"effect_1_resilience", "desc":"I sure don't want to get in troubles"},
    {"name":"Stone Fish", "rarity":4, "toughness":30, "weight":150, "effect":"effect_stone", "desc":"You wouldn't want this in your kidney"},
    {"name":"FISCP-169", "rarity":4, "toughness":50, "weight":225, "effect":"effect_10_size", "desc":"You have offishially become the legendary fisher"},
]
default fish_catch_counts = {}

init python:
    def apply_fish_effect(fish):
        global fish_effect, nemu_manhake

        fish_name = fish.get("name")
        if fish_name:
            fish_catch_counts[fish_name] = fish_catch_counts.get(fish_name, 0) + 1

        eff = fish.get("effect", "nothing")

        # --- No Effect ---
        if eff == "nothing":
            fish_effect = "NO EFFECT"
            return

        # --- Manual Effects ---
        if eff == "effect_10_sol":
            sol_add(10)
            fish_effect = "SOL + 10"
            return

        if eff == "effect_5_sol":
            sol_add(5)
            fish_effect = "SOL + 5"
            return

        if eff == "effect_20_sol":
            sol_add(20)
            fish_effect = "SOL + 20"
            return

        if eff == "effect_neg_5_sol":
            sol_lose(5)
            fish_effect = "SOL - 5"
            return

        if eff == "effect_neg_10_sol":
            sol_lose(10)
            fish_effect = "SOL - 10"
            return

        if eff == "effect_neg_20_sol":
            sol_lose(20)
            fish_effect = "SOL - 20"
            return

        if eff == "effect_1_weight":
            upgrade_rod("maxweight", 1)
            fish_effect = "+1 MAX WEIGHT"
            return

        if eff == "effect_1_luck":
            upgrade_rod("luck", 1)
            fish_effect = "+1 LUCK"
            return

        if eff == "effect_1_resilience":
            upgrade_rod("resilience", 1)
            fish_effect = "+1 RESILIENCE"
            return

        if eff == "effect_10_size":
            upgrade_rod("size", 10)
            fish_effect = "+10 SIZE"
            return

        if eff == "effect_nemu_1":
            nemu_manhake = True
            fish_effect = "NO EFFECT"
            return
        
        if eff == "effect_toko_1":
            toko_jumbo = True
            fish_effect = "CAN BE USED FOR TOKO'S COOKING"
            return

        # --- fallback ---
        fish_effect = eff.upper()



#    Luck  Common%  Rare%  Epic%  Legendary%
#0      0     80.0   20.0    0.0         0.0
#1      5     76.7   22.1    1.1         0.2
#2     10     73.3   24.2    2.2         0.3
#3     15     70.0   26.2    3.2         0.5
#4     20     66.7   28.3    4.3         0.7
#5     25     63.3   30.4    5.4         0.8
#6     30     60.0   32.5    6.5         1.0
#7     35     56.7   34.6    7.6         1.2
#8     40     53.3   36.7    8.7         1.3
#9     45     50.0   38.8    9.8         1.5
#10    50     46.7   40.8   10.8         1.7
#11    55     43.3   42.9   11.9         1.8
#12    60     40.0   45.0   13.0         2.0
#13    65     36.9   45.0   15.8         2.4
#14    70     33.8   45.0   18.5         2.8
#15    75     30.6   45.0   21.2         3.1
#16    80     27.5   45.0   24.0         3.5
#17    85     24.4   45.0   26.8         3.9
#18    90     21.2   45.0   29.5         4.2
#19    95     18.1   45.0   32.2         4.6
#20   100     15.0   45.0   35.0         5.0
#21   105     14.5   43.1   36.3         6.0
#22   110     14.1   41.3   37.7         7.0
#23   115     13.6   39.4   39.0         8.0
#24   120     13.1   37.5   40.3         9.0
#25   125     12.7   35.7   41.7        10.0
#26   130     12.2   33.8   43.0        11.0
#27   135     11.7   31.9   44.3        12.0
#28   140     11.3   30.1   45.7        13.0
#29   145     10.8   28.2   47.0        14.0
#30   150     10.3   26.3   48.3        15.0
#31   155      9.9   24.5   49.7        16.0
#32   160      9.4   22.6   51.0        17.0
#33   165      8.9   20.7   52.3        18.0
#34   170      8.5   18.9   53.7        19.0
#35   175      8.0   17.0   55.0        20.0
#36   180      7.7   16.3   53.0        23.1
#37   185      7.3   15.5   51.0        26.1
#38   190      7.0   14.8   49.0        29.2
#39   195      6.7   14.1   47.0        32.3
#40   200      6.3   13.3   45.0        35.3
#41   205      6.0   12.6   43.0        38.4
#42   210      5.7   11.9   41.0        41.5
#43   215      5.3   11.1   39.0        44.5
#44   220      5.0   10.4   37.0        47.6
#45   225      4.7    9.7   35.0        50.7
#46   230      4.3    8.9   33.0        53.7
#47   235      4.0    8.2   31.0        56.8
#48   240      3.7    7.5   29.0        59.9
#49   245      3.3    6.7   27.0        62.9
#50   250      3.0    6.0   25.0        66.0