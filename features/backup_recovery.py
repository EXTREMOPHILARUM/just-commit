import os
import shutil
import subprocess
import time

class BackupRecovery:
    def __init__(self, backup_dir='backups'):
        self.backup_dir = backup_dir
        self.ensure_backup_dir_exists()

    def ensure_backup_dir_exists(self):
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def backup_repository(self):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        backup_path = os.path.join(self.backup_dir, f"backup-{timestamp}")
        subprocess.run(['git', 'bundle', 'create', backup_path, '--all'], check=True)
        print(f"Repository backed up to {backup_path}")

    def recover_repository(self, backup_path):
        if os.path.exists(backup_path):
            recovery_path = 'recovery'
            if os.path.exists(recovery_path):
                shutil.rmtree(recovery_path)
            os.makedirs(recovery_path)
            subprocess.run(['git', 'clone', backup_path, recovery_path], check=True)
            print(f"Repository recovered from {backup_path} to {recovery_path}")
        else:
            print("Backup file does not exist.")

if __name__ == "__main__":
    backup_recovery = BackupRecovery()
    # Example usage
    backup_recovery.backup_repository()
    # To recover, specify the path to the backup file
    # backup_recovery.recover_repository('backups/backup-20210101-120000')
