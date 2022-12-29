class Environment:

    def __init__(self):
        self.performed_stages = []

    def update_env_stage(self, stage):
        self.performed_stages.append(stage)

    def clear(self):
        self.performed_stages.clear()

    def __str__(self):
        NEW_LINE = '\n'
        return f"IN STR: {NEW_LINE.join(self.performed_stages)}"
