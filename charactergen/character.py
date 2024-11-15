import copy
import operator
import random

import charactergen.characterclass as characterclass 
from charactergen.mixins import BasicAttributesMixin, BasicAttribRaceMixin, AppearenceMixin, AscendingAcMixin, HitDiceMixin, PsionicWildTalentMixin
from charactergen.dice import d, xdy


def _is_halfling(INT, CON, DEX, STR):
    return STR > 11 and DEX >= 9 and CON >= 9, characterclass.HALFLING

def _is_elf(INT, CON, DEX, STR):
    return INT > 11 and STR >= 9, characterclass.ELF

def _is_dwarf(INT, CON, DEX, STR):
    return CON > 11 and STR >= 9, characterclass.DWARF

def _num_to_str(num):
    if num > 0:
        num = "+%d" % num
    return str(num)

class Character(BasicAttributesMixin, AppearenceMixin):
    """
    D&D characters are structurally quite similar. Common aspects of character
    creation are managed here. Subclasses for the different systems handle
    differences between the editions.
    """

    def __init__(self, *args, **kwargs):
        classname = kwargs.pop('classname', None)
        testing = kwargs.pop('testing', False)

        super(Character, self).__init__(*args, **kwargs)

        self.character_class = self.get_character_class(classname)
        self.level = 1
        self.class_name = self.character_class['name']
        self.personality = self.get_personality()
        if testing:
            return
        self.equipment = self.get_equipment()
        self.hp = self.get_hp()
        if self.hp is not None and self.hp < 1:
            self.hp = 1
        self.ac = self.get_ac()
        self.thac9 = self.get_thac9()
        self.to_hit = self.get_to_hit_table()
        self.saves = self.get_saves()
        self.languages = self.get_languages()
        self.spell = self.get_spell()
        self.notes = self.get_notes()
        self.skills = self.get_skills()

    def to_dict(self):
        """
        We use vars to convert the object to a dictionary, and then replace
        the character_class attribute with it's name.
        """
        attributes = vars(self)
        attributes["class"] = attributes["class_name"]
        del attributes["character_class"]
        del attributes["class_name"]
        attributes["system"] = self.system
        return attributes

    @property
    def system(self):
        raise NotImplementedError()

    @property
    def thieves(self):
        return True

    @property
    def demihumans(self):
        return True

    @property
    def num_first_level_spells(self):
        return 12

    @property
    def hit_die(self):
        """
        Get the character's hit die.
        """
        return self.character_class['hitdice']

    @property
    def max_ac(self):
        """
        The max AC to display in to-hit table.
        """
        return 0

    @property
    def max_to_hit(self):
        """
        The max value to display in to-hit table.
        """
        return 9 - self.max_ac + 1

    @property
    def save_name_table(self):
        return characterclass.SAVES

    @property
    def saves_with_names(self):
        return dict((s, (self.save_name_table[s], v)) for s, v in self.saves.items())

    def get_character_class(self, classname=None):
        """
        We determine character class based on your prime attribute.
        """
        if classname:
            return characterclass.CLASS_BY_NAME[classname]
        if self.demihumans and d(100) < 50:
            # sorted attributes (excluding charisma)
            attributes = sorted(self.attributes[:5], reverse=True,
                                key=operator.itemgetter(1))
            if not (self.thieves and 'DEX' == attributes[0][0] and d(100) < 80):
                # We randomly test because there is overlap in what could
                # succeed and we want each to be equally likely in the long
                # run.
                tests = [_is_dwarf, _is_halfling, _is_elf]
                random.shuffle(tests)
                for t in tests:
                    result, c = t(self.INT, self.CON, self.DEX, self.STR)
                    if result:
                        return c
        # You're playing a human!
        index = 4 if self.thieves else 3
        prime_attribute, _ = sorted(self.attributes[:index],
                                    reverse=True, key=operator.itemgetter(1))[0]
        return characterclass.PRIME_REQUISITE[prime_attribute]

    def get_equipment(self):
        return self.character_class['equipment'][xdy(3,6)-3]

    def get_hp(self):
        """
        Determine HP based on hit dice and CON modifiers. Note: this value may
        be negative and that is handled by the caller.
        """
        return d(self.hit_die) + self.get_bonus(*self.attributes[characterclass.CON])

    def get_ac(self):
        """
        The character's armor class based on their starting equipment.
        """
        if "Leather Armor" in self.equipment:
            ac = 7
        elif "Chain Armor" in self.equipment:
            ac = 5
        elif "Plate Armor" in self.equipment:
            ac = 3
        else: # no armor
            ac = 9
        if "Shield" in self.equipment:
            ac = ac - 1
        return ac

    def get_thac9(self):
        """
        To Hit AC 9 is 10 by default.
        """
        return 10

    def get_to_hit_table(self):
        """
        Generate the to-hit table.
        """
        acs = range(9, self.max_ac - 1, -1)
        rolls = range(self.thac9, self.thac9 + self.max_to_hit)
        return [(ac, roll) for ac, roll in zip(acs, rolls)]

    def get_saves(self):
        """
        The character's saving throw tables. We proxy to the CharacterClass
        tables.
        """
        return self.character_class['saves']

    def get_languages(self):
        """
        For each bonus point for intelligence, a character knows an additional
        language, beyond Common and their alignment language.
        """
        bonus = self.get_bonus(*self.attributes[characterclass.INT])
        if bonus < 0:
            bonus = 0
        return random.sample(characterclass.LANGUAGES, bonus)

    def get_spell(self):
        """
        Magic-Users and Elves begin with a single first level spell.
        """
        if 'spells' in self.character_class.keys():
            spells = self.character_class['spells'][:self.num_first_level_spells]
            return [random.choice(spells)]
        return None

    def get_personality(self):
        return ', '.join(random.sample(characterclass.PERSONALITY, 1))

    def get_notes(self):
        """
        Are there any additional notes about the character?
        """
        return []

    def get_skills(self):
        """
        Return any character skills, like thief abilities.
        """
        return None


