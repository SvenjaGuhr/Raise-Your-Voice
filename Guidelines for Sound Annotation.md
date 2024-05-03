## Sound Word Annotation

The manual sound word annotation was done according to the following decision tree:
1) Given a tokenized literary text, the first question in the annotation process should be whether the token is a lexical sound word.
2) If it is not, then the follow-up question arises, whether the word indicates a sound quality providing more detailed information on the realization of a sound in the fiction. If that is the case, the word is annotated with the tag 'sound_quality' (such as 'kratzig' ('crunchy'), 'hell' ('bright')). 
- If the word is neither a sound word nor indicates a sound quality, it should be annotated with 'O' for 'other annotation'. 
- If the token is a lexical sound word, the next question is whether the sound word supports the representation of a specific realized sound in the fictional world, or whether it represents only a hypothetical sound (see the Ex.1 or a generalization (see the Ex.2) of sounds in the fiction. 
Iterative sounds are annotated because they have been realized at least once in the fiction and are therefore part of the fictional soundscape (see the example Ex.3), which distinguishes them from hypothetical sounds or generalizations.
If it does not represent a specific realized sound in the fiction, it should be annotated with 'O' for 'other annotation'.

Ex.1:    Sollte er an den Hut fassen und **grüßen**:  ''Salü! Komme später''? (_Flametti_, H. Ball, formatting by SG)  -> hypothetical sound

Ex.2:    Dennoch hat er Zeit seines Lebens von den äußeren Gewohnheiten, von den Sitten und Manieren dieser Kreise nicht das Mindeste sich angeeignet. Wie man sich bei dieser und jener Gelegenheit kleidet, wie man sich gegen Diesen, wie gegen Jenen verbeugt, in welcher Form man mit dem Einen oder dem Andern **redet**, wie und wann man kommt und wieder geht, sich setzt, **spricht**, **schweigt**, lächelt, ernsthaft ist – von Alledem wußte Hans Gasser nichts. (_Meister Hans_, M. Tenger, formatting by SG)  -> generalization

Ex.3:    Herr Leporello, Parterre, hatte **sq** vertrackte **sq** politische **cs** Disputationen mit einem vierzigjährigen zelotischen Schriftsetzer, der selbstverfaßte revolutionäre Verse **sq** voller **sq** ästhetischen **cs** Klangs **jeden Nachmittag**, eh' er zur Arbeit ging, eine Viertelstunde lang, **sq** zielbewußt **cs** rezitierte.  (_Flametti_, H. Ball, formatting by SG)  -> iterative sound
 
If a lexical sound word represents a specific realized sound in the fiction, it should be annotated as a sound whose classification should be decided with the next and last question of the decision tree: 
5) Is the source of the represented sound recognizable as an identifiable character or group of identifiable characters in the fiction? 
- If it is not, the sound word should be classified as ambient sound and annotated with the tag 'ambient_sound', if it is, the sound word should be classified as character sound and annotated with the tag 'character_sound'.


<img title="Decision Tree for Sound Word Annotation" alt="Decision Tree for Sound Word Annotation" src="/Visualizations/20240503_DT_sound_words.png">




## Sound Event Annotation

The manual sound event annotation was done according to the following decision tree:
1) Given a literary text pre-annotated with sound words that represent realized sounds in the fiction, the annotation of the sound word gets extended to the short span of a sound event as follows:
- If the unit contains a lexical sound word, one should check if the lexical sound word triggers an explicit sound event, which is a _realis_ sound event in the fictional world. 
- If it does not, e.g. because the lexical sound word in the minimal unit represents a hypothetical event or a generalization, or contains an imperative or a question (like 'non-events' according to Vauth et al. 2012), the unit is treated as 'other event' or 'no event' and, in contrast to the manual token-wise annotation of sound words, does not get an annotation. This step is only necessary for automatically pre-annotated text, which may still contain false positive sound word annotations.
- The chosen annotation span should be as short as possible to enclose the sound event, but as long as necessary to cover all the information about the sound event, including its sound quality elements.
This can be a verbal phrase that contains at least one sound verb, such as 'she said', or a verbal phrase that contains a noun phrase, such as 'she said in a lower voice'. 
Moreover, the span can be as short as a one-word phrase such as the concatenated sound verbs ''schrie'', ''brüllte'', or in combination with a clause-joining conjunction (`and', `or', `but') such as the `und' in the annotation span in Ex.4.
The span may also be a longer construction interrupted by relative clauses containing additional information about the sound event such as the beginning of the Ex.5.

Ex.4:    **cs(** Seine Rede, mit poetischen Floskeln ''aus den Werken der besten Schriftsteller'' geschmückt, schilderte nachdrücklich die Seelenpein des Sünders gegenüber der heiligen Sabbathfeier im Gemüthe des Schuldlosen **)**. (_Nicht zu hoch_, H. Lingg) 

Ex.5:    Sprechproben wurden angesetzt; Ensembleproben. | Die Rollen wurden verteilt. | Persönlich probte Flametti vor dem Spiegel. | Probierte mit den Mädels, | **cs(** teilte Ohrfeigen aus **)**, | rannte Köpfe an die Wand; | **cs(** schrie **)**, | **cs(** brüllte **)** | **cs(** und fluchte **)**. (_Flametti_, H. Ball)

2) If the sound word does trigger an explicit sound event and the sound-event-covering span is detected, the next question is whether the sound source is recognizable as an identifiable character or group of identifiable characters in the fiction. 
- If this is the case, the sound event should be annotated as a character sound event annotated with the XML TEI element 'character_sound'. 
- If this is not the case, for example, if the source of the sound is recognized as nature, weather, animals, or machines, the sound event should be annotated as an ambient sound event with the XML TEI element 'ambient_sound'. 

In some cases, sounds whose source can be identified as a fictional person will also be annotated as ambient sound if the entity cannot be identified as one of the characters in the fiction, but rather as a group of fictional people with unidentifiable members. It is also classified as ambient sound if the sound is produced by an unidentifiable fictional person, such as the representation of a human scream in the night.
Furthermore, animals, especially anthropomorphic animals in fiction that communicate through verbal dialogue, are treated as individual characters. 
Their sounds are annotated as character sounds, because they cannot simply be reduced to the fictional ambient soundscape, but are the main sound elements of the fiction (e.g. conversations). 
This is the case, for example, with the dog Krambambuli in the text of the same name by M. v. Ebner-Eschenbach, who communicates with his master either by barking or even dialogically in narrated conversations between the dog and his master. 
This is in contrast to animal sounds that are only part of the ambient soundscape, e.g. descriptions of background noises such as howling wolves or screaming deer, whose sounds are annotated as ambient sounds.

<img title="Decision Tree for Sound Event Annotation" alt="Decision Tree for Sound Event Annotation" src="/Visualizations/20240503_DT_sound_event.png">


## Loudness Level Labeling

From the last step of the sound event decision tree, the following steps have been added to the manual annotation process to label the loudness level of a detected and classified sound event.
1) Once the sound event has been classified as an ambient or character sound, the loudness level is examined from the loudest to the quietest sound level, with a separate distinction for silence.
- Since loudness level '5' exceeds the human ability to produce sound, this loudness level is reserved for ambient sounds only. 
- The loudness levels '4' to '1' and the loudness level 'S' for explicit silence can be selected for both ambient and character sounds. 

The level annotation is done independently of any distance to the sound source and only with respect to the given lexical and semantic information about the sound or its assumed loudness level if it was measured directly next to the sound source. 
Thus, the annotation approach allows the inclusion of context in the loudness level labeling, which is limited to the information given in the minimal unit, without the need for further information about the space and time the sound is located in the fiction.
Consequently, the context is reduced to lexical and semantic elements such as adverbs in the annotation unit that intensify loud or soft sounds, such as `very' or `less', and comparative forms of sound adjectives that provide information to support loudness level labeling.

Ex.6:    "Gräfin, hören Sie mich?" | **cs=4(** wiederholte er lauter **)**, |  **as=5(** während gewaltige Akkorde von drüben her erbrausten **)**. (_Reichsgräfin Gisela_, E. Marlitt)


<img title="Decision Tree for Sound Event Annotation" alt="Decision Tree for Sound Event Annotation" src="/Visualizations/20240503_DT_loudness_level.png">



