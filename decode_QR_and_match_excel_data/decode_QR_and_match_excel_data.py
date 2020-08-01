

def get_student_id(image_input):

    from pyzbar.pyzbar import decode
    from PIL import Image

    image_name = image_input

    image_QR = decode(Image.open(image_name))
    input_string = image_QR[0].data.decode("ascii")

    # display details in console
    #print(input_string)

    dummy_list = input_string.split("= ")
    id_taken = dummy_list[-1].split(" ")[0]
    return id_taken


def student_details(student_id) :
    import pandas as pd
    fileName = pd.read_excel("master_data_file.xlsx")
    #print(fileName.head())

    ## Change Student ID type to string
    fileName['Student ID']  = fileName['Student ID'].apply(str)
    # print(fileName.info())

    for r in range(fileName.shape[0]):
        if student_id == fileName.loc[r, "Student ID"] :
            print(fileName.loc[r, :])
            boolValue = 1
            break
        else :
            boolValue = 0
    if boolValue == 0 :
        print("Invalid QR Code.")



image_input = "image" + ".png"
student_id = get_student_id(image_input)
student_details(student_id)







