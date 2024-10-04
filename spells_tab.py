import tkinter as tk
from tkinter import ttk
import json
from PIL import Image, ImageTk

class SpellsTab:
    def __init__(self, notebook):
        self.spells_frame = ttk.Frame(notebook)
        notebook.add(self.spells_frame, text="Spells")

        self.load_spell_data()
        self.spell_entries = []
        self.selected_spells = []  # New list to keep track of selected spells

        self.create_ui()

    def create_ui(self):
        # Add headers
        """
        Creates the UI for the Spells tab.

        This function creates a series of frames and widgets to allow the user to select spells for each key.
        The frames are arranged in a vertical stack, with each frame containing a label with the spell number,
        an entry widget for the key ID, a combobox for selecting the spell, and a label to display the icon.
        The combobox is bound to the ComboboxSelected event, which updates the icon label when a new spell is selected.
        """
        header_frame = ttk.Frame(self.spells_frame)
        header_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(header_frame, text="Spell #", width=8).pack(side='left', padx=(0, 2))
        ttk.Label(header_frame, text="Key ID", width=7).pack(side='left', padx=(0, 2))
        ttk.Label(header_frame, text="Spell ID", width=22).pack(side='left', padx=(0, 2))
        ttk.Label(header_frame, text="Spell Name", width=32).pack(side='left', padx=(0, 2))
        ttk.Label(header_frame, text="Icon", width=6).pack(side='left')

        for i in range(1, 11):
            frame = ttk.Frame(self.spells_frame)
            frame.pack(fill='x', padx=5, pady=2)
            
            ttk.Label(frame, text=f"Spell {i}:", width=8).pack(side='left')
            spell_entry = ttk.Entry(frame, width=7)
            spell_entry.pack(side='left', padx=(0, 2))
            spell_entry.insert(0, str(48 + i))
            
            spell_id_entry = ttk.Entry(frame, width=22)
            spell_id_entry.pack(side='left', padx=(0, 2))
            spell_id_entry.insert(0, f"spellId{i}")
            
            spell_var = tk.StringVar()
            spell_dropdown = ttk.Combobox(frame, textvariable=spell_var, values=self.spell_options, width=30)
            spell_dropdown.pack(side='left', padx=(0, 2))
            spell_dropdown.bind('<<ComboboxSelected>>', lambda event, i=i: self.update_spell_icon(event, i))
            
            icon_label = ttk.Label(frame, width=4)
            icon_label.pack(side='left')
            
            self.spell_entries.append((spell_entry, spell_id_entry, spell_var, icon_label, spell_dropdown))

    def get_spell_config(self):
        """
        Returns a string containing the current spell configuration.

        This function iterates over the list of spell entries, and for each entry, it
        constructs a string in the format "spell<i>=<key_id>\nslot<i>spell=chid<i>,(VAR % <spell_id>)\n"
        where <i> is the 1-based index of the spell entry, <key_id> is the value of the key ID
        entry, and <spell_id> is the value of the spell ID entry.

        The resulting strings are concatenated together to form the final string, which is
        returned by the function.
        """
        config = ""
        for i, (spell_entry, spell_id_entry, spell_var, _, _) in enumerate(self.spell_entries, 1):
            config += f"spell{i}={spell_entry.get()}\n"
            config += f"slot{i}spell=chid{i},(VAR % {spell_id_entry.get()})\n"
        return config
          
    def load_spell_data(self):
        """
        Loads the spell data from the image_data.json file and extracts the spell options from it.

        The image_data.json file is expected to contain a list of dictionaries, where each dictionary contains a 'title' key with the name of the spell, and a 'saved_location' key with the path to the image file.

        The function reads the file, loads the data as a list of dictionaries, and extracts the spell options as a list of strings, which is stored in the 'spell_options' attribute of the SpellsTab instance.
        """
        with open('images/image_data.json', 'r') as f:
            self.spell_data = json.load(f)
        self.spell_options = [spell['title'] for spell in self.spell_data]

    def update_spell_icon(self, event, spell_index):
        """
        Updates the spell icon for a given spell index.

        This function is called whenever the selected spell changes for a given spell index.

        It gets the selected spell name from the spell_var StringVar, and looks up the matching
        spell info in the spell_data list. If a match is found, it attempts to load the image
        from the saved location and display it in the icon_label. If the image cannot be loaded,
        it prints an error message and clears the icon_label.

        The function also updates the selected_spells list with tuples of (name, id) for all
        selected spells.
        """
        spell_entry, spell_id_entry, spell_var, icon_label, _ = self.spell_entries[spell_index - 1]
        selected_spell = spell_var.get()
        spell_info = next((spell for spell in self.spell_data if spell['title'] == selected_spell), None)
        if spell_info:
            image_path = spell_info['saved_location']
            try:
                image = Image.open(image_path)
                image = image.resize((32, 32), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                icon_label.config(image=photo)
                icon_label.image = photo
                
                # Update selected_spells list with tuples of (name, id)
                self.selected_spells = [(f"{i+1}: {spell_var.get()}", spell_id_entry.get()) 
                                        for i, (_, spell_id_entry, spell_var, _, _) in enumerate(self.spell_entries) 
                                        if spell_var.get()]
            except Exception as e:
                print(f"Error loading image: {e}")
        else:
            icon_label.config(image='')

    def get_selected_spells(self):
        """
        Returns a list of tuples containing the name and id of all selected spells.
        
        Each tuple in the list is of the form (name, id), where name is the name of the
        selected spell and id is the id of the selected spell.
        
        The list is empty if no spells are selected.
        """

        return self.selected_spells

    def get_spells_data(self):
        """
        Returns a list of dictionaries containing the data for all selected spells.

        Each dictionary contains the key, id, and name of a selected spell.
        """

        spells_data = []
        for spell_entry, spell_id_entry, spell_var, _, _ in self.spell_entries:
            spells_data.append({
                'spell_entry': spell_entry.get(),
                'spell_id_entry': spell_id_entry.get(),
                'spell_var': spell_var.get(),
            })
        return spells_data

    def set_spells_data(self, data):
        """
        Sets the data for all selected spells from a list of dictionaries.

        Each dictionary contains the key, id, and name of a selected spell.

        The function iterates over the list of dictionaries and sets the text of the
        corresponding spell entries, spell ID entries, and spell dropdowns to the
        values in the dictionary. If a dictionary key is not present in the data, the
        corresponding entry is left unchanged.

        The function also updates the spell icons by calling update_spell_icon for
        each spell entry.

        The function prints debug messages to the console to indicate the values of
        the spell entries, spell ID entries, and spell dropdowns after setting the
        data.

        :param data: A list of dictionaries containing the key, id, and name of all
            selected spells.
        :type data: list[dict[str, str]]
        """
        print("Setting spells data:", data)  # Debug print
        print(f"Number of spell entries: {len(self.spell_entries)}")  # Debug print
        for i, spell_data in enumerate(data):
            print(f"Processing spell data {i}: {spell_data}")  # Debug print
            if i >= len(self.spell_entries):
                print(f"Warning: More spell data than entries. Skipping data for index {i}")
                break
            spell_entry, spell_id_entry, spell_var, icon_label, spell_dropdown = self.spell_entries[i]

            spell_entry.delete(0, tk.END)
            spell_entry.insert(0, spell_data.get('spell_entry', ''))
            print(f"Set spell entry {i} to: {spell_entry.get()}")  # Debug print

            spell_id_entry.delete(0, tk.END)
            spell_id_entry.insert(0, spell_data.get('spell_id_entry', ''))
            print(f"Set spell ID entry {i} to: {spell_id_entry.get()}")  # Debug print

            spell_var.set(spell_data.get('spell_var', ''))
            spell_dropdown.set(spell_data.get('spell_var', ''))  # Update the dropdown
            print(f"Set spell dropdown {i} to: {spell_dropdown.get()}")  # Debug print

            self.update_spell_icon(None, i+1)

        print("Finished setting spells data")  # Debug print
        self.spells_frame.update()  # Force update of the frame