class BasicCharacter(Character):
    """
    Models a Moldvay/Mentzer basic D&D character.
    """

    @property
    def system(self):
        return "Basic D&D"

    def get_ac(self):
        """
        In Basic D&D DEX improves your AC.
        """
        ac = super(BasicCharacter, self).get_ac()
        ac = ac - self.get_bonus(*self.attributes[characterclass.DEX])
        return ac

    def get_thac9(self):
        """
        In Basic D&D your strength improves your to hit.
        """
        thac9 = super(BasicCharacter,self).get_thac9()
        str_bonus = self.get_bonus(*self.attributes[characterclass.STR])
        return thac9 - str_bonus

    def get_saves(self):
        """
        Your magic based saves are effected by your WIS.
        """
        saves = copy.copy(self.character_class['saves'])
        wisdom_bonus = self.get_bonus(*self.attributes[characterclass.WIS])
        for save in ['magic', 'stone', 'wands']:
            saves[save] = saves[save] - wisdom_bonus
        return saves


class LotFPCharacter(AscendingAcMixin, Character):

    @property
    def system(self):
        return "LotFP"

    @property
    def save_name_table(self):
        return characterclass.LOTFP['saves']

    @property
    def hit_die(self):
        return characterclass.LOTFP['hitdice'][self.character_class['name']]

    def roll_attribute_scores(self):
        """
        In LotFP you re-roll your characters scores if they don't produce a
        positive value for your total bonuses.
        """
        while True:
            attributes = super(LotFPCharacter, self).roll_attribute_scores()
            bonuses = [self.get_bonus(attr, val) for attr, val in attributes]
            total_bonuses = sum(bonuses)
            if total_bonuses >= 0:
                break
        return attributes

    def get_hp(self):
        """
        LotFP characters have a minimum number of HP.
        """
        hp = d(self.hit_die) + self.get_bonus(*self.attributes[characterclass.CON])
        hp = max(hp, characterclass.LOTFP['min_hp'][self.character_class['name']])
        return hp

    def get_saves(self):
        """
        Your magic based saves are effected by your INT, other saves by your
        WIS.
        """
        saves = copy.copy(characterclass.LOTFP['lotfp_saves'][self.character_class['name']])
        wis_bonus = self.get_bonus(*self.attributes[characterclass.WIS])
        int_bonus = self.get_bonus(*self.attributes[characterclass.INT])
        saves['magic'] = saves['magic'] - int_bonus
        for save in ['wands', 'poison', 'stone', 'breath']:
            saves[save] = saves[save] - wis_bonus
        return saves

    def get_spell(self):
        """
        Magic-Users and Elves begin with a single first level spell and 3 random
        spells in their spell book.
        """
        if 'spells' in self.character_class.keys():
            if self.character_class == characterclass.MAGICUSER:
                return ['Read Magic'] + random.sample(characterclass.LOTFP['spells'], 3)
            elif self.character_class == characterclass.ELF:
                return ['Read Magic']
        elif self.character_class == characterclass.CLERIC:
            return ['One clerical spell a day']
        return None

    def get_skills(self):
        skills = dict((s, x) for s, x in characterclass.LOTFP['skills'])
        if self.character_class == characterclass.THIEF:
            self.class_name = 'Specialist'
            for s in random.choice(characterclass.LOTFP['specialist_builds']):
                skills[s] = skills[s] + 1
        elif self.character_class == characterclass.DWARF:
            skills['Architecture'] = 3
        elif self.character_class == characterclass.ELF:
            skills['Search'] = 2
        elif self.character_class == characterclass.HALFLING:
            skills['Bushcraft'] = 3
            skills['Stealth'] = 5
        str_bonus = self.get_bonus(*self.attributes[characterclass.STR])
        skills['Open Doors'] = max(skills['Open Doors'] + str_bonus, 0)
        int_bonus = self.get_bonus(*self.attributes[characterclass.INT])
        skills['Languages'] = max(skills['Languages'] + int_bonus, 0)
        self.sneak_attack = skills.pop('Sneak Attack')
        skills = [(s, v) for s, v in skills.items()]
        return skills

    def get_equipment(self):
        return characterclass.LOTFP['equipment'][self.class_name][xdy(3,6)-3]

    def get_languages(self): return []


