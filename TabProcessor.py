from NLPInstance import *


# Loads CoNLL 2000 chunk data.

# @author Sebastian Riedel


class CoNLL2000(object):

    name = "CoNLL 2000"

    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return CoNLL2000.name

    # @see TabProcessor#create(List<? extends List<String>>)
    def create(self, rows):
        instance = NLPInstance()
        index = 0
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            chunk = row[2]
            instance.addToken().\
                addProperty(property = "Word", value = row[0]).\
                addProperty(property = "Index", value = str(index))
            instance.addSpan(index, index, row[1], "pos")
            instance.addSpan(index, index, chunk, "Chunk (BIO)")
            index += 1
        return instance

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        return None

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def supportOpen(self):
        return False


# Loads CoNLL 2002 NER data.

# @author Sebastian Riedel


class CoNLL2002(object):

    name = "CoNLL 2002"

    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return CoNLL2002.name

    def create(self, rows):
        instance = NLPInstance()
        index = 0
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property = "Word", value = row[0]).\
                addProperty(property = "Index", value = str(index))
            instance.addSpan(index, index, row[1], "ner (BIO)")
            index += 1

        # TODO: TabFormat.extractSpan00(rows, 1, "ner", instance)

        return instance

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        return None

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def supportOpen(self):
        return False


# Loads CoNLL 2003 chunk and NER data.

# @author Sebastian Riedel


class CoNLL2003(object):

    name = "CoNLL 2003"

    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return CoNLL2002.name

    def create(self, rows):
        instance = NLPInstance()
        index = 0
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property = "Word", value = row[0]).\
                addProperty(property = "Index", value = str(index))
            instance.addSpan(index, index, row[1], "pos")
            instance.addSpan(index, index, row[2], "chunk (BIO")
            instance.addSpan(index, index, row[3], "ner (BIO)")
            index += 1

        # TODO: TabFormat.extractSpan03(rows, 2, "chunk", instance)
        # TODO: TabFormat.extractSpan03(rows, 3, "ner", instance)

        return instance

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        return None

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def supportOpen(self):
        return False


# Loads CoNLL 2004 SRL data.

# @author Sebastian Riedel


class CoNLL2004(object):

    name = "CoNLL 2004"

    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return CoNLL2002.name

    def create(self, rows):
        instance = NLPInstance()
        index = 0
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property = "Word", value = row[0]).\
                addProperty(property = "Index", value = str(index))
            index += 1
        predicateCount = 0
        index = 0
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            if row[1] != "-":
                sense = row[1]
                instance.addSpan(index, index, sense, "sense")
                #  TODO: TabFormat.extractSpan05(rows, 2 + predicateCount, "role", sense + ":", instance)
                predicateCount = predicateCount + 1
            index += 1
        return instance

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        return None

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def supportOpen(self):
        return False


# Loads CoNLL 2005 SRL data.

# @author Sebastian Riedel


class CoNLL2005(object):

    name = "CoNLL 2005"

    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return CoNLL2002.name

    def create(self, rows):
        instance = NLPInstance()
        index = 0
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property = "Word", value = row[0]).\
                addProperty(property = "Index", value = str(index))
            index += 1
        predicateCount = 0
        index = 0
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            if row[9] != "-": # TODO: nincs 9 szó ebben?
                sense = row[10] + "." + row[9]
                instance.addSpan(index, index, sense, "sense")
                # TODO:  TabFormat.extractSpan05(ros, 11 + predicateCount, "role", sense + ":", instance
                predicateCount += 1
            index += 1
        return instance

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        return None

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def supportOpen(self):
        return False


# Loads CoNLL 2006 Dependency data.

# @author Sebastian Riedel


class CoNLL2006(object):

    name = "CoNLL 2006"

    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return CoNLL2002.name

    def create(self, rows):
        instance = NLPInstance()
        instance.addToken().addProperty("Word", "-Root-")
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property = "Word", value = row[1]).\
                addProperty(property = "Index", value = row[0]).\
                addProperty(property = "Lemma", value = row[2]).\
                addProperty(property = "CPos", value = row[3]).\
                addProperty(property = "Pos", value = row[4]).\
                addProperty(property = "Feats", value = row[5])
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            # dependency
            mod = row[0]
            try:
                instance.addEdge(From = row[6], to = mod, label = row[7], type ="dep")
            except:
                print("Can't parse dependency")
                instance.tokens[mod].addProperty("DepMissing", "missing")
            # role
        return instance


    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        return None

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def supportOpen(self):
        return False


# Loads CoNLL 2008 Joint SRL and Dependency data.

# @author Sebastian Riedel


class CoNLL2008(object):

    # The name of the processor.
    name = "CoNLL 2008"

    @property
    def ne(self):
        return TokenProperty("Named Entity", 10)

    @property
    def bbn(self):
        return TokenProperty("NamedEntity BBN", 11)

    @property
    def wn(self):
        return TokenProperty("WordNet", 12)


    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return CoNLL2008.name

    # @see TabProcessor#create(List<? extends List<String>>)

    def crate(self, rows):
        instance = NLPInstance()
        instance.addToken().addProperty("Word", "-Root-")
        predicates = []
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property="Word",value=row[1]).\
                addProperty(property="Index", value=row[0]).\
                addProperty(property = "Lemma", value = row[2]).\
                addProperty(property="Pos",value= row[3]).\
                addProperty(property="Split Form", value=row[5]).\
                addProperty(property="Split Lemma", value=row(6)).\
                addProperty(property="Split PoS", value=row[7])
            if row[10] != "_":
                index = row[0]
                predicates.append(index)
                instance.addSpan(index, index, row[10], "sense")
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            # dependency
            if row[8] != "_":
                instance.addEdge(row[8], row[0], row[9], "dep")
            # role
            for col in range(11, len(row)):
                label = row[col]
                if label != "_":
                    pred = predicates[col-11]
                    arg = row[0]
                    # if arg != pred
                    instance.addEdge(From = pred, to = arg, label = label, type = "role")
        return instance

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        instance = NLPInstance()
        instance.addToken()
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property=self.ne, value=row[0]).\
                addProperty(property=self.bbn, value=row[1]).\
                addProperty(property=self.wn, value= row[2])
        index = 1
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            #dependency
            instance.addEdge(From = row[3], to = index, label = row[4], type = "malt")
            index += 1
        return index

    # @see TabProcessor#supportsOpen()
    def supportsOpen(self):
        return True


# Loads CoNLL 2008 Joint SRL and Dependency data.

# @author Sebastian Riedel


class CoNLL2009(object):

    # The name of the processor.
    name = "CoNLL 2009"

    @property
    def ne(self):
        return TokenProperty("Named Entity", 10)

    @property
    def bbn(self):
        return TokenProperty("NamedEntity BBN", 11)

    @property
    def wn(self):
        return TokenProperty("WordNet", 12)

    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return CoNLL2009.name

    # @see com.googlecode.whatswrong.io.TabProcessor#create(java.util.List<? extends java.util.List<String>>)
    def create(self, rows):
        instance = NLPInstance()
        instance.addToken().addProperty(property="Word", value="-Root-")
        predicates = []
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property="Word", value=row[1]).\
                addProperty(property="Index", value=row[0]).\
                addProperty(property="Lemma", value=row[2]).\
                addProperty(property="PLemma", value=row[3]).\
                addProperty(property="PoS", value=row[4]).\
                addProperty(property="PPoS", value=row[5]).\
                addProperty(property="Feat", value=row[6]).\
                addProperty(property="PFeat", value=row[7])
            if row[13] != "_":
                index = row[0]
                predicates.append(index)
                instance.addSpan(index, index, row[13], "sense")
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            #dependency
            if row[0] != "_":
                instance.addEdge(From = row[8], to = row[0], label = row[10], type = "dep")
            if row[9] != "_":
                instance.addEdge(From = row[9], to = row[0], label = row[11], type = "pdep")
            #role
            for col in range(14, len(row)):
                label = row[col]
                if label != "_":
                    pred = predicates[col - 14]
                    arg = row[0]
                    # if arg != pred:
                    instance.addEdge(From = pred, to = arg, label = label, type = "role")
        return instance

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        return None

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def supportOpen(self):
        return False


# Loads Malt-TAB dependencies.

# @author Sebastian Riedel

class MaltTab(object):

    # The name of the processor.
    name = "Malt-Tab"

    # Returns the name of this processor.

    # @return the name of this processor.
    def __str__(self):
        return MaltTab.name

    # @see com.googlecode.whatswrong.io.TabProcessor#create(java.util.List<? extends java.util.List<String>>)
    def create(self, rows):
        instance = NLPInstance()
        instance.addToken().addProperty("Word", "-Root-")
        index = 1
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            instance.addToken().\
                addProperty(property = "Word", value = row[0]).\
                addProperty(property="Index", value=str(index)).\
                addProperty(property="Pos", value=row[1])
            index += 1
        mod = 1
        for row in rows:
            if row == "\n":
                continue
            row = row.split()
            # dependency
            try:
                instance.addEdge(From = row[2], to = str(mod), label = row[3], type = "dep")
            except:
                print("Can't parse dependency")
                instance.tokens[mod].addProperty("DepMissing", "missing")
            # role
            mod += 1
        return instance

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def createOpen(self, rows):
        return None

    # @see TabProcessor#createOpen(List<? extends List<String>>)
    def supportOpen(self):
        return False




























