---
entity_id: "protein.P0AEY5"
entity_type: "protein"
name: "mdaB"
source_database: "UniProt"
source_id: "P0AEY5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:8611590}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdaB mda66 b3028 JW2996"
---

# mdaB

`protein.P0AEY5`

## Static

- Type: `protein`
- Source: `UniProt:P0AEY5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:8611590}.

## Enriched Summary

FUNCTION: NADPH-specific quinone reductase (PubMed:8611590). Is most active with quinone derivatives and ferricyanide as electron acceptors (PubMed:8611590). Can use menadione, 1,4-naphthoquinone and 1,4-benzoquinone (PubMed:8611590). May work in concert with YgiN to form a quinone redox cycle (PubMed:15613473). {ECO:0000269|PubMed:15613473, ECO:0000269|PubMed:8611590}.

## Biological Role

Component of NADPH:quinone oxidoreductase MdaB (complex.ecocyc.CPLX0-253).

## Annotation

FUNCTION: NADPH-specific quinone reductase (PubMed:8611590). Is most active with quinone derivatives and ferricyanide as electron acceptors (PubMed:8611590). Can use menadione, 1,4-naphthoquinone and 1,4-benzoquinone (PubMed:8611590). May work in concert with YgiN to form a quinone redox cycle (PubMed:15613473). {ECO:0000269|PubMed:15613473, ECO:0000269|PubMed:8611590}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-253|complex.ecocyc.CPLX0-253]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3028|gene.b3028]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEY5`
- `KEGG:ecj:JW2996;eco:b3028;ecoc:C3026_16540;`
- `GeneID:86861166;947512;`
- `GO:GO:0003955; GO:0005829; GO:0008753; GO:0034599; GO:0050660`
- `EC:1.6.5.10`

## Notes

NADPH:quinone oxidoreductase MdaB (EC 1.6.5.10) (Modulator of drug activity B)
