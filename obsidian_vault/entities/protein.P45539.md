---
entity_id: "protein.P45539"
entity_type: "protein"
name: "frlA"
source_database: "UniProt"
source_id: "P45539"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frlA yhfM b3370 JW3333"
---

# frlA

`protein.P45539`

## Static

- Type: `protein`
- Source: `UniProt:P45539`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Is likely involved in the transport of fructoselysine and psicoselysine to the cytoplasm, where they are degraded. {ECO:0000305|PubMed:12147680, ECO:0000305|PubMed:14641112}. FrlA is an uncharacterized member of the APC superfamily of amino acid transporters . Based on the activities of FrlB and FrlD, FrlA is suggested to transport fructoselysine, which can be utilized as a carbon source . A frlA mutant is unable to grow on 20mM fructoselysine or psicoselysine as the sole source of carbon . FrlA: "fructoselysine"

## Biological Role

Catalyzes TRANS-RXN0-417 (reaction.ecocyc.TRANS-RXN0-417), TRANS-RXN0-418 (reaction.ecocyc.TRANS-RXN0-418).

## Annotation

FUNCTION: Is likely involved in the transport of fructoselysine and psicoselysine to the cytoplasm, where they are degraded. {ECO:0000305|PubMed:12147680, ECO:0000305|PubMed:14641112}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-417|reaction.ecocyc.TRANS-RXN0-417]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-418|reaction.ecocyc.TRANS-RXN0-418]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3370|gene.b3370]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45539`
- `KEGG:ecj:JW3333;eco:b3370;ecoc:C3026_18300;`
- `GeneID:93778627;947878;`
- `GO:GO:0003333; GO:0005886; GO:0015179; GO:1901281`

## Notes

Probable fructoselysine/psicoselysine transporter FrlA
