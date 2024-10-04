import tkinter as tk
from tkinter import ttk, messagebox
from key_config_frame import KeyConfigFrame
from spells_tab import SpellsTab
from variables_tab import VariablesTab
from command_types import command_types
from config_manager_tab import ConfigManagerTab
import json

class RotationConfigGenerator:
    def __init__(self, master):
        """
        Initialize the RotationConfigGenerator class.

        Parameters
        ----------
        master : tkinter.Tk
            The parent window for this application.

        """
        self.master = master
        master.title("Enhanced Rotation Config Generator")
        master.geometry("1200x800")

        self.command_types = command_types

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.variables_tab = VariablesTab(self.notebook)
        self.spells_tab = SpellsTab(self.notebook)
        self.create_rotation_tab()
        self.config_manager_tab = ConfigManagerTab(self.notebook, self.handle_config_load)

        self.variables_tab.add_variable_change_callback(self.update_variable_lists)

        self.generate_button = ttk.Button(master, text="Generate Config", command=self.generate_config)
        self.generate_button.pack(pady=10)

        self.load_data()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def handle_config_load(self, data):
        """
        Handles loading of a configuration.

        If data is None, returns the current configuration data for saving.
        If data is not None, loads the provided data into the application.

        Parameters
        ----------
        data : dict or None
            If None, returns current data for saving.
            If not None, loads the provided data into the application.

        Returns
        -------
        dict or None
            If data is None, returns the current configuration data for saving.
            If data is not None, returns None.
        """
        if data is None:
            # Return current data for saving
            return self.get_rotation_data()
        else:
            # Load the provided data
            self.set_rotation_data(data)

    def save_data(self):
        """
        Saves the current configuration data to a file named config_data.json.

        This function is called when the application is closed.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        data = self.get_rotation_data()
        with open('config_data.json', 'w') as f:
            json.dump(data, f)

    def load_data(self):
        """
        Loads the current configuration data from a file named config_data.json.

        This function is called when the application is started.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        try:
            with open('config_data.json', 'r') as f:
                data = json.load(f)
            self.set_rotation_data(data)
        except FileNotFoundError:
            pass  # No data to load

    def on_closing(self):
        """
        Called when the application is being closed.

        Saves the current configuration data and then closes the application.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        self.save_data()
        self.master.destroy()

    def create_rotation_tab(self):
        """
        Creates the Rotation tab.

        This function creates the Rotation tab within the main notebook and adds a
        notebook to it to hold the makros. It also adds buttons to add and remove
        makros. The self.makro_frames list is initialized to store the makro frames.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        rotation_frame = ttk.Frame(self.notebook)
        self.notebook.add(rotation_frame, text="Rotation")

        # Create a notebook within rotation_frame to hold makros
        self.makro_notebook = ttk.Notebook(rotation_frame)
        self.makro_notebook.pack(expand=True, fill='both')

        # Add buttons to add and remove makros
        button_frame = ttk.Frame(rotation_frame)
        button_frame.pack(pady=5)

        add_makro_button = ttk.Button(button_frame, text="Add Makro", command=self.add_makro)
        add_makro_button.pack(side='left', padx=5)

        remove_makro_button = ttk.Button(button_frame, text="Remove Makro", command=self.remove_makro)
        remove_makro_button.pack(side='left', padx=5)

        self.makro_frames = []  # List to store makro frames

        # Add initial makro
        self.add_makro()

    def add_makro(self):
        """
        Adds a new makro to the rotation configuration.

        This function creates a new notebook page with a scrollable frame and a
        frame to hold buttons to add and remove keys. The new makro is added to
        the end of the self.makro_frames list.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        makro_frame = ttk.Frame(self.makro_notebook)
        makro_name = f"Makro {len(self.makro_frames) + 1}"

        # Store makro info
        makro_info = {
            'makro_frame': makro_frame,
            'key_frames': [],
            'makro_name': makro_name,
            'scrollable_frame': None  # Will set this after creating scrollable_frame
        }

        self.makro_notebook.add(makro_frame, text=makro_name)

        # Canvas and scrollbar for each makro frame
        canvas = tk.Canvas(makro_frame)
        scrollbar = ttk.Scrollbar(makro_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Set scrollable_frame in makro_info
        makro_info['scrollable_frame'] = scrollable_frame

        # Create a frame for buttons to add/remove keys
        key_button_frame = ttk.Frame(makro_frame)
        key_button_frame.pack(pady=5)

        add_key_button = ttk.Button(key_button_frame, text="Add Key", command=lambda mi=makro_info: self.add_key(mi))
        add_key_button.pack(side='left', padx=5)

        remove_key_button = ttk.Button(key_button_frame, text="Remove Key", command=lambda mi=makro_info: self.remove_key(mi))
        remove_key_button.pack(side='left', padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.makro_frames.append(makro_info)

    def add_key(self, makro_info):
        """
        Adds a new key to the makro configuration.

        This function creates a new KeyConfigFrame instance and adds it to the
        list of key frames for the makro. The new key is added to the end of the
        list of key frames.

        Parameters
        ----------
        makro_info : dict
            The dictionary containing the info for the makro to add the key to.

        Returns
        -------
        None
        """
        
        key_number = len(makro_info['key_frames']) + 1
        key_frame = KeyConfigFrame(
            makro_info['scrollable_frame'], key_number, self.command_types, self.spells_tab, self.variables_tab.get_variable_names()
        )
        key_frame.pack(fill='x', padx=5, pady=5)
        makro_info['key_frames'].append(key_frame)
        self.update_key_numbers(makro_info)

    def remove_key(self, makro_info):
        """
        Removes a key from the makro configuration.

        This function removes the last key from the list of key frames for the
        makro and updates the key numbers of the remaining keys.

        Parameters
        ----------
        makro_info : dict
            The dictionary containing the info for the makro to remove the key from.

        Returns
        -------
        None
        """
        if makro_info['key_frames']:
            key_frame = makro_info['key_frames'].pop()
            key_frame.destroy()
            self.update_key_numbers(makro_info)

    def update_key_numbers(self, makro_info):
        """
        Updates the key numbers of the key frames in the makro configuration.

        This function updates the key numbers of the key frames in the makro
        configuration by calling the update_key_number method of each key frame.

        Parameters
        ----------
        makro_info : dict
            The dictionary containing the info for the makro to update the key
            numbers in.

        Returns
        -------
        None
        """
        
        for idx, key_frame in enumerate(makro_info['key_frames'], start=1):
            key_frame.update_key_number(idx)

    def remove_makro(self):
        """
        Removes the currently selected makro from the rotation configuration.

        This function removes the currently selected makro from the rotation
        configuration by forgetting the notebook page and deleting the
        associated makro info from the list of makro frames.

        Parameters
        ----------
        None

        Returns
        -------
        None        
        """
        if self.makro_frames:
            current_tab = self.makro_notebook.index(self.makro_notebook.select())
            self.makro_notebook.forget(current_tab)
            del self.makro_frames[current_tab]

    def get_rotation_data(self):
        """
        Gets the rotation data from the rotation configuration.

        This function generates the rotation data by iterating over the makro
        frames and collecting the key configuration data from each key frame.
        The function then adds the variables and spells data from the
        variables and spells tabs to the rotation data.

        Returns
        -------
        dict
            The generated rotation data.
        """
        data = {
            'MAKRO': []
        }

        for makro_info in self.makro_frames:
            key_frames = makro_info['key_frames']
            makro_data = {
                'Keys': []
            }
            for key_frame in key_frames:
                key_data = key_frame.get_key_config_data()
                makro_data['Keys'].append(key_data)
            data['MAKRO'].append(makro_data)

        # Add variables and spells data
        data['variables'] = self.variables_tab.get_variables_data()
        data['spells'] = self.spells_tab.get_spells_data()

        return data

    def set_rotation_data(self, data):
        """
        Sets the rotation data from a given data dictionary.

        This function will set the rotation data by clearing all existing makros
        and then adding new makros from the given data. The data dictionary should
        have a key 'MAKRO' whose value is a list of makro data dictionaries. Each
        makro data dictionary should have a key 'Keys' whose value is a list of key
        configuration data dictionaries. The function will then add each key
        configuration to the corresponding makro.

        The function will also set the variables and spells data from the given
        data.

        Parameters
        ----------
        data : dict
            The data dictionary containing the rotation data to set.

        Returns
        -------
        None
        """
        print("Setting rotation data:", data)  # Debug print

        # Clear existing makros
        for makro_info in self.makro_frames[:]:
            index = self.makro_notebook.index(makro_info['makro_frame'])
            self.makro_notebook.forget(index)
            self.makro_frames.remove(makro_info)

        makro_list = data.get('MAKRO', [])
        print(f"Loading {len(makro_list)} makros")  # Debug print
        for makro_data in makro_list:
            self.add_makro()
            makro_info = self.makro_frames[-1]
            keys_list = makro_data.get('Keys', [])
            print(f"Loading {len(keys_list)} keys for makro")  # Debug print
            for key_data in keys_list:
                self.add_key(makro_info)
                key_frame = makro_info['key_frames'][-1]
                key_frame.set_key_config_data(key_data)
            self.update_key_numbers(makro_info)

        # Set variables
        self.variables_tab.set_variables_data(data.get('variables', {}))

        # Set spells
        spells_data = data.get('spells', [])
        print(f"Setting spells data: {spells_data}")  # Debug print
        if isinstance(spells_data, list) and len(spells_data) > 0 and isinstance(spells_data[0], dict):
            self.spells_tab.set_spells_data(spells_data)
        else:
            print("Invalid spells data structure")  # Debug print

        print("Finished setting rotation data")  # Debug print
        self.master.update()  # Force update of the main window

    def update_variable_lists(self, variable_names):
        """
        Updates the variable names for each key frame in the rotation configuration.

        This function takes a list of variable names and updates the variable names
        for each key frame in the rotation configuration.

        Parameters
        ----------
        variable_names : list
            The list of variable names to update the key frames with.

        Returns
        -------
        None
        """
        
        for makro_info in self.makro_frames:
            for key_frame in makro_info['key_frames']:
                key_frame.update_variable_names(variable_names)

    def generate_config(self):
        """
        Generates the configuration string for the rotation configuration.

        This function will generate a configuration string by concatenating the
        variables config, spells config, and key config for each makro. The
        generated configuration string will be written to a file named
        'rotation_config.txt' in the current directory.

        Returns
        -------
        None
        """
        config = "[variables]\n"
        config += self.variables_tab.get_variables_config()
        config += "\n"

        config += self.spells_tab.get_spell_config()

        # Iterate over makros
        for idx, makro_info in enumerate(self.makro_frames, start=1):
            config += f"\n[Makro {idx}]\n"
            key_frames = makro_info['key_frames']
            for key_frame in key_frames:
                key_config = key_frame.get_config()
                if key_config:
                    config += key_config + "\n"

        # Additional config settings if needed
        config += "repeat=1\n"
        config += "endkeys=dbg % stopped|store % releaseTimer,0|!eq % key,0|(VAR % key)u|store % key,0\n"

        with open("rotation_config.txt", "w") as f:
            f.write(config)

        messagebox.showinfo("Success", "Config file 'rotation_config.txt' has been generated.")