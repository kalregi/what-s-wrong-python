from CorpusFormat import *
from TabProcessor import *


class TabFormat(CorpusFormat):

    @property
    def accessory(self):
        return self._accessory

    @accessory.setter
    def accessory(self, value):
        self._accessory = value # TODO: JPanel

    @property
    def processors(self):
        return self._processors

    @processors.setter
    def processors(self, value):
        self._processors = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value # TODO: JComboBox

    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value # TODO: JCheckBox

    @property
    def name(self):
        return self._name


    def __init__(self, MainWindow):

        self._name = "TAB-separated"

        self.addProcessor(name = "CoNLL 2009", processor = CoNLL2009())
        self.addProcessor(name = "CoNLL 2008", processor = CoNLL2008())
        self.addProcessor(name = "CoNLL 2006", processor = CoNLL2006())
        self.addProcessor(name = "CoNLL 2004", processor = CoNLL2004())
        self.addProcessor(name = "CoNLL 2002", processor = CoNLL2002())
        self.addProcessor(name = "CoNLL 2003", processor = CoNLL2003())
        self.addProcessor(name = "CoNLL 2000", processor = CoNLL2000())
        self.addProcessor(processor = MaltTab())

        # TODO: grafikus rész

        self._accessory = MainWindow
        self._type = MainWindow
        self._open = MainWindow

    def addProcessor(self, processor, name = None):
        if name is not None:
            self._processors[name] = processor
        else:
            self._processors[str(processor)] = property

    def __str__(self):
        return self._name

    def load(self, file, From, to):
        processor = self._type.getSelectedItem() # TODO grafika
        result = self.loadTabs(file, From, to, processor, False)
        if self._open.isSelected():
            filename = file.name()[0, file.name.rfind('.')+".open"]
            openFile = open(filename)
            openCorpus = self.loadTabs(openFile, From, to, processor, True)
            for i in range(0, len(openCorpus)):
                result[i].merge(openCorpus[i])

    def loadTabs(self, file, From, to, processor, open):
        corpus = []
        rows = []
        instnceNr = 0
        for line in file:
            if instnceNr < to:
                line = line.strip()
                if line == "":
                    self._monitor.progressed(instnceNr)
                    if instnceNr+1 < From:
                        continue
                    if open:
                        instance = processor.createOpen(rows)
                    else:
                        instance = processor.create(rows)
                    corpus.append(instance)
                    rows.clear()
                else:
                    instnceNr += 1
                    if instnceNr < From:
                        continue
                    rows.append(line.split("\\s+")) # TODO: rows.add(Arrays.asList(line.split("\\s+")));
        if len(rows) > 0:
            if open:
                corpus.append(processor.createOpen(rows))
            else:
                corpus.append(processor.create(rows))
        return corpus


    def setMonitor(self, monitor):
        self._monitor = monitor

    def loadProperties(self, properties, prefix):
        yearString = properties.getProperties(prefix + ".tay.type", "CoNLL 2008")
        self._type.setSelectedItem(self._processors[yearString])
        # TODO: grafika

    @property
    def longName(self):
        #  TODO: type
        return self._name + "(" + str(self._type.getSelectedItem()) + ")"


    def saveProperties(self, properties, prefix):
        properties.setProperty(prefix + ".tab.type", str(self._type.getSelectedItem()))

    def extractSpan03(self, rows, column, type, instance):
        index = 0
        inChunk = False
        begin = 0
        currentChunk = ""
        for row in rows:
            chunk = row[column]
            minus = chunk.find('-')
            if minus != -1:
                bio = chunk[0, minus]
                label = chunk[minus + 1, len(chunk)]
                if inChunk:
                    # start a new chunk and finish old one
                    if 'B' == bio or "I" == bio and label !=currentChunk:
                        instance.addSpan(begin, index -1, currentChunk, type)
                        begin = index
                        currentChunk = label
                    else:
                        inChunk = True
                        begin = index
                        currentChunk = label
                else:
                    if inChunk:
                        instance.addSpan(begin, index-1, currentChunk, type)
                        inChunk = False
            index += 1
        if inChunk:
            instance.addSpan(begin, index -1, currentChunk, type)

    def extractSpan00(self, rows, column, type, instance):
        index = 0
        inChunk = False
        begin = 0
        currentChunk = False
        for row in rows:
            chunk = row[column]
            minus = chunk.find('-')
            if minus != -1:
                bio = chunk[0, minus]
                label = chunk[minus + 1, len(chunk)]
                if 'B' == bio:
                    if inChunk:
                        instance.addSpan(begin, index -1, currentChunk, type)
                    begin = index
                    currentChunk = label
                    inChunk = True
            else:
                if inChunk:
                    instance.addSpan(begin, index -1, currentChunk, type)
                    inChunk = False
            index += 1

    def extractSpan05(self, rows, column, type, prefix, instance):
        index = 0
        begin = 0
        currentChunk = ""
        for row in rows:
            chunk = row[column]
            if chunk.startswith('('):
                currentChunk = chunk[1, chunk.find('*')]
                begin = index
            if chunk.endswith(')'):
                instance.addSpan(begin, index, prefix + currentChunk, type)
            index += 1

