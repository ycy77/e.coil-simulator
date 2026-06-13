---
entity_id: "protein.P0AB74"
entity_type: "protein"
name: "kbaY"
source_database: "UniProt"
source_id: "P0AB74"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kbaY agaY kba yraC b3137 JW3106"
---

# kbaY

`protein.P0AB74`

## Static

- Type: `protein`
- Source: `UniProt:P0AB74`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalytic subunit of the tagatose-1,6-bisphosphate aldolase KbaYZ, which catalyzes the reversible aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to produce tagatose 1,6-bisphosphate (TBP). Requires KbaZ subunit for full activity and stability. {ECO:0000269|PubMed:10712619, ECO:0000269|PubMed:11976750}.

## Biological Role

Component of tagatose-1,6-bisphosphate aldolase 1 (complex.ecocyc.CPLX0-240).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalytic subunit of the tagatose-1,6-bisphosphate aldolase KbaYZ, which catalyzes the reversible aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to produce tagatose 1,6-bisphosphate (TBP). Requires KbaZ subunit for full activity and stability. {ECO:0000269|PubMed:10712619, ECO:0000269|PubMed:11976750}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-240|complex.ecocyc.CPLX0-240]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3137|gene.b3137]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB74`
- `KEGG:ecj:JW3106;eco:b3137;ecoc:C3026_17095;`
- `GeneID:75173310;75203745;947644;`
- `GO:GO:0005829; GO:0005975; GO:0008270; GO:0009025; GO:0032991; GO:0042802; GO:0051289; GO:1902494; GO:2001059`
- `EC:4.1.2.40`

## Notes

D-tagatose-1,6-bisphosphate aldolase subunit KbaY (TBPA) (TagBP aldolase) (EC 4.1.2.40) (D-tagatose-bisphosphate aldolase class II) (Ketose 1,6-bisphosphate aldolase class II) (Tagatose-bisphosphate aldolase)
