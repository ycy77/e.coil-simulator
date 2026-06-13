---
entity_id: "protein.P52101"
entity_type: "protein"
name: "glrK"
source_database: "UniProt"
source_id: "P52101"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glrK yfhK b2556 JW5407"
---

# glrK

`protein.P52101`

## Static

- Type: `protein`
- Source: `UniProt:P52101`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system GlrR/GlrK that up-regulates transcription of the glmY sRNA when cells enter the stationary growth phase. Activates GlrR by phosphorylation. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:19843219}. This is the phosphorylated form of G7345-MONOMER "GlrK" - the sensor histidine kinase of the GlrKR two-component signal transduction system.

## Biological Role

Component of histidine kinase GlrK (complex.ecocyc.CPLX0-8275).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system GlrR/GlrK that up-regulates transcription of the glmY sRNA when cells enter the stationary growth phase. Activates GlrR by phosphorylation. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:19843219}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8275|complex.ecocyc.CPLX0-8275]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2556|gene.b2556]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52101`
- `KEGG:ecj:JW5407;eco:b2556;ecoc:C3026_14150;`
- `GeneID:947013;`
- `GO:GO:0000155; GO:0000156; GO:0004673; GO:0005524; GO:0005886; GO:0007165; GO:0007234; GO:0016774; GO:0030288; GO:0030295; GO:0055082; GO:0071871`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase GlrK (EC 2.7.13.3)
