---
entity_id: "protein.P16686"
entity_type: "protein"
name: "phnH"
source_database: "UniProt"
source_id: "P16686"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnH b4100 JW4061"
---

# phnH

`protein.P16686`

## Static

- Type: `protein`
- Source: `UniProt:P16686`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Together with PhnG, PhnI and PhnL is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. {ECO:0000269|PubMed:22089136}. PhnH, in a mixture together with PhnG, PhnL and PhnI, catalyzes the nucleophilic attack of CPD0-1068 on the anomeric carbon of ATP to form adenine and CPD0-2479 . PhnH was also found to be a component of a protein complex that was thought to function as a carbon-phosphorous lyase . phnH is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . PhnH is essential for C-P bond cleavage . A phnH mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation . A crystal structure of PhnH has been solved at 1.77 Å resolution. The purified protein is a dimer in solution .

## Biological Role

Component of carbon-phosphorus lyase core complex (complex.ecocyc.CPLX0-10309), carbon-phosphorus lyase core complex (complex.ecocyc.CPLX0-7935), carbon-phosphorus lyase system (complex.ecocyc.CPLX0-7958).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Together with PhnG, PhnI and PhnL is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. {ECO:0000269|PubMed:22089136}.

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10309|complex.ecocyc.CPLX0-10309]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7935|complex.ecocyc.CPLX0-7935]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7958|complex.ecocyc.CPLX0-7958]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4100|gene.b4100]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16686`
- `KEGG:ecj:JW4061;eco:b4100;ecoc:C3026_22160;`
- `GeneID:948619;`
- `GO:GO:0015716; GO:0019634; GO:0019700; GO:0042802; GO:0042803; GO:0061693; GO:0061694; GO:1904176`
- `EC:2.7.8.37`

## Notes

Alpha-D-ribose 1-methylphosphonate 5-triphosphate synthase subunit PhnH (RPnTP synthase subunit PhnH) (EC 2.7.8.37)
