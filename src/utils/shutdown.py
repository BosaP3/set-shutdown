import platform
import subprocess

#TODO: Refactor to validate shutdown command for other operating systems
def schedule_shutdown_in(seconds: int):
    system = platform.system()
    
    if seconds <= 0:
        raise ValueError("O tempo deve ser maior que zero.")

    try:
        if system == "Windows":
            subprocess.run(["shutdown", "/s", "/t", str(seconds)], check=True)
        elif system == "Linux" or system == "Darwin":  # macOS
            minutes = max(1, int(seconds / 60))
            subprocess.run(["shutdown", f"+{minutes}"], check=True)
        else:
            raise NotImplementedError(f"Sistema não suportado: {system}")
    except Exception as e:
        print(f"[ERROR] Falha ao agendar desligamento: {e}")
        raise

#TODO: Refactor to validate shutdown command for other operating systems
def abort_shutdown():
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.run(["shutdown", "/a"], check=True)
        elif system == "Linux" or system == "Darwin":
            subprocess.run(["shutdown", "-c"], check=True)
        else:
            raise NotImplementedError(f"Sistema não suportado: {system}")
    except Exception as e:
        print(f"[ERROR] Falha ao cancelar desligamento: {e}")
        raise
