from llama_index.core.tools import FunctionTool
import os

note_file_path = os.path.join('data', 'notes.txt')

def save_note(new_note):
    if not os.path.exists(note_file_path):
        open(note_file_path, 'w')

    else:
        with open(note_file_path, 'a') as f:
            f.writelines([new_note + "\n"])
    return "note saved"

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user"
)
