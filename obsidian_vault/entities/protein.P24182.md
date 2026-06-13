---
entity_id: "protein.P24182"
entity_type: "protein"
name: "accC"
source_database: "UniProt"
source_id: "P24182"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "accC fabG b3256 JW3224"
---

# accC

`protein.P24182`

## Static

- Type: `protein`
- Source: `UniProt:P24182`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is a component of the acetyl coenzyme A carboxylase complex; first, biotin carboxylase catalyzes the carboxylation of the carrier protein and then the transcarboxylase transfers the carboxyl group to form malonyl-CoA. {ECO:0000305|PubMed:16793549, ECO:0000305|PubMed:19213731}. Mutations in the homologous and functionally identical subunit in mammalian proprionyl-CoA carboxylase and 3-methylcrotonyl-CoA carboxylase result in the metabolic deficiency diseases of propionic acidemia or methylcrotonylglycinuria. Kinetic analysis of mutants analogous to the disease-causing mutants has been performed to determine the function of those residues . Studies with dimerization-deficient accC mutants showed that only dimeric biotin carboxylase fulfills its physiological function in vivo .

## Biological Role

Catalyzes acetyl-CoA:carbon-dioxide ligase (ADP-forming) (reaction.R00742). Component of acetyl-CoA carboxylase complex (complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX), biotin carboxylase (complex.ecocyc.BIOTIN-CARBOXYL-CPLX).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

FUNCTION: This protein is a component of the acetyl coenzyme A carboxylase complex; first, biotin carboxylase catalyzes the carboxylation of the carrier protein and then the transcarboxylase transfers the carboxyl group to form malonyl-CoA. {ECO:0000305|PubMed:16793549, ECO:0000305|PubMed:19213731}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00742|reaction.R00742]] `KEGG` `database` - via EC:6.4.1.2
- `is_component_of` --> [[complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.BIOTIN-CARBOXYL-CPLX|complex.ecocyc.BIOTIN-CARBOXYL-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3256|gene.b3256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24182`
- `KEGG:ecj:JW3224;eco:b3256;ecoc:C3026_17715;`
- `GeneID:93778731;947761;`
- `GO:GO:0003989; GO:0004075; GO:0005524; GO:0005737; GO:0005829; GO:0006633; GO:0009317; GO:0042803; GO:0045717; GO:0046872; GO:2001295`
- `EC:6.3.4.14`

## Notes

Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A)
