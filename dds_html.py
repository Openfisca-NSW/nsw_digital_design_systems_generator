from string import Template

def textField(label, uniqueName, uniqueID, helperText=None):
    helperForm = helperTextElement(uniqueID, helperText)
    html = Template("""
        <div class="nsw-container nsw-wysiwyg-content">
            <div class="nsw-forms">
                <div class="nsw-form-group">
                  <label for="${uniqueID}" class="nsw-form-label">${label}</label>
                  ${helperForm}
                  <input id="${uniqueID}" name="${uniqueName}" class="nsw-form-input">
                </div>
            </div>
        </div>

        """)
    return html.safe_substitute(label=label, uniqueID=uniqueID, uniqueName=uniqueName, helperForm=helperForm)


def dropDown(optionList, label, uniqueName, uniqueID, helperText=None):

    option = Template(""" <option value="${value}">${option}</option> """)
    options = [option.safe_substitute(value=i, option=opt) for i, opt in enumerate(optionList)]
    default_option = option.safe_substitute(value="", option="Please select")
    options = [default_option] + options
    opt_str = "\n"
    opt_str = opt_str.join(options)

    helperForm = helperTextElement(uniqueID, helperText)
    html = Template("""
       <div class="nsw-forms">
            <div class="nsw-form-group">
              <label for="${uniqueID}" class="nsw-form-label">${label}</label>
              ${helperForm}
              <select id="${uniqueID}" class="nsw-form-select">
                ${opt_str}          
              </select>
            </div>
        </div>

    """ )
    return html.safe_substitute(uniqueID=uniqueID, label=label, opt_str=opt_str, helperForm=helperForm)



def singleCheckbox(label, uniqueName, uniqueID, helperText=None):
    helperForm = helperTextElement(uniqueID, helperText)
    html = Template("""
       <div class="nsw-forms">
            <div class="nsw-form-group">
                <div class="nsw-form-checkbox">
                   <input class="nsw-form-checkbox__input" type="checkbox" name="${inputName}" id="${uniqueID}">
                   <label class="nsw-form-checkbox__label" for="${uniqueID}">${label}:</label>     
                   ${helperForm}
                </div>
            </div>
        </div>
    """)
    return html.safe_substitute(uniqueID=uniqueID, label=label, uniqueName=uniqueName, helperForm=helperForm)


def checkboxList(optionList, groupLabel, uniqueName, uniqueID, helperText=None):

    helperForm = helperTextElement(uniqueID, helperText)
    option = Template("""<input class="nsw-form-checkbox__input" type="checkbox" name="${uniqueName}" id="checkbox${value}"> 
                         <label class="nsw-form-checkbox__label" for="checkbox${value}">${option}</label>
            """)
    options = [option.safe_substitute(value=i, option=opt, uniqueName=uniqueName) for i, opt in enumerate(optionList)]
    opt_str = "\n"
    opt_str = opt_str.join(options)

    html = Template("""
        <div class="nsw-forms">
            <div class="nsw-form-group">
                <fieldset class="nsw-form-fieldset">
                <legend>
                <span class="nsw-form-legend-text">${groupLabel}</span>
                </legend>
                ${helperForm}
                <div class="nsw-form-checkbox">
                ${opt_str}
                </div>
                </fieldset>
            </div>
        </div>
    """)
    return html.safe_substitute(uniqueID=uniqueID, groupLabel=groupLabel, opt_str=opt_str, helperForm=helperForm)


def radioList(optionList, groupLabel, uniqueName, uniqueID, helperText=None):

    helperForm = helperTextElement(uniqueID, helperText)
    option = Template("""
                   <input class="nsw-form-radio__input" type="radio" name="${uniqueName}" id="radio${value}">
                   <label class="nsw-form-radio__label" for="radio${value}">${option}</label>      
                     """)
    options = [option.safe_substitute(value=i, option=opt, uniqueName=uniqueName) for i, opt in enumerate(optionList)]
    opt_str = "\n"
    opt_str = opt_str.join(options)

    html = Template("""
        <div class="nsw-forms">
            <div class="nsw-form-group">
                <fieldset class="nsw-form-fieldset">
                <legend>
                <span class="nsw-form-legend-text">${groupLabel}</span>
                </legend>
                ${helperForm}
                <div class="nsw-form-radio">
                    ${opt_str}
                </div>
               </fieldset>
            </div>
        </div>
        """)
    return html.safe_substitute(uniqueID=uniqueID, groupLabel=groupLabel, opt_str=opt_str, helperForm=helperForm)


def helperTextElement(helperID, helperText):
    if(helperText==None):
        return ""
    html = Template(""" <span id="${helperID}" class="nsw-form-helper">${helperText}</span> """)
    return html.safe_substitute(helperText=helperText, helperID=helperID)



if __name__ == "__main__":
    print(checkboxList(["abc", "def", "ghi"], "alphabet", "alphabet_name", "moof", "this is some helper text"))
    print(radioList(["abc", "def", "ghi"], "alphabet", "alphabet_name", "moof", "this is some helper text"))
    print(singleCheckbox("singleCheckbox", "IamUnique", "uniqueSingleCheckBox", "Help this single checkbox")) 
    print(dropDown(["abc", "def", "ghi"], "drop down", "uniqueDropDown", "uniqueDropDown1", "helping the drop down"))
    print(textField("label", "uniqueName", "uniqueID", "helperText=None"))
