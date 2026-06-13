---
entity_id: "protein.P77215"
entity_type: "protein"
name: "rhmD"
source_database: "UniProt"
source_id: "P77215"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhmD yfaW b2247 JW2241"
---

# rhmD

`protein.P77215`

## Static

- Type: `protein`
- Source: `UniProt:P77215`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of L-rhamnonate to 2-keto-3-deoxy-L-rhamnonate (KDR). Can also dehydrate L-lyxonate, L-mannonate and D-gulonate, although less efficiently, but not 2-keto-4-hydroxyheptane-1,7-dioate. {ECO:0000269|PubMed:18754693}. YfaW is a L-rhamnonate dehydratase (RhamD) with promiscuous substrate specificity . RhamD is a member of the mandelate racemase (MR) subgroup of the enolase superfamily. A crystal structure has been solved at 2.1 Å resolution, where the enzyme is a tetramer of dimers. Although the enzyme is also an octamer in solution, based on the location of the active site, the minimum functional unit appears to be the monomer. A reaction mechanism and likely catalytic residues have been proposed, and site-directed mutants were assayed to confirm lack of activity .

## Biological Role

Catalyzes L-rhamnonate hydro-lyase (reaction.R03774). Component of L-rhamnonate dehydratase (complex.ecocyc.CPLX0-7722).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of L-rhamnonate to 2-keto-3-deoxy-L-rhamnonate (KDR). Can also dehydrate L-lyxonate, L-mannonate and D-gulonate, although less efficiently, but not 2-keto-4-hydroxyheptane-1,7-dioate. {ECO:0000269|PubMed:18754693}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03774|reaction.R03774]] `KEGG` `database` - via EC:4.2.1.90
- `is_component_of` --> [[complex.ecocyc.CPLX0-7722|complex.ecocyc.CPLX0-7722]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b2247|gene.b2247]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77215`
- `KEGG:ecj:JW2241;eco:b2247;ecoc:C3026_12555;`
- `GeneID:945881;`
- `GO:GO:0000287; GO:0009063; GO:0016052; GO:0016836; GO:0042802; GO:0050032`
- `EC:4.2.1.90`

## Notes

L-rhamnonate dehydratase (RhamD) (EC 4.2.1.90)
