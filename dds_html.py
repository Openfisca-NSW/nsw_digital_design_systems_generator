from string import Template

def header(label, uniqueName, uniqueID, helperText=None):

    html = Template("""
            <div class="nsw-infobar">
                <div class="nsw-container">
                    <p>A NSW Government website</p>
                </div>
            </div>

            <header class="nsw-header">
                <div class="nsw-container">
                    <div class="nsw-header__wrapper">
                      <div class="nsw-header__center">
                        <a href="#" class="nsw-header__logo-link">
                          <svg class="nsw-icon nsw-header__logo" focusable="false" aria-hidden="true">
                            <use xlink:href="#dpc-logo"></use>
                          </svg>
                          <span class="sr-only">NSW Department of Premier and Cabinet</span>
                        </a>
                      </div>
                      <div class="nsw-header__left">
                        <button type="button" class="nsw-header-btn nsw-header-btn--menu">
                          <svg class="nsw-icon nsw-header-btn__icon" focusable="false" aria-hidden="true">
                            <use xlink:href="#menu"></use>
                            <span class="nsw-header-btn__sub"><span class="sr-only">Open</span> Menu</span>
                          </svg>
                        </button>
                      </div>
                      <div class="nsw-header__right">
                        <button type="button" class="nsw-header-btn nsw-header-btn--search js-open-search" aria-expanded="false"
                          aria-controls="header-search">
                          <svg class="nsw-icon nsw-header-btn__icon" focusable="false" aria-hidden="true">
                            <use xlink:href="#search"></use>
                          </svg>
                          <span class="nsw-header-btn__sub"><span class="sr-only">Show</span> Search</span>
                        </button>
                      </div>
                    </div>
                    <div class="nsw-search">
                      <div id="header-search" class="nsw-search__area js-search-area" hidden>
                        <form role="search">
                          <label for="nsw-search__input" class="sr-only">Search site for:</label>
                          <input autocomplete="off" class="nsw-search__input js-search-input" id="nsw-search__input"
                            name="input-autocomplete" type="text">
                          <svg class="nsw-icon nsw-search__search-icon" focusable="false" aria-hidden="true">
                            <use xlink:href="#search"></use>
                          </svg>
                        </form>
                        <button class="nsw-search__close-btn js-close-search" aria-expanded="true" aria-controls="header-search">
                          <svg class="nsw-icon nsw-search__close-icon" focusable="false" aria-hidden="true">
                            <use xlink:href="#close"></use>
                          </svg>
                          <span class="sr-only">Close search</span>
                        </button>
                      </div>
                    </div>
                </header>
                """)
        return html.safe_substitute(label=label, uniqueID=uniqueID, uniqueName=uniqueName, helperForm=helperForm)



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


def header(label, uniqueName, uniqueID, helperText=None):
    helperForm = helperTextElement(uniqueID, helperText)
    html = Template("""
        <footer class="nsw-footer">
          <div class="nsw-footer__upper">
            <div class="nsw-container section-links">
                <div class="section-links__group">
                  <h3 class="section-links__heading"><a href="#">Section Link</a></h3>
                  <ul class="section-links__list">
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                  </ul>
                </div>
                <div class="section-links__group">
                  <h3 class="section-links__heading"><a href="#">Section Link</a></h3>
                  <ul class="section-links__list">
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                  </ul>
                </div>
                <div class="section-links__group">
                  <h3 class="section-links__heading"><a href="#">Section Link</a></h3>
                  <ul class="section-links__list">
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                  </ul>
                </div>
                <div class="section-links__group">
                  <h3 class="section-links__heading"><a href="#">Section Link</a></h3>
                  <ul class="section-links__list">
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                      <li class="section-links__item"><a href="#">Secondary link</a></li>
                  </ul>
                </div>
            </div>
          </div>
          <div class="nsw-footer__lower">
            <div class="nsw-container">
              <p>We pay respect to the Traditional Custodians and First Peoples of NSW, and acknowledge their continued connection to their country and culture.</p>
              <hr>
              <ul class="nsw-footer-links">
                  <li class="nsw-footer-links__item">
                    <a href="#" class="nsw-footer-links__link">Tertiary</a>
                  </li>
                  <li class="nsw-footer-links__item">
                    <a href="#" class="nsw-footer-links__link">Tertiary</a>
                  </li>
                  <li class="nsw-footer-links__item">
                    <a href="#" class="nsw-footer-links__link">Tertiary</a>
                  </li>
                  <li class="nsw-footer-links__item">
                    <a href="#" class="nsw-footer-links__link">Tertiary</a>
                  </li>
              </ul>
              <p>Copyright © 2019</p>
            </div>
          </div>
        </footer>
    """)
    return html.safe_substitute(uniqueID=uniqueID, label=label, uniqueName=uniqueName, helperForm=helperForm)



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
