
import sys



from happytransformer import HappyTextClassification

happy_tc = HappyTextClassification(model_type="DISTILBERT", model_name="distilbert-base-uncased-finetuned-sst-2-english", num_labels=2)

def main(argv):
    #print("argv")
    #print(argv)
    return get_doc_score(argv[1])


def get_doc_score(doc_path):
    with open(doc_path) as f:
        lines = f.readlines()
    documentScore = 0
    for line in lines:
        line_score = happy_tc.classify_text(line)
        if line_score.label == 'POSITIVE':
            documentScore+=line_score.score
        else:
            documentScore-=line_score.score
    documentScore = (documentScore/len(lines)+1)*5
    return round(documentScore)


def getScore(review_array):
    documentScore = 0
    for line in review_array:
        line_score = happy_tc.classify_text(line)
        if line_score.label == 'POSITIVE':
            documentScore+=line_score.score
        else:
            documentScore-=line_score.score
    documentScore = (documentScore/len(lines)+1)*5
    return round(documentScore)


if __name__ == "__main__":
   #result = main(sys.argv)
   #print(result)
   # sys.stdout.write(str(result))



"""
sampleDocScore = get_doc_score("neg_sample.txt")
print(sampleDocScore)
sampleDocScore = get_doc_score("pos_sample.txt")
print(sampleDocScore)
"""