class LotFP_Homebrew_Character(LotFPCharacter, BasicAttribRaceMixin):
    """ Alternative model for our homebrew campaign.
    """ 

    @property
    def system(self): return "Homebrew"

    @property
    def initiative_bonus(self):
        return self.get_bonus(*self.attributes[characterclass.DEX])

    @property
    def melee_attack_bonus(self):
        bonus = self.get_bonus(*self.attributes[characterclass.STR])
        bonus += self.attack_bonus

        # check occupation, may add a bonus
        occupation = self.get_occupation()
        bonus += occupation['MB']

        if bonus > 0:
            bonus = "+%d" % bonus
        return bonus

    @property
    def ranged_attack_bonus(self):
        bonus = self.get_bonus(*self.attributes[characterclass.DEX])
        bonus += self.attack_bonus
        # check occupation, may add a bonus
        occupation = self.get_occupation()
        bonus += occupation['RB']

        if bonus > 0:
            bonus = "+%d" % bonus
        return bonus

    @property
    def ready_items_allowed(self):
        ready_items_by_dex = {'3': 1, '4': 2, '6': 5, '9': 10, '13': 15, '16': 20, '18': 25 } 
        dex = self.attributes[characterclass.DEX][1]

        ready_items_allowed = 0
        for ri_dex, ri_allowed in ready_items_by_dex.items():
            v = int(ri_dex)
            if dex >= v:
                ready_items_allowed = ri_allowed

        return ready_items_allowed

    @property
    def backpack_items_allowed(self):
        return 5 # small backpack only 

    @property
    def backpack_name(self):
        return "Small Backpack"

    @property
    def save_name_table(self):
        return characterclass.HOMEBREW['saves']

    @property
    def hit_die(self):
        base_hit_die = characterclass.LOTFP['hitdice'][self.character_class['name']]
        if self.race == 'Dwarf':
            # dwarves get bump up in hit die
            base_hit_die += 2
            
        return base_hit_die

    @property
    def demihumans(self):
        # demihumans are not a class, but a race 
        return False

    @staticmethod
    def _update_tuple (stuple, change):
        v = int(stuple[1]) + change
        return (stuple[0], v)

    def _str_to_characterclass_index (value:str)->int:
        # doing this type of thing is a sign of poorly designed code...sigh.
        #
        if value == 'STR':
            return characterclass.STR
        if value == 'CON':
            return characterclass.CON
        if value == 'DEX':
            return characterclass.DEX
        if value == 'INT':
            return characterclass.INT
        if value == 'WIS':
            return characterclass.WIS
        if value == 'CHA':
            return characterclass.CHA
        return None

    def get_occupation(self):
        occupations = characterclass.HOMEBREW['occupations']
        return occupations[self.occupation]

    def get_equipment(self):
        equipment = super().get_equipment()

        # Add any extra equipment from occupation
        occupation = self.get_occupation()
        
        for equip in occupation['equip']:
            if equip in equipment:
                # give them 1d6 x 10 sp instead
                equipment.append(f"%s sp" % str(xdy(1,6) * 10))
            else:
                equipment.append(equip)

        # assign equipment to slots
        self.prime_hand = None
        self.off_hand = None
        self.worn = "Clothing"
        self.ready_equipment = []
        self.purse = []
        backpack_equipment = []
        for item in equipment:
            check = item.lower()
            if "armor" in check or "clothing" in check:
                self.worn = item
            # figure out what to put in our hands
            elif "spear" in check or "sword" in check or "dagger" in check\
                    or "shield" in check or "torch" in check \
                    or "mace" in check or "club" in check\
                    or "axe" in check or "flail" in check\
                    or "lantern" in check or "garotte" in check\
                    or "holy" in check or "cross" in check or "pistol" in check\
                    or "tools" in check or "pick" in check:
                if self.prime_hand == None:
                    self.prime_hand = item
                elif self.off_hand == None:
                    self.off_hand = item
                else:
                    # overflow
                    self.ready_equipment.append(item)
            elif " cp" in check or " sp" in check and "iron" not in check:
                self.purse.append(item)
            elif "bow" in check or "quiver" in check:
                self.ready_equipment.append(item)
            elif "pack" in check:
                # these are containers
                self.ready_equipment.append(item)
            else:
                backpack_equipment.append(item)

        # calculate Encumbrance and move
        self.encumbrance = 0
        self.move = "8m/round"
        if "chain" in self.worn.lower():
            self.encumbrance += 1
        elif "plate" in self.worn.lower():
            self.encumbrance += 2

        if len(self.ready_equipment) + 2 >= 5:
            self.encumbrance += 1

        if len(self.ready_equipment) + 2 >= 10:
            self.encumbrance += 1

        if self.race == "Dwarf":
            self.encumbrance -= 1

        if self.encumbrance < 0: self.encumbrance = 0
        if self.encumbrance > 5: self.encumbrance = 5

        move_str = ["8m/round", "8m/round", "6m/round", "4m/round", "2m/round", "0m/round"]
        enc_str = ["Unencumbered", "Unencumbered", "Lightly", "Heavily", "Severely", "Over"]

        self.move = move_str[self.encumbrance]
        self.encumbrance = f"%d %s" % (self.encumbrance, enc_str[self.encumbrance])

        return backpack_equipment

    def roll_attribute_scores(self):

        attributes = super(LotFP_Homebrew_Character, self).roll_attribute_scores()

        # randomize (former) occupation
        occupations = characterclass.HOMEBREW['occupations']
        o_name = random.choice(list(occupations.keys())) 
        self.occupation = o_name
        occupation = occupations[o_name]

        # update stats by occupation. This is the time to do this.
        # IF indicated in the occupation, update the character to change
        # (raise) their stats by indicated amount 
        for stat in occupation['stats'].keys():
            change = occupation['stats'][stat]
            attrib = LotFP_Homebrew_Character._str_to_characterclass_index(stat)
            attributes[attrib] = LotFP_Homebrew_Character._update_tuple(attributes[attrib], change)

        return attributes

    def get_bonus(self, attr, val):
        """
        Like LotFP but race can influence bonus returned.
        """
        bonus = super().get_bonus(attr, val)

        if self.race != None:
            if attr == 'INT' and self.race == 'Elf':
                # bonus to Elves
                bonus += 1

            elif attr == 'CON' and self.race == 'Dwarf':
                bonus += 1

            elif attr == 'DEX' and self.race == 'Elf':
                bonus += 1

            elif attr == 'DEX' and self.race == 'Halfling':
                bonus += 2

            elif attr == 'CHA' and self.race == 'Elf':
                bonus += 1

        return bonus


    def get_spell(self):
        """
        Magic-Users begin with Read Magic, Summon and 2 random spells.
        """
        if 'spells' in self.character_class.keys():
            if self.character_class == characterclass.MAGICUSER:
                number = 2
                if self.race == 'Human':
                    number = 3
                return ['Read Magic', 'Summon'] + random.sample(characterclass.LOTFP['spells'], number)
        elif self.character_class == characterclass.CLERIC:
            return ['One clerical spell a day']
        return None


    def get_character_class(self, classname=None):
        """
        We determine character class based on your prime attribute.
        """
        if classname:
            return characterclass.CLASS_BY_NAME[classname]

        prime_attribute, _ = sorted(self.attributes[:4],
                                    reverse=True, key=operator.itemgetter(1))[0]

        return characterclass.PRIME_REQUISITE[prime_attribute]


    def _randomize_skills(skills:dict, skill_list:list, points_to_spend:int)->dict:
        while (points_to_spend > 0):
            s = random.choice(skill_list)
            skills[s] = skills[s] + 1
            points_to_spend -= 1
        return skills

    def get_sbonus(self, attr, val)->str: 
        bonus = self.get_bonus(attr, val)
        return _num_to_str(bonus) 

    def get_skills(self):
        
        skills = dict((s, x) for s, x in characterclass.HOMEBREW['skills'])

        str_bonus = self.get_bonus(*self.attributes[characterclass.STR])
        dex_bonus = self.get_bonus(*self.attributes[characterclass.DEX])
        int_bonus = self.get_bonus(*self.attributes[characterclass.INT])
        cha_bonus = self.get_bonus(*self.attributes[characterclass.CHA])

        # everyone gets 1 + Int Bonus to spend on any skill. 
        add_skill_points = max(int_bonus+1, 0)

        # deal with class-based skill tailoring 
        if self.character_class == characterclass.THIEF:
            skills['Sneak Attack'] = 0

            # add some thief skills
            thief_skills = random.choice(characterclass.HOMEBREW['specialist_builds'])
            skills = LotFP_Homebrew_Character._randomize_skills(skills, thief_skills, 10)

        if self.character_class == characterclass.CLERIC:
            v = random.sample([2,3],2)
            skills['Theology'] = v[0]
            skills['Languages'] = v[1]

        if self.character_class == characterclass.MAGICUSER:
            v = random.sample([2,3],2)
            skills['Arcana'] = v[0]
            skills['Languages'] = v[1]

        if self.character_class == characterclass.FIGHTER:
            # distribute 5 points randomly
            v = random.sample([1,2,2],3)
            skills['Armory'] = v[0] 
            skills['Athletics'] = v[1]
            skills['Open Doors'] = v[2]

        # bump up skills for some races
        if self.race == 'Dwarf':
            dwarf_skills = ['Armory', 'Architecture']
            skills = LotFP_Homebrew_Character._randomize_skills(skills, dwarf_skills, 5)

        if self.race == 'Halfling':
            halfling_skills = ['Bushcraft', 'Stealth']
            skills = LotFP_Homebrew_Character._randomize_skills(skills, halfling_skills, 5)

        if self.race == 'Human' and self.character_class != characterclass.MAGICUSER:
            # m-us get an extra spell, others get 5 rando points in skills
            add_skill_points += 5

        # set some defaults on core skills
        # We dont adopt a setting a minimum of '0' except for social skill
        skills['Athletics'] = skills['Athletics'] + max(str_bonus, dex_bonus)
        skills['Languages'] = skills['Languages'] + int_bonus
        skills['Open Doors'] = skills['Open Doors'] + str_bonus
        skills['Search'] = skills['Search'] + int_bonus
        skills['Stealth'] = skills['Stealth'] + dex_bonus
        skills['Social'] = max(skills['Social'] + cha_bonus, 0)

        # apportion all remaining skill points randomly
        skill_names = list(skills.keys()) 
        while (add_skill_points > 0):
            s = random.choice(skill_names)
            skills[s] = skills[s] +1
            add_skill_points -= 1

        # add in any occupational skills
        occupation = self.get_occupation()
        for skill in occupation['skills']:
            skills[skill] += 1

        # for special formatting which we aren't using
        if self.character_class == characterclass.THIEF:
            self.sneak_attack = skills.pop('Sneak Attack')
            self.sneak_attack_dmg = '+1d6'

        # pass thru and make an array
        skills = [(s, _num_to_str(v)) for s, v in skills.items()]

        return skills



    def get_saves(self):
        """
        We use ability checks.
        """
        saves = {'poison': 0, 'wands': 0, 'stone': 0, 'breath': 0, 'magic': 0} 

        # Health
        saves['poison'] = self.get_sbonus(*self.attributes[characterclass.CON])

        # Dodge
        saves['wands'] = self.get_sbonus(*self.attributes[characterclass.DEX])

        # Perception
        saves['stone'] = self.get_sbonus(*self.attributes[characterclass.INT])

        # Willpower
        saves['breath'] = self.get_sbonus(*self.attributes[characterclass.WIS])

        # Fortitude
        saves['magic'] = self.get_sbonus(*self.attributes[characterclass.STR])

        return saves


