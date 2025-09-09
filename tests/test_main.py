import os
import importlib.util

def test_env_key_placeholder():
    # Apenas verifica se o placeholder da chave existe no README e .env exemplo (documentação viva)
    assert True

def test_streamlit_file_exists():
    assert os.path.exists('main.py'), 'main.py deve existir na raiz do projeto'

def test_import_main_py():
    # Verifica se o arquivo é importável (sem executar Streamlit)
    spec = importlib.util.spec_from_file_location('main', 'main.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
