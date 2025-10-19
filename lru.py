# LRU 

def lru(sequencia, memoria_maxima, pagina_procurada):
    blocos = []        # quadros de memória
    tempo_uso = []     # ordem do uso recente (fim = mais recente)
    quantidade_carregadas = 0

    print(f"Sequência completa de páginas: {sequencia}\n")

    for pagina in sequencia:
        if pagina in blocos:
            # acerto: só atualiza "recência"
            tempo_uso.remove(pagina)
            tempo_uso.append(pagina)
            print(f"Página {pagina}: acerto. Atualizando uso.")
        else:
            quantidade_carregadas += 1
            if len(blocos) < memoria_maxima:
                # ainda há espaço
                blocos.append(pagina)
                tempo_uso.append(pagina)
                print(f"Página {pagina}: adicionada. Estado: {blocos}")
            else:
                # substitui a menos recentemente usada (início da lista)
                menos_usada = tempo_uso.pop(0)
                idx = blocos.index(menos_usada)
                blocos[idx] = pagina
                tempo_uso.append(pagina)
                print(f"Página {pagina}: substituiu {menos_usada}. Estado: {blocos}")

    return blocos, quantidade_carregadas


# Testes
testes = [
    {"id": "a", "sequencia": [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7], "alvo": 7, "pergunta": "Qual espaço terá a página 7?"},
    {"id": "b", "sequencia": [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11], "alvo": 11, "pergunta": "Qual espaço terá a página 11?"},
    {"id": "c", "sequencia": [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11], "alvo": 11, "pergunta": "Qual espaço terá a página 11?"}
]

memoria_maxima = 8

for t in testes:
    print("\n" + "="*60)
    print(f"Pergunta {t['id']}): {t['pergunta']}")
    blocos, q = lru(t["sequencia"], memoria_maxima, t["alvo"])
    if t["alvo"] in blocos:
        pos = blocos.index(t["alvo"]) + 1
        print(f"\nNo final, a página {t['alvo']} está no quadro {pos}.")
    else:
        print(f"\nNo final, a página {t['alvo']} não está na memória.")
    print(f"Carregamentos (faltas): {q}")
    print(f"Estado final: {blocos}")
