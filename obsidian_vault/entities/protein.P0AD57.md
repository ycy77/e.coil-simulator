---
entity_id: "protein.P0AD57"
entity_type: "protein"
name: "ispB"
source_database: "UniProt"
source_id: "P0AD57"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ispB cel yhbD b3187 JW3154"
---

# ispB

`protein.P0AD57`

## Static

- Type: `protein`
- Source: `UniProt:P0AD57`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Supplies octaprenyl diphosphate, the precursor for the side chain of the isoprenoid quinones ubiquinone and menaquinone. {ECO:0000269|PubMed:8037730}.

## Biological Role

Component of all-trans-octaprenyl-diphosphate synthase (complex.ecocyc.CPLX0-7426).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Supplies octaprenyl diphosphate, the precursor for the side chain of the isoprenoid quinones ubiquinone and menaquinone. {ECO:0000269|PubMed:8037730}.

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7426|complex.ecocyc.CPLX0-7426]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3187|gene.b3187]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD57`
- `KEGG:ecj:JW3154;eco:b3187;ecoc:C3026_17350;`
- `GeneID:89518030;93778794;947364;`
- `GO:GO:0004659; GO:0005829; GO:0006744; GO:0008299; GO:0016094; GO:0042802; GO:0042803; GO:0046872; GO:0106350`
- `EC:2.5.1.90`

## Notes

Octaprenyl diphosphate synthase (EC 2.5.1.90) (All-trans-octaprenyl-diphosphate synthase) (Octaprenyl pyrophosphate synthase) (OPP synthase)
