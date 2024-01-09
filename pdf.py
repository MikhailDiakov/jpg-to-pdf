from fpdf import FPDF

def img_to_pdf(images,output_file):
    pdf = FPDF()
    for image in images:
        pdf.add_page()
        pdf.image(image)
    
    pdf.output(output_file+'.pdf','F')

def main():
    image_names = input("Введите название файлов через пробел: ").split()
    image_paths = [f"{name}.jpg" for name in image_names]
    output_file = input("Введите название для выходного PDF-файла: ")

    img_to_pdf(image_paths, output_file)

if __name__ == "__main__":
    main()