class HolmesCharacter(Character):
    """
    Models a Holmes Basic Edition D&D Character. Holmes is much closer to
    original D&D than Moldvay/Cook.
    """

    @property
    def system(self):
        return "Holmes D&D"

    def get_bonus(self, attr, val):
        """
        Return the Holmes' D&D attribute bonuses.
        """
        if attr == 'INT':
            # Bonus to languages
            if val > 10:
                return val - 10
        elif attr == 'CON':
            # Bonus to HP
            if val <= 6:
                return -1
            elif val == 15:
                return 1
            elif val > 15:
                return val - 15
        elif attr == 'DEX':
            # missile damage
            if val <= 8:
                return -1
            elif val >= 13:
                return 1
        return 0


class LBBCharacter(Character):
    """
    Models an Original D&D character. (1974 Little Brown Books.)
    """

    @property
    def system(self):
        return "Original (Little Brown Books) D&D"

    @property
    def thieves(self):
        """
        The thief isn't a playable class in the original D&D books.
        """
        return False

    @property
    def num_first_level_spells(self):
        """
        4 spells in Basic D&D don't exist in Original D&D, so we trim them
        when making spell selection.
        """
        return 8

    @property
    def hit_die(self):
        """
        In LLB D&D all characters have the same hit die (d6).
        """
        return 6

    @property
    def max_ac(self):
        """
        In Original D&D Plate and Shield provides the absolute maximum
        armour bonus.
        """
        return 2

    def get_hp(self):
        """
        Determine HP based on hit dice and CON modifiers. Fighters have an
        additional hit point at first level.
        """
        hp = super(LBBCharacter, self).get_hp()
        if self.character_class == characterclass.FIGHTER:
            hp = hp + 1
        return hp

    def get_bonus(self, attr, val):
        """
        Return the Original D&D attribute bonuses.
        """
        if attr == 'INT':
            # Bonus to languages
            if val > 10:
                return val - 10
        elif attr == 'CON':
            # Bonus to HP
            if val <= 6:
                return -1
            elif val >= 15:
                return 1
        elif attr == 'DEX':
            # missile damage
            if val <= 8:
                return -1
            elif val >= 13:
                return 1
        elif attr == 'CHA':
            # loyalty bonus
            if val <= 4:
                return -2
            elif val <= 6:
                return -1
            elif 13 <= val <= 15:
                return 1
            elif 16 <= val <= 17:
                return 2
            elif val >= 18:
                return 4
        return 0


