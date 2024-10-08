class SessionStats:
    def __init__(self):
        self.total_commits = 0
        self.modified_files = set()

    def add_commit(self):
        self.total_commits += 1

    def add_modified_file(self, filename):
        self.modified_files.add(filename)

    def get_stats(self):
        return {
            'total_commits': self.total_commits,
            'total_modified_files': len(self.modified_files),
            'modified_files_list': list(self.modified_files)
        }

