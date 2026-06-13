---
entity_id: "protein.P16687"
entity_type: "protein"
name: "phnI"
source_database: "UniProt"
source_id: "P16687"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnI b4099 JW4060"
---

# phnI

`protein.P16687`

## Static

- Type: `protein`
- Source: `UniProt:P16687`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Together with PhnG, PhnH and PhnL is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. PhnI alone has nucleosidase activity, catalyzing the hydrolysis of ATP or GTP forming alpha-D-ribose 5-triphosphate and adenine or guanine, respectively. {ECO:0000269|PubMed:22089136}. The phnI gene is part of a 14-gene phnCDEFGHIJKLMNOP operon that is involved in phosphonate uptake and metabolism and is a member of the phosphate regulon . A phnI mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation . The PhnI protein alone has nucleosidase activity, producing D-ribose-5-triphosphate and the free base from GTP and ATP. However, in a mixture together with PhnG, PhnH and PhnL it catalyzes the nucleophilic attack of CPD0-1068 on the anomeric carbon of ATP to form adenine and CPD0-2479 . Immucillin-A triphosphate mimics the transition state structure for the nucleosidase reaction and inhibits PhnI activity . PhnI is a component of the CPLX0-10309 .

## Biological Role

Catalyzes RXN-17954 (reaction.ecocyc.RXN-17954), RXN0-6732 (reaction.ecocyc.RXN0-6732). Component of carbon-phosphorus lyase core complex (complex.ecocyc.CPLX0-10309), carbon-phosphorus lyase core complex (complex.ecocyc.CPLX0-7935), carbon-phosphorus lyase system (complex.ecocyc.CPLX0-7958).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Together with PhnG, PhnH and PhnL is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. PhnI alone has nucleosidase activity, catalyzing the hydrolysis of ATP or GTP forming alpha-D-ribose 5-triphosphate and adenine or guanine, respectively. {ECO:0000269|PubMed:22089136}.

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN-17954|reaction.ecocyc.RXN-17954]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6732|reaction.ecocyc.RXN0-6732]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-10309|complex.ecocyc.CPLX0-10309]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7935|complex.ecocyc.CPLX0-7935]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7958|complex.ecocyc.CPLX0-7958]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4099|gene.b4099]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16687`
- `KEGG:ecj:JW4060;eco:b4099;ecoc:C3026_22155;`
- `GeneID:948605;`
- `GO:GO:0015716; GO:0019634; GO:0019700; GO:0061693; GO:0061694; GO:1904176`
- `EC:2.7.8.37`

## Notes

Alpha-D-ribose 1-methylphosphonate 5-triphosphate synthase subunit PhnI (RPnTP synthase subunit PhnI) (EC 2.7.8.37) (Ribose 1-methylphosphonate 5-triphosphate synthase nucleosidase subunit)