class ApollyonCharacter(AscendingAcMixin, HitDiceMixin, LBBCharacter):
    """
    Models characters from Gus L's OD&D game Apollyon. More information on
    his blog: http://dungeonofsigns.blogspot.ca/search/label/HMS%20Apollyon
    """

    # Gus's Apollyon Appearences
    DRESS = [
        "Feral tribal loincloth or untanned hull beast skins.",
        "The diaphanous fripperies of a burlesque hall performer.",
        "Apocalypse rags and bindings.  Stinking and dyed the same colour by grime or intent.",
        "Threadbare robe with detachable cowl and several hidden pockets.",
        "Bright loose shirt and tight dungarees in the style of a Vory tough.",
        "Casual worker's canvas pantaloons and white undershirt, accented by leather braces.",
        "Horizontal Striped sweater and dungarees with too many buttons.",
        "Cannery toilers dull jumpsuit and heavy tarred boots.",
        "Wool or felt uniform jacket encrusted with rotting braid.",
        "Patched, stained, torn and bedraggled fop's or pirate finery.",
        "Worn velvet livery of vest, knickers, jacket and absurd lacy cravat.",
        "Fisher's sea leathers, walrus and shark with bone toggles and Frogling hexagrams.",
        "Brightly patterned sarong and string and shell vest.",
        "Thin leather catsuit, accented with too many buckles and black pigeon feather cloak.",
        "A good quality clerk's tweed suit and bowler, cuffs stained with ink.",
        "Black suit or dress of fine dog wool, opera cape, mask and tall stylish hat.",
    ]

    APPEARENCE = [
        "Impressive facial scarring, either intentional and harmonious or the sign of battle and accident.",
        "1D8 front teeth replaced with prosthetics of gold or other metal and possibly decorated.",
        "Necklaces of teeth, ears or similar savage trophies and corresponding swagger.",
        "Bald head, may be shaved, genetic or the product of chemic exposure.",
        "Fastidious in dress and grooming.  Clothing and equipment immaculate whenever possible.",
        "The cold dead eyes of a heartless murdering ruffian, may conceal kindly soul.",
        "Collection of medals and awards worn on person, may or may not be earned.",
        "Face and hands permanently marked by industrial grit that has worked itself under the skin.  ",
        "General aura of decrepitude, clothing often dishevelled, eyes drooping or red, hair unkempt.",
        "Elaborately dyed and coiffed hair, fierce mustachio or similar affectation of high style.",
        "Wears gaudy trinkets and costume jewelry in nauseating profusion.",
        "Always wears gloves:  heavy leather, gutta-percha skin or soft velvet pick one.",
        "Unexpectedly heavy-set.  Perhaps not obese, but large and bulky for race.",
        "Several novelty tattoos.  Bright colours and lack of faction symbolism mark them as a mere affect.",
        "Monocle clamped firmly in eye. Sneer of cold command on lips.",
        "One eye replaced by a magically enhanced shell or stone.  Normal vision, may glow.",
    ]

    @property
    def system(self):
        return "Apollyon / Original D&D"

    def get_bonus(self, attr, val):
        """
        On the Apollyon bonuses are simplified.
        """
        if val >= 15:
            return 1
        if val <= 6:
            return -1
        return 0

    @property
    def thieves(self):
        return True

    @property
    def attack_bonus(self):
        return 2 if self.character_class == characterclass.FIGHTER else 0

    @property
    def appearance(self):
        return ' '.join([random.choice(self.DRESS), random.choice(self.APPEARENCE)])

    def get_ac(self):
        """
        Gus' crazy scheme: AC 11 unarmored, AC 12 light, AC 14 medium, AC 16
        heavy, AC17 plate. +1 AC for a shield. AC 18 is the maximum possible AC
        without heavy magic; AC 20 is the absolute maximum.
        """
        ac = 11
        if "Leather Armor" in self.equipment:
            ac += 1
        elif "Chain Armor" in self.equipment:
            ac += 3
        elif "Plate Armor" in self.equipment:
            ac += 5
            # rename plate to splint
            plate_idx = self.equipment.index("Plate Armor")
            self.equipment[plate_idx] = "Splint Armor"
        if "Shield" in self.equipment:
            ac += 1
        ac += self.get_bonus(*self.attributes[characterclass.DEX])
        return ac

    @property
    def demihumans(self):
        """
        Player's can't play demihumans the usual demi humans in Apollyon.
        """
        return False


