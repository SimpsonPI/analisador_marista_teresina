# -*- coding: utf-8 -*-
"""
Checklist Bolsa de Estudo — Marista Champagnat Teresina
Versão com Abas, Checkboxes e Links Oficiais
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Checklist Bolsa Marista Teresina")

# DADOS DO EDITAL
DOCS_IDENTIFICACAO = [
    {"texto": "RG e CPF de TODOS os membros do grupo familiar", "link": ""},
    {"texto": "Certidão de Nascimento do aluno/candidato (OBRIGATÓRIA)", "link": ""},
    {"texto": "Certidão de Nascimento substitui RG para menores de 18 anos", "link": ""},
    {"texto": "Laudo/relatório de acompanhamento ATUALIZADO (se necessidades especiais)", "link": ""},
    {"texto": "Certidão de Casamento OU Declaração de União Estável (se for o caso)", "link": ""},
    {"texto": "Averbação de Divórcio OU Declaração de Separação Conjugal (se for o caso)", "link": ""},
    {"texto": "Certidão de Óbito (se pais/responsáveis falecidos)", "link": ""},
    {"texto": "Termo de Guarda ou Tutela / Decisão Judicial (guarda compartilhada)", "link": ""},
    {"texto": "CTPS Digital — impressa nos últimos 30 dias (≥18 anos; 14-17 se aprendiz)", "link": "https://servicos.mte.gov.br"},
    {"texto": "CTPS deve conter os 3 últimos contratos de trabalho", "link": "https://servicos.mte.gov.br"},
    {"texto": "Páginas da CTPS: série/foto, qualificação civil, contratos (penúltima, última e subsequente em branco)", "link": ""},
    {"texto": "Páginas de alteração de salário (se registro vigente assinado)", "link": ""},
    {"texto": "2 primeiras páginas do contrato em branco (se CTPS nunca assinada)", "link": ""},
    {"texto": "Carteira de Trabalho física (se não tiver CTPS Digital)", "link": ""},
    {"texto": "Declaração de Ausência de CTPS — RETIRAR NA SECRETARIA DA ESCOLA", "link": "#escola"}
]

DOCS_RESIDENCIA = [
    {"texto": "Comprovante de residência: água, energia ou telefone em nome dos responsáveis (ÚLTIMO MÊS)", "link": ""},
    {"texto": "❌ NÃO ACEITAMOS carnês ou faturas de cartão", "link": ""},
    {"texto": "Documento do imóvel: escritura / termo de posse / cessão de direitos / IPTU", "link": ""},
    {"texto": "Se ALUGADO: contrato de aluguel + recibo", "link": ""},
    {"texto": "Se FINANCIADO: contrato de financiamento", "link": ""},
    {"texto": "Se CEDIDO: declaração do proprietário", "link": ""},
    {"texto": "Sem documento: Declaração na Associação de Moradores do bairro", "link": ""},
    {"texto": "Declaração de Situação de Moradia — RETIRAR NA SECRETARIA DA ESCOLA", "link": "#escola"}
]

RENDA = {
    "Assalariados (renda fixa)": [
        {"texto": "03 últimos contracheques", "link": ""},
        {"texto": "Extrato bancário conta salário — últimos 3 meses", "link": ""}
    ],
    "Assalariados (renda variável)": [
        {"texto": "06 últimos contracheques", "link": ""},
        {"texto": "Extrato bancário conta salário — últimos 6 meses", "link": ""}
    ],
    "Sem contracheques / recém-contratado": [
        {"texto": "Declaração da firma empregadora com valor bruto dos vencimentos", "link": ""}
    ],
    "Autônomos / Informais": [
        {"texto": "Declaração de Comprovação de Renda (3 últimos meses) — RETIRAR NA ESCOLA", "link": "#escola"}
    ],
    "Trabalhador Rural": [
        {"texto": "Declaração de Atividade Remunerada — RETIRAR NA ESCOLA", "link": "#escola"},
        {"texto": "Comprovante de contribuição mensal ao sindicato de trabalhadores rurais", "link": ""}
    ],
    "Aposentados / Pensionistas": [
        {"texto": "Último contracheque/extrato do benefício", "link": "https://meu.inss.gov.br"}
    ],
    "Sócios de Empresa": [
        {"texto": "03 últimos comprovantes de pró-labore", "link": ""},
        {"texto": "Contrato Social / Comprovação da empresa", "link": ""},
        {"texto": "Carnê do INSS com comprovante de pagamento do último mês", "link": "https://meu.inss.gov.br"},
        {"texto": "Declaração de Imposto de Renda — TODAS as páginas", "link": "https://www.receita.fazenda.gov.br"}
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

LINKS_UTEIS = [
    {"nome": "🔗 Emitir CTPS Digital", "url": "https://servicos.mte.gov.br"},
    {"nome": "🔗 Extrato INSS / Aposentadoria", "url": "https://meu.inss.gov.br"},
    {"nome": "🔗 Declaração Imposto de Renda", "url": "https://www.receita.fazenda.gov.br"},
    {"nome": "📋 Modelos de Declarações (retirar na escola)", "url": "#escola"}
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
        *{{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',Arial,sans-serif;}}
        :root{{--primaria:#1e40af;--secundaria:#3b82f6;--destaque:#fef3c7;--alerta:#fef2f2;--sucesso:#f0fdf4;--borda:#e2e8f0;--texto:#1f2937;--texto-claro:#6b7280;}}
        body{{background:#f8fafc;padding:15px;max-width:900px;margin:0 auto;color:var(--texto);}}
        h1{{text-align:center;color:var(--primaria);margin-bottom:5px;font-size:1.5rem;}}
        .sub{{text-align:center;color:var(--texto-claro);margin-bottom:20px;font-size:.9rem;}}
        .aviso{{background:var(--destaque);border-left:4px solid #f59e0b;padding:12px;margin-bottom:20px;border-radius:6px;}}
        .abas{{display:flex;flex-wrap:wrap;border-bottom:2px solid var(--borda);margin-bottom:20px;}}
        .aba{{padding:10px 16px;cursor:pointer;border-top-left-radius:8px;border-top-right-radius:8px;border:1px solid transparent;margin-bottom:-1px;transition:all .2s;font-weight:500;font-size:.9rem;}}
        .aba.ativa{{border:1px solid var(--borda);border-bottom:2px solid white;background:white;color:var(--primaria);font-weight:bold;}}
        .aba:hover{{background:#eff6ff;}}
        .conteudo-aba{{display:none;animation:aparece .3s ease;}}
        .conteudo-aba.ativa{{display:block;}}
        @keyframes aparece{{from{{opacity:0;}}to{{opacity:1;}}}}
        .item{{display:flex;align-items:flex-start;gap:10px;padding:10px 12px;border-bottom:1px solid #f1f5f9;transition:background .2s;}}
        .item:hover{{background:#f8fafc;}}
        .item.feito{{background:var(--sucesso);}}
        .check{{width:20px;height:20px;margin-top:2px;cursor:pointer;accent-color:var(--primaria);}}
        .txt{{flex:1;line-height:1.5;font-size:.93rem;}}
        .link{{color:var(--secundaria);text-decoration:none;font-size:.85rem;white-space:nowrap;margin-left:8px;}}
        .link:hover{{text-decoration:underline;}}
        .categoria{{font-weight:bold;color:#7c3aed;margin:18px 0 8px;padding-bottom:4px;border-bottom:1px dashed #ddd;}}
        .linha{{padding:8px 0;border-bottom:1px solid #eee;display:flex;justify-content:space-between;}}
        .etapa{{font-weight:500;}}
        .prazo{{font-weight:bold;color:#d97706;}}
        .obs{{background:white;padding:15px;border-radius:8px;margin-top:20px;box-shadow:0 1px 3px rgba(0,0,0,.05);font-size:.85rem;line-height:1.7;color:var(--texto-claro);}}
        .obs h3{{font-size:.95rem;margin-bottom:8px;color:var(--texto);}}
        .resumo{{display:flex;gap:15px;margin-top:10px;flex-wrap:wrap;}}
        .resumo span{{padding:4px 10px;border-radius:20px;font-size:.85rem;font-weight:500;}}
        .sim{{background:#dcfce7;color:#166534;}}
        .nao{{background:#f1f5f9;color:#64748b;}}
        .card-links{{background:#eff6ff;padding:12px;border-radius:8px;margin-bottom:15px;}}
        .card-links a{{display:block;padding:6px 0;color:var(--primaria);text-decoration:none;}}
        .card-links a:hover{{text-decoration:underline;}}
    </style>
</head>
<body>

    <h1>📋 CHECKLIST — BOLSA DE ESTUDO</h1>
    <p class="sub">Marista Champagnat Teresina • Renovação 2026/2027</p>

    <div class="aviso">
        ⚠️ <strong>URGENTE:</strong> Entrevista da 2ª Série já está em andamento! Confira prazos na aba Cronograma.
    </div>

    <div class="abas">
        <div class="aba ativa" onclick="abrirAba(0)">🪪 Identificação</div>
        <div class="aba" onclick="abrirAba(1)">🏠 Residência</div>
        <div class="aba" onclick="abrirAba(2)">💰 Renda</div>
        <div class="aba" onclick="abrirAba(3)">📅 Cronograma</div>
        <div class="aba" onclick="abrirAba(4)">🔗 Links Úteis</div>
    </div>

    <!-- ABA 0: IDENTIFICAÇÃO -->
    <div class="conteudo-aba ativa" id="aba0">
        {"".join([f'''<div class="item" id="item0-{i}">
            <input type="checkbox" class="check" onchange="marcar(this,'item0-{i}')">
            <div class="txt">{doc['texto']}{f'<a href="{doc["link"]}" target="_blank" class="link">→ Abrir</a>' if doc['link'] else ''}</div>
        </div>''' for i,doc in enumerate(DOCS_IDENTIFICACAO)])}
    </div>

    <!-- ABA 1: RESIDÊNCIA -->
    <div class="conteudo-aba" id="aba1">
        {"".join([f'''<div class="item" id="item1-{i}">
            <input type="checkbox" class="check" onchange="marcar(this,'item1-{i}')">
            <div class="txt">{doc['texto']}{f'<a href="{doc["link"]}" target="_blank" class="link">→ Abrir</a>' if doc['link'] else ''}</div>
        </div>''' for i,doc in enumerate(DOCS_RESIDENCIA)])}
    </div>

    <!-- ABA 2: RENDA -->
    <div class="conteudo-aba" id="aba2">
        {"".join([f'<div class="categoria">{titulo}</div>' + "".join([f'''<div class="item" id="item2-{titulo[:6]}-{j}">
            <input type="checkbox" class="check" onchange="marcar(this,'item2-{titulo[:6]}-{j}')">
            <div class="txt">{doc['texto']}{f'<a href="{doc["link"]}" target="_blank" class="link">→ Abrir</a>' if doc['link'] else ''}</div>
        </div>''' for j,doc in enumerate(lista)]) for titulo,lista in RENDA.items()])}
    </div>

    <!-- ABA 3: CRONOGRAMA -->
    <div class="conteudo-aba" id="aba3">
        {"".join([f'<div class="linha"><span class="etapa">{etapa}</span><span class="prazo">{prazo}</span></div>' for etapa,prazo in CRONOGRAMA])}
    </div>

    <!-- ABA 4: LINKS ÚTEIS -->
    <div class="conteudo-aba" id="aba4">
        <div class="card-links">
            {"".join([f'<a href="{link["url"]}" target="_blank">{link["nome"]}</a>' for link in LINKS_UTEIS])}
        </div>
        <div class="obs">
            <h3>📌 Onde retirar declarações na escola:</h3>
            <p>Declarações de: Ausência de CTPS, Comprovação de Renda, Atividade Remunerada, Situação de Moradia, União Estável e Separação Conjugal → <strong>Retirar na Secretaria da Escola Marista Champagnat Teresina</strong>.</p>
            <br>
            <h3>⚠️ Regras importantes:</h3>
            <ul style="margin-left:15px;line-height:1.6;">
                <li>CTPS Digital impressa nos últimos <strong>30 dias</strong></li>
                <li>Comprovante de residência: referente ao <strong>último mês</strong></li>
                <li>Declaração de IR: entregar <strong>TODAS as páginas</strong></li>
            </ul>
        </div>
    </div>

    <div class="obs">
        <h3>✅ Progresso</h3>
        <div class="resumo">
            <span class="sim" id="contagem-feitos">0 feitos</span>
            <span class="nao" id="contagem-total">de 0 itens</span>
        </div>
    </div>

<script>
const totalItens = document.querySelectorAll('.item').length;
document.getElementById('contagem-total').textContent = `de ${totalItens} itens`;

function abrirAba(n) {{
    document.querySelectorAll('.aba').forEach((el,i)=>el.classList.toggle('ativa',i===n));
    document.querySelectorAll('.conteudo-aba').forEach((el,i)=>el.classList.toggle('ativa',i===n));
}}

function marcar(checkbox, id) {{
    const item = document.getElementById(id);
    if (checkbox.checked) {{
        item.classList.add('feito');
    }} else {{
        item.classList.remove('feito');
    }}
    salvarProgresso();
    atualizarContagem();
}}

function atualizarContagem() {{
    const feitos = document.querySelectorAll('.item input:checked').length;
    document.getElementById('contagem-feitos').textContent = `${feitos} feito(s)`;
}}

function salvarProgresso() {{
    const estado = [];
    document.querySelectorAll('.item input[type=checkbox]').forEach((cb,i)=>{{
        estado.push({{id:i, checked:cb.checked}});
    }});
    localStorage.setItem('checklist-bolsa-marista', JSON.stringify(estado));
}}

function carregarProgresso() {{
    const salvo = localStorage.getItem('checklist-bolsa-marista');
    if (!salvo) return;
    const estado = JSON.parse(salvo);
    document.querySelectorAll('.item input[type=checkbox]').forEach((cb,i)=>{{
        if (estado[i] && estado[i].checked) {{
            cb.checked = true;
            cb.closest('.item').classList.add('feito');
        }}
    }});
    atualizarContagem();
}}
carregarProgresso();
</script>
</body>
</html>"""
    return HTMLResponse(html)

handler = app