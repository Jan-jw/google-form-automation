from googleForm.formInputs import Form

form = Form("https://docs.google.com/forms/d/e/1FAIpQLSedOg4iDi6W60PPLxr0ys6LZojs9bXXO7STNmA2h6jJW7Puig/viewform?usp=sf_link")
formItems = form.inputList

# type => response
#q1
form.input_shorttext(formItems[0], "paragraph")

#q2
form.input_textarea(formItems[1], "short text")

#q3
form.select_mc(formItems[2], "Option 1")

#q4
form.select_checkbox(formItems[3], "Option 3")

#q5
form.dropdown(formItems[4], "Option 1")

#q7
form.linear_scale(formItems[6], "6")

#q8
form.mc_grid( [("b", 0), ("Row 2", 1)])

#q9
form.checkbox_grid({"Row 1": {"Column 1"}, "Row 2": {"Column 1", "Column 2"}})

#q10
form.input_date(formItems[9], "2000-01-24")

#q11
form.input_time(formItems[10], "12:12", "PM")