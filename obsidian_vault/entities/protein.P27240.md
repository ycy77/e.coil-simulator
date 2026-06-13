---
entity_id: "protein.P27240"
entity_type: "protein"
name: "waaY"
source_database: "UniProt"
source_id: "P27240"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaY rfaY b3625 JW3600"
---

# waaY

`protein.P27240`

## Static

- Type: `protein`
- Source: `UniProt:P27240`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Kinase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS). Catalyzes the phosphorylation of the second heptose unit (HepII) of the inner core. {ECO:0000250|UniProtKB:Q9ZIS7}. WaaY is a heptose specific lipopolysaccharide (LPS) core kinase which catalyses phosphorylation of the second heptose residue in the inner core of LPS . Non-polar inactivation of waaY in the non K-12 E. coli strain F470 (CPD-21352 "R1 core type") results in a minor increase in sensitivity to novobiocin and SDS and the core oligosaccharide of this mutant is not phosphorylated on heptose II . WaaY activity is dependent on prior WaaP, WaaQ (and possibly WaaG ) function; the core oligosaccharide of both waaP and waaQ mutants does not have a phosphoryl substituent on heptose II despite the presence of functional waaY . Inactivation of waaY produces a phenotype of decreased susceptibility to the human cathelicidin antimicrobial peptide (LL-37); reduced peptide binding to the cell surface and a diminished capacity to compromise the inner membrane were observed . In Salmonella typhimurium LT2 a screen for resistance to the antimicrobial peptides LL-37, CNY100HL and wheat germ histones yielded a waaY mutant among others . The chromosomal waa region (formerly rfa) contains the major core-oligosaccharide assembly operons in E. coli...

## Biological Role

Catalyzes RXN0-5123 (reaction.ecocyc.RXN0-5123).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Kinase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS). Catalyzes the phosphorylation of the second heptose unit (HepII) of the inner core. {ECO:0000250|UniProtKB:Q9ZIS7}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5123|reaction.ecocyc.RXN0-5123]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3625|gene.b3625]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27240`
- `KEGG:ecj:JW3600;eco:b3625;ecoc:C3026_19650;`
- `GeneID:948145;`
- `GO:GO:0005524; GO:0005886; GO:0009244; GO:0016301; GO:0046835`
- `EC:2.7.1.-`

## Notes

Lipopolysaccharide core heptose(II) kinase WaaY (EC 2.7.1.-)
