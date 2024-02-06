from enum import Enum


class LevelInfo(Enum):
    #Week Titles
    NEWBIE = (1, 10, '#E0FFFF', 'Newbie')
    PAPER_SOLDIER = (11, 20, '#E0EEEE', 'Paper Soldier')
    PLASTIC_WARRIOR = (21, 30, '#D1EEEE', 'Plastic Warrior')
    TIN_SQUIRE = (31, 40, '#B0E0E6', 'Tin Squire')
    CARDBOARD_KNIGHT = (41, 50, '#ADD8E6', 'Cardboard Knight')
    SPONGE_DUKE = (51, 60, '#87CEEB', 'Sponge Duke')
    RUBBER_BARON = (61, 70, '#87CEFA', 'Rubber Baron')
    WOODEN_PRINCE = (71, 80, '#00BFFF', 'Wooden Prince')
    SOAPY_EMPEROR = (81, 90, '#1E90FF', 'Soapy Emperor')
    BUBBLE_KING = (91, 100, '#0000FF', 'Bubble King')
    #Better Titles
    STURDY_PAPER_WARRIOR = (101, 110, '#E6E0F8', 'Sturdy Paper Warrior')
    HARDENED_PLASTIC_KNIGHT = (111, 120, '#E0E6EE', 'Hardened Plastic Knight')
    REINFORCED_TIN_GUARDIAN = (121, 130, '#D1D1E0', 'Reinforced Tin Guardian')
    LAMINATED_CARDBOARD_CHAMPION = (131, 140, '#C2C2D6', 'Laminated Cardboard Champion')
    COMPRESSED_SPONGE_LORD = (141, 150, '#B3B3CC', 'Compressed Sponge Lord')
    DENSE_RUBBER_PATRIARCH = (151, 160, '#A4A4C2', 'Dense Rubber Patriarch')
    POLISHED_WOODEN_MONARCH = (161, 170, '#9595B8', 'Polished Wooden Monarch')
    GLOSSY_SOAPY_RULER = (171, 180, '#8686AE', 'Glossy Soapy Ruler')
    SHINY_BUBBLE_EMPEROR = (181, 190, '#7777A4', 'Shiny Bubble Emperor')
    ULTIMATE_BUBBLE_DEITY = (191, 200, '#68689A', 'Ultimate Bubble Deity')
    #Advanced Titles
    BUDDING_LEAF = (201, 210, '#A2CD5A', 'Budding Leaf')
    YOUNG_SAPLING = (211, 220, '#7CCD7C', 'Young Sapling')
    STURDY_BRANCH = (221, 230, '#8FBC8F', 'Sturdy Branch')
    WHISPERING_WILLOW = (231, 240, '#90EE90', 'Whispering Willow')
    ANCIENT_OAK = (241, 250, '#8B4513', 'Ancient Oak')
    MYSTIC_MAPLE = (251, 260, '#D2691E', 'Mystic Maple')
    ETERNAL_YEW = (261, 270, '#556B2F', 'Eternal Yew')
    WISE_WALNUT = (271, 280, '#DEB887', 'Wise Walnut')
    SOVEREIGN_SEQUOIA = (281, 290, '#A0522D', 'Sovereign Sequoia')
    DIVINE_DOUGLAS_FIR = (291, 300, '#B8860B', 'Divine Douglas Fir')
    #Common Titles
    EMERGING_HERO = (301, 310, '#7D9EC0', 'Emerging Hero')
    BRAVE_WANDERER = (311, 320, '#6B8E23', 'Brave Wanderer')
    DARING_ADVENTURER = (321, 330, '#DAA520', 'Daring Adventurer')
    CLEVER_STRATEGIST = (331, 340, '#B8860B', 'Clever Strategist')
    FEARLESS_SCOUT = (341, 350, '#CD853F', 'Fearless Scout')
    RESOURCEFUL_RANGER = (351, 360, '#8FBC8F', 'Resourceful Ranger')
    BOLD_WARRIOR = (361, 370, '#A52A2A', 'Bold Warrior')
    SWIFT_ROGUE = (371, 380, '#C0C0C0', 'Swift Rogue')
    KEEN_EXPLORER = (381, 390, '#4682B4', 'Keen Explorer')
    SHREWD_SURVIVOR = (391, 400, '#708090', 'Shrewd Survivor')
    #Rare Titles
    VALIANT_KNIGHT = (401, 410, '#4169E1', 'Valiant Knight')
    WISE_SAGE = (411, 420, '#6A5ACD', 'Wise Sage')
    FEARLESS_COMMANDER = (421, 430, '#483D8B', 'Fearless Commander')
    MYSTICAL_ENCHANTER = (431, 440, '#9370DB', 'Mystical Enchanter')
    SHADOW_ASSASSIN = (441, 450, '#4B0082', 'Shadow Assassin')
    ARCANE_WIZARD = (451, 460, '#9400D3', 'Arcane Wizard')
    DRAGON_SLAYER = (461, 470, '#FF4500', 'Dragon Slayer')
    DEMON_HUNTER = (471, 480, '#B22222', 'Demon Hunter')
    CELESTIAL_GUARDIAN = (481, 490, '#00CED1', 'Celestial Guardian')
    PHOENIX_RIDER = (491, 500, '#FF8C00', 'Phoenix Rider')
    #Epic Titles
    IMMORTAL_PHOENIX = (501, 510, '#FF4500', 'Immortal Phoenix')
    ETERNAL_DRAGON = (511, 520, '#C71585', 'Eternal Dragon')
    LEGENDARY_WIZARD = (521, 530, '#4B0082', 'Legendary Wizard')
    MYTHICAL_KNIGHT = (531, 540, '#8A2BE2', 'Mythical Knight')
    SUPREME_SORCERER = (541, 550, '#9400D3', 'Supreme Sorcerer')
    INVINCIBLE_WARRIOR = (551, 560, '#FF8C00', 'Invincible Warrior')
    SAGE_OF_TIME = (561, 570, '#00CED1', 'Sage of Time')
    GUARDIAN_OF_REALMS = (571, 580, '#20B2AA', 'Guardian of Realms')
    MASTER_OF_SHADOWS = (581, 590, '#696969', 'Master of Shadows')
    CONQUEROR_OF_CHAOS = (591, 600, '#708090', 'Conqueror of Chaos')
    #Master Titles
    ARCHMAGE_OF_ELEMENTS = (601, 610, '#FFD700', 'Archmage of Elements')
    OVERLORD_OF_SHADOWS = (611, 620, '#9400D3', 'Overlord of Shadows')
    WARDEN_OF_THE_REALMS = (621, 630, '#48D1CC', 'Warden of the Realms')
    CHAMPION_OF_THE_LIGHT = (631, 640, '#FAFAD2', 'Champion of the Light')
    BEASTMASTER_OF_THE_WILD = (641, 650, '#228B22', 'Beastmaster of the Wild')
    FORGEMASTER_OF_RUNES = (651, 660, '#B8860B', 'Forgemaster of Runes')
    SORCERER_OF_THE_ABYSS = (661, 670, '#4B0082', 'Sorcerer of the Abyss')
    GUARDIAN_OF_TIME = (671, 680, '#00FFFF', 'Guardian of Time')
    DRAGONLORD_OF_ETERNITY = (681, 690, '#FF8C00', 'Dragonlord of Eternity')
    EMPEROR_OF_THE_GALAXY = (691, 700, '#800080', 'Emperor of the Galaxy')
    #Legendar Titles
    COSMIC_SORCERER = (701, 710, '#FFD700', 'Cosmic Sorcerer')
    GALACTIC_OVERLORD = (711, 720, '#9400D3', 'Galactic Overlord')
    ETERNAL_GUARDIAN = (721, 730, '#48D1CC', 'Eternal Guardian')
    LIGHT_BRINGER = (731, 740, '#FAFAD2', 'Light Bringer')
    WILD_SPIRIT_MASTER = (741, 750, '#228B22', 'Wild Spirit Master')
    RUNIC_DEMIGOD = (751, 760, '#B8860B', 'Runic Demigod')
    ABYSSAL_COMMANDER = (761, 770, '#4B0082', 'Abyssal Commander')
    TIMELESS_PROTECTOR = (771, 780, '#00FFFF', 'Timeless Protector')
    DRAGON_EMPEROR = (781, 790, '#FF8C00', 'Dragon Emperor')
    GALAXY_CONQUEROR = (791, 800, '#800080', 'Galaxy Conqueror')
    #Mistic Titles
    ARCHITECT_OF_REALITIES = (801, 810, '#FF69B4', 'Architect of Realities')
    TIME_WEAVER = (811, 820, '#C71585', 'Time Weaver')
    COSMOS_COMMANDER = (821, 830, '#8A2BE2', 'Cosmos Commander')
    VOID_WALKER = (831, 840, '#9400D3', 'Void Walker')
    ELEMENTAL_SAGE = (841, 850, '#9932CC', 'Elemental Sage')
    SHADOW_MASTER = (851, 860, '#8B008B', 'Shadow Master')
    LIGHT_KEEPER = (861, 870, '#FF00FF', 'Light Keeper')
    GALAXY_SHAPER = (871, 880, '#BA55D3', 'Galaxy Shaper')
    REALM_FORGER = (881, 890, '#9370DB', 'Realm Forger')
    DIVINITY_ASCENDANT = (891, 900, '#8A2BE2', 'Divinity Ascendant')
    

    def __init__(self, min_level, max_level, color, title):
        self.min_level = min_level
        self.max_level = max_level
        self.color = color
        self.title = title

    @classmethod
    def get_info_for_level(cls, level):
        for level_info in cls:
            if level_info.min_level <= level <= level_info.max_level:
                return level_info.color, level_info.title
        return None, None
