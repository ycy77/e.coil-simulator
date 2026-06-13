---
entity_id: "protein.P37095"
entity_type: "protein"
name: "pepB"
source_database: "UniProt"
source_id: "P37095"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00504}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pepB yfhI b2523 JW2507"
---

# pepB

`protein.P37095`

## Static

- Type: `protein`
- Source: `UniProt:P37095`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00504}.

## Enriched Summary

FUNCTION: Probably plays an important role in intracellular peptide degradation (PubMed:20067529). {ECO:0000255|HAMAP-Rule:MF_00504, ECO:0000305|PubMed:20067529}.

## Biological Role

Component of aminopeptidase B (complex.ecocyc.CPLX0-8122).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Probably plays an important role in intracellular peptide degradation (PubMed:20067529). {ECO:0000255|HAMAP-Rule:MF_00504, ECO:0000305|PubMed:20067529}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8122|complex.ecocyc.CPLX0-8122]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2523|gene.b2523]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37095`
- `KEGG:ecj:JW2507;eco:b2523;ecoc:C3026_13985;`
- `GeneID:948766;`
- `GO:GO:0004177; GO:0005737; GO:0005829; GO:0006508; GO:0008233; GO:0030145; GO:0042802; GO:0043171; GO:0070006`
- `EC:3.4.11.23`

## Notes

Peptidase B (EC 3.4.11.23) (Aminopeptidase B)
