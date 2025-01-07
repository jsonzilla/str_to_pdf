import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import grey
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate, PageBreak
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

def parse_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    entries = content.split('\n\n')
    captions = []
    for entry in entries:
        lines = entry.split('\n')
        if len(lines) >= 3:
            time = lines[1]
            text = ' '.join(lines[2:])
            captions.append((time, text))
    return captions

def create_pdf(captions, output_path, file_name):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(name='Title', parent=styles['Normal'], fontSize=14, spaceAfter=inch)
    time_style = ParagraphStyle(name='Time', parent=styles['Normal'], fontSize=10, textColor=grey)
    caption_style = ParagraphStyle(name='Caption', parent=styles['Normal'], fontSize=12)
    
    elements = []
    elements.append(Paragraph(file_name, title_style))
    elements.append(PageBreak())
    
    data = []
    for time_sub, text_sub in captions:
        data.append([Paragraph(time_sub, time_style), Paragraph(text_sub, caption_style)])
    
    table = Table(data, colWidths=[doc.width*0.3, doc.width*0.7])
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    elements.append(table)
    doc.build(elements)

def main():
    input_folder = 'subtitles'
    output_folder = 'output_pdfs'
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.srt'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}.pdf')
            
            captions = parse_srt(input_path)
            create_pdf(captions, output_path, file_name)
            print(f'PDF criado com sucesso: {output_path}')

if __name__ == '__main__':
    main()