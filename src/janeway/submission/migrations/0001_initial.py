# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-11 12:03
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import submission.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('journal', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(blank=True, max_length=300, null=True)),
                ('abstract', models.TextField(blank=True)),
                ('language', models.CharField(blank=True, choices=[('eng', 'English'), ('abk', 'Abkhazian'), ('ace', 'Achinese'), ('ach', 'Acoli'), ('ada', 'Adangme'), ('ady', 'Adyghe; Adygei'), ('aar', 'Afar'), ('afh', 'Afrihili'), ('afr', 'Afrikaans'), ('afa', 'Afro-Asiatic languages'), ('ain', 'Ainu'), ('aka', 'Akan'), ('akk', 'Akkadian'), ('sqi', 'Albanian'), ('ale', 'Aleut'), ('alg', 'Algonquian languages'), ('tut', 'Altaic languages'), ('amh', 'Amharic'), ('anp', 'Angika'), ('apa', 'Apache languages'), ('ara', 'Arabic'), ('arg', 'Aragonese'), ('arp', 'Arapaho'), ('arw', 'Arawak'), ('hye', 'Armenian'), ('rup', 'Aromanian; Arumanian; Macedo-Romanian'), ('art', 'Artificial languages'), ('asm', 'Assamese'), ('ast', 'Asturian; Bable; Leonese; Asturleonese'), ('ath', 'Athapascan languages'), ('aus', 'Australian languages'), ('map', 'Austronesian languages'), ('ava', 'Avaric'), ('ave', 'Avestan'), ('awa', 'Awadhi'), ('aym', 'Aymara'), ('aze', 'Azerbaijani'), ('ban', 'Balinese'), ('bat', 'Baltic languages'), ('bal', 'Baluchi'), ('bam', 'Bambara'), ('bai', 'Bamileke languages'), ('bad', 'Banda languages'), ('bnt', 'Bantu languages'), ('bas', 'Basa'), ('bak', 'Bashkir'), ('eus', 'Basque'), ('btk', 'Batak languages'), ('bej', 'Beja; Bedawiyet'), ('bel', 'Belarusian'), ('bem', 'Bemba'), ('ben', 'Bengali'), ('ber', 'Berber languages'), ('bho', 'Bhojpuri'), ('bih', 'Bihari languages'), ('bik', 'Bikol'), ('bin', 'Bini; Edo'), ('bis', 'Bislama'), ('byn', 'Blin; Bilin'), ('zbl', 'Blissymbols; Blissymbolics; Bliss'), ('nob', 'Bokmål, Norwegian; Norwegian Bokmål'), ('bos', 'Bosnian'), ('bra', 'Braj'), ('bre', 'Breton'), ('bug', 'Buginese'), ('bul', 'Bulgarian'), ('bua', 'Buriat'), ('mya', 'Burmese'), ('cad', 'Caddo'), ('cat', 'Catalan; Valencian'), ('cau', 'Caucasian languages'), ('ceb', 'Cebuano'), ('cel', 'Celtic languages'), ('cai', 'Central American Indian languages'), ('khm', 'Central Khmer'), ('chg', 'Chagatai'), ('cmc', 'Chamic languages'), ('cha', 'Chamorro'), ('che', 'Chechen'), ('chr', 'Cherokee'), ('chy', 'Cheyenne'), ('chb', 'Chibcha'), ('nya', 'Chichewa; Chewa; Nyanja'), ('zho', 'Chinese'), ('chn', 'Chinook jargon'), ('chp', 'Chipewyan; Dene Suline'), ('cho', 'Choctaw'), ('chu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'), ('chk', 'Chuukese'), ('chv', 'Chuvash'), ('nwc', 'Classical Newari; Old Newari; Classical Nepal Bhasa'), ('syc', 'Classical Syriac'), ('cop', 'Coptic'), ('cor', 'Cornish'), ('cos', 'Corsican'), ('cre', 'Cree'), ('mus', 'Creek'), ('crp', 'Creoles and pidgins'), ('cpe', 'Creoles and pidgins, English based'), ('cpf', 'Creoles and pidgins, French-based'), ('cpp', 'Creoles and pidgins, Portuguese-based'), ('crh', 'Crimean Tatar; Crimean Turkish'), ('hrv', 'Croatian'), ('cus', 'Cushitic languages'), ('ces', 'Czech'), ('dak', 'Dakota'), ('dan', 'Danish'), ('dar', 'Dargwa'), ('del', 'Delaware'), ('din', 'Dinka'), ('div', 'Divehi; Dhivehi; Maldivian'), ('doi', 'Dogri'), ('dgr', 'Dogrib'), ('dra', 'Dravidian languages'), ('dua', 'Duala'), ('dum', 'Dutch, Middle (ca. 1050-1350)'), ('nld', 'Dutch; Flemish'), ('dyu', 'Dyula'), ('dzo', 'Dzongkha'), ('frs', 'Eastern Frisian'), ('efi', 'Efik'), ('egy', 'Egyptian (Ancient)'), ('eka', 'Ekajuk'), ('elx', 'Elamite'), ('enm', 'English, Middle (1100-1500)'), ('ang', 'English, Old (ca. 450-1100)'), ('myv', 'Erzya'), ('epo', 'Esperanto'), ('est', 'Estonian'), ('ewe', 'Ewe'), ('ewo', 'Ewondo'), ('fan', 'Fang'), ('fat', 'Fanti'), ('fao', 'Faroese'), ('fij', 'Fijian'), ('fil', 'Filipino; Pilipino'), ('fin', 'Finnish'), ('fiu', 'Finno-Ugrian languages'), ('fon', 'Fon'), ('fra', 'French'), ('frm', 'French, Middle (ca. 1400-1600)'), ('fro', 'French, Old (842-ca. 1400)'), ('fur', 'Friulian'), ('ful', 'Fulah'), ('gaa', 'Ga'), ('gla', 'Gaelic; Scottish Gaelic'), ('car', 'Galibi Carib'), ('glg', 'Galician'), ('lug', 'Ganda'), ('gay', 'Gayo'), ('gba', 'Gbaya'), ('gez', 'Geez'), ('kat', 'Georgian'), ('deu', 'German'), ('gmh', 'German, Middle High (ca. 1050-1500)'), ('goh', 'German, Old High (ca. 750-1050)'), ('gem', 'Germanic languages'), ('gil', 'Gilbertese'), ('gon', 'Gondi'), ('gor', 'Gorontalo'), ('got', 'Gothic'), ('grb', 'Grebo'), ('grc', 'Greek, Ancient (to 1453)'), ('ell', 'Greek, Modern (1453-)'), ('grn', 'Guarani'), ('guj', 'Gujarati'), ('gwi', "Gwich'in"), ('hai', 'Haida'), ('hat', 'Haitian; Haitian Creole'), ('hau', 'Hausa'), ('haw', 'Hawaiian'), ('heb', 'Hebrew'), ('her', 'Herero'), ('hil', 'Hiligaynon'), ('him', 'Himachali languages; Western Pahari languages'), ('hin', 'Hindi'), ('hmo', 'Hiri Motu'), ('hit', 'Hittite'), ('hmn', 'Hmong; Mong'), ('hun', 'Hungarian'), ('hup', 'Hupa'), ('iba', 'Iban'), ('isl', 'Icelandic'), ('ido', 'Ido'), ('ibo', 'Igbo'), ('ijo', 'Ijo languages'), ('ilo', 'Iloko'), ('smn', 'Inari Sami'), ('inc', 'Indic languages'), ('ine', 'Indo-European languages'), ('ind', 'Indonesian'), ('inh', 'Ingush'), ('ina', 'Interlingua (International Auxiliary Language Association)'), ('ile', 'Interlingue; Occidental'), ('iku', 'Inuktitut'), ('ipk', 'Inupiaq'), ('ira', 'Iranian languages'), ('gle', 'Irish'), ('mga', 'Irish, Middle (900-1200)'), ('sga', 'Irish, Old (to 900)'), ('iro', 'Iroquoian languages'), ('ita', 'Italian'), ('jpn', 'Japanese'), ('jav', 'Javanese'), ('jrb', 'Judeo-Arabic'), ('jpr', 'Judeo-Persian'), ('kbd', 'Kabardian'), ('kab', 'Kabyle'), ('kac', 'Kachin; Jingpho'), ('kal', 'Kalaallisut; Greenlandic'), ('xal', 'Kalmyk; Oirat'), ('kam', 'Kamba'), ('kan', 'Kannada'), ('kau', 'Kanuri'), ('kaa', 'Kara-Kalpak'), ('krc', 'Karachay-Balkar'), ('krl', 'Karelian'), ('kar', 'Karen languages'), ('kas', 'Kashmiri'), ('csb', 'Kashubian'), ('kaw', 'Kawi'), ('kaz', 'Kazakh'), ('kha', 'Khasi'), ('khi', 'Khoisan languages'), ('kho', 'Khotanese;Sakan'), ('kik', 'Kikuyu; Gikuyu'), ('kmb', 'Kimbundu'), ('kin', 'Kinyarwanda'), ('kir', 'Kirghiz; Kyrgyz'), ('tlh', 'Klingon; tlhIngan-Hol'), ('kom', 'Komi'), ('kon', 'Kongo'), ('kok', 'Konkani'), ('kor', 'Korean'), ('kos', 'Kosraean'), ('kpe', 'Kpelle'), ('kro', 'Kru languages'), ('kua', 'Kuanyama; Kwanyama'), ('kum', 'Kumyk'), ('kur', 'Kurdish'), ('kru', 'Kurukh'), ('kut', 'Kutenai'), ('lad', 'Ladino'), ('lah', 'Lahnda'), ('lam', 'Lamba'), ('day', 'Land Dayak languages'), ('lao', 'Lao'), ('lat', 'Latin'), ('lav', 'Latvian'), ('lez', 'Lezghian'), ('lim', 'Limburgan; Limburger; Limburgish'), ('lin', 'Lingala'), ('lit', 'Lithuanian'), ('jbo', 'Lojban'), ('nds', 'Low German; Low Saxon; German, Low; Saxon, Low'), ('dsb', 'Lower Sorbian'), ('loz', 'Lozi'), ('lub', 'Luba-Katanga'), ('lua', 'Luba-Lulua'), ('lui', 'Luiseno'), ('smj', 'Lule Sami'), ('lun', 'Lunda'), ('luo', 'Luo (Kenya and Tanzania)'), ('lus', 'Lushai'), ('ltz', 'Luxembourgish; Letzeburgesch'), ('mkd', 'Macedonian'), ('mad', 'Madurese'), ('mag', 'Magahi'), ('mai', 'Maithili'), ('mak', 'Makasar'), ('mlg', 'Malagasy'), ('msa', 'Malay'), ('mal', 'Malayalam'), ('mlt', 'Maltese'), ('mnc', 'Manchu'), ('mdr', 'Mandar'), ('man', 'Mandingo'), ('mni', 'Manipuri'), ('mno', 'Manobo languages'), ('glv', 'Manx'), ('mri', 'Maori'), ('arn', 'Mapudungun; Mapuche'), ('mar', 'Marathi'), ('chm', 'Mari'), ('mah', 'Marshallese'), ('mwr', 'Marwari'), ('mas', 'Masai'), ('myn', 'Mayan languages'), ('men', 'Mende'), ('mic', "Mi'kmaq; Micmac"), ('min', 'Minangkabau'), ('mwl', 'Mirandese'), ('moh', 'Mohawk'), ('mdf', 'Moksha'), ('mol', 'Moldavian; Moldovan'), ('mkh', 'Mon-Khmer languages'), ('lol', 'Mongo'), ('mon', 'Mongolian'), ('mos', 'Mossi'), ('mul', 'Multiple languages'), ('mun', 'Munda languages'), ('nqo', "N'Ko"), ('nah', 'Nahuatl languages'), ('nau', 'Nauru'), ('nav', 'Navajo; Navaho'), ('nde', 'Ndebele, North; North Ndebele'), ('nbl', 'Ndebele, South; South Ndebele'), ('ndo', 'Ndonga'), ('nap', 'Neapolitan'), ('new', 'Nepal Bhasa; Newari'), ('nep', 'Nepali'), ('nia', 'Nias'), ('nic', 'Niger-Kordofanian languages'), ('ssa', 'Nilo-Saharan languages'), ('niu', 'Niuean'), ('zxx', 'No linguistic content; Not applicable'), ('nog', 'Nogai'), ('non', 'Norse, Old'), ('nai', 'North American Indian languages'), ('frr', 'Northern Frisian'), ('sme', 'Northern Sami'), ('nor', 'Norwegian'), ('nno', 'Norwegian Nynorsk; Nynorsk, Norwegian'), ('nub', 'Nubian languages'), ('nym', 'Nyamwezi'), ('nyn', 'Nyankole'), ('nyo', 'Nyoro'), ('nzi', 'Nzima'), ('oci', 'Occitan (post 1500)'), ('arc', 'Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)'), ('oji', 'Ojibwa'), ('ori', 'Oriya'), ('orm', 'Oromo'), ('osa', 'Osage'), ('oss', 'Ossetian; Ossetic'), ('oto', 'Otomian languages'), ('pal', 'Pahlavi'), ('pau', 'Palauan'), ('pli', 'Pali'), ('pam', 'Pampanga; Kapampangan'), ('pag', 'Pangasinan'), ('pan', 'Panjabi; Punjabi'), ('pap', 'Papiamento'), ('paa', 'Papuan languages'), ('nso', 'Pedi; Sepedi; Northern Sotho'), ('fas', 'Persian'), ('peo', 'Persian, Old (ca. 600-400 B.C.)'), ('phi', 'Philippine languages'), ('phn', 'Phoenician'), ('pon', 'Pohnpeian'), ('pol', 'Polish'), ('por', 'Portuguese'), ('pra', 'Prakrit languages'), ('pro', 'Provençal, Old (to 1500); Occitan, Old (to 1500)'), ('pus', 'Pushto; Pashto'), ('que', 'Quechua'), ('raj', 'Rajasthani'), ('rap', 'Rapanui'), ('rar', 'Rarotongan; Cook Islands Maori'), ('qaa-qtz', 'Reserved for local use'), ('roa', 'Romance languages'), ('ron', 'Romanian'), ('roh', 'Romansh'), ('rom', 'Romany'), ('run', 'Rundi'), ('rus', 'Russian'), ('sal', 'Salishan languages'), ('sam', 'Samaritan Aramaic'), ('smi', 'Sami languages'), ('smo', 'Samoan'), ('sad', 'Sandawe'), ('sag', 'Sango'), ('san', 'Sanskrit'), ('sat', 'Santali'), ('srd', 'Sardinian'), ('sas', 'Sasak'), ('sco', 'Scots'), ('sel', 'Selkup'), ('sem', 'Semitic languages'), ('srp', 'Serbian'), ('srr', 'Serer'), ('shn', 'Shan'), ('sna', 'Shona'), ('iii', 'Sichuan Yi; Nuosu'), ('scn', 'Sicilian'), ('sid', 'Sidamo'), ('sgn', 'Sign Languages'), ('bla', 'Siksika'), ('snd', 'Sindhi'), ('sin', 'Sinhala; Sinhalese'), ('sit', 'Sino-Tibetan languages'), ('sio', 'Siouan languages'), ('sms', 'Skolt Sami'), ('den', 'Slave (Athapascan)'), ('sla', 'Slavic languages'), ('slk', 'Slovak'), ('slv', 'Slovenian'), ('sog', 'Sogdian'), ('som', 'Somali'), ('son', 'Songhai languages'), ('snk', 'Soninke'), ('wen', 'Sorbian languages'), ('sot', 'Sotho, Southern'), ('sai', 'South American Indian languages'), ('alt', 'Southern Altai'), ('sma', 'Southern Sami'), ('spa', 'Spanish; Castilian'), ('srn', 'Sranan Tongo'), ('zgh', 'Standard Moroccan Tamazight'), ('suk', 'Sukuma'), ('sux', 'Sumerian'), ('sun', 'Sundanese'), ('sus', 'Susu'), ('swa', 'Swahili'), ('ssw', 'Swati'), ('swe', 'Swedish'), ('gsw', 'Swiss German; Alemannic; Alsatian'), ('syr', 'Syriac'), ('tgl', 'Tagalog'), ('tah', 'Tahitian'), ('tai', 'Tai languages'), ('tgk', 'Tajik'), ('tmh', 'Tamashek'), ('tam', 'Tamil'), ('tat', 'Tatar'), ('tel', 'Telugu'), ('ter', 'Tereno'), ('tet', 'Tetum'), ('tha', 'Thai'), ('bod', 'Tibetan'), ('tig', 'Tigre'), ('tir', 'Tigrinya'), ('tem', 'Timne'), ('tiv', 'Tiv'), ('tli', 'Tlingit'), ('tpi', 'Tok Pisin'), ('tkl', 'Tokelau'), ('tog', 'Tonga (Nyasa)'), ('ton', 'Tonga (Tonga Islands)'), ('tsi', 'Tsimshian'), ('tso', 'Tsonga'), ('tsn', 'Tswana'), ('tum', 'Tumbuka'), ('tup', 'Tupi languages'), ('tur', 'Turkish'), ('ota', 'Turkish, Ottoman (1500-1928)'), ('tuk', 'Turkmen'), ('tvl', 'Tuvalu'), ('tyv', 'Tuvinian'), ('twi', 'Twi'), ('udm', 'Udmurt'), ('uga', 'Ugaritic'), ('uig', 'Uighur; Uyghur'), ('ukr', 'Ukrainian'), ('umb', 'Umbundu'), ('mis', 'Uncoded languages'), ('und', 'Undetermined'), ('hsb', 'Upper Sorbian'), ('urd', 'Urdu'), ('uzb', 'Uzbek'), ('vai', 'Vai'), ('ven', 'Venda'), ('vie', 'Vietnamese'), ('vol', 'Volapük'), ('vot', 'Votic'), ('wak', 'Wakashan languages'), ('wln', 'Walloon'), ('war', 'Waray'), ('was', 'Washo'), ('cym', 'Welsh'), ('fry', 'Western Frisian'), ('wal', 'Wolaitta; Wolaytta'), ('wol', 'Wolof'), ('xho', 'Xhosa'), ('sah', 'Yakut'), ('yao', 'Yao'), ('yap', 'Yapese'), ('yid', 'Yiddish'), ('yor', 'Yoruba'), ('ypk', 'Yupik languages'), ('znd', 'Zande languages'), ('zap', 'Zapotec'), ('zza', 'Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki'), ('zen', 'Zenaga'), ('zha', 'Zhuang; Chuang'), ('zul', 'Zulu'), ('zun', 'Zuni')], max_length=200, null=True)),
                ('is_remote', models.BooleanField(default=False, help_text='Check if this article is remote', verbose_name='Remote article')),
                ('remote_url', models.URLField(blank=True, help_text='If the article is remote, its URL should be added.', null=True)),
                ('competing_interests_bool', models.BooleanField(default=False)),
                ('competing_interests', models.TextField(blank=True, null=True)),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('date_accepted', models.DateTimeField(blank=True, null=True)),
                ('date_declined', models.DateTimeField(blank=True, null=True)),
                ('date_submitted', models.DateTimeField(blank=True, null=True)),
                ('date_published', models.DateTimeField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('current_step', models.IntegerField(default=1)),
                ('page_numbers', models.CharField(blank=True, max_length=20, null=True)),
                ('stage', models.CharField(choices=[('Unsubmitted', 'Unsubmitted'), ('Unassigned', 'Unassigned'), ('Assigned', 'Assigned'), ('Under Review', 'Under Review'), ('Under Revision', 'Under Revision'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Editor Copyediting', 'Editor Copyediting'), ('Author Copyediting', 'Author Copyediting'), ('Final Copyediting', 'Final Copyediting'), ('Typesetting', 'Typesetting'), ('Proofing', 'Proofing'), ('pre_publication', 'Pre Publication'), ('Published', 'Published')], default='Unsubmitted', max_length=200)),
                ('publication_fees', models.BooleanField(default=False)),
                ('submission_requirements', models.BooleanField(default=False)),
                ('copyright_notice', models.BooleanField(default=False)),
                ('comments_editor', models.TextField(blank=True, null=True, verbose_name='Comments to the Editor')),
                ('exclude_from_slider', models.BooleanField(default=False)),
                ('peer_reviewed', models.BooleanField(default=True)),
                ('is_import', models.BooleanField(default=False)),
                ('article_agreement', models.TextField(default='')),
                ('ithenticate_id', models.TextField(blank=True, null=True)),
                ('ithenticate_score', models.IntegerField(blank=True, null=True)),
                ('meta_image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/ajrbyers/code/janeway/src/media'), upload_to=submission.models.article_media_upload)),
                ('authors', models.ManyToManyField(blank=True, null=True, related_name='authors', to=settings.AUTH_USER_MODEL)),
                ('correspondence_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='correspondence_author', to=settings.AUTH_USER_MODEL)),
                ('data_figure_files', models.ManyToManyField(blank=True, null=True, related_name='data_figure_files', to='core.File')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Journal')),
            ],
            options={
                'ordering': ('-date_published', 'title'),
            },
        ),
        migrations.CreateModel(
            name='ArticleStageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_from', models.CharField(max_length=200)),
                ('stage_to', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.Article')),
            ],
            options={
                'ordering': ('-date_time',),
            },
        ),
        migrations.CreateModel(
            name='FrozenAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('institution', models.CharField(max_length=1000)),
                ('department', models.CharField(blank=True, max_length=300, null=True)),
                ('order', models.PositiveIntegerField(default=1)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='submission.Article')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Country')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('short_name', models.CharField(max_length=15)),
                ('url', models.URLField(max_length=1000)),
                ('text', models.TextField(blank=True, null=True)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.Article')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_time',),
            },
        ),
        migrations.CreateModel(
            name='PublisherNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=4000)),
                ('sequence', models.PositiveIntegerField(default=999)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('sequence',),
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_reviewers', models.IntegerField(default=2)),
                ('is_filterable', models.BooleanField(default=True)),
                ('public_submissions', models.BooleanField(default=True)),
                ('indexing', models.BooleanField(default=True)),
                ('sequence', models.PositiveIntegerField(default=0)),
                ('editors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Journal')),
                ('section_editors', models.ManyToManyField(related_name='section_editors', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('sequence',),
            },
        ),
        migrations.CreateModel(
            name='SectionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('plural', models.CharField(blank=True, max_length=200, null=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='submission.Section')),
            ],
            options={
                'db_table': 'submission_section_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='submission.Keyword'),
        ),
        migrations.AddField(
            model_name='article',
            name='large_image_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_file', to='core.File'),
        ),
        migrations.AddField(
            model_name='article',
            name='license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='submission.Licence'),
        ),
        migrations.AddField(
            model_name='article',
            name='manuscript_files',
            field=models.ManyToManyField(blank=True, null=True, related_name='manuscript_files', to='core.File'),
        ),
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='primary_issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.Issue'),
        ),
        migrations.AddField(
            model_name='article',
            name='publisher_notes',
            field=models.ManyToManyField(blank=True, null=True, related_name='publisher_notes', to='submission.PublisherNote'),
        ),
        migrations.AddField(
            model_name='article',
            name='render_galley',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='render_galley', to='core.Galley'),
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='submission.Section'),
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail_image_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thumbnail_file', to='core.File'),
        ),
        migrations.AlterUniqueTogether(
            name='sectiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]