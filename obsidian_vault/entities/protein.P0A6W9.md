---
entity_id: "protein.P0A6W9"
entity_type: "protein"
name: "gshA"
source_database: "UniProt"
source_id: "P0A6W9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gshA gsh-I b2688 JW2663"
---

# gshA

`protein.P0A6W9`

## Static

- Type: `protein`
- Source: `UniProt:P0A6W9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) gshA was first cloned and sequenced from E. coli B ; the sequence of the E. coli B and K-12 genes are identical. γ-Glutamate-cysteine ligase catalyzes the first of two steps in the pathway for the biosynthesis of GLUTATHIONE, also referred to as GSH for its γ-Glu-Cys-Gly tripeptide structure. The enzyme is feedback-inhibited by glutathione . The enzyme contains two divalent metal ions which play a role in amino acid binding. Substrate specificity depends on whether Mg2+ or Mn2+ is present; Mn2+ broadens the specificity . Transition state analog inhibitors have been used to study substrate recognition . The enzyme can utilize ethylamine as a substrate, thus producing theanine (γ-glutamylethylamide) . Crystal structures of the enzyme from E. coli B (whose wild-type sequence is identical to the K-12 enzyme) have been solved . The structure shows coordination of an inhibitor by three Mg2+ ions, and showing that the binding of cysteine follows an induced-fit model . Although not highly conserved, the cysteine residues C372 and C395 of the intrachain disulfide bond are important for catalytic activity and stability of the enzyme...

## Biological Role

Catalyzes GLUTCYSLIG-RXN (reaction.ecocyc.GLUTCYSLIG-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase)

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTCYSLIG-RXN|reaction.ecocyc.GLUTCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2688|gene.b2688]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6W9`
- `KEGG:ecj:JW2663;eco:b2688;ecoc:C3026_14800;`
- `GeneID:944881;`
- `GO:GO:0004357; GO:0005524; GO:0005829; GO:0006750; GO:0006972; GO:0046872; GO:0071243; GO:0071288`
- `EC:6.3.2.2`

## Notes

Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase)
