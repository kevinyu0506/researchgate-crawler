import heapq as hq
import logging


class Ranker:

    def __init__(self):
        self.references = []
        self.count = 0

    def add_reference(self, referenceItem):
        self.count += 1
        score = -1*int(referenceItem.get('citation_count', 0))
        logging.info(f"Add reference to ranker, c_count: {score}")
        hq.heappush(self.references, (score, self.count, referenceItem))

    def references_count(self):
        logging.info(f"Reference count: {self.count}")
        return self.count

    def yield_reference(self):
        if self.references_count() != 0:
            item = hq.heappop(self.references)
            logging.info(f"Popping smallest item: {item}")
            self.count -= 1
            return item[2]
        else:
            return None