class PahvelornCharacter(HitDiceMixin, LBBCharacter):
    """
    Models characters from the OD&D game Pahvelorn. (Essentially 1974 D&D.)
    More info here: http://www.necropraxis.com/tag/pahvelorn/.
    """

    @property
    def system(self):
        return "Pahvelorn / Original D&D"

    @property
    def thieves(self):
        """
        Pahvelorn includes the Greyhawk Thief as a playable character,
        but this is the only addition from Greyhawk in Pahvelorn. The Thief's
        hit dice is 6, just like all the other characters.
        """
        return True

    @property
    def demihumans(self):
        """
        Player's can't play demihumans in Pahvelorn.
        """
        return False

    @property
    def retainer(self):
        """
        Players start with a random retainer.
        """
        return random.choice(characterclass.RETAINERS)

    def get_thac9(self):
        """
        In Pahvelorn characters all begin at different combat ranks,
        as per this post:
          http://www.necropraxis.com/2012/11/11/adjusted-attack-ranks/
        """
        return {
            'Fighter': 7,
            'Cleric': 9,
            'Thief': 9,
            'Magic-User': 11,
        }[self.character_class['name']]

    def get_spell(self):
        """
        Players start with a basic spell book, and one random spell book. We
        tack on grimoires to the equipment list, instead of calling out a
        single spell.
        """
        if 'spells' in self.character_class.keys():
            self.grimoires = [
                characterclass.STARTING_GRIMOIRE,
                random.choice(characterclass.GRIMOIRES),
            ]
        return None


