---
entity_id: "protein.P0AG07"
entity_type: "protein"
name: "rpe"
source_database: "UniProt"
source_id: "P0AG07"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpe dod yhfD b3386 JW3349"
---

# rpe

`protein.P0AG07`

## Static

- Type: `protein`
- Source: `UniProt:P0AG07`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible epimerization of D-ribulose 5-phosphate to D-xylulose 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_02227, ECO:0000269|PubMed:21402925}. Ribulose-5-phosphate 3-epimerase (Rpe) is an enzyme of the non-oxidative branch of the pentose phosphate pathway. Rpe requires ferrous iron for activity and is vulnerable to damage by H2O2 due to Fenton chemistry. Mn2+, Co2+ and Zn2+ can substitute for Fe2+ to varying degrees, and Rpe containing these alternative cations is not vulnerable to H2O2. Induction of the manganese transporter can protect Rpe from H2O2 damage . An rpe mutant strain does not grow on minimal medium containing either ribose or xylose, but grows when both sugars are present . rpe mutant strains have a growth defect in complex medium and a more severe growth defect in minimal medium containing glycolytic carbon sources or gluconate . A mutation in rpe, drsE30, supresses the temperature-sensitive growth defect of the dnaR130 mutant allele . Review:

## Biological Role

Catalyzes D-ribulose-5-phosphate 3-epimerase (reaction.R01529), RIBULP3EPIM-RXN (reaction.ecocyc.RIBULP3EPIM-RXN). Bound by Fe2+ (molecule.C14818).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible epimerization of D-ribulose 5-phosphate to D-xylulose 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_02227, ECO:0000269|PubMed:21402925}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01529|reaction.R01529]] `KEGG` `database` - via EC:5.1.3.1
- `catalyzes` --> [[reaction.ecocyc.RIBULP3EPIM-RXN|reaction.ecocyc.RIBULP3EPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3386|gene.b3386]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG07`
- `KEGG:ecj:JW3349;eco:b3386;ecoc:C3026_18375;`
- `GeneID:86862216;93778612;947896;`
- `GO:GO:0004750; GO:0005829; GO:0005975; GO:0008198; GO:0009052; GO:0019323; GO:0046872`
- `EC:5.1.3.1`

## Notes

Ribulose-phosphate 3-epimerase (EC 5.1.3.1) (Pentose-5-phosphate 3-epimerase) (PPE) (R5P3E)
