---
entity_id: "protein.P0AEN1"
entity_type: "protein"
name: "fre"
source_database: "UniProt"
source_id: "P0AEN1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fre fadI flrD fsrC ubiB b3844 JW3820"
---

# fre

`protein.P0AEN1`

## Static

- Type: `protein`
- Source: `UniProt:P0AEN1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of soluble flavins by reduced pyridine nucleotides. {ECO:0000250|UniProtKB:Q9L6L9}. Flavin reductase (Fre) catalyzes the reduction of free flavins (riboflavin, FMN, or FAD) by NADPH or NADH . The enzyme appears to be an important physiological source of superoxide radicals . The enzyme follows a sequential ordered reaction mechanism, with binding of NADPH followed by flavin binding . After both NADPH and riboflavin are bound, a charge-transfer complex of NADPH and riboflavin is formed as the first intermediate, followed by a second charge-transfer intermediate of enzyme-bound NADP+ and reduced riboflavin . The enzyme is A-side-specific, selectively transfering the pro-R hydrogen from the C-4 position of the nicotinamide group . Flavin reductase utilizes flavins only as substrates, not as cofactors. The interaction of the enzyme with its flavin substrates has been studied . FAD appears to interact with Fre at a site overlapping with the NAD(P)H-binding site, binding more tightly than either FMN or riboflavin. In the presence of both FMN and FAD, Fre preferentially reduces FAD; FAD thereby inhibits Fre activity at low NADH concentrations...

## Biological Role

Catalyzes FMNREDUCT-RXN (reaction.ecocyc.FMNREDUCT-RXN), NADPH-DEHYDROGENASE-FLAVIN-RXN (reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN), RXN-12445 (reaction.ecocyc.RXN-12445), RXN-8506 (reaction.ecocyc.RXN-8506).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of soluble flavins by reduced pyridine nucleotides. {ECO:0000250|UniProtKB:Q9L6L9}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.FMNREDUCT-RXN|reaction.ecocyc.FMNREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN|reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12445|reaction.ecocyc.RXN-12445]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8506|reaction.ecocyc.RXN-8506]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3844|gene.b3844]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEN1`
- `KEGG:ecj:JW3820;eco:b3844;ecoc:C3026_20785;`
- `GeneID:93778093;948325;`
- `GO:GO:0005829; GO:0006826; GO:0006979; GO:0008047; GO:0016491; GO:0030091; GO:0042602; GO:0052875`
- `EC:1.5.1.41`

## Notes

NAD(P)H-flavin reductase (EC 1.5.1.41) (FMN reductase) (Ferrisiderophore reductase C) (NAD(P)H:flavin oxidoreductase) (Riboflavin reductase [NAD(P)H])
