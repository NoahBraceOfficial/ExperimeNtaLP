from pyspark.ml import Pipeline
### from sparknlp.base import LightPipeline




document_assembler = DocumentAssembler()\
 .setInputCol(“text”)\
 .setOutputCol(“document”)
sentenceDetector = SentenceDetector()\
 .setInputCols([“document”])\
 .setOutputCol(“sentences”)
tokenizer = Tokenizer() \
 .setInputCols([“sentences”]) \
 .setOutputCol(“token”)
normalizer = Normalizer()\
 .setInputCols([“token”])\
 .setOutputCol(“normal”)
word_embeddings=WordEmbeddingsModel.pretrained()\
 .setInputCols([“document”,”normal”])\
 .setOutputCol(“embeddings”)
nlpPipeline = Pipeline(stages=[
 document_assembler, 
 sentenceDetector,
 tokenizer,
 normalizer,
 word_embeddings,
 ])
pipelineModel = nlpPipeline.fit(df)


### LightPipeline(someTrainedPipeline).annotate(someStringOrArray)
