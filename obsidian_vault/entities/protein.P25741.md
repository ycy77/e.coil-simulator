---
entity_id: "protein.P25741"
entity_type: "protein"
name: "waaP"
source_database: "UniProt"
source_id: "P25741"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaP rfaP b3630 JW3605"
---

# waaP

`protein.P25741`

## Static

- Type: `protein`
- Source: `UniProt:P25741`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Kinase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (By similarity). Catalyzes the phosphorylation of heptose I (HepI), the first heptose added to the Kdo2-lipid A module (By similarity). {ECO:0000250|UniProtKB:Q9R9D6}. WaaP is a heptose specific lipopolysaccharide (LPS) core kinase; it is required for the addition of phosphate to O-4 of the first heptose residue in the core oligosaccharide of LPS . waaP is highly conserved in E. coli strains with K-12, R1, R2, R3 and R4 core types and between E. coli and Salmonella typhimurium . Non-polar inactivation of waaP in the non K-12 E. coli strain F470 (CPD-21352 "R1 core type") results in hypersensitivity to novobiocin and SDS; the core oligosaccharide of this mutant (which contains functional waaQ and waaY) lacks all phosphoryl substituents and a heptose III residue indicating that WaaP function is a prerequisite for EG11341-MONOMER "WaaQ" and EG11425-MONOMER "WaaY" activity (see also ). Non-polar inactivation of EG11339 "waaG" (encoding LPS glucosyltransferase) in E. coli strain F470 also decreases core phosphorylation suggesting that WaaP activity may be partially dependent on WaaG . Mutants lacking WaaP exhibit a deep rough phenotype but do not have altered outer membrane profiles . Purified WaaP from E...

## Biological Role

Catalyzes RXN-22461 (reaction.ecocyc.RXN-22461), RXN0-5121 (reaction.ecocyc.RXN0-5121). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Kinase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (By similarity). Catalyzes the phosphorylation of heptose I (HepI), the first heptose added to the Kdo2-lipid A module (By similarity). {ECO:0000250|UniProtKB:Q9R9D6}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-22461|reaction.ecocyc.RXN-22461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5121|reaction.ecocyc.RXN0-5121]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3630|gene.b3630]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25741`
- `KEGG:ecj:JW3605;eco:b3630;ecoc:C3026_19675;`
- `GeneID:948150;`
- `GO:GO:0005524; GO:0009244; GO:0016301; GO:0046835`
- `EC:2.7.1.235`

## Notes

Lipopolysaccharide core heptose(I) kinase WaaP (EC 2.7.1.235)
