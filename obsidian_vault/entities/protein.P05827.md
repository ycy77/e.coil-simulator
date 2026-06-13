---
entity_id: "protein.P05827"
entity_type: "protein"
name: "ilvY"
source_database: "UniProt"
source_id: "P05827"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvY b3773 JW3746"
---

# ilvY

`protein.P05827`

## Static

- Type: `protein`
- Source: `UniProt:P05827`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: This protein activates the transcription of the ilvC gene in the presence of acetolactate or acetohydroxybutyrate. IlvY is also a negative regulator of its own expression.

## Biological Role

Component of IlvY-(S)-2-acetolactate DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7715).

## Annotation

FUNCTION: This protein activates the transcription of the ilvC gene in the presence of acetolactate or acetohydroxybutyrate. IlvY is also a negative regulator of its own expression.

## Outgoing Edges (3)

- `activates` --> [[gene.b3774|gene.b3774]] `RegulonDB` `C` - regulator=IlvY; target=ilvC; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7715|complex.ecocyc.CPLX0-7715]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3773|gene.b3773]] `RegulonDB` `C` - regulator=IlvY; target=ilvY; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3773|gene.b3773]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05827`
- `KEGG:ecj:JW3746;eco:b3773;ecoc:C3026_20435;`
- `GeneID:948284;`
- `GO:GO:0000976; GO:0003700; GO:0005737; GO:0006355; GO:0008652; GO:0009082`

## Notes

HTH-type transcriptional regulator IlvY
