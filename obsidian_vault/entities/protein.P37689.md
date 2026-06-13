---
entity_id: "protein.P37689"
entity_type: "protein"
name: "gpmI"
source_database: "UniProt"
source_id: "P37689"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gpmI pgmI yibO b3612 JW3587"
---

# gpmI

`protein.P37689`

## Static

- Type: `protein`
- Source: `UniProt:P37689`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the interconversion of 2-phosphoglycerate (2-PGA) and 3-phosphoglycerate (3-PGA). {ECO:0000269|PubMed:10437801}. E. coli contains both a 2,3-bisphosphoglyerate-dependent phosphoglycerate mutase (dPGM, GpmA) and this cofactor-independent phosphoglycerate mutase (PGMI-MONOMER GpmM, also called iPGM). The GpmM enzyme has significantly lower specific activity . Differential inhibition by vanadate allowed independent measurement of both enzymes during the E. coli growth cycle . A gpmM deletion strain does not have a growth defect under the conditions tested, while a gpmA gpmM double mutant strain does not appear to be viable. The growth phenotype of a gpmA mutant can be rescued by expression of gpmM from a medium-copy plasmid . gpmM shows differential codon adaptation, resulting in differential translation efficiency signatures in aerotolerant compared to obligate anaerobic microbes. It was therefore predicted to play a role in the oxidative stress response. A gpmM deletion mutant was shown to be more sensitive than wild-type specifically to hydrogen peroxide exposure, but not other stresses . Using a method that distinguishes N-phosphorylation from O-phosphorylation, N-phosphorylation was detected in vitro...

## Biological Role

Catalyzes D-phosphoglycerate 2,3-phosphomutase (reaction.R01518), 3PGAREARR-RXN (reaction.ecocyc.3PGAREARR-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion of 2-phosphoglycerate (2-PGA) and 3-phosphoglycerate (3-PGA). {ECO:0000269|PubMed:10437801}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01518|reaction.R01518]] `KEGG` `database` - via EC:5.4.2.12
- `catalyzes` --> [[reaction.ecocyc.3PGAREARR-RXN|reaction.ecocyc.3PGAREARR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3612|gene.b3612]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37689`
- `KEGG:ecj:JW3587;eco:b3612;ecoc:C3026_19585;`
- `GeneID:948130;`
- `GO:GO:0004619; GO:0005737; GO:0005829; GO:0005975; GO:0006007; GO:0006096; GO:0006979; GO:0030145`
- `EC:5.4.2.12`

## Notes

2,3-bisphosphoglycerate-independent phosphoglycerate mutase (BPG-independent PGAM) (Phosphoglyceromutase) (iPGM) (EC 5.4.2.12)
