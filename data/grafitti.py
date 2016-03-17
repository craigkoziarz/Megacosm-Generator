
# The following message is written in _______ with blood.
self.redis.lpush('grafitti_language', 'Common')
self.redis.lpush('grafitti_language', 'Dwarven')
self.redis.lpush('grafitti_language', 'Elven')
self.redis.lpush('grafitti_language', 'Draconic')
self.redis.lpush('grafitti_language', 'Halfling')
self.redis.lpush('grafitti_language', 'Giant')
self.redis.lpush('grafitti_language', 'Infernal')
self.redis.lpush('grafitti_language', 'Celestial')
self.redis.lpush('grafitti_language', 'Abyssal')
self.redis.lpush('grafitti_language', 'Gnomish')
self.redis.lpush('grafitti_language', 'Gnollish')
self.redis.lpush('grafitti_language', 'Slimese')

#The following message is written in Common with _________.
self.redis.lpush('grafitti_material', 'blood')
self.redis.lpush('grafitti_material', 'crayon')
self.redis.lpush('grafitti_material', 'marker')
self.redis.lpush('grafitti_material', 'chalk')
self.redis.lpush('grafitti_material', 'slime ')
self.redis.lpush('grafitti_material', 'feces')
self.redis.lpush('grafitti_material', 'paint')
self.redis.lpush('grafitti_material', 'ink')
self.redis.lpush('grafitti_material', 'graphite')
self.redis.lpush('grafitti_material', 'liver mush')

self.redis.lpush('grafitti_hero', 'king')
self.redis.lpush('grafitti_hero', 'knight')
self.redis.lpush('grafitti_hero', 'queen')
self.redis.lpush('grafitti_hero', 'mage')
self.redis.lpush('grafitti_hero', 'warrior')

self.redis.lpush('grafitti_monster', 'dragon')
self.redis.lpush('grafitti_monster', 'lich')
self.redis.lpush('grafitti_monster', 'mummy')
self.redis.lpush('grafitti_monster', 'death')
self.redis.lpush('grafitti_monster', 'hydra')
self.redis.lpush('grafitti_monster', 'mimic')
self.redis.lpush('grafitti_monster', 'cannibal')

self.redis.lpush('grafitti_loss', 'life')
self.redis.lpush('grafitti_loss', 'a hand')
self.redis.lpush('grafitti_loss', 'an arm')
self.redis.lpush('grafitti_loss', 'a leg')
self.redis.lpush('grafitti_loss', 'a foot')
self.redis.lpush('grafitti_loss', 'a friend')
self.redis.lpush('grafitti_loss', 'your mind')

self.redis.lpush('grafitti_stare', 'paintings')
self.redis.lpush('grafitti_stare', 'gemstone')
self.redis.lpush('grafitti_stare', 'the leader')
self.redis.lpush('grafitti_stare', 'the medusa')
self.redis.lpush('grafitti_stare', 'the lights')

self.redis.lpush('grafitti_threatcount', '1')
self.redis.lpush('grafitti_threatcount', '2')


self.redis.lpush('grafitti_message', 'This isn\'t a dungeon, it\'s a prison!')
self.redis.lpush('grafitti_message', '{{params.npcname}} sees all.')
self.redis.lpush('grafitti_message', 'The {{params.hero}} tried to protect us, but was too late...')
self.redis.lpush('grafitti_message', 'The {{params.hero}} is no hero...')
self.redis.lpush('grafitti_message', 'Beware the whispers, they will make you understand.')
self.redis.lpush('grafitti_message', 'Sorry, we already cleaned this place out!')
self.redis.lpush('grafitti_message', 'There is nothing of value here.')
self.redis.lpush('grafitti_message', 'The dead watch with unblinking eyes.')
self.redis.lpush('grafitti_message', 'Beware the cracks and crevices.')
self.redis.lpush('grafitti_message', 'Madness awaits those unprepared.')
self.redis.lpush('grafitti_message', 'I\'m right behind you.')
self.redis.lpush('grafitti_message', 'Sleep well tonight.')
self.redis.lpush('grafitti_message', 'This was not what I signed up for.')
self.redis.lpush('grafitti_message', '{{params.monster|capitalize|pluralize(params.threatcount)}} ahead.')
self.redis.lpush('grafitti_message', 'Beware the {{params.npc.profession|pluralize(2)}} and their lies!')
self.redis.lpush('grafitti_message', 'BEWARE THE {{params.monster|upper|pluralize(params.threatcount)}}!')
self.redis.lpush('grafitti_message', 'Hail the {{params.monster}} and you may survive.')
self.redis.lpush('grafitti_message', 'I am all that is left.')
self.redis.lpush('grafitti_message', 'Betrayal is the darkest sin.')
self.redis.lpush('grafitti_message', 'They weren\'t statues.')
self.redis.lpush('grafitti_message', 'They weren\'t allies.')
self.redis.lpush('grafitti_message', 'Those aren\'t children.')
self.redis.lpush('grafitti_message', 'Traps ahead!')
self.redis.lpush('grafitti_message', 'There are worse fates than the loss of {{params.loss}}')
self.redis.lpush('grafitti_message', 'Don\'t stare at the {{params.stare}}.')
self.redis.lpush('grafitti_message', 'A fool will lead you. Beware the hall.')
self.redis.lpush('grafitti_message', '{{params.npcname}} LIED!')
self.redis.lpush('grafitti_message', '{{params.npcname}} was here!')
self.redis.lpush('grafitti_message', 'Make no noise if you wish to live.')
self.redis.lpush('grafitti_message', 'Are you sure they\'re dead?')

#The message is signed ________
SET grafitti_signature_chance 50
self.redis.lpush('grafitti_signature', 'with a paw print.')
self.redis.lpush('grafitti_signature', 'with a claw print.')
self.redis.lpush('grafitti_signature', 'with a hand print.')
self.redis.lpush('grafitti_signature', 'with a vulgar drawing.')
self.redis.lpush('grafitti_signature', '"Igor the Mad."')
self.redis.lpush('grafitti_signature', 'illegibly.')
self.redis.lpush('grafitti_signature', 'but smeared from the wall.')
self.redis.lpush('grafitti_signature', '"{{params.npcname}}."')
self.redis.lpush('grafitti_signature', 'by {{params.npcname}}.')
self.redis.lpush('grafitti_signature', 'by someone named {{params.npcname}}.')
self.redis.lpush('grafitti_signature', 'with a sigil.')
self.redis.lpush('grafitti_signature', 'with a series of scratches.')
self.redis.lpush('grafitti_signature', 'with a pictogram.')

self.redis.lpush('grafitti_template', 'The following message is written in {{params.language}} with {{params.material}}: "{{params.message}}"')
self.redis.lpush('grafitti_template', 'The see the following message in {{params.language}}: "{{params.message}}" It is written in {{params.material}}.')

# You\'d guess the writing is _____
SET grafitti_age_chance 30
self.redis.lpush('grafitti_age', 'relatively fresh.')
self.redis.lpush('grafitti_age', 'less than a day old.')
self.redis.lpush('grafitti_age', 'over a week old.')
self.redis.lpush('grafitti_age', 'over a month old.')
self.redis.lpush('grafitti_age', 'over a year old.')
self.redis.lpush('grafitti_age', 'centuries old.')
