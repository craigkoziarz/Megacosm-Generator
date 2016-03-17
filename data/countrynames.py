self.redis.lpush('countryname_fullname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
self.redis.lpush('countryname_shortname_template', '{{params.fullname}}')
self.redis.lpush('countryname_formalname_template', '{{params.fullname}}')


set countryname_title_chance 22
set countryname_pre_chance 100
set countryname_root_chance 100
set countryname_post_chance 40
set countryname_trailer_chance 50

self.redis.lpush('countryname_title', 'Central')
self.redis.lpush('countryname_title', 'Inner')
self.redis.lpush('countryname_title', 'Outer')
self.redis.lpush('countryname_title', 'Lesser')
self.redis.lpush('countryname_title', 'Greater')
self.redis.lpush('countryname_title', 'Lower')
self.redis.lpush('countryname_title', 'Middle')
self.redis.lpush('countryname_title', 'Upper')
self.redis.lpush('countryname_title', 'United')
self.redis.lpush('countryname_title', 'East')
self.redis.lpush('countryname_title', 'Eastern')
self.redis.lpush('countryname_title', 'West')
self.redis.lpush('countryname_title', 'Western')
self.redis.lpush('countryname_title', 'North')
self.redis.lpush('countryname_title', 'Northern')
self.redis.lpush('countryname_title', 'South')
self.redis.lpush('countryname_title', 'Southern')
self.redis.lpush('countryname_title', 'The')

self.redis.lpush('countryname_pre', 'Af')
self.redis.lpush('countryname_pre', 'Alb')
self.redis.lpush('countryname_pre', 'Alg')
self.redis.lpush('countryname_pre', 'And')
self.redis.lpush('countryname_pre', 'Ang')
self.redis.lpush('countryname_pre', 'Ant')
self.redis.lpush('countryname_pre', 'Aqui')
self.redis.lpush('countryname_pre', 'Ar')
self.redis.lpush('countryname_pre', 'Arg')
self.redis.lpush('countryname_pre', 'Arm')
self.redis.lpush('countryname_pre', 'Ash')
self.redis.lpush('countryname_pre', 'Aus')
self.redis.lpush('countryname_pre', 'Azer')
self.redis.lpush('countryname_pre', 'Ba')
self.redis.lpush('countryname_pre', 'Bah')
self.redis.lpush('countryname_pre', 'Bang')
self.redis.lpush('countryname_pre', 'Bar')
self.redis.lpush('countryname_pre', 'Bel')
self.redis.lpush('countryname_pre', 'Ben')
self.redis.lpush('countryname_pre', 'Ber')
self.redis.lpush('countryname_pre', 'Bhu')
self.redis.lpush('countryname_pre', 'Bol')
self.redis.lpush('countryname_pre', 'Bos')
self.redis.lpush('countryname_pre', 'Bots')
self.redis.lpush('countryname_pre', 'Bra')
self.redis.lpush('countryname_pre', 'Brit')
self.redis.lpush('countryname_pre', 'Bru ')
self.redis.lpush('countryname_pre', 'Bul')
self.redis.lpush('countryname_pre', 'Bur')
self.redis.lpush('countryname_pre', 'Cala')
self.redis.lpush('countryname_pre', 'Cam')
self.redis.lpush('countryname_pre', 'Can')
self.redis.lpush('countryname_pre', 'Cap')
self.redis.lpush('countryname_pre', 'Cen')
self.redis.lpush('countryname_pre', 'Cham')
self.redis.lpush('countryname_pre', 'Chi')
self.redis.lpush('countryname_pre', 'Chil')
self.redis.lpush('countryname_pre', 'Col')
self.redis.lpush('countryname_pre', 'Com')
self.redis.lpush('countryname_pre', 'Con')
self.redis.lpush('countryname_pre', 'Cona')
self.redis.lpush('countryname_pre', 'Cos')
self.redis.lpush('countryname_pre', 'Cote  ')
self.redis.lpush('countryname_pre', 'Cro')
self.redis.lpush('countryname_pre', 'Cu')
self.redis.lpush('countryname_pre', 'Cur')
self.redis.lpush('countryname_pre', 'Cy')
self.redis.lpush('countryname_pre', 'Den')
self.redis.lpush('countryname_pre', 'Dji')
self.redis.lpush('countryname_pre', 'Dom')
self.redis.lpush('countryname_pre', 'Don')
self.redis.lpush('countryname_pre', 'Ec')
self.redis.lpush('countryname_pre', 'Eg')
self.redis.lpush('countryname_pre', 'Eri')
self.redis.lpush('countryname_pre', 'Es')
self.redis.lpush('countryname_pre', 'Eth')
self.redis.lpush('countryname_pre', 'Fi')
self.redis.lpush('countryname_pre', 'Fin')
self.redis.lpush('countryname_pre', 'Fra')
self.redis.lpush('countryname_pre', 'Ful')
self.redis.lpush('countryname_pre', 'Gab')
self.redis.lpush('countryname_pre', 'Gam')
self.redis.lpush('countryname_pre', 'Geor')
self.redis.lpush('countryname_pre', 'Germ')
self.redis.lpush('countryname_pre', 'Ghan')
self.redis.lpush('countryname_pre', 'Gre')
self.redis.lpush('countryname_pre', 'Gren')
self.redis.lpush('countryname_pre', 'Guat')
self.redis.lpush('countryname_pre', 'Gui')
self.redis.lpush('countryname_pre', 'Guy')
self.redis.lpush('countryname_pre', 'Hai')
self.redis.lpush('countryname_pre', 'Hon')
self.redis.lpush('countryname_pre', 'Hun')
self.redis.lpush('countryname_pre', 'Ice')
self.redis.lpush('countryname_pre', 'Ind')
self.redis.lpush('countryname_pre', 'Ir')
self.redis.lpush('countryname_pre', 'Ire')
self.redis.lpush('countryname_pre', 'Is')
self.redis.lpush('countryname_pre', 'It')
self.redis.lpush('countryname_pre', 'Jam')
self.redis.lpush('countryname_pre', 'Jap')
self.redis.lpush('countryname_pre', 'Jor')
self.redis.lpush('countryname_pre', 'Ka')
self.redis.lpush('countryname_pre', 'Ken')
self.redis.lpush('countryname_pre', 'Kin')
self.redis.lpush('countryname_pre', 'Kir')
self.redis.lpush('countryname_pre', 'Ko')
self.redis.lpush('countryname_pre', 'Kon')
self.redis.lpush('countryname_pre', 'Kor')
self.redis.lpush('countryname_pre', 'Ku')
self.redis.lpush('countryname_pre', 'Kyr')
self.redis.lpush('countryname_pre', 'Lan')
self.redis.lpush('countryname_pre', 'Lao')
self.redis.lpush('countryname_pre', 'Lat')
self.redis.lpush('countryname_pre', 'Leb')
self.redis.lpush('countryname_pre', 'Les')
self.redis.lpush('countryname_pre', 'Lib')
self.redis.lpush('countryname_pre', 'Liech')
self.redis.lpush('countryname_pre', 'Lith')
self.redis.lpush('countryname_pre', 'Lor')
self.redis.lpush('countryname_pre', 'Lux')
self.redis.lpush('countryname_pre', 'Mac')
self.redis.lpush('countryname_pre', 'Mad')
self.redis.lpush('countryname_pre', 'Mal')
self.redis.lpush('countryname_pre', 'Malay')
self.redis.lpush('countryname_pre', 'Mar')
self.redis.lpush('countryname_pre', 'Maur')
self.redis.lpush('countryname_pre', 'Mex')
self.redis.lpush('countryname_pre', 'Micro')
self.redis.lpush('countryname_pre', 'Mol')
self.redis.lpush('countryname_pre', 'Mon')
self.redis.lpush('countryname_pre', 'Mont')
self.redis.lpush('countryname_pre', 'Mool')
self.redis.lpush('countryname_pre', 'Mor')
self.redis.lpush('countryname_pre', 'Moz')
self.redis.lpush('countryname_pre', 'Na')
self.redis.lpush('countryname_pre', 'Nam')
self.redis.lpush('countryname_pre', 'Nep')
self.redis.lpush('countryname_pre', 'Nether')
self.redis.lpush('countryname_pre', 'Ni')
self.redis.lpush('countryname_pre', 'Nica')
self.redis.lpush('countryname_pre', 'Nill')
self.redis.lpush('countryname_pre', 'Nor')
self.redis.lpush('countryname_pre', 'Om')
self.redis.lpush('countryname_pre', 'Pak')
self.redis.lpush('countryname_pre', 'Pal')
self.redis.lpush('countryname_pre', 'Pan')
self.redis.lpush('countryname_pre', 'Pap')
self.redis.lpush('countryname_pre', 'Par')
self.redis.lpush('countryname_pre', 'Per')
self.redis.lpush('countryname_pre', 'Phil')
self.redis.lpush('countryname_pre', 'Pica')
self.redis.lpush('countryname_pre', 'Pol')
self.redis.lpush('countryname_pre', 'Port')
self.redis.lpush('countryname_pre', 'Qa')
self.redis.lpush('countryname_pre', 'Rom')
self.redis.lpush('countryname_pre', 'Rus')
self.redis.lpush('countryname_pre', 'Rwa')
self.redis.lpush('countryname_pre', 'Sal')
self.redis.lpush('countryname_pre', 'Sam')
self.redis.lpush('countryname_pre', 'Sar')
self.redis.lpush('countryname_pre', 'Saud')
self.redis.lpush('countryname_pre', 'Sen')
self.redis.lpush('countryname_pre', 'Ser')
self.redis.lpush('countryname_pre', 'Sey')
self.redis.lpush('countryname_pre', 'Sier')
self.redis.lpush('countryname_pre', 'Sing')
self.redis.lpush('countryname_pre', 'Sint')
self.redis.lpush('countryname_pre', 'Slo')
self.redis.lpush('countryname_pre', 'Sol')
self.redis.lpush('countryname_pre', 'Som')
self.redis.lpush('countryname_pre', 'Sp')
self.redis.lpush('countryname_pre', 'Su')
self.redis.lpush('countryname_pre', 'Sur')
self.redis.lpush('countryname_pre', 'Swaz')
self.redis.lpush('countryname_pre', 'Swe')
self.redis.lpush('countryname_pre', 'Switz')
self.redis.lpush('countryname_pre', 'Syr')
self.redis.lpush('countryname_pre', 'Tai')
self.redis.lpush('countryname_pre', 'Tajik')
self.redis.lpush('countryname_pre', 'Tanz')
self.redis.lpush('countryname_pre', 'Thai')
self.redis.lpush('countryname_pre', 'Tim')
self.redis.lpush('countryname_pre', 'Tog')
self.redis.lpush('countryname_pre', 'Ton')
self.redis.lpush('countryname_pre', 'Tre')
self.redis.lpush('countryname_pre', 'Trin')
self.redis.lpush('countryname_pre', 'Tun')
self.redis.lpush('countryname_pre', 'Tur')
self.redis.lpush('countryname_pre', 'Turk')
self.redis.lpush('countryname_pre', 'Tuv')
self.redis.lpush('countryname_pre', 'Ug')
self.redis.lpush('countryname_pre', 'Ukr')
self.redis.lpush('countryname_pre', 'Umb')
self.redis.lpush('countryname_pre', 'Uru')
self.redis.lpush('countryname_pre', 'Uzb')
self.redis.lpush('countryname_pre', 'Van')
self.redis.lpush('countryname_pre', 'Ven')
self.redis.lpush('countryname_pre', 'Viet')
self.redis.lpush('countryname_pre', 'Wal')
self.redis.lpush('countryname_pre', 'Yem')
self.redis.lpush('countryname_pre', 'Zam')
self.redis.lpush('countryname_pre', 'Zeal')
self.redis.lpush('countryname_pre', 'Zim')

self.redis.lpush('countryname_root', 'ad')
self.redis.lpush('countryname_root', 'ag')
self.redis.lpush('countryname_root', 'agas')
self.redis.lpush('countryname_root', 'aic')
self.redis.lpush('countryname_root', 'ain ')
self.redis.lpush('countryname_root', 'al')
self.redis.lpush('countryname_root', 'am')
self.redis.lpush('countryname_root', 'amb')
self.redis.lpush('countryname_root', 'an')
self.redis.lpush('countryname_root', 'and')
self.redis.lpush('countryname_root', 'ap')
self.redis.lpush('countryname_root', 'aq')
self.redis.lpush('countryname_root', 'ar')
self.redis.lpush('countryname_root', 'ark')
self.redis.lpush('countryname_root', 'at')
self.redis.lpush('countryname_root', 'au')
self.redis.lpush('countryname_root', 'aw')
self.redis.lpush('countryname_root', 'ays')
self.redis.lpush('countryname_root', 'b')
self.redis.lpush('countryname_root', 'bab')
self.redis.lpush('countryname_root', 'be')
self.redis.lpush('countryname_root', 'bod')
self.redis.lpush('countryname_root', 'bor')
self.redis.lpush('countryname_root', 'bou')
self.redis.lpush('countryname_root', 'can')
self.redis.lpush('countryname_root', 'dan')
self.redis.lpush('countryname_root', 'den')
self.redis.lpush('countryname_root', 'din')
self.redis.lpush('countryname_root', 'do')
self.redis.lpush('countryname_root', 'dur')
self.redis.lpush('countryname_root', 'ea')
self.redis.lpush('countryname_root', 'ec')
self.redis.lpush('countryname_root', 'ech ')
self.redis.lpush('countryname_root', 'ed')
self.redis.lpush('countryname_root', 'eg')
self.redis.lpush('countryname_root', 'ekis')
self.redis.lpush('countryname_root', 'el')
self.redis.lpush('countryname_root', 'em')
self.redis.lpush('countryname_root', 'en')
self.redis.lpush('countryname_root', 'er')
self.redis.lpush('countryname_root', 'est')
self.redis.lpush('countryname_root', 'ezu')
self.redis.lpush('countryname_root', 'ga')
self.redis.lpush('countryname_root', 'gan')
self.redis.lpush('countryname_root', 'gar')
self.redis.lpush('countryname_root', 'ger')
self.redis.lpush('countryname_root', 'ghan')
self.redis.lpush('countryname_root', 'gia')
self.redis.lpush('countryname_root', 'gium')
self.redis.lpush('countryname_root', 'go')
self.redis.lpush('countryname_root', 'gol')
self.redis.lpush('countryname_root', 'gyz')
self.redis.lpush('countryname_root', 'ham')
self.redis.lpush('countryname_root', 'hr')
self.redis.lpush('countryname_root', 'ia')
self.redis.lpush('countryname_root', 'ib')
self.redis.lpush('countryname_root', 'ic')
self.redis.lpush('countryname_root', 'id')
self.redis.lpush('countryname_root', 'ig')
self.redis.lpush('countryname_root', 'il')
self.redis.lpush('countryname_root', 'in')
self.redis.lpush('countryname_root', 'inic')
self.redis.lpush('countryname_root', 'iop')
self.redis.lpush('countryname_root', 'ip')
self.redis.lpush('countryname_root', 'is')
self.redis.lpush('countryname_root', 'itan')
self.redis.lpush('countryname_root', 'its')
self.redis.lpush('countryname_root', 'iv')
self.redis.lpush('countryname_root', 'ize')
self.redis.lpush('countryname_root', 'ji')
self.redis.lpush('countryname_root', 'kan')
self.redis.lpush('countryname_root', 'kil')
self.redis.lpush('countryname_root', 'kin')
self.redis.lpush('countryname_root', 'kmen')
self.redis.lpush('countryname_root', 'kry')
self.redis.lpush('countryname_root', 'lak')
self.redis.lpush('countryname_root', 'land ')
self.redis.lpush('countryname_root', 'loon')
self.redis.lpush('countryname_root', 'ma')
self.redis.lpush('countryname_root', 'man')
self.redis.lpush('countryname_root', 'mar')
self.redis.lpush('countryname_root', 'mou')
self.redis.lpush('countryname_root', 'na')
self.redis.lpush('countryname_root', 'nad')
self.redis.lpush('countryname_root', 'nah')
self.redis.lpush('countryname_root', 'nam')
self.redis.lpush('countryname_root', 'nes')
self.redis.lpush('countryname_root', 'ngl')
self.redis.lpush('countryname_root', 'oa ')
self.redis.lpush('countryname_root', 'om')
self.redis.lpush('countryname_root', 'on')
self.redis.lpush('countryname_root', 'or')
self.redis.lpush('countryname_root', 'prus')
self.redis.lpush('countryname_root', 'rac')
self.redis.lpush('countryname_root', 'rag')
self.redis.lpush('countryname_root', 'ran')
self.redis.lpush('countryname_root', 'rbad')
self.redis.lpush('countryname_root', 'ri')
self.redis.lpush('countryname_root', 'rin')
self.redis.lpush('countryname_root', 's')
self.redis.lpush('countryname_root', 'sak')
self.redis.lpush('countryname_root', 'shal')
self.redis.lpush('countryname_root', 'ten')
self.redis.lpush('countryname_root', 'tene')
self.redis.lpush('countryname_root', 'ti')
self.redis.lpush('countryname_root', 'ton')
self.redis.lpush('countryname_root', 'tra')
self.redis.lpush('countryname_root', 'ua')
self.redis.lpush('countryname_root', 'uan')
self.redis.lpush('countryname_root', 'uat')
self.redis.lpush('countryname_root', 'ub')
self.redis.lpush('countryname_root', 'ug')
self.redis.lpush('countryname_root', 'ur')
self.redis.lpush('countryname_root', 'vak')
self.redis.lpush('countryname_root', 'ven')
self.redis.lpush('countryname_root', 'wan')
self.redis.lpush('countryname_root', 'zakh')

self.redis.lpush('countryname_post', 'a')
self.redis.lpush('countryname_post', 'ad')
self.redis.lpush('countryname_post', 'ain')
self.redis.lpush('countryname_post', 'ak')
self.redis.lpush('countryname_post', 'al')
self.redis.lpush('countryname_post', 'an')
self.redis.lpush('countryname_post', 'and')
self.redis.lpush('countryname_post', 'andy')
self.redis.lpush('countryname_post', 'anti')
self.redis.lpush('countryname_post', 'ao')
self.redis.lpush('countryname_post', 'as')
self.redis.lpush('countryname_post', 'aso')
self.redis.lpush('countryname_post', 'at')
self.redis.lpush('countryname_post', 'ati')
self.redis.lpush('countryname_post', 'bia')
self.redis.lpush('countryname_post', 'bique')
self.redis.lpush('countryname_post', 'bourg')
self.redis.lpush('countryname_post', 'bwe')
self.redis.lpush('countryname_post', 'ca')
self.redis.lpush('countryname_post', 'car')
self.redis.lpush('countryname_post', 'cco')
self.redis.lpush('countryname_post', 'ce')
self.redis.lpush('countryname_post', 'co')
self.redis.lpush('countryname_post', 'da')
self.redis.lpush('countryname_post', 'dia')
self.redis.lpush('countryname_post', 'dor')
self.redis.lpush('countryname_post', 'ea')
self.redis.lpush('countryname_post', 'ech')
self.redis.lpush('countryname_post', 'eese')
self.redis.lpush('countryname_post', 'egro')
self.redis.lpush('countryname_post', 'elles')
self.redis.lpush('countryname_post', 'ep')
self.redis.lpush('countryname_post', 'esh')
self.redis.lpush('countryname_post', 'gua')
self.redis.lpush('countryname_post', 'guay')
self.redis.lpush('countryname_post', 'ia')
self.redis.lpush('countryname_post', 'ica')
self.redis.lpush('countryname_post', 'ican')
self.redis.lpush('countryname_post', 'ijan')
self.redis.lpush('countryname_post', 'il')
self.redis.lpush('countryname_post', 'ina')
self.redis.lpush('countryname_post', 'ines')
self.redis.lpush('countryname_post', 'ique')
self.redis.lpush('countryname_post', 'ish')
self.redis.lpush('countryname_post', 'istan')
self.redis.lpush('countryname_post', 'ives')
self.redis.lpush('countryname_post', 'key')
self.redis.lpush('countryname_post', 'l')
self.redis.lpush('countryname_post', 'la')
self.redis.lpush('countryname_post', 'land')
self.redis.lpush('countryname_post', 'lia')
self.redis.lpush('countryname_post', 'lu')
self.redis.lpush('countryname_post', 'ly')
self.redis.lpush('countryname_post', 'm')
self.redis.lpush('countryname_post', 'mon')
self.redis.lpush('countryname_post', 'mou')
self.redis.lpush('countryname_post', 'n')
self.redis.lpush('countryname_post', 'name')
self.redis.lpush('countryname_post', 'nce')
self.redis.lpush('countryname_post', 'nd')
self.redis.lpush('countryname_post', 'nda')
self.redis.lpush('countryname_post', 'ne')
self.redis.lpush('countryname_post', 'nea')
self.redis.lpush('countryname_post', 'nei')
self.redis.lpush('countryname_post', 'non')
self.redis.lpush('countryname_post', 'ny')
self.redis.lpush('countryname_post', 'or')
self.redis.lpush('countryname_post', 'os')
self.redis.lpush('countryname_post', 'oupe')
self.redis.lpush('countryname_post', 'ovo')
self.redis.lpush('countryname_post', 'pia')
self.redis.lpush('countryname_post', 'pore')
self.redis.lpush('countryname_post', 'q')
self.redis.lpush('countryname_post', 'ra')
self.redis.lpush('countryname_post', 'rael')
self.redis.lpush('countryname_post', 'ria')
self.redis.lpush('countryname_post', 'rk')
self.redis.lpush('countryname_post', 'roon')
self.redis.lpush('countryname_post', 'ros')
self.redis.lpush('countryname_post', 'rra')
self.redis.lpush('countryname_post', 'rus')
self.redis.lpush('countryname_post', 'ry')
self.redis.lpush('countryname_post', 'stan')
self.redis.lpush('countryname_post', 'stein')
self.redis.lpush('countryname_post', 'ta')
self.redis.lpush('countryname_post', 'tan')
self.redis.lpush('countryname_post', 'tar')
self.redis.lpush('countryname_post', 'tho')
self.redis.lpush('countryname_post', 'tu')
self.redis.lpush('countryname_post', 'u')
self.redis.lpush('countryname_post', 'ubia')
self.redis.lpush('countryname_post', 'undi')
self.redis.lpush('countryname_post', 'us')
self.redis.lpush('countryname_post', 'uti')
self.redis.lpush('countryname_post', 'va')
self.redis.lpush('countryname_post', 'via')
self.redis.lpush('countryname_post', 'way')
self.redis.lpush('countryname_post', 'wi')
self.redis.lpush('countryname_post', 'ya')
self.redis.lpush('countryname_post', 'ypt')
self.redis.lpush('countryname_post', 'ysia')
self.redis.lpush('countryname_post', 'ze')


self.redis.lpush('countryname_trailer', 'District')
self.redis.lpush('countryname_trailer', 'Domain')
self.redis.lpush('countryname_trailer', 'Province')
self.redis.lpush('countryname_trailer', 'Region')
self.redis.lpush('countryname_trailer', 'Territory')
self.redis.lpush('countryname_trailer', 'Territories')
self.redis.lpush('countryname_trailer', 'Empire')
self.redis.lpush('countryname_trailer', 'Kingdom')
self.redis.lpush('countryname_trailer', 'states')
self.redis.lpush('countryname_trailer', 'Coalition')
self.redis.lpush('countryname_trailer', 'Republic')
self.redis.lpush('countryname_trailer', 'Lands')