class CarcosaBase(object):
    """
    The common base for a Carcosa character.
    """

    @property
    def appearance(self):
        colour = random.choice([
            "Black", "Blue", "Bone", "Brown", "Dolm", "Green", "Jale",
            "Orange", "Purple", "Red", "Ulfire", "White", "Yellow"])
        sex = random.choice(['Man', 'Woman'])
        return "%s %s" % (colour, sex)

    def get_character_class(self, classname):
        figher_score = max(self.CON, self.STR, self.DEX)
        if self.INT > figher_score or figher_score < 9:
            return characterclass.SORCERER
        return characterclass.FIGHTER

    def get_equipment(self):
        """
        We generate a more Gonzo list of starting equipment.
        """
        weapon = "%s %s" % (random.choice(characterclass.GONZO.METERIAL),
                            random.choice(characterclass.GONZO.WEAPONS))
        self.equipment = [random.choice(characterclass.GONZO.ARMOUR), weapon]
        self.equipment += random.sample(characterclass.GONZO.GEAR, 2)
        self.equipment += random.sample(characterclass.GONZO.STRANGE, 1)
        self.equipment += ["%s GP" % xdy(3,6)]
        return self.equipment

    def get_languages(self): return []


class CarcosaCharacter(CarcosaBase, LBBCharacter):
    """
    Characters for an OD&D Carcosa game.
    """

    @property
    def system(self):
        return "Carcosa / Original D&D"


