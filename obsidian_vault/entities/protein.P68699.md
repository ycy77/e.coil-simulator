---
entity_id: "protein.P68699"
entity_type: "protein"
name: "atpE"
source_database: "UniProt"
source_id: "P68699"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpE papH uncE b3737 JW3715"
---

# atpE

`protein.P68699`

## Static

- Type: `protein`
- Source: `UniProt:P68699`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation.; FUNCTION: Key component of the F(0) channel; it plays a direct role in translocation across the membrane. A homomeric c-ring of 10 subunits forms the central stalk rotor element with the F(1) delta and epsilon subunits. The c subunit of the Fo complex of ATP synthase is absolutely required for proton translocation and is also necessary for binding of the F1 complex. The number of subunit c monomers determines the number of transported ions per revolution. The stoichiometry of the subunits has been obtained within the range of 9 to 18 ; the preferred number of c subunits is 10 . Quantitation, cross-linking and reconstitution experiments with wild-type and mutant F0 show that the stoichiometry of subunit-c is independent of its rate of synthesis . This is the subunit affected by the inhibitor dicyclohexylcarbodiimide...

## Biological Role

Component of ATP synthase Fo complex - subunit c (complex.ecocyc.ATPE-CPLX), ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX), ATP synthase Fo complex (complex.ecocyc.F-O-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation.; FUNCTION: Key component of the F(0) channel; it plays a direct role in translocation across the membrane. A homomeric c-ring of 10 subunits forms the central stalk rotor element with the F(1) delta and epsilon subunits.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.ATPE-CPLX|complex.ecocyc.ATPE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10
- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=10 | EcoCyc transporter component coefficient=10
- `is_component_of` --> [[complex.ecocyc.F-O-CPLX|complex.ecocyc.F-O-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b3737|gene.b3737]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68699`
- `KEGG:ecj:JW3715;eco:b3737;ecoc:C3026_20250;`
- `GeneID:948253;99708207;99810414;`
- `GO:GO:0005886; GO:0008289; GO:0015986; GO:0033177; GO:0042777; GO:0045259; GO:0046933; GO:0046961`

## Notes

ATP synthase subunit c (ATP synthase F(0) sector subunit c) (Dicyclohexylcarbodiimide-binding protein) (F-type ATPase subunit c) (F-ATPase subunit c) (Lipid-binding protein)
