import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os

class ConfigManagerTab:
    def __init__(self, notebook, load_config_callback):
        """
        Initialize the ConfigManagerTab class.

        Parameters
        ----------
        notebook : ttk.Notebook
            The parent notebook.
        load_config_callback : function
            A callback function that takes a dictionary of config data as an argument.
        """
        
        self.config_frame = ttk.Frame(notebook)
        notebook.add(self.config_frame, text="Config Files")
        
        self.load_config_callback = load_config_callback
        self.config_files = []
        self.current_config = None
        
        self.create_widgets()
        self.load_config_list()

    def create_widgets(self):
        # Listbox for config files
        """
        Create the widgets for the ConfigManagerTab.

        This function creates the following widgets:

        - A Listbox widget to display the list of config files
        - Four buttons: New Config, Load Config, Save Current Config, Delete Config
        """
        self.config_listbox = tk.Listbox(self.config_frame, width=50)
        self.config_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Buttons
        button_frame = ttk.Frame(self.config_frame)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="New Config", command=self.new_config).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Load Config", command=self.load_selected_config).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save Current Config", command=self.save_current_config).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete Config", command=self.delete_config).pack(side=tk.LEFT, padx=5)

    def load_config_list(self):
        """
        Load the list of config files into the Listbox widget.

        This function reads the files in the current directory, filters out
        non-JSON files and the image_data.json file, and loads the remaining
        files into the Listbox widget for the user to select from.
        """
        self.config_files = [f for f in os.listdir() if f.endswith('.json') and f != 'images/image_data.json']
        self.config_listbox.delete(0, tk.END)
        for config in self.config_files:
            self.config_listbox.insert(tk.END, config)

    def new_config(self):
        """
        Opens a file dialog for the user to select a filename to save a new config file to.
        If the user selects a filename, it will create a new file with an empty JSON object and
        load the new config file into the listbox. It will also set the current config to the
        new file and call the load_config_callback function with an empty dictionary.
        """
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'w') as f:
                json.dump({}, f)
            self.load_config_list()
            self.current_config = filename
            self.load_config_callback({})

    def load_selected_config(self):
        """
        Loads the selected config file into the application.

        If the Listbox widget has a selected item, this function will load the
        selected config file into the application by calling the load_config
        method with the selected filename. If the Listbox widget does not have a
        selected item, a message box will appear with a friendly reminder to
        select a configuration file to load.

        This function is called when the user clicks the "Load Config" button.
        """
        if self.config_listbox.curselection():
            selected_config = self.config_listbox.get(self.config_listbox.curselection())
            print(f"Selected config: {selected_config}")  # Debug print
            self.load_config(selected_config)
        else:
            messagebox.showinfo("Info", "Please select a configuration file to load.")

    def load_config(self, filename):
        """
        Loads the selected config file into the application.

        If the filename parameter is not None or an empty string, this function
        will load the selected config file into the application by opening the
        file and parsing it as a JSON object. It will then call the
        load_config_callback function with the loaded data. If there is an error
        loading the configuration file, a message box will appear with an error
        message. If the filename parameter is None or an empty string, this
        function does nothing.

        This function is called when the user clicks the "Load Config" button
        or when the user selects a new configuration file to load from the
        Listbox widget.

        :param filename: str - The name of the file to load.
        """
        if filename:
            try:
                print(f"Loading config from file: {filename}")  # Debug print
                with open(filename, 'r') as f:
                    data = json.load(f)
                print(f"Loaded data: {data}")  # Debug print
                self.current_config = filename
                self.load_config_callback(data)
                messagebox.showinfo("Success", f"Loaded configuration from {filename}")
            except Exception as e:
                print(f"Error loading config: {str(e)}")  # Debug print
                messagebox.showerror("Error", f"Failed to load configuration: {str(e)}")
                
    def save_current_config(self):
        """
        Saves the current configuration to the current config file.

        If the current config is not set, this function will ask the user to
        select a filename to save to. If the user selects a filename, it will
        then load the selected config file into the application by calling the
        load_config method with the selected filename. It will also call the
        load_config_callback function with the loaded data.

        If the current config is set, this function will save the current data
        from the main app into the current config file by calling the
        load_config_callback function with None as the argument, and then
        writing the loaded data to the current config file. It will then show a
        message box with a success message.

        This function is called when the user clicks the "Save Config" button.
        """
        if not self.current_config:
            self.current_config = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if self.current_config:
            data = self.load_config_callback(None)  # Get current data from main app
            with open(self.current_config, 'w') as f:
                json.dump(data, f)
            messagebox.showinfo("Success", f"Saved configuration to {self.current_config}")
            self.load_config_list()

    def delete_config(self):
        """
        Deletes the selected configuration file.

        If the Listbox widget has a selected item, this function will ask the
        user to confirm the deletion of the selected config file. If the user
        confirms the deletion, it will delete the selected config file and
        reload the list of config files. If the current config is the deleted
        config, it will reset the current config to None and call the
        load_config_callback function with an empty dictionary.

        This function is called when the user clicks the "Delete Config" button.
        """
        if self.config_listbox.curselection():
            selected_config = self.config_listbox.get(self.config_listbox.curselection())
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {selected_config}?"):
                os.remove(selected_config)
                self.load_config_list()
                if self.current_config == selected_config:
                    self.current_config = None
                    self.load_config_callback({})