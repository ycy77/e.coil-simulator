---
entity_id: "protein.P15029"
entity_type: "protein"
name: "fecD"
source_database: "UniProt"
source_id: "P15029"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2651410}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fecD b4288 JW4248"
---

# fecD

`protein.P15029`

## Static

- Type: `protein`
- Source: `UniProt:P15029`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2651410}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:17660286, PubMed:2651410). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:17660286, ECO:0000269|PubMed:2651410, ECO:0000305}. FecD is one of two (along with FecC) integral membrane proteins of the iron dicitrate ABC transport system. fecD encodes a hydrophobic inner membrane protein; FecD has 34% identity with FecC and also shows similarity to FhuB of the iron(III) hydroxamate uptake system and BtuC of the Vitamin B uptake system

## Biological Role

Component of ferric citrate ABC transporter (complex.ecocyc.ABC-9-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:17660286, PubMed:2651410). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:17660286, ECO:0000269|PubMed:2651410, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-9-CPLX|complex.ecocyc.ABC-9-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4288|gene.b4288]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15029`
- `KEGG:ecj:JW4248;eco:b4288;ecoc:C3026_23125;`
- `GeneID:946816;`
- `GO:GO:0005886; GO:0006879; GO:0015603; GO:0016020; GO:0022857; GO:0033212; GO:0033214; GO:0055052`

## Notes

Fe(3+) dicitrate transport system permease protein FecD (Iron(III) dicitrate transport system permease protein FecD)
