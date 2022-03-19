
import sys
from happytransformer import HappyTextClassification
happy_tc = HappyTextClassification(model_type="DISTILBERT", model_name="distilbert-base-uncased-finetuned-sst-2-english", num_labels=2)
import statistics
import numpy

def main(argv):
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


def getScore(review_array,word=None):
    totaldocumentScore = 0
    scores = []
    print(review_array)
    for line in review_array:
        if word is None or word in line:
            line_score = happy_tc.classify_text(line)
            if line_score.label == 'POSITIVE':
                line_score_val=line_score.score
            else:
                line_score_val = -line_score.score
            totaldocumentScore+=line_score_val
            #scores.append(((line_score_val+1)*5))
            scores.append(line_score_val)
    print(scores)
    #normalization of list
    pos_scores = []
    neg_scores = []
    for score in scores:
        if score>0:
            pos_scores.append(score)
        else:
            neg_scores.append(score)

    if len(pos_scores) >0:
        avg_pos = sum(pos_scores)/len(pos_scores)
        st_dev_pos = statistics.pstdev(pos_scores)
    else:
        avg_pos = 0.5
        st_dev_pos = 0.25
    if len(pos_scores) >0:
        avg_neg = sum(neg_scores)/len(neg_scores)
        st_dev_neg = statistics.pstdev(neg_scores)
    else:
        avg_pos = -0.5
        st_dev_pos = 0.25

    new_scores = []
    for score in scores:
        sign = numpy.sign(score)
        if score>0:
            new_score = sign*(score-avg_pos)/st_dev_pos
        else:
            new_score = sign*(score-avg_neg)/st_dev_neg
        new_score = ((new_score+1)*5)
        if new_score > 10:
            new_score = 10
        elif new_score < -10:
            new_score = -10
        new_score = round((new_score+10)/2)
        new_scores.append(new_score)




    avgdocumentScore = sum(new_scores)/len(new_scores)
    return round(avgdocumentScore),new_scores


if __name__ == "__main__":
    pass
   #result = main(sys.argv)
   #print(result)
   # sys.stdout.write(str(result))





"""
sampleDocScore = get_doc_score("neg_sample.txt")
print(sampleDocScore)
sampleDocScore = get_doc_score("pos_sample.txt")
print(sampleDocScore)
"""