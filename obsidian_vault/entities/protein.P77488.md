---
entity_id: "protein.P77488"
entity_type: "protein"
name: "dxs"
source_database: "UniProt"
source_id: "P77488"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dxs yajP b0420 JW0410"
---

# dxs

`protein.P77488`

## Static

- Type: `protein`
- Source: `UniProt:P77488`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the acyloin condensation reaction between C atoms 2 and 3 of pyruvate and glyceraldehyde 3-phosphate to yield 1-deoxy-D-xylulose-5-phosphate (DXP). {ECO:0000269|PubMed:17135236, ECO:0000269|PubMed:9371765, ECO:0000269|PubMed:9482846}.

## Biological Role

Component of 1-deoxy-D-xylulose-5-phosphate synthase (complex.ecocyc.CPLX0-743).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the acyloin condensation reaction between C atoms 2 and 3 of pyruvate and glyceraldehyde 3-phosphate to yield 1-deoxy-D-xylulose-5-phosphate (DXP). {ECO:0000269|PubMed:17135236, ECO:0000269|PubMed:9371765, ECO:0000269|PubMed:9482846}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-743|complex.ecocyc.CPLX0-743]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0420|gene.b0420]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77488`
- `KEGG:ecj:JW0410;eco:b0420;ecoc:C3026_02050;`
- `GeneID:945060;`
- `GO:GO:0000287; GO:0005829; GO:0006744; GO:0008299; GO:0008615; GO:0008661; GO:0009228; GO:0016114; GO:0019288; GO:0030976; GO:0042803`
- `EC:2.2.1.7`

## Notes

1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS)
