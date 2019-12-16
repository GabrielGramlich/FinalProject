USE FinalProjectDB;

INSERT INTO AbilityScores (Name)
	VALUES ("Strength"),
    ("Dexterity"),
    ("Constitution"),
    ("Intelligence"),
    ("Wisdom"),
    ("Charisma");

INSERT INTO Armor (Name, Base, Type)
	VALUES ("Leather", 11, "Light"),
    ("Scale Male", 14, "Medium"),
    ("Shield", 2, "Shield"),
    ("Chain Mail", 16, "Heavy");

INSERT INTO Backgrounds (Name)
	VALUES ("Acolyte"),
    ("Charlatan"),
    ("Criminal"),
    ("Entertainer"),
	("Folk Hero");

INSERT INTO Classes (Name, HitPoints, Skills)
	VALUES ("Barbarian", 12, 2),
    ("Bard", 8, 3),
    ("Cleric", 8, 2),
    ("Druid", 8, 2),
    ("Fighter", 10, 2),
    ("Monk", 8, 2);

INSERT INTO Features (Name, Description)
	VALUES ("Darkvision", "You can see dim light within 60’ as if it were bright light, and darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),
    ("Dwarven Resilience", "You have advantage on saving throws against poison, and you have resistance against poison damage."),
    ("Stonecunning", "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."),
    ("Dwarven Toughness", "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."),
    ("Dwarven Armor Training", "You have proficiency with light and medium armor."),

    ("Fey Ancestry", "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."),
    ("Trance", "Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."),
    ("Cantrip", "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it."),
    ("Fleet of Foot", "You have a +5 to your base walking speed."),
    ("Mask of the Wild", "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."),

    ("Superior Darkvision", "Your darkvision has a radius of 120 feet."),
    ("Sunlight Sensitivity", "You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."),
    ("Drow Magic", "You know the dancing lights cantrip. When you reach 3rd level, you can cast the faerie fire spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the darkness spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."),
    ("Rage", "On your turn, you can enter a rage as a bonus action. While raging, you gain the following benefits if you aren’t wearing heavy armor: You have advantage on Strength checks and Strength saving throws. When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian. You have resistance to bludgeoning, piercing, and slashing damage. Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven’t attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn a bonus action."),
	("Unarmored Defense", "While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. Uou can use a shield and still gain this benefit."),

	("Bardic Spellcasting", "You know two cantrips of your choice from the bard spell list. You know four 1st-level spells of your choice from the bard spell list. Charisma is your spellcasting ability for your bard spells. Spell save DC = 8 + your proficiency modifier + your charisma modifier. Spell attack modifier = your proficiency bonus + your charisma modifier. You can use a musical instrument as a spellcasting focus for your bard spells."),
	("Bardic Inspiration", "You can inspire other through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains on Bardic Inspiration die, a d6. Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw is makes."),
	("Cleric Spellcasting", "You know three cantrips of your choice from the cleric spell list. You prepare the list of cleric spells that are available for you to cast, choosing from the cleric spell list. When you do so, choose a number of cleric spells equal to your Wisdom modifier + your cleric level. You can change your list of prepared spells when you finish a long rest. Spell save DC = 8 + your proficiency bonus + your Wisdom modifier. Spell attack modifier = your proficiency bonus + your Wisdom modifier. You can us a holy symbol as a spellcasting focus for your cleric spells."),
	("Divine Domain", "Choose one domain related to your deity: Knowledge, Life, Light, Nature, Tempest, Trickery, or War. Your choice grants you domain spells and other features when you choose it at 1st level, detailed in the PHB."),
	("Druidic", "You know druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You can others who know this language automatically spot such a message. Others spot the message’s presence with a successful DC 15 Wisdom (Perception) check but can’t decipher it without magic."),

	("Druidic Spellcasting", "At 1st level, you know two cantrips of your choice from the druid spell list. You prepare your list of druid spells that are available for you to cast, choosing from the druid spell list. When you do so, choose a number of druid spells equal to you Wisdom modifier + your druid level. Wisdom is our spellcasting ability for your druid spells. Spell save DC = 8 + your proficiency bonus + your Wisdom modifier. Spell attack modifier = your proficiency bonus + your Wisdom modifier. You can use a druidic focus as a spellcasting focus for your druid spells."),
	("Fighting Style", "You adopt a particular style of fighting as your specialty. Choose one of the following options: Archery, Defense, Dueling, Great Weapon Fighting, Protection, Two-Weapon Fighting."),
	("Second Wind", "You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10+ your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again."),
	("Unarmored Defense", "While you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier."),
	("Martial Arts", "Your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons. You gain the following benefits while you are unarmed or wielding only monk weapons and you aren’t wearing armor or wielding a shield: You can use Dexterity instead of Strength for the attack and damage rolls. You can roll a d4 in place of the normal damage. When you use the Attack action, you can make one unarmed strike as a bonus action."),

	("Shelter of the Faithful", "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you at a modest lifestyle."),
	("False Identity", "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy."),
	("Criminal Contact", "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."),
	("Popular Demand", "You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble’s court. At such a place, you receive free lodging and food of a modest or comfortable standard, as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you."),
	("Rustic Hospitality", "Since you come from the ranks of the common folk. You fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you.");

INSERT INTO Languages (Name)
	VALUES ("Abyssal"),
    ("Aquan"),
    ("Auran"),
    ("Celestial"),
    ("Common"),

    ("Deep Speech"),
    ("Draconic"),
    ("Dwarvish"),
    ("Elvish"),
    ("Giant"),

    ("Gnomish"),
    ("Goblin"),
    ("Gnoll"),
    ("Halfling"),
    ("Ignan"),

    ("Infernal"),
    ("Orc"),
    ("Primordial"),
    ("Sylvan"),
    ("Terran"),

	("Undercommon"),
    ("Any");

INSERT INTO Proficiencies (Name, Type)
	VALUES ("Athletics", "Skill"),
    ("Acrobatics", "Skill"),
    ("Sleight of Hand", "Skill"),
    ("Stealth", "Skill"),
    ("Arcana", "Skill"),
#5
    ("History", "Skill"),
    ("Investigation", "Skill"),
    ("Nature", "Skill"),
    ("Religion", "Skill"),
    ("Animal Handling", "Skill"),
#10
    ("Insight", "Skill"),
    ("Medicine", "Skill"),
    ("Perception", "Skill"),
    ("Survival", "Skill"),
    ("Deception", "Skill"),
#15
    ("Intimidation", "Skill"),
    ("Performance", "Skill"),
    ("Persuasion", "Skill"),
    ("Alchemist's supplies", "Tool"),
    ("Brewer's supplies", "Tool"),
#20
    ("Calligrapher's supplies", "Tool"),
    ("Carpenter's tools", "Tool"),
    ("Cartographer's tools", "Tool"),
    ("Cobbler's tools", "Tool"),
    ("Cook's utensils", "Tool"),
#25
    ("Glassblower's tools", "Tool"),
    ("Jeweler's tools", "Tool"),
    ("Leatherworker's tools", "Tool"),
    ("Mason's tools", "Tool"),
    ("Painter's supplies", "Tool"),
#30
    ("Potter's tools", "Tool"),
    ("Smith's tools", "Tool"),
    ("Tinker's tools", "Tool"),
    ("Weaver's tools", "Tool"),
	("Woodcarver's tools", "Tool"),
#35    
    ("Artisan's tools", "Tool"),
    ("Disguise kit", "Tool"),
    ("Forgery kit", "Tool"),
    ("Gaming set", "Tool"),
    ("Herbalism kit", "Tool"),
#40
    ("Musical instrument", "Tool"),
    ("Navigator's tools", "Tool"),
    ("Poisoner's kit", "Tool"),
    ("Thieves' tools", "Tool"),
    ("Vehicles (land)", "Tool"),
#45
    ("Vehicles (water)", "Tool"),
    ("Any", "Skill");

INSERT INTO Races (Name)
	VALUES ("Hill Dwarf"),
    ("Mountain Dwarf"),
    ("High Elf"),
    ("Wood Elf"),
    ("Dark Elf");

INSERT INTO Weapons (Name, Damage, Modifier)
	VALUES ("Greataxe", "1d12", 0),
    ("Handaxe", "1d6", 0),
	("Javelin", "1d6", 0),
    ("Rapier", "1d8", 2),
    ("Dagger", "1d4", 2),

    ("Mace", "1d6", 0),
    ("Light Crossbow", "1d8", 1),
    ("Scimitar", "1d6", 2),
    ("Battleaxe", "1d8", 0),
    ("Shortsword", "1d6", 2),

    ("Dart", "1d4", 2);

INSERT INTO AbilityScoreBridge (Modifier, AbilityScoreID, RaceID)
	VALUES (2 ,3 ,1),
    (1, 5, 1),
    (2, 3, 2),
    (2, 1, 2),
    (2, 2, 3),
    (1, 4, 3),
    (2, 2, 4),
    (1, 5, 4),
    (2, 2, 5),
	(1, 6, 5);

INSERT INTO ArmorBridge (ArmorID, ClassID)
	VALUES (1, 2),
    (2, 3),
    (3, 3),
    (1, 4),
    (3, 4),
    (4, 5),
	(3, 5);

INSERT INTO FeatureBridge (FeatureID, BackgroundID)
	VALUES (26, 1),
    (27, 2),
    (28, 3),
    (29, 4),
	(30, 5);

INSERT INTO FeatureBridge (FeatureID, ClassID)
	VALUES (14, 1),
    (15, 1),
    (16, 2),
    (17, 2),
    (18, 3),
    (19, 3),
    (20, 4),
    (21, 4),
    (22, 5),
    (23, 5),
    (24, 6),
	(25, 6);

INSERT INTO FeatureBridge (FeatureID, RaceID)
	VALUES (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (1, 2),
    (2, 2),
    (3, 2),
    (5, 2),
    (1, 3),
    (6, 3),
    (7, 3),
    (8, 3),
    (1, 4),
    (6, 4),
    (7, 4),
    (9, 4),
    (10, 4),
    (1, 5),
    (6, 5),
    (7, 5),
    (11, 5),
    (12, 5),
	(13, 5);

INSERT INTO LanguageBridge (LanguageID, RaceID, Choice)
	VALUES (5, 1, 0),
    (8, 1, 0),
    (5, 2, 0),
    (8, 2, 0),
    (5, 3, 0),
    (9, 3, 0),
    (22, 3, 1),
    (5, 4, 0),
    (9, 4, 0),
    (5, 5, 0),
	(9, 5, 0);

INSERT INTO LanguageBridge (LanguageID, BackgroundID, Choice)
	VALUES (22, 1, 1),
	(22, 1, 1);

INSERT INTO ProficiencyBridge (ProficiencyID, BackgroundID, Choice)
	VALUES (11, 1, 0),
    (9, 1, 0),
    (15, 2, 0),
    (3, 2, 0),
    (37, 2, 0),
    (38, 2, 0),
    (15, 3, 0),
    (4, 3, 0),
    (39, 3, 0),
    (44, 3, 0),
    (2, 4, 0),
    (17, 4, 0),
    (37, 4, 0),
    (41, 4, 0),
    (10, 5, 0),
    (14, 5, 0),
    (36, 5, 0),
	(45, 5, 0);

INSERT INTO ProficiencyBridge (ProficiencyID, ClassID, Choice)
	VALUES (10, 1, 1),
    (1, 1, 1),
    (16, 1, 1),
    (8, 1, 1),
    (13, 1, 1),
    (14, 1, 1),
    (47, 2, 1),
    (47, 2, 1),
    (47, 2, 1),
    (6, 3, 1),
    (11, 3, 1),
    (12, 3, 1),
    (18, 3, 1),
    (9, 3, 1),
    (5, 4, 1),
    (10, 4, 1),
    (11, 4, 1),
    (12, 4, 1),
    (8, 4, 1),
    (13, 4, 1),
    (9, 4, 1),
    (14, 4, 1),
    (2, 5, 1),
    (10, 5, 1),
    (1, 5, 1),
    (6, 5, 1),
    (11, 5, 1),
    (16, 5, 1),
    (13, 5, 1),
	(14, 5, 1),
	(2, 6, 1),
	(1, 6, 1),
	(6, 6, 1),
	(11, 6, 1),
	(9, 6, 1),
	(4, 6, 1);

INSERT INTO ProficiencyBridge (ProficiencyID, RaceID, Choice)
	VALUES (32, 1, 0),
    (20, 1, 0),
    (32, 2, 0),
    (29, 2, 0),
    (13, 3, 0),
    (13, 4, 0),
	(13, 5, 0);

INSERT INTO SavingThrowBridge (ClassID, AbilityScoreID)
	VALUES (1, 1),
    (1, 3),
    (2, 2),
    (2, 6),
    (3, 5),
    (3, 6),
    (4, 4),
    (4, 5),
    (5, 1),
    (5, 3),
    (6, 1),
	(6, 2);

INSERT INTO WeaponBridge (WeaponID, ClassID, Amount)
	VALUES (1, 1, 1),
    (2, 1, 2),
    (3, 1, 4),
    (4, 2, 1),
    (5, 2, 1),
    (6, 3, 1),
    (7, 3, 1),
    (8, 4, 1),
    (9, 5, 1),
    (2, 5, 2),
    (10, 6, 1),
	(11, 6, 10);

