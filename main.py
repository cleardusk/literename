#!/usr/bin/env python
# coding: utf-8

from pyPdf import PdfFileReader
import PyPDF2
import os


def get_pdf_info(filepath=None):
    pdf_rd = PdfFileReader(open(filepath, 'rb'))
    pdf_info = pdf_rd.getDocumentInfo()
    return pdf_info


def get_pdf_info2(filepath=None):
    pdf_rd = PyPDF2.PdfFileReader(open(filepath, 'rb'))
    pdf_info = pdf_rd.getDocumentInfo()
    return pdf_info


def extract_text(filepath=None):
    pdf_rd = PyPDF2.PdfFileReader(open(filepath, 'rb'))
    page_one = pdf_rd.getPage(0)
    return page_one.extractText()


def get_suffix(filepath=None):
    return filepath[filepath.rfind('.') + 1:].lower()


def main():
    # filename = './test/imagenet.pdf'
    data_dir = './test/ieee'

    num_has_title, num_total = 0, 0
    for flnm in os.listdir(data_dir):
        flpath = os.path.join(data_dir, flnm)
        if not get_suffix(flpath) == 'pdf':
            continue

        ret = get_pdf_info(flpath)
        # print ret
        # print

        num_total += 1
        if ret.has_key(u'/Title') and ret[u'/Title'] != u'':
            print '##%d ' % num_total + ret['/Title']
            num_has_title += 1
        else:
            print '$$%d ' % num_total + extract_text(flpath)[:50]

    print '\n%d / %d' % (num_has_title, num_total)


if __name__ == '__main__':
    main()
