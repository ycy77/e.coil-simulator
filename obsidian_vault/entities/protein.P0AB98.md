---
entity_id: "protein.P0AB98"
entity_type: "protein"
name: "atpB"
source_database: "UniProt"
source_id: "P0AB98"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01393, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01393, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpB papD uncB b3738 JW3716"
---

# atpB

`protein.P0AB98`

## Static

- Type: `protein`
- Source: `UniProt:P0AB98`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01393, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01393, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Key component of the proton channel; it plays a direct role in the translocation of protons across the membrane. Subunit-a of the Fo complex is an integral membrane protein that plays a critical role in the proton translocation mechanism. Subunit-a is thought to provide aqueous access channels to and from the H+ binding site that is located in the decameric c-ring . Subunit-a contains 5 transmembrane helices (TMH); the amino terminus is located in the periplasm and the carboxy terminus is located in the cytoplasm . Mutational and cross-linking studies indicate that transmembrane helices 2,3,4 and 5 form a four helix bundle that interacts with subunit c. pH-dependent conformational change of helices 4 and 5 has been implicated in the gating of H+ . Structural divergence of the c-subunit ring and the a-subunits between bacterial species may allow development of species specific drugs which target these subunits . Reviews:

## Biological Role

Component of ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX), ATP synthase Fo complex (complex.ecocyc.F-O-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Key component of the proton channel; it plays a direct role in the translocation of protons across the membrane.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.F-O-CPLX|complex.ecocyc.F-O-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3738|gene.b3738]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB98`
- `KEGG:ecj:JW3716;eco:b3738;ecoc:C3026_20255;`
- `GeneID:93778229;948252;`
- `GO:GO:0005886; GO:0042777; GO:0045259; GO:0046933`

## Notes

ATP synthase subunit a (ATP synthase F0 sector subunit a) (F-ATPase subunit 6)
