# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checklist — Bolsa Marista Teresina</title>
    <style>
        *{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif;}
        body{background:#f8fafc;padding:20px;max-width:900px;margin:0 auto;}
        h1{text-align:center;color:#1e40af;margin-bottom:20px;}
        .aviso{background:#fef3c7;border-left:4px solid #f59e0b;padding:12px;margin-bottom:20px;border-radius:6px;}
        .abas{display:flex;flex-wrap:wrap;border-bottom:2px solid #e2e8f0;margin-bottom:20px;}
        .aba{padding:10px 16px;cursor:pointer;border-top-left-radius:8px;border-top-right-radius:8px;border:1px solid transparent;margin-bottom:-1px;}
        .aba.ativa{border:1px solid #e2e8f0;border-bottom:2px solid white;background:white;color:#1e40af;font-weight:bold;}
        .aba:hover{background:#eff6ff;}
        .conteudo{display:none;}
        .conteudo.ativa{display:block;}
        .item{display:flex;align-items:flex-start;gap:10px;padding:10px;border-bottom:1px solid #f1f5f9;}
        .item.feito{background:#f0fdf4;}
        input{margin-top:3px;}
        .link{color:#3b82f6;text-decoration:none;margin-left:10px;}
        .link:hover{text-decoration:underline;}
        .categoria{font-weight:bold;color:#7c3aed;margin:15px 0 5px;padding-bottom:3px;border-bottom:1px dashed #ddd;}
        .linha{padding:8px 0;border-bottom:1px solid #eee;display:flex;justify-content:space-between;}
        .prazo{font-weight:bold;color:#d97706;}
        .card-links{background:#eff6ff;padding:15px;border-radius:8px;margin:15px 0;}
        .card-links a{display:block;padding:5px 0;color:#1e40af;text-decoration:none;}
    </style>
</head>
<body>

    <h1>📋 CHECKLIST — BOLSA DE ESTUDO</h1>
    <p style="text-align:center;color:#6b7280;margin-bottom:15px;">Marista Champagnat Teresina • Renovação 2026/2027</p>

    <div class="aviso">
        ⚠️ <strong>URGENTE:</strong> Entrevista da 2ª Série já está em andamento! Confira prazos na aba Cronograma.
    </div>

    <div class="abas">
        <div class="aba ativa" onclick="abrir(0)">🪪 Identificação</div>
        <div class="aba" onclick="abrir(1)">🏠 Residência</div>
        <div class="aba" onclick="abrir(2)">💰 Renda</div>
        <div class="aba" onclick="abrir(3)">📅 Cronograma</div>
        <div class="aba" onclick="abrir(4)">🔗 Links Úteis</div>
    </div>

    <div class="conteudo ativa" id="c0">
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>RG e CPF de TODOS os membros do grupo familiar</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Certidão de Nascimento do aluno/candidato (OBRIGATÓRIA)</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Certidão de Nascimento substitui RG para menores de 18 anos</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Laudo/relatório de acompanhamento ATUALIZADO (se necessidades especiais)</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Certidão de Casamento OU Declaração de União Estável</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Averbação de Divórcio OU Declaração de Separação Conjugal</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Certidão de Óbito (se pais falecidos)</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Termo de Guarda ou Tutela / Decisão Judicial</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>CTPS Digital — impressa nos últimos 30 dias <a href="https://servicos.mte.gov.br" target="_blank" class="link">→ Emitir</a></span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>CTPS deve conter os 3 últimos contratos de trabalho</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Páginas da CTPS: série/foto, qualificação civil, contratos</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Páginas de alteração de salário (se registro assinado)</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>2 primeiras páginas do contrato em branco (se nunca assinada)</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Carteira de Trabalho física (se não tiver digital)</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Declaração de Ausência de CTPS — RETIRAR NA ESCOLA</span></div>
    </div>

    <div class="conteudo" id="c1">
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Comprovante de residência: água, energia ou telefone (ÚLTIMO MÊS)</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>❌ NÃO ACEITAMOS carnês ou faturas de cartão</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Documento do imóvel: escritura / posse / IPTU</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Se ALUGADO: contrato + recibo</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Se FINANCIADO: contrato de financiamento</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Se CEDIDO: declaração do proprietário</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Sem documento: Declaração na Associação de Moradores</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Declaração de Situação de Moradia — RETIRAR NA ESCOLA</span></div>
    </div>

    <div class="conteudo" id="c2">
        <div class="categoria">Assalariados (renda fixa)</div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>03 últimos contracheques</span></div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Extrato bancário — últimos 3 meses</span></div>
        
        <div class="categoria">Aposentados / Pensionistas</div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Último extrato do INSS <a href="https://meu.inss.gov.br" target="_blank" class="link">→ Baixar</a></span></div>
        
        <div class="categoria">Autônomos / Informais</div>
        <div class="item"><input type="checkbox" onclick="marcar(this)"><span>Declaração de Renda — RETIRAR NA ESCOLA</span></div>
    </div>

    <div class="conteudo" id="c3">
        <div class="linha"><span>Publicação do Edital</span><span class="prazo">08/09/2026</span></div>
        <div class="linha"><span>Entrevista — 2ª Série</span><span class="prazo">14 a 25/09/2026 ⚠️ EM ANDAMENTO</span></div>
        <div class="linha"><span>Entrevista — 12ª Série</span><span class="prazo">25/09 a 08/10/2026</span></div>
        <div class="linha"><span>Entrevista — 9º Ano</span><span class="prazo">08 a 23/10/2026</span></div>
        <div class="linha"><span>Divulgação do Resultado</span><span class="prazo">30/10/2026</span></div>
        <div class="linha"><span>Rematrícula</span><span class="prazo">10 a 12/11/2026</span></div>
    </div>

    <div class="conteudo" id="c4">
        <div class="card-links">
            <h3>🔗 Sites Oficiais</h3>
            <a href="https://servicos.mte.gov.br" target="_blank">Emitir CTPS Digital</a>
            <a href="https://meu.inss.gov.br" target="_blank">Extrato INSS / Aposentadoria</a>
            <a href="https://www.receita.fazenda.gov.br" target="_blank">Declaração Imposto de Renda</a>
        </div>
        <div style="background:#fff;padding:15px;border-radius:8px;margin-top:15px;line-height:1.6;">
            <h3>📋 Declarações da Escola</h3>
            <p>Todas as declarações padrão (Ausência de CTPS, Renda, Moradia, União Estável) devem ser <strong>retiradas na Secretaria da Escola Marista Champagnat Teresina</strong>.</p>
        </div>
    </div>

<script>
function abrir(n){
    document.querySelectorAll('.aba').forEach((el,i)=>el.classList.toggle('ativa',i===n));
    document.querySelectorAll('.conteudo').forEach((el,i)=>el.classList.toggle('ativa',i===n));
}
function marcar(cb){
    cb.closest('.item').classList.toggle('feito', cb.checked);
}
</script>
</body>
</html>"""

handler = app