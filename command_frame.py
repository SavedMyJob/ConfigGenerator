import tkinter as tk
from tkinter import ttk, messagebox

class CommandFrame(ttk.Frame):
    def __init__(self, parent, command_types, remove_callback, spells_tab, variable_names):
        """
        Constructor for CommandFrame.

        Parameters:
            parent (ttk.Frame): The parent widget.
            command_types (dict): A dictionary of command types.
            remove_callback (callable): A callback to remove the command frame.
            spells_tab (SpellsTab): The SpellsTab instance.
            variable_names (list): A list of variable names.
        """
        super().__init__(parent)
        self.command_types = command_types
        self.remove_callback = remove_callback
        self.spells_tab = spells_tab
        self.variable_names = variable_names  # List of variable names
        self.create_widgets()

    def create_widgets(self):
        # Configure grid layout
        """
        Creates the widgets for the command frame.

        Configures the grid layout, adds a delete button, a command type combobox, a parameters frame, and an info label.
        """
        self.grid_columnconfigure(3, weight=1)

        # Delete button
        self.delete_button = ttk.Button(self, text="X", width=2, command=self.remove_callback)
        self.delete_button.grid(row=0, column=0, padx=(0, 5), sticky='w')

        # Command type combobox
        self.command_type = ttk.Combobox(
            self,
            values=list(self.command_types.keys()),
            width=25,
            state='readonly'
        )
        self.command_type.bind("<<ComboboxSelected>>", self.update_parameters)
        self.command_type.grid(row=0, column=1, padx=5, sticky='w')

        # Parameters frame
        self.parameters_frame = ttk.Frame(self)
        self.parameters_frame.grid(row=0, column=2, padx=5, sticky='w')

        # Info label
        self.info_label = ttk.Label(self, text="", anchor='w')
        self.info_label.grid(row=0, column=3, padx=5, sticky='ew')

    def update_parameters(self, event=None):
        # Clear existing parameter widgets
        """
        Updates the parameter widgets when the command type is changed.

        Clears any existing parameter widgets, gets the new command type, and creates parameter labels and input widgets.

        For each parameter, creates a label, a toggle button to switch between 'Value' and 'Var', an entry widget for literal values, and a combobox for variable or spell selection.

        Stores the parameter widgets and toggle states in the `parameter_entries` list.

        Finally, calls `update_preview` to update the preview text.
        """
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()

        command_type = self.command_type.get()
        if not command_type:
            self.info_label.config(text="")
            return

        command = self.command_types[command_type]
        self.parameter_entries = []

        for idx, param in enumerate(command.get('params', [])):
            # Parameter label
            label = ttk.Label(self.parameters_frame, text=param, width=20)
            label.grid(row=idx, column=0, padx=2, pady=2, sticky='w')

            # Frame to hold toggle and input widgets
            param_frame = ttk.Frame(self.parameters_frame)
            param_frame.grid(row=idx, column=1, padx=2, pady=2, sticky='w')

            # Toggle variable between 'Value' and 'Var'
            toggle_var = tk.StringVar(value='Value')

            # Toggle button
            toggle_button = ttk.Checkbutton(
                param_frame,
                text='Var',
                variable=toggle_var,
                onvalue='Var',
                offvalue='Value',
                command=lambda sv=toggle_var, idx=idx: self.toggle_variable(sv, idx)
            )
            toggle_button.pack(side='left')

            # Entry widget for literal value
            entry = ttk.Entry(param_frame, width=25)
            entry.pack(side='left')
            entry.bind("<KeyRelease>", self.update_preview)

            # Combobox for variable or spell selection
            if param.lower() == 'slot number':
                # For 'Slot Number', display spells when 'Var' is selected
                combobox = ttk.Combobox(
                    param_frame,
                    values=[spell[0] for spell in self.spells_tab.get_selected_spells()],
                    width=25,
                    state='readonly'
                )
            else:
                # For other parameters, display variables
                combobox = ttk.Combobox(
                    param_frame,
                    values=self.variable_names,
                    width=25,
                    state='readonly'
                )
            combobox.pack(side='left')
            combobox.bind("<<ComboboxSelected>>", self.update_preview)

            # Initially hide combobox
            combobox.pack_forget()

            # Store widgets and toggle state
            self.parameter_entries.append({
                'param_name': param.lower(),
                'toggle_var': toggle_var,
                'entry': entry,
                'combobox': combobox
            })

        self.update_preview()

    def toggle_variable(self, toggle_var, idx):
        """
        Handles toggling between literal value and variable/spell selection.

        If toggle_var is set to 'Var', shows the combobox for selecting a variable or spell.
        If toggle_var is set to 'Value', shows the entry widget for entering a literal value.

        :param toggle_var: StringVar with values 'Var' or 'Value'
        :param idx: Index of parameter entry in self.parameter_entries
        :return: None
        """
        widgets = self.parameter_entries[idx]
        param_name = widgets['param_name']
        if toggle_var.get() == 'Var':
            widgets['entry'].pack_forget()
            if param_name == 'slot number':
                # Update combobox with latest spells
                widgets['combobox']['values'] = [spell[0] for spell in self.spells_tab.get_selected_spells()]
            else:
                widgets['combobox']['values'] = self.variable_names
            widgets['combobox'].pack(side='left')
        else:
            widgets['combobox'].pack_forget()
            widgets['entry'].pack(side='left')
        self.update_preview()

    def update_variable_names(self, variable_names):
        """
        Updates the list of variable names that can be selected in parameter entries.
        Clears comboboxes that have values that are no longer valid.
        :param variable_names: List of variable names
        :return: None
        """
        self.variable_names = variable_names
        for widgets in self.parameter_entries:
            param_name = widgets['param_name']
            if param_name != 'slot number':
                combobox = widgets['combobox']
                combobox['values'] = self.variable_names
                # If combobox is visible and value is no longer valid, clear it
                if str(combobox.get()) not in self.variable_names:
                    combobox.set('')

    def update_preview(self, event=None):
        """
        Updates the preview text when a parameter is changed or when the command type is changed.

        Gets the current command type and parameters, formats them according to the command format, and displays the result in the info_label.

        If the formatted string is too long, truncates it to 30 characters and adds an ellipsis ('...').

        :param event: Optional event argument for tkinter's bind method.
        :return: None
        """
        command_type = self.command_type.get()
        if not command_type:
            self.info_label.config(text="")
            return

        command = self.command_types[command_type]
        params = []
        for widgets in self.parameter_entries:
            toggle_state = widgets['toggle_var'].get()
            if toggle_state == 'Var':
                param_value = widgets['combobox'].get()
                if widgets['param_name'] == 'slot number':
                    # Get spell_id from spell name
                    spell = next(
                        (s for s in self.spells_tab.get_selected_spells() if s[0] == param_value),
                        None
                    )
                    if spell:
                        param_value = spell[1]  # Assuming spell[1] is the ID
                        params.append(f"(VAR % {param_value})")
                    else:
                        params.append(f"(VAR % )")  # Handle missing spell_id
                else:
                    params.append(f"(VAR % {param_value})" if param_value else "")
            else:
                param_value = widgets['entry'].get()
                params.append(param_value)

        try:
            preview = command['format'].format(*params)
        except IndexError:
            preview = "Incomplete parameters"
        except Exception as e:
            preview = f"Error: {e}"

        description = command['description'][:30] + ('...' if len(command['description']) > 30 else '')
        preview_display = preview[:30] + ('...' if len(preview) > 30 else '')
        self.info_label.config(text=f"{description} | {preview_display}")

    def get_command(self):
        """
        Returns the formatted command based on the current command type and parameters.

        :return: Formatted command string
        """
        command_type = self.command_type.get()
        if not command_type:
            return ""
        command = self.command_types[command_type]
        if command_type == "Custom Command":
            return self.parameter_entries[0]['entry'].get()
        params = []
        for widgets in self.parameter_entries:
            toggle_state = widgets['toggle_var'].get()
            if toggle_state == 'Var':
                param_value = widgets['combobox'].get()
                if widgets['param_name'] == 'slot number':
                    # Get spell_id from spell name
                    spell = next(
                        (s for s in self.spells_tab.get_selected_spells() if s[0] == param_value),
                        None
                    )
                    if spell:
                        param_value = spell[1]  # Assuming spell[1] is the ID
                        params.append(f"(VAR % {param_value})")
                    else:
                        params.append(f"(VAR % )")  # Handle missing spell_id
                else:
                    if param_value:
                        params.append(f"(VAR % {param_value})")
                    else:
                        params.append("")  # Or handle as needed
            else:
                param_value = widgets['entry'].get()
                params.append(param_value)
        try:
            return command['format'].format(*params)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate command: {e}")
            return ""

    def get_command_data(self):
        """
        Returns a dictionary containing the command type and parameters as values.
        The 'parameters' key contains a list of dictionaries, each with a 'type' and 'value' key.
        The 'type' key is either 'Value' or 'Var' depending on the toggle state of the parameter.
        The 'value' key is the value in the parameter entry widget, or the selected value in the combobox for 'Var' parameters.
        """        
        command_type = self.command_type.get()
        parameters = []
        for widgets in self.parameter_entries:
            toggle_state = widgets['toggle_var'].get()
            if toggle_state == 'Var':
                param_value = widgets['combobox'].get()
                parameters.append({'type': 'Var', 'value': param_value})
            else:
                param_value = widgets['entry'].get()
                parameters.append({'type': 'Value', 'value': param_value})
        return {
            'command_type': command_type,
            'parameters': parameters
        }

    def set_command_data(self, data):
        """
        Sets the command type and parameter values based on a dictionary of data.
        
        The dictionary should have the following keys:
        - 'command_type': A string representing the command type.
        - 'parameters': A list of dictionaries, each with two keys: 'type' and 'value'. The 'type' key is either 'Value' or 'Var', and the 'value' key is the value for the parameter.
        
        If the 'parameters' key is not present, or if the value is not a list, the function will do nothing.
        
        The function will also handle the old format where 'parameters' is a list of strings, and update the toggle state and value accordingly.
        """
        command_type = data.get('command_type', '')
        self.command_type.set(command_type)
        self.update_parameters()  # Recreate parameter entries based on command_type
        parameters = data.get('parameters', [])

        for widgets, param_data in zip(self.parameter_entries, parameters):
            if isinstance(param_data, dict):
                toggle_state = param_data.get('type', 'Value')
                param_value = param_data.get('value', '')
            else:
                # Handle the old format where param_data is a string
                toggle_state = 'Value'
                param_value = param_data

            widgets['toggle_var'].set(toggle_state)
            if toggle_state == 'Var':
                widgets['entry'].pack_forget()
                widgets['combobox'].pack(side='left')
                if widgets['param_name'] == 'slot number':
                    # Update combobox with spells
                    widgets['combobox']['values'] = [spell[0] for spell in self.spells_tab.get_selected_spells()]
                else:
                    widgets['combobox']['values'] = self.variable_names
                widgets['combobox'].set(param_value)
            else:
                widgets['combobox'].pack_forget()
                widgets['entry'].pack(side='left')
                widgets['entry'].delete(0, tk.END)
                widgets['entry'].insert(0, param_value)
