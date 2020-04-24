from scrapy.exporters import JsonItemExporter
from scrapy.utils.python import to_bytes

from RGCrawler.ranker import Ranker
from scrapy.utils.serialize import ScrapyJSONEncoder


class ReferenceItemExporter(JsonItemExporter):
    # https://stackoverflow.com/questions/48827688/order-a-json-by-field-using-scrapy/48888398
    # https://docs.scrapy.org/en/latest/topics/exporters.html#using-item-exporters

    def __init__(self, file, **kwargs):
        super().__init__(file, **kwargs)

        self.ranker = Ranker()

    def start_exporting(self):
        self.file.write(b"[")
        self._beautify_newline()

    def finish_exporting(self):
        while self.ranker.references_count() != 0:
            item = self.ranker.yield_reference()

            self.file.write(b',')
            self._beautify_newline()

            itemdict = dict(self._get_serialized_fields(item))
            data = self.encoder.encode(itemdict)
            self.file.write(to_bytes(data, self.encoding))

        self._beautify_newline()
        self.file.write(b"]")

    def export_item(self, item):
        if self.first_item:
            self.first_item = False

            itemdict = dict(self._get_serialized_fields(item))
            data = self.encoder.encode(itemdict)
            self.file.write(to_bytes(data, self.encoding))

        else:
            # self.file.write(b',')
            # self._beautify_newline()
            self.ranker.add_reference(item)

        # itemdict = dict(self._get_serialized_fields(item))
        # data = self.encoder.encode(itemdict)
        # self.file.write(to_bytes(data, self.encoding))
