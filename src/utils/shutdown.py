import platform
import subprocess
import threading
from typing import Optional

def _run_shutdown_command(command: list[str], check: bool = True) -> None:

    system = platform.system()
    
    if system == "Windows":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.run(
            command,
            check=check,
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    else:
        raise NotImplementedError(f"Sistema não suportado: {system}")

def schedule_shutdown_in(seconds: int, background: bool = True) -> Optional[threading.Thread]:

    if seconds <= 0:
        raise ValueError("O tempo deve ser maior que zero.")

    system = platform.system()
    command = []
    
    try:
        if system == "Windows":
            command = ["shutdown", "/s", "/t", str(seconds)]
        else:
            raise NotImplementedError(f"Sistema não suportado: {system}")

        if background:
            thread = threading.Thread(
                target=_run_shutdown_command,
                args=(command,),
                daemon=True
            )
            thread.start()
            return thread
        else:
            _run_shutdown_command(command)
            return None

    except Exception as e:
        print(f"[ERROR] Falha ao agendar desligamento: {e}")
        raise

def abort_shutdown(background: bool = True) -> Optional[threading.Thread]:

    system = platform.system()
    command = []
    
    try:
        if system == "Windows":
            command = ["shutdown", "/a"]
        else:
            raise NotImplementedError(f"Sistema não suportado: {system}")

        if background:
            thread = threading.Thread(
                target=_run_shutdown_command,
                args=(command,),
                daemon=True
            )
            thread.start()
            return thread
        else:
            _run_shutdown_command(command)
            return None

    except Exception as e:
        print(f"[ERROR] Falha ao cancelar desligamento: {e}")
        raise
