from pypdf import PdfMerger

files_to_merge = ["invoice123_page1.pdf", "invoice123_page2.pdf"]
merger = PdfMerger()
for pdf in files_to_merge:
    merger.append(pdf)
merger.write("invoice123_complete.pdf")
merger.close()