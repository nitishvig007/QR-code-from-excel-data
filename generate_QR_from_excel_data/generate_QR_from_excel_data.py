

def generate_QR(fileName):

    for r in range(fileName.shape[0]) :
        name = fileName.loc[r, 'Name']
        student_id = fileName.loc[r, "Student ID"]
        website_name = "www.keepuplearning.com"

        # Import QRCode from pyqrcode
        import pyqrcode
        display_string = "Name = {} \nStudent ID = {} \n{}".format(name, student_id, website_name)
        url = pyqrcode.create(display_string)

        # Create and save the png
        output_image = str(student_id) + "_" + name + '.png'
        url.png(output_image, scale = 10)


import pandas as pd
fileName = pd.read_excel("data_file.xlsx")
print(fileName.head())

## Change Student ID type to string
fileName['Student ID']  = fileName['Student ID'].apply(str)
# print(fileName.info())

generate_QR(fileName)


