## Sound Word Annotation

The manual sound word annotation was done according to the following decision tree:
1) Given a tokenized literary text, the first question in the annotation process should be whether the token is a lexical sound word.
2) If it is not, then the follow-up question arises, whether the word indicates a sound quality providing more detailed information on the realization of a sound in the fiction. If that is the case, the word is annotated with the tag `sound\_quality' (such as `kratzig' ('crunchy'), `hell' (`bright')). 
- If the word is neither a sound word nor indicates a sound quality, it should be annotated with `O' for `other annotation'. 
- If the token is a lexical sound word, the next question is whether the sound word supports the representation of a specific realized sound in the fictional world, or whether it represents only a hypothetical sound (see the Ex.1 or a generalization (see the Ex.2) of sounds in the fiction. 
Iterative sounds are annotated because they have been realized at least once in the fiction and are therefore part of the fictional soundscape (see the example Ex.3), which distinguishes them from hypothetical sounds or generalizations.
If it does not represent a specific realized sound in the fiction, it should be annotated with `O' for `other annotation'.

Ex.1:    Sollte er an den Hut fassen und **grüßen**:  ``Salü! Komme später''? (_Flametti_, H. Ball, formatting by SG)  -> hypothetical sound

Ex.2:    Dennoch hat er Zeit seines Lebens von den äußeren Gewohnheiten, von den Sitten und Manieren dieser Kreise nicht das Mindeste sich angeeignet. Wie man sich bei dieser und jener Gelegenheit kleidet, wie man sich gegen Diesen, wie gegen Jenen verbeugt, in welcher Form man mit dem Einen oder dem Andern **redet**, wie und wann man kommt und wieder geht, sich setzt, **spricht**, **schweigt**, lächelt, ernsthaft ist – von Alledem wußte Hans Gasser nichts. (_Meister Hans_, M. Tenger, formatting by SG)  -> generalization

Ex.3:    Herr Leporello, Parterre, hatte **(sq)** vertrackte **(sq)** politische **(cs)** Disputationen mit einem vierzigjährigen zelotischen Schriftsetzer, der selbstverfaßte revolutionäre Verse **(sq)** voller **(sq)** ästhetischen **(cs)** Klangs **jeden Nachmittag**, eh' er zur Arbeit ging, eine Viertelstunde lang, **(sq)** zielbewußt **(cs)** rezitierte.  (_Flametti_, H. Ball, formatting by SG)  -> iterative sound
 
If a lexical sound word represents a specific realized sound in the fiction, it should be annotated as a sound whose classification should be decided with the next and last question of the decision tree: 
5) Is the source of the represented sound recognizable as an identifiable character or group of identifiable characters in the fiction? 
- If it is not, the sound word should be classified as ambient sound and annotated with the tag `ambient_sound', if it is, the sound word should be classified as character sound and annotated with the tag `character_sound'.