class MastersOfCarcosaCharacter(CarcosaBase,
                                AscendingAcMixin,
                                HitDiceMixin,
                                PsionicWildTalentMixin,
                                LBBCharacter):
    """
    Characters for my Carcosa game.
    """

    @property
    def system(self):
        return "Masters of Carcosa"

    @property
    def base_armour_class(self):
        return 10

    @property
    def attack_bonus(self):
        """
        Attack bonuses are as OD&D, so 0 at first level if using ascending AC.
        (You need a 10 to hit descending AC 9, or a 10 to hit ascending AC 10.)
        A house rule grants a +1 to Fighters at first level.
        """
        return 1 if self.character_class == characterclass.FIGHTER else 0

    def get_bonus(self, attr, val):
        """
        There are no bonuses for attribute scores.
        """
        return 0

    def get_ac(self):
        return 14


class DelvingDeeperCharacter(LBBCharacter):
    """
    Models a Delving Deeper (OD&D clone) character.
    """

    @property
    def system(self):
        return "Delving Deeper"

    def get_hp(self):
        """
        Determine HP based on hit dice and CON modifiers. Fighters have an
        additional 2 hit points at first level.
        """
        hp = super(LBBCharacter, self).get_hp()
        if self.character_class == characterclass.FIGHTER:
            hp = hp + 1
        return hp

    def get_bonus(self, attr, val):
        """
        Bonuses are similar to LLB, but even less pronounced. Also there is
        bonus damage for high strength.
        """
        if attr == 'STR':
            # bonus to damage
            if val >= 15:
                return 1
        elif attr == 'INT':
            # Bonus to languages
            if val > 10:
                return val - 10
        elif attr == 'CON':
            # Bonus to HP
            if val <= 6:
                return -1
            elif val >= 15:
                return 1
        elif attr == 'DEX':
            # missile damage
            if val <= 6:
                return -1
            elif val >= 15:
                return 1
        elif attr == 'CHA':
            # loyalty bonus
            if val <= 3:
                return -2
            elif val <= 5:
                return -1
            elif 13 <= val <= 15:
                return 1
            elif 16 <= val <= 17:
                return 2
            elif val >= 18:
                return 4
        return 0
