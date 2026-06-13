---
entity_id: "protein.P32675"
entity_type: "protein"
name: "pflC"
source_database: "UniProt"
source_id: "P32675"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pflC yijM b3952 JW3924"
---

# pflC

`protein.P32675`

## Static

- Type: `protein`
- Source: `UniProt:P32675`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Activation of pyruvate formate-lyase 2 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000250}. PflC was identified by sequence similarity as a homolog of pyruvate formate-lyase activating enzyme . The protein belongs to the radical SAM superfamily. Effects of a pflC knockout have been studied; the fermentation pattern under microaerobic conditions is similar to wild type .

## Biological Role

Catalyzes protein-glycine,dihydroflavodoxin:S-adenosyl-L-methionine oxidoreductase (S-adenosyl-L-methionine cleaving) (reaction.R04710).

## Annotation

FUNCTION: Activation of pyruvate formate-lyase 2 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000250}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R04710|reaction.R04710]] `KEGG` `database` - via EC:1.97.1.4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3952|gene.b3952]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32675`
- `KEGG:ecj:JW3924;eco:b3952;ecoc:C3026_21355;`
- `GeneID:948453;`
- `GO:GO:0005737; GO:0006006; GO:0043365; GO:0046872; GO:0051539`
- `EC:1.97.1.4`

## Notes

Pyruvate formate-lyase 2-activating enzyme (EC 1.97.1.4) (Formate-C-acetyltransferase-activating enzyme 2) (PFL-activating enzyme 2)
