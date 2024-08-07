from cx_Freeze import setup, Executable
import os

# Obtendo o caminho para o diretório onde o script está localizado
base_path = os.path.dirname(__file__)

# Adicionando a imagem à lista de arquivos de dados
build_exe_options = {
    'packages': [],  # Adicione pacotes adicionais se necessário
    'excludes': [],
    'include_files': [('eueela.jpg', base_path)],  # Adicione a imagem
}

setup(
    name="MeuExecutavel",
    version="0.1",
    description="Descrição do seu aplicativo",
    options={"build_exe": build_exe_options},
    executables=[Executable("MarioDaPenha.py", base="console")]  # Ou 'base="Win32GUI"' para uma GUI
)
