import tkinter as tk
from tkinter import ttk

class VariablesTab:
    def __init__(self, notebook):
        """
        Initialize the VariablesTab class.

        Parameters
        ----------
        notebook : ttk.Notebook
            The parent notebook.

        """
        self.variables_frame = ttk.Frame(notebook)
        notebook.add(self.variables_frame, text="Variables")

        self.variables = {}
        self.variable_change_callbacks = []
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the VariablesTab.

        This function creates a Treeview widget to display the variables, a scrollbar to scroll the Treeview, an entry
        widget to enter the variable name, an entry widget to enter the variable value, a button to add or update a
        variable, and a button to remove a variable.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.tree = ttk.Treeview(self.variables_frame, columns=('Name', 'Value'), show='headings')
        self.tree.heading('Name', text='Variable Name')
        self.tree.heading('Value', text='Value')
        self.tree.column('Name', width=150)
        self.tree.column('Value', width=150)
        self.tree.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(self.variables_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')

        self.tree.configure(yscrollcommand=scrollbar.set)

        control_frame = ttk.Frame(self.variables_frame)
        control_frame.pack(side='bottom', fill='x', pady=10)

        self.var_name_entry = ttk.Entry(control_frame, width=20)
        self.var_name_entry.pack(side='left', padx=5)
        self.var_value_entry = ttk.Entry(control_frame, width=20)
        self.var_value_entry.pack(side='left', padx=5)

        ttk.Button(control_frame, text="Add/Update Variable", command=self.add_update_variable).pack(side='left', padx=5)
        ttk.Button(control_frame, text="Remove Variable", command=self.remove_variable).pack(side='left', padx=5)

        self.tree.bind('<Double-1>', self.on_double_click)

    def on_double_click(self, event):
        """
        Handles double-click event on Treeview item.

        When a Treeview item is double-clicked, this function is called. It gets the selected item's values and inserts
        them into the variable name and value entry widgets.

        Parameters
        ----------
        event : tk.Event
            The event object. Not used.

        Returns
        -------
        None
        """
        item = self.tree.selection()[0]
        var_name, var_value = self.tree.item(item, "values")
        self.var_name_entry.delete(0, tk.END)
        self.var_name_entry.insert(0, var_name)
        self.var_value_entry.delete(0, tk.END)
        self.var_value_entry.insert(0, var_value)

    def add_update_variable(self):
        """
        Adds or updates a variable in the variables dictionary and the Treeview widget.

        When the "Add/Update Variable" button is clicked, this function is called. It gets the variable name and value
        from the entry widgets, and adds or updates the variable in the variables dictionary and the Treeview widget.

        If the variable name already exists in the Treeview widget, this function updates the value of the existing item
        in the Treeview widget. If the variable name does not exist, this function creates a new item in the Treeview
        widget.

        Finally, this function clears the entry widgets and notifies any registered callbacks that the variables have
        changed.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        var_name = self.var_name_entry.get().strip()
        var_value = self.var_value_entry.get().strip()
        if var_name:
            self.variables[var_name] = var_value
            if self.tree.exists(var_name):
                self.tree.item(var_name, values=(var_name, var_value))
            else:
                self.tree.insert('', 'end', iid=var_name, values=(var_name, var_value))
            self.var_name_entry.delete(0, tk.END)
            self.var_value_entry.delete(0, tk.END)
            self.notify_variable_change()

    def remove_variable(self):
        """
        Removes a variable from the variables dictionary and the Treeview widget.

        When the "Remove Variable" button is clicked, this function is called. It gets the selected item's values from
        the Treeview widget, removes the variable from the variables dictionary, deletes the item from the Treeview
        widget, and notifies any registered callbacks that the variables have changed.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        selected_item = self.tree.selection()
        if selected_item:
            var_name = self.tree.item(selected_item)['values'][0]
            del self.variables[var_name]
            self.tree.delete(selected_item)
            self.notify_variable_change()

    def get_variables_config(self):
        """
        Returns a string containing the current variable configuration.

        This function takes the variables dictionary and constructs a string in the format
        "var1=value1\nvar2=value2\n...". The string is then returned.

        Parameters
        ----------
        None

        Returns
        -------
        str
            The current variable configuration as a string.
        """
        return "\n".join(f"{var}={value}" for var, value in self.variables.items() if value)

    def get_variable_names(self):
        """
        Returns a list of variable names.

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of variable names.
        """
        return list(self.variables.keys())

    def add_variable_change_callback(self, callback):
        """
        Adds a callback function to the list of functions to call when the variables change.

        When the variables change, this callback will be called with a list of variable names as the argument.

        Parameters
        ----------
        callback : function
            A function that takes a list of variable names as an argument.

        Returns
        -------
        None
        """
        self.variable_change_callbacks.append(callback)

    def notify_variable_change(self):
        """
        Notifies all registered callbacks that the variables have changed.

        Calls each registered callback function with a list of variable names as the argument.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        for callback in self.variable_change_callbacks:
            callback(self.get_variable_names())

    def get_variables_data(self):
        """
        Returns a copy of the variables dictionary.

        Parameters
        ----------
        None

        Returns
        -------
        dict
            A copy of the variables dictionary.
        """
        return self.variables.copy()

    def set_variables_data(self, data):
        """
        Sets the variables dictionary to the given data and updates the Treeview widget.

        Clears the Treeview widget and populates it with the given data.

        Parameters
        ----------
        data : dict
            A dictionary of variable names to values.

        Returns
        -------
        None
        """
        self.variables = data.copy()
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Populate the treeview
        for var_name, var_value in self.variables.items():
            self.tree.insert('', 'end', iid=var_name, values=(var_name, var_value))
        self.notify_variable_change()
        