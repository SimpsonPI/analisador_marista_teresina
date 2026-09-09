# -*- coding: utf-8 -*-
"""
Checklist Bolsa de Estudo — Marista Champagnat Teresina
Processo Seletivo Renovação 2026 / Cronograma 2027
Versão otimizada para Vercel
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Checklist Bolsa Marista Teresina")

# DADOS DO EDITAL
DOCS_IDENTIFICACAO = [
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

DOCS_RESIDENCIA = [
    "Comprovante de residência: água, energia ou telefone em nome dos pais/responsáveis (ÚLTIMO MÊS)",
    "❌ NÃO ACEITAMOS carnês ou faturas de cartão",
    "Documento do imóvel: escritura / termo de posse / cessão de direitos / IPTU",
    "Se ALUGADO: contrato de aluguel + recibo",
    "Se FINANCIADO: contrato de financiamento",
    "Se CEDIDO: declaração do proprietário",
    "Sem documento do imóvel: Declaração na Associação de Moradores do bairro",
    "Declaração de Situação de Moradia (disponível na escola)"
]

RENDA = {
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
        "Último contracheque ou extrato do INSS → meu.inss.gov.br"
    ],
    "Sócios de Empresa": [
        "03 últimos comprovantes de pró-labore",
        "Contrato Social / Comprovação da empresa",
        "Carnê do INSS com comprovante de pagamento do último mês",
        "Declaração de Imposto de Renda — TODAS as páginas"
    ]
}

CRONOGRAMA = [
    ("Publicação do Edital", "08/09/2026"),
    ("Entrevista social — 2ª Série", "14 a 25/09/2026 ⚠️ EM ANDAMENTO"),
    ("Entrevista social — 12ª Série", "25/09 a 08/10/2026"),
    ("Entrevista social — 9º Ano", "08 a 23/10/2026"),
    ("Divulgação do Resultado", "30/10/2026"),
    ("Rematrícula", "10 a 12/11/2026"),
    ("Encerramento", "30/10/2026")
]


@app.get("/", response_class=HTMLResponse)
async def pagina_principal():
    html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checklist — Bolsa Marista Champagnat Teresina</title>
    <style>
        *{{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif;}}
        body{{background:#f0f4f8;padding:15px;max-width:850px;margin:0 auto;}}
        h1{{color:#1a365d;text-align:center;margin-bottom:5px;font-size:1.5rem;}}
        h2{{color:#2c5282;margin:25px 0 10px;border-bottom:2px solid #3182ce;padding-bottom:5px;font-size:1.1rem;}}
        .card{{background:#fff;border-radius:8px;padding:15px;margin-bottom:15px;box-shadow:0 2px 8px rgba(0,0,0,.08);}}
        .item{{padding:8px 6px;border-bottom:1px solid #edf2f7;display:flex;gap:8px;}}
        .item:last-child{{border:none;}}
        .n{{color:#718096;font-weight:bold;min-width:26px;}}
        .t{{flex:1;color:#2d3748;font-size:.92rem;line-height:1.4;}}
        .cat{{font-weight:bold;color:#805ad5;margin:10px 0 5px;}}
        .linha{{padding:6px 0;border-bottom:1px solid #edf2f7;}}
        .etapa{{font-weight:500;}}
        .prazo{{color:#2b6cb0;font-weight:bold;float:right;}}
        .aviso{{background:#fffaf0;border-left:4px solid #ed8936;padding:10px;margin-bottom:15px;border-radius:4px;}}
        .obs{{background:#f7fafc;padding:12px;border-radius:6px;margin-top:15px;font-size:.85rem;line-height:1.6;color:#4a5568;}}
        a{{color:#3182ce;text-decoration:none;}}
    </style>
</head>
<body>
    <h1>📋 CHECKLIST — BOLSA DE ESTUDO</h1>
    <p style="text-align:center;color:#718096;margin-bottom:15px;">Marista Champagnat Teresina • Renovação 2026/2027</p>

    <div class="aviso">
        ⚠️ <strong>URGENTE:</strong> Entrevista da 2ª Série já está em andamento! Confira prazos abaixo.
    </div>

    <div class="card">
        <h2>🪪 1. DOCUMENTOS DE IDENTIFICAÇÃO</h2>
        {"".join([f'<div class="item"><span class="n">{i+1}.</span><span class="t">{doc}</span></div>' for i,doc in enumerate(DOCS_IDENTIFICACAO)])}
    </div>

    <div class="card">
        <h2>🏠 2. COMPROVANTE DE RESIDÊNCIA</h2>
        {"".join([f'<div class="item"><span class="n">{i+1}.</span><span class="t">{doc}</span></div>' for i,doc in enumerate(DOCS_RESIDENCIA)])}
    </div>

    <div class="card">
        <h2>💰 3. COMPROVAÇÃO DE RENDA</h2>
        {"".join([f'<div class="cat">{titulo}</div>' + "".join([f'<div class="item"><span class="n">{j+1}.</span><span class="t">{txt}</span></div>' for j,txt in enumerate(lista)]) for titulo,lista in RENDA.items()])}
    </div>

    <div class="card">
        <h2>📅 4. CRONOGRAMA E PRAZOS</h2>
        {"".join([f'<div class="linha"><span class="etapa">{etapa}</span><span class="prazo">{prazo}</span></div>' for etapa,prazo in CRONOGRAMA])}
    </div>

    <div class="obs">
        <strong>📌 OBSERVAÇÕES IMPORTANTES:</strong><br>
        • CTPS Digital: impressa nos últimos <strong>30 dias</strong> → <a href="https://servicos.mte.gov.br" target="_blank">servicos.mte.gov.br</a><br>
        • Comprovante de residência: referente ao <strong>último mês</strong><br>
        • Declarações (Ausência de CTPS, Renda, Atividade Remunerada, Moradia) → <strong>RETIRAR NA SECRETARIA DA ESCOLA</strong><br>
        • Extrato INSS → <a href="https://meu.inss.gov.br" target="_blank">meu.inss.gov.br</a>
    </div>
</body>
</html>"""
    return HTMLResponse(html)
handler = app