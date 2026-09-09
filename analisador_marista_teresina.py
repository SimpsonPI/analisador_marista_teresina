# -*- coding: utf-8 -*-
"""
Analisador de Edital — Escola Marista Champagnat de Teresina
Processo Seletivo Renovação de Bolsa de Estudo — Documentação 2026 / Cronograma 2027
Baseado EXATAMENTE nos documentos fornecidos.
"""

class AnalisadorEditalMarista:
    def __init__(self):
        self.documentos_identificacao = [
            "RG e CPF de TODOS os membros do grupo familiar",
            "Certidão de Nascimento do aluno/candidato (OBRIGATÓRIA)",
            "Certidão de Nascimento para menores de 18 anos sem RG (substitui RG)",
            "Laudo/relatório de acompanhamento ATUALIZADO (se necessidades especiais)",
            "Certidão de Casamento OU Declaração de União Estável (se for o caso)",
            "Averbação de Divórcio OU Declaração de Separação Conjugal (se for o caso)",
            "Certidão de Óbito (se pais/responsáveis falecidos)",
            "Termo de Guarda ou Tutela / Decisão Judicial (guarda compartilhada)",
            "CTPS Digital — impressa nos últimos 30 dias (≥18 anos; 14-17 se aprendiz)",
            "CTPS deve conter os 3 últimos contratos de trabalho",
            "Páginas da CTPS: série/foto, qualificação civil, contratos (penúltima, última e subsequente em branco)",
            "Páginas de alteração de salário (se registro vigente assinado)",
            "2 primeiras páginas do contrato em branco (se CTPS nunca assinada)",
            "Carteira de Trabalho física (se não tiver CTPS Digital)",
            "Declaração de Ausência de CTPS — RETIRAR NA ESCOLA"
        ]

        self.comprovante_residencia = [
            "Comprovante de residência: água, energia ou telefone em nome dos pais/responsáveis (ÚLTIMO MÊS)",
            "❌ NÃO ACEITAMOS carnês ou faturas de cartão",
            "Documento do imóvel: escritura / termo de posse / cessão de direitos / IPTU",
            "Se ALUGADO: contrato de aluguel + recibo",
            "Se FINANCIADO: contrato de financiamento",
            "Se CEDIDO: declaração do proprietário",
            "Sem documento do imóvel: Declaração na Associação de Moradores do bairro",
            "Declaração de Situação de Moradia (disponível na escola)"
        ]

        self.comprovacao_renda = {
            "Assalariados (renda fixa)": [
                "03 últimos contracheques",
                "Extrato bancário conta salário — últimos 3 meses"
            ],
            "Assalariados (renda variável)": [
                "06 últimos contracheques",
                "Extrato bancário conta salário — últimos 6 meses"
            ],
            "Sem contracheques / recém-contratado": [
                "Declaração da firma empregadora com valor bruto dos vencimentos"
            ],
            "Autônomos / Informais": [
                "Declaração de Comprovação de Renda (3 últimos meses) — RETIRAR NA ESCOLA"
            ],
            "Trabalhador Rural": [
                "Declaração de Atividade Remunerada — RETIRAR NA ESCOLA",
                "Comprovante de contribuição mensal ao sindicato de trabalhadores rurais"
            ],
            "Aposentados / Pensionistas": [
                "Último contracheque ou extrato do INSS (meu.inss.gov.br)"
            ],
            "Sócios de Empresa": [
                "03 últimos comprovantes de pró-labore",
                "Contrato Social / Comprovação da empresa",
                "Carnê do INSS com comprovante de pagamento do último mês",
                "Declaração de Imposto de Renda — TODAS as páginas"
            ]
        }

        self.cronograma = [
            ("Publicação do Edital", "08/09/2026"),
            ("Entrevista social — 2ª Série", "14 a 25/09/2026"),
            ("Entrevista social — 12ª Série", "25/09 a 08/10/2026"),
            ("Entrevista social — 9º Ano", "08 a 23/10/2026"),
            ("Divulgação do Resultado", "30/10/2026"),
            ("Rematrícula", "10 a 12/11/2026"),
            ("Encerramento", "30/10/2026")
        ]

    def gerar_checklist(self, status_usuario=None):
        status_usuario = status_usuario or {}

        print("=" * 80)
        print("📋 CHECKLIST — BOLSA DE ESTUDO MARISTA CHAMPAGNAT TERESINA")
        print("📌 Processo Seletivo Renovação — Edital 2026 / Cronograma 2027")
        print("=" * 80)

        print("\n🪪 SEÇÃO 1 — DOCUMENTOS DE IDENTIFICAÇÃO")
        print("-" * 80)
        for idx, doc in enumerate(self.documentos_identificacao, 1):
            chave = f"ident_{idx}"
            status = status_usuario.get(chave, "❌ NÃO VERIFICADO")
            print(f"  {idx:2d}. {doc:<70} {status}")

        print("\n🏠 SEÇÃO 2 — COMPROVANTE DE RESIDÊNCIA")
        print("-" * 80)
        for idx, doc in enumerate(self.comprovante_residencia, 1):
            chave = f"resid_{idx}"
            status = status_usuario.get(chave, "❌ NÃO VERIFICADO")
            print(f"  {idx:2d}. {doc:<70} {status}")

        print("\n💰 SEÇÃO 3 — COMPROVAÇÃO DE RENDA")
        print("-" * 80)
        for categoria, docs in self.comprovacao_renda.items():
            print(f"\n  📂 {categoria}:")
            for idx, doc in enumerate(docs, 1):
                chave = f"renda_{categoria[:10]}_{idx}"
                status = status_usuario.get(chave, "❌ NÃO VERIFICADO")
                print(f"     {idx}. {doc:<66} {status}")

        print("\n📅 SEÇÃO 4 — CRONOGRAMA E PRAZOS")
        print("-" * 80)
        for etapa, periodo in self.cronograma:
            print(f"  • {etapa:<30} → {periodo}")

        print("\n" + "=" * 80)
        print("💡 LEGENDA: ✅ PRONTO  |  ⚠️ PROVIDENCIAR  |  ❌ AUSENTE/NÃO SE APLICA")
        print("📌 Itens 'RETIRAR NA ESCOLA' → solicitar à secretaria")
        print("📌 CTPS impressa: NO MÁXIMO 30 dias de emissão")
        print("📌 Comprovante de residência: ÚLTIMO MÊS")
        print("=" * 80)


