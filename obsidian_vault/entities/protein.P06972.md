---
entity_id: "protein.P06972"
entity_type: "protein"
name: "fhuB"
source_database: "UniProt"
source_id: "P06972"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fhuB b0153 JW0149"
---

# fhuB

`protein.P06972`

## Static

- Type: `protein`
- Source: `UniProt:P06972`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:1551849, ECO:0000269|PubMed:3020380, ECO:0000269|PubMed:34887516}. FhuB is the integral membrane subunit of an iron(III) hydroxamate ABC transporter. FhuB consists of N and C terminal domains that have significant sequence similarity to each other; when expressed separately they can combine to form a functional permease; FhuB may function as a pseudo heterodimer

## Biological Role

Component of Fe(3+) hydroxamate ABC transporter (complex.ecocyc.ABC-11-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:1551849, ECO:0000269|PubMed:3020380, ECO:0000269|PubMed:34887516}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-11-CPLX|complex.ecocyc.ABC-11-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0153|gene.b0153]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06972`
- `KEGG:ecj:JW0149;eco:b0153;ecoc:C3026_00695;`
- `GeneID:946890;`
- `GO:GO:0005886; GO:0015344; GO:0015687; GO:0022857; GO:0033214; GO:0043190; GO:0055052; GO:0098711`

## Notes

Iron(3+)-hydroxamate import system permease protein FhuB (Ferric hydroxamate uptake protein B) (Ferrichrome transport system permease protein FhuB) (Ferrichrome uptake protein FhuB) (Iron(III)-hydroxamate import system permease protein FhuB)
