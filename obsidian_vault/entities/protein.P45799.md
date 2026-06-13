---
entity_id: "protein.P45799"
entity_type: "protein"
name: "nudE"
source_database: "UniProt"
source_id: "P45799"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudE yrfE b3397 JW3360"
---

# nudE

`protein.P45799`

## Static

- Type: `protein`
- Source: `UniProt:P45799`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Active on adenosine(5')triphospho(5')adenosine (Ap3A), ADP-ribose, NADH, adenosine(5')diphospho(5')adenosine (Ap2A). NudE belongs to the family of Nudix hydrolases . The enzyme is specific for nucleoside pyrophosphates with an ADP moiety; preferred substrates of NudE include adenosine(5')triphospho(5')adenosine (Ap3A), ADP-ribose, and NADH . Gel filtration experiments suggest that the enzyme is a dimer in solution . A crystal structure has been solved at 2.32 Å resolution . An mrcA nudE yrfF triple mutant exhibits phenotypes including mucoidy, heat sensitivity, growth defects, and resistance to phage or antibiotic drugs, whereas a single mrcA mutant does not . Expression of nudE may be regulated by ArcA . Review:

## Biological Role

Component of ADP-sugar diphosphatase NudE (complex.ecocyc.CPLX0-1221).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Active on adenosine(5')triphospho(5')adenosine (Ap3A), ADP-ribose, NADH, adenosine(5')diphospho(5')adenosine (Ap2A).

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1221|complex.ecocyc.CPLX0-1221]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3397|gene.b3397]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45799`
- `KEGG:ecj:JW3360;eco:b3397;ecoc:C3026_18430;`
- `GeneID:75206335;947906;`
- `GO:GO:0000287; GO:0005829; GO:0006753; GO:0019144; GO:0019693; GO:0042803; GO:0047631`
- `EC:3.6.1.-`

## Notes

ADP compounds hydrolase NudE (EC 3.6.1.-)
