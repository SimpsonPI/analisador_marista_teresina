# -*- coding: utf-8 -*-
"""
Checklist Bolsa de Estudo — Marista Champagnat Teresina
Processo Seletivo Renovação 2026 / Cronograma 2027
Deploy no Vercel — FastAPI
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI(title="Checklist Bolsa Marista Teresina")

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

analisador = AnalisadorEditalMarista()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checklist — Bolsa Marista Champagnat Teresina</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }}
        body {{ background: #f5f7fa; padding: 20px; max-width: 900px; margin: 0 auto; }}
        h1 {{ color: #2c3e50; text-align: center; margin-bottom: 5px; font-size: 1.6rem; }}
        h2 {{ color: #34495e; margin: 25px 0 10px 0; font-size: 1.2rem; border-bottom: 2px solid #3498db; padding-bottom: 5px; }}
        .card {{ background: white; border-radius: 8px; padding: 15px; margin-bottom: 15px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }}
        .item {{ padding: 8px 10px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; }}
        .item:last-child {{ border-bottom: none; }}
        .item-num {{ color: #7f8c8d; font-weight: bold; min-width: 28px; }}
        .item-text {{ flex: 1; color: #2d3436; font-size: 0.92rem; line-height: 1.4; }}
        .status {{ font-weight: bold; white-space: nowrap; font-size: 0.85rem; }}
        .sim {{ color: #27ae60; }}
        .nao {{ color: #e74c3c; }}
        .aviso {{ color: #f39c12; }}
        .cronograma-item {{ padding: 6px 0; border-bottom: 1px solid #eee; }}
        .etapa {{ font-weight: 500; }}
        .periodo {{ color: #2980b9; font-weight: bold; float: right; }}
        .legenda {{ background: #ecf0f1; padding: 10px; border-radius: 6px; margin-top: 20px; font-size: 0.85rem; line-height: 1.6; }}
        .categoria {{ font-weight: bold; color: #8e44ad; margin: 10px 0 5px 0; }}
        .urgente {{ background: #fff3cd; border-left: 4px solid #ffc107; padding: 10px; margin-bottom: 15px; border-radius: 4px; }}
    </style>
</head>
<body>
    <h1>📋 CHECKLIST — BOLSA DE ESTUDO</h1>
    <p style="text-align:center; color:#7f8c8d; margin-bottom:20px;">Marista Champagnat Teresina • Processo Seletivo Renovação 2026/2027</p>

    <div class="urgente">
        ⚠️ <strong>ATENÇÃO:</strong> Entrevista social da 2ª Série já está em andamento! Confira prazos abaixo.
    </div>

    <div class="card">
        <h2>🪪 1. DOCUMENTOS DE IDENTIFICAÇÃO</h2>
        {"".join([f'<div class="item"><span class="item-num">{i+1}.</span><span class="item-text">{doc}</span><span class="status aviso">ⓘ Conferir</span></div>' for i, doc in enumerate(analisador.documentos_identificacao)])}
    </div>

    <div class="card">
        <h2>🏠 2. COMPROVANTE DE RESIDÊNCIA</h2>
        {"".join([f'<div class="item"><span class="item-num">{i+1}.</span><span class="item-text">{doc}</span><span class="status aviso">ⓘ Conferir</span></div>' for i, doc in enumerate(analisador.comprovante_residencia)])}
    </div>

    <div class="card">
        <h2>💰 3. COMPROVAÇÃO DE RENDA</h2>
        {"".join([f'<div class="categoria">{cat}</div>' + "".join([f'<div class="item"><span class="item-num">{j+1}.</span><span class="item-text">{doc}</span><span class="status aviso">ⓘ Conferir</span></div>' for j, doc in enumerate(docs)]) for cat, docs in analisador.comprovacao_renda.items()])}
    </div>

    <div class="card">
        <h2>📅 4. CRONOGRAMA E PRAZOS</h2>
        {"".join([f'<div class="cronograma-item"><span class="etapa">{etapa}</span><span class="periodo">{periodo}</span></div>' for etapa, periodo in analisador.cronograma])}
    </div>

    <div class="legenda">
        <strong>💡 LEGENDA:</strong> ✅ Pronto | ⚠️ Providenciar | ❌ Não se aplica<br>
        <strong>📌 Observações importantes:</strong><br>
        • CTPS Digital impressa há NO MÁXIMO 30 dias<br>
        • Comprovante de residência: ÚLTIMO MÊS<br>
        • Declarações de Ausência de CTPS, Renda, Atividade Remunerada e Situação de Moradia → RETIRAR NA SECRETARIA DA ESCOLA<br>
        • Link para emitir CTPS Digital: <a href="https://servicos.mte.gov.br" target="_blank">servicos.mte.gov.br</a><br>
        • Extrato INSS: <a href="https://meu.inss.gov.br" target="_blank">meu.inss.gov.br</a>
    </div>
</body>
</html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)