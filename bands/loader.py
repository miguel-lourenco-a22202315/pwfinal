from bands.models import Bandas, Albuns, Musicas
import json

Bandas.objects.all().delete()
Albuns.objects.all().delete()
Musicas.objects.all().delete()

with open('bands/json/bandas.json') as f:
    bandasdata = json.load(f)
    for bandadata in bandasdata['bandas']:
        banda, _ = Bandas.objects.get_or_create(
            nome=bandadata['nome'],
            nacionalidade=bandadata['nacionalidade'],
            ano_criacao=bandadata['ano_criacao']
        )

with open('bands/json/discos.json') as f:
    discos_data = json.load(f)
    for disco_data in discos_data['discos']:

        banda, _ = Bandas.objects.get_or_create(nome=disco_data['banda'])


        album, _ = Albuns.objects.get_or_create(
            titulo=disco_data['titulo'],
            ano_lancamento=disco_data['ano_lancamento'],
            banda=banda
        )


        for musica_data in disco_data['musicas']:
            Musicas.objects.create(
                titulo=musica_data['titulo'],
                duracao=musica_data['duracao'],
                album=album
            )
