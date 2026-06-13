---
entity_id: "protein.P29680"
entity_type: "protein"
name: "hemE"
source_database: "UniProt"
source_id: "P29680"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00218}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemE b3997 JW3961"
---

# hemE

`protein.P29680`

## Static

- Type: `protein`
- Source: `UniProt:P29680`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00218}.

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation of four acetate groups of uroporphyrinogen-III to yield coproporphyrinogen-III. {ECO:0000255|HAMAP-Rule:MF_00218}. Uroporphyrinogen decarboxylase catalyzes the decarboxylation of all four acetate residues of uroporphyrinogen III to generate coproporphyrinogen III. This is the first committed step after the branch point between heme and siroheme biosynthesis. The E. coli enzyme has not been biochemically studied. A hemE mutant accumulates uroporphyrinogen III .

## Biological Role

Catalyzes UROGENDECARBOX-RXN (reaction.ecocyc.UROGENDECARBOX-RXN).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation of four acetate groups of uroporphyrinogen-III to yield coproporphyrinogen-III. {ECO:0000255|HAMAP-Rule:MF_00218}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UROGENDECARBOX-RXN|reaction.ecocyc.UROGENDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3997|gene.b3997]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P29680`
- `KEGG:ecj:JW3961;eco:b3997;ecoc:C3026_21590;`
- `GeneID:86861602;93777897;948497;`
- `GO:GO:0004853; GO:0005829; GO:0006779; GO:0006780; GO:0006783; GO:0006785; GO:0019353`
- `EC:4.1.1.37`

## Notes

Uroporphyrinogen decarboxylase (UPD) (URO-D) (EC 4.1.1.37)
