from string import Template

def textField(label, uniqueName, uniqueID):
    html = Template("""
        <div class="nsw-container nsw-wysiwyg-content">
            <div class="nsw-forms">
                <div class="nsw-form-group">
                  <label for="${uniqueID}" class="nsw-form-label">${label}</label>
                  <input id="${uniqueID}" name="${uniqueName}" class="nsw-form-input">
                </div>
            </div>
        </div>

        """)
    return html.safe_substitute(label=label, uniqueID=uniqueID, uniqueName=uniqueName)


def dropDown(option_list, label, uniqueName, uniqueID):

    option = Template(""" <option value="${value}">${option}</option> """)
    options = [option.safe_substitute(value=i, option=opt) for i, opt in enumerate(option_list)]
    default_option = option.safe_substitute(value="", option="Please select")
    options = [default_option] + options
    opt_str = "\n"
    opt_str = opt_str.join(options)

    html = Template("""
       <div class="nsw-forms">
            <div class="nsw-form-group">
              <label for="${uniqueID}" class="nsw-form-label">${label}</label>
              <select id="${uniqueID}" class="nsw-form-select">
                ${opt_str}          
              </select>
            </div>
        </div>

    """ )
    return html.safe_substitute(uniqueID=uniqueID, label=label, opt_str=opt_str)



def singleCheckbox(label, uniqueName, uniqueID):
    html = Template("""
       <div class="nsw-forms">
            <div class="nsw-form-group">
                <div class="nsw-form-checkbox">
                   <input class="nsw-form-checkbox__input" type="checkbox" name="${inputName}" id="${uniqueID}">
                   <label class="nsw-form-checkbox__label" for="${uniqueID}">${label}:</label>     
                </div>
            </div>
        </div>
    """)
    return html.safe_substitute(uniqueID=uniqueID, label=label, uniqueName=uniqueName)





