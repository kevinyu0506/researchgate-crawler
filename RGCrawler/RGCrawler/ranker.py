import heapq as hq
import logging


class Ranker:

    def __init__(self):
        self.references = []

    def add_reference(self, referenceItem):
        score = int(referenceItem.get('citation_count', 0))
        logging.info(f"Add reference to ranker, c_count: {score}")
        hq.heappush(self.references, (score, referenceItem))

    def references_count(self):
        r_count = len(self.references)
        logging.info(f"Reference count: {r_count}")
        return r_count

    def yield_all_reference(self):
        while self.references_count() != 0:
            item = hq.heappop(self.references)
            logging.info(f"Popping smallest item: {item}")
            yield item
