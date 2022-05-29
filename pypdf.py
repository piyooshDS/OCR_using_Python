from pypdfocr.pypdfocr import PyPDFOCR

if __name__ == '__main__':
    converter = PyPDFOCR()
    converter.go(['Nedbank.pdf'])