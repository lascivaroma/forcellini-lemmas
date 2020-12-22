# forcellini-lemmas

Cite as 

```tex
@data{thibault_clerice_2020_3822041,
  author       = {Thibault Clérice},
  title        = {Référentiel du Latin pour Pyrrha, d'après le dictionnaire et travaux du LASLA de D. Longrée et al},
  month        = may,
  year         = 2020,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.3822040},
  url          = {https://github.com/lascivaroma/forcellini-lemmas}
}
```

## POS Tags

| Tag        | French                          | English                          | UD POS | Example                                          |
|------------|---------------------------------|----------------------------------|--------|--------------------------------------------------|
| ADJadv.mul | Numéral Adverbial Multiplicatif | Multiplicative numeral adverbial | ADV    | quadragies                                       |
| ADJadv.ord | Numéral Adverbial Ordinal       | Ordinal numeral adverb           | ADV    | secundo                                          |
| ADJcar     | Numéral Cardinal                | Cardinal                         | NUM    | decem, ducenti, duo                              |
| ADJdis     | Numéral Distributif             | Distributive numeral             | ADJ    | tricenus, trinus, uicenus, undenus               |
| ADJmul     | Numéral Multiplicatif           | Multiplicative numeral           | ADJ    | septemplex, simplex, triplex                     |
| ADJord     | Numéral Ordinal                 | Ordinal numeral                  | ADJ    | octogesimus, primus, prior                       |
| ADJqua     | Adjectif qualificatif           | Adjective                        | ADJ    |                                                  |
| ADV        | Adverbe                         | Adverb                           | ADV    |                                                  |
| ADVint     | Adverbe interrogatif            | Interogative Adverb              | ADV    | an, anne, cuicuimodi2                            |
| ADVint.neg | Adverbe interrogatif négatif    | Negative Interrogative Adverb    | ADV    | necne, nonne, quidni                             |
| ADVneg     | Adverbe négatif                 | Negative Adverb                  | ADV    | haud, ne3, nec1                                  |
| ADVrel     | Adverbe relatif                 | Relative Adverb                  | ADV    | proquam, prout                                   |
| CONcoo     | Conjonction de coordination     | Coordinating conjunction         | CCONJ  |                                                  |
| CONsub     | Conjonction de subordination    | Subordinating conjunction        | SCONJ  |                                                  |
| INJ        | Interjection                    | Interjection                     | INTJ   |                                                  |
| NOMcom     | Nom commun                      | Noun                             | NOUN   |                                                  |
| NOMpro     | Nom propre                      | Proper Noun                      | PROPN  |                                                  |
| OUT        | Non-Géré                        | Out                              | X      |                                                  |
| PRE        | Préposition                     | Preposition                      | ADP    |                                                  |
| PROdem     | Pronom démonstratif             | Demonstrative Pronoun            | PRON   | hic, idem, ille                                  |
| PROind     | Pronom indéfini                 | Indefinite Pronoun               | PRON   | aliquantus, aliquis, aliquot, alis, alius, alter |
| PROint     | Pronom interrogatif             | Interrogative Pronoun            | PRON   | cuias, cuius, ecquis                             |
| PROper     | Pronom personnel                | Personal Pronoun                 | PRON   | ego, nos, tu, uos                                |
| PROpos     | Pronom possessif                | Possessive Pronoun               | PRON   | mei, meus, noster                                |
| PROpos.ref | Pronom possessif réfléchi       | Relfexive Possessive Pronoun     | PRON   | Sui, suus                                        |
| PROref     | Pronom réfléchi                 | Reflexive Pronoun                | PRON   | sepse, sui                                       |
| PROrel     | Pronom relatif                  | Relative Pronoun                 | PRON   | cuius, qualis, qualiscumque                      |
| PUNC       | Ponctuation                     | Punctuation                      | PUNCT  |                                                  |
| VER        | Verbe                           | Verb                             | VERB   |                                                  |
| VERaux     | Verbe auxiliaire                | Auxiliary Verb                   | AUX    |                                                  |
| FOR        | Termes étrangers                | Foreign words                    | X      |                                                  |

## Commits Message structure

- `+` means a lemma was **added**
- `*` means a lemma ha been more thoroughly **detailed**
- `1/2` means lemma1 and lemma2 (disambiguation) were both modified
- `@` fixed a typo

## Source

*   D. Longrée, C. Philippart de Foy & G. Purnelle. « Structures phrastiques et analyse automatique des données morphosyntaxiques : le projet LatSynt », in S. Bolasco, I. Chiari & L. Giuliano (eds), Statistical Analysis of Textual Data, Proceedings of 10th International Conference Journées d'Analyse statistique des Données Textuelles, 9-11 June 2010, Sapienza University of Rome, Rome, LED, pp. 433-442.
*   D. Longrée & C. Poudat, « New Ways of Lemmatizing and Tagging Classical and post-Classical Latin: the LATLEM project of the LASLA », in P. Anreiter & M. Kienpointner (éd.), Proceedings of the 15th International Colloquium on Latin Linguistics, (Innsbrucker Beiträge zur Sprachwissenschaft), Innsbruck, 2010, pp. 683-694.
*   D. Longrée & C. Philippart de Foy & G. Purnelle, « Subordinate clause boundaries and word order in Latin: the contribution of the L.A.S.L.A. syntactic parser project LatSynt », in P. Anreiter & M. Kienpointner, éd.), Proceedings of the 15th International Colloquium on Latin Linguistics, (Innsbrucker Beiträge zur Sprachwissenschaft), Innsbruck, 2010, pp. 673-681.
*   D. Longrée & Poudat C., « Variations langagières et annotation morphosyntaxique du latin classique », TAL, 50 – n° 2/2009, Special issue on "Natural Language Processing and Ancient Languages", pp. 129-148.
