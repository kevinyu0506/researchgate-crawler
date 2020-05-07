import heapq as hq
import logging


class Ranker:

    def __init__(self):
        self.references = []
        self._count = 0
        self.total = 0
        self.index = 1

    def add_reference(self, referenceItem):
        self._count += 1
        score = -1*int(referenceItem.get('citation_count', 0))
        logging.info(f"Add reference to ranker, c_count: {score}")
        hq.heappush(self.references, (score, self._count, referenceItem))

    def references_count(self):
        return self._count

    def yield_reference(self):
        self.total = self.references_count()
        if self.references_count() != 0:
            item = hq.heappop(self.references)
            self._count -= 1
            item[2]['id'] = self.index
            self.index += 1
            return item[2]
        else:
            return None