if __name__ == "__main__":
    analisador = AnalisadorEditalMarista()

    meu_checklist = {
        "ident_1": "⚠️ PROVIDENCIAR",
        "ident_2": "✅ PRONTO",
        "ident_3": "✅ PRONTO",
        "ident_4": "❌ NÃO SE APLICA",
        "ident_5": "✅ PRONTO",
        "ident_6": "❌ NÃO SE APLICA",
        "ident_7": "❌ NÃO SE APLICA",
        "ident_8": "✅ PRONTO",
        "ident_9": "⚠️ VERIFICAR PÁGINAS",
        "ident_10": "⚠️ VERIFICAR",
        "ident_11": "✅ PRONTO",
        "ident_12": "❌ NÃO SE APLICA",
        "ident_13": "❌ NÃO SE APLICA",
        "ident_14": "❌ NÃO SE APLICA",
        "ident_15": "⚠️ RETIRAR NA ESCOLA",

        "resid_1": "✅ PRONTO",
        "resid_2": "✅ CUMPRIDO",
        "resid_3": "✅ PRONTO",
        "resid_4": "❌ NÃO SE APLICA",
        "resid_5": "❌ NÃO SE APLICA",
        "resid_6": "❌ NÃO SE APLICA",
        "resid_7": "❌ NÃO SE APLICA",
        "resid_8": "❌ NÃO SE APLICA",

        "renda_Assalari__1": "✅ PRONTO",
        "renda_Assalari__2": "✅ PRONTO",
    }

    analisador.gerar_checklist(meu_checklist)