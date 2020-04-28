import dds_html

def form(label, uniqueName, uniqueID, helperText=None):
    header_str = dds_html.header(label, uniqueName, uniqueID, helperText=None)
    text_field_str = dds_html.textField(label, uniqueName, uniqueID, helperText=None)
    footer_str = dds_html.footer(label, uniqueName, uniqueID, helperText=None)
    print(header_str + text_field_str + footer_str)

if __name__ == "__main__":
    print(form("hello", "world", "233", "this is a hello world form"))