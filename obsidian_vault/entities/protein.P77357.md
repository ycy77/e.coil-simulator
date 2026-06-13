---
entity_id: "protein.P77357"
entity_type: "protein"
name: "abgA"
source_database: "UniProt"
source_id: "P77357"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "abgA ydaJ b1338 JW5205"
---

# abgA

`protein.P77357`

## Static

- Type: `protein`
- Source: `UniProt:P77357`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the p-aminobenzoyl-glutamate hydrolase multicomponent enzyme system which catalyzes the cleavage of p-aminobenzoyl-glutamate (PABA-GLU) to form p-aminobenzoate (PABA) and glutamate. AbgAB does not degrade dipeptides and the physiological role of abgABT should be clarified. {ECO:0000269|PubMed:17307853, ECO:0000269|PubMed:20190044}. Transcription of the potential abgABT operon may be regulated by the predicted transcriptional regulator AbgR . AbgA: "p-aminobenzoyl-glutamate utilization"

## Biological Role

Component of p-aminobenzoyl-glutamate hydrolase (complex.ecocyc.CPLX0-7844).

## Annotation

FUNCTION: Component of the p-aminobenzoyl-glutamate hydrolase multicomponent enzyme system which catalyzes the cleavage of p-aminobenzoyl-glutamate (PABA-GLU) to form p-aminobenzoate (PABA) and glutamate. AbgAB does not degrade dipeptides and the physiological role of abgABT should be clarified. {ECO:0000269|PubMed:17307853, ECO:0000269|PubMed:20190044}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7844|complex.ecocyc.CPLX0-7844]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1338|gene.b1338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77357`
- `KEGG:ecj:JW5205;eco:b1338;ecoc:C3026_07835;`
- `GeneID:945742;`
- `GO:GO:0005737; GO:0016805; GO:0046657; GO:0046982; GO:0071713; GO:1902494`
- `EC:3.5.1.-`

## Notes

p-aminobenzoyl-glutamate hydrolase subunit A (EC 3.5.1.-) (PABA-GLU hydrolase) (PGH)
