import csv
from io import StringIO

import pdfkit
from django.template.loader import get_template


class Helpers:
    @staticmethod
    async def generate_pdf(template_path, json_data, flag_html=False):
        """

        Generated PDF object from template and json data provided
        if only HTML rendering is required then flag_html needs to be true

        @param template_path: Path to the template
        @param json_data: Context for template
        @param flag_html: default false, set true if HTML is required
        @return: PDF object / Html String

        """
        options = {
            'page-size': 'A4',
            'margin-top': '6',
            'margin-right': '0',
            'margin-bottom': '6',
            'margin-left': '0',
        }
        template = get_template(template_path)
        html = template.render(json_data)
        if flag_html:
            return html

        r = pdfkit.PDFKit(html, 'string', verbose=True, options=options)
        pdf = r.to_pdf()

        return pdf

    @staticmethod
    def generate_csv(header=[], table_header=[], table_data=[], table_footer=[], footer=[], file_object=StringIO()):

        writer = csv.writer(file_object)

        # Adding file header
        for data in header:
            writer.writerow(data)

        # Adding table header
        writer.writerow(table_header)

        # Adding table data
        for data in table_data:
            if isinstance(data, dict):
                writer.writerow(list(data.values()))
            else:
                writer.writerow(data)

        # Adding table footer
        writer.writerow(table_footer)

        # Adding file footer
        for data in footer:
            writer.writerow(data)

        return file_object
