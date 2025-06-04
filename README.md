# 🎥 YouTube Playlist Downloader

Um script Python simples e intuitivo para baixar playlists completas do YouTube com seleção de qualidade personalizada.

## ✨ Características

### 🔧 **Instalação Automática**
- Verifica automaticamente se o `yt-dlp` está instalado
- Instala as dependências necessárias automaticamente
- Sem configuração manual complexa

### 🎯 **Opções de Qualidade**
- **Melhor qualidade disponível** - Vídeo + áudio na máxima qualidade
- **Pior qualidade disponível** - Para economizar espaço
- **Melhor vídeo + áudio separados** - Máxima qualidade em arquivos separados
- **HD 720p** - Qualidade HD padrão
- **SD 480p** - Qualidade média
- **SD 360p** - Qualidade básica
- **Apenas áudio (melhor qualidade)** - Para criar biblioteca de música
- **Áudio em MP3** - Formato universal de áudio
- **Formato personalizado** - Defina seus próprios parâmetros

### 📁 **Organização Inteligente**
- Cria pastas de destino automaticamente
- Organiza arquivos por nome da playlist
- Nomes de arquivos limpos e padronizados
- Estrutura: `downloads/[Nome da Playlist]/[Nome do Vídeo].[extensão]`

### ⚡ **Recursos Extras**
- ✅ Validação de URLs do YouTube
- 🛡️ Tratamento robusto de erros
- ⚠️ Possibilidade de cancelar downloads (Ctrl+C)
- 🎨 Interface amigável com emojis e cores
- 📊 Progresso de download em tempo real

## 🚀 Instalação

### Pré-requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)

### Instalação Rápida

1. **Clone o repositório:**
```bash
git clone https://github.com/Neshzz/Dowload-videos-youtube.git
cd youtube-playlist-downloader
```

2. **O script instalará automaticamente as dependências, mas você pode instalar manualmente:**
```bash
pip install yt-dlp
```

## 📖 Como Usar

### Execução Básica
```bash
python dwl.py
```

### Passo a Passo
1. **Execute o script**
2. **Cole a URL da playlist** do YouTube
3. **Escolha a qualidade desejada** (1-9)
4. **Defina a pasta de destino** (opcional)
5. **Confirme o download**

### Exemplo de Uso
```
🎥 YouTube Playlist Downloader
========================================
📋 Digite a URL da playlist do YouTube: https://www.youtube.com/playlist?list=PLxxxxxx
🎯 Escolha uma opção (1-9): 1
📁 Pasta de destino (Enter para 'downloads'): minha_musica
✅ Confirma o download? (s/N): s
```

## 🔧 Configurações Avançadas

### Formatos Personalizados
Ao escolher a opção "9. Formato personalizado", você pode usar:
- `best[height<=720]` - Melhor qualidade até 720p
- `worst[ext=mp4]` - Pior qualidade em MP4
- `bestaudio[ext=m4a]` - Melhor áudio em M4A

### Estrutura de Pastas
```
downloads/
├── Nome da Playlist 1/
│   ├── Video 1.mp4
│   ├── Video 2.mp4
│   └── ...
└── Nome da Playlist 2/
    ├── Audio 1.mp3
    ├── Audio 2.mp3
    └── ...
```

## 🛡️ Tratamento de Erros

O script trata automaticamente:
- URLs inválidas ou não reconhecidas
- Vídeos privados ou removidos
- Problemas de conexão
- Interrupções do usuário
- Formatos não disponíveis

## ⚠️ Aviso Legal

Este script é apenas para uso pessoal e educacional. Respeite os direitos autorais e os termos de serviço do YouTube. O usuário é responsável pelo uso adequado desta ferramenta.

## 🐛 Reportar Problemas

Encontrou um bug? [Abra uma issue](https://github.com/Neshzz/Dowload-videos-youtube/issues) com:
- Descrição do problema
- Passos para reproduzir
- Mensagem de erro (se houver)
- Versão do Python e sistema operacional

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** ⭐
