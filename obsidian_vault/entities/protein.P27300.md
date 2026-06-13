---
entity_id: "protein.P27300"
entity_type: "protein"
name: "lpxK"
source_database: "UniProt"
source_id: "P27300"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxK ycaH b0915 JW0898"
---

# lpxK

`protein.P27300`

## Static

- Type: `protein`
- Source: `UniProt:P27300`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transfers the gamma-phosphate of ATP to the 4'-position of a tetraacyldisaccharide 1-phosphate intermediate (termed DS-1-P) to form tetraacyldisaccharide 1,4'-bis-phosphate (lipid IVA). {ECO:0000269|PubMed:9268317, ECO:0000269|PubMed:9575203}. Tetraacyldisaccharide 4'-kinase (LpxK) catalyzes the sixth step in lipid A biosynthesis. LpxK transfers a phosphate from ATP to the 4' position of a tetraacyldisaccharide1-phosphate intermediate to form tetraacyldisaccharide 1,4'-bis-phosphate (lipid IVA). The reaction requires Mg2+ and is stimulated by phospholipids. Though it can function with all nucleotide triphosphates, the enzymatic reaction is most efficient with ATP . LpxK is an integral membrane protein, which contains predicted membrane-spanning segments at its N-terminus. Most of the LpxK sedimented with the membrane pellet rather than the cell free extract. lpxK is an essential gene, which cotranscribes with msbA . msbA is also an essential gene which codes for a transport protein that brings lipid A from the inner membrane to the outer membrane . LpxK from Aquifex aeolicus has been characterized. The crystal structure of LpxK from Aquifex aeolicus shows an N-terminal domain that is responsible for catalysis at the P-loop and positioning of the disaccharide-1-phosphate substrate for phosphoryl transfer on the inner membrane...

## Biological Role

Catalyzes ATP:2,3,2',3'-tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-beta-D-1,6-glucosaminyl-alpha-phosphate 4-O'-phosphotransferase (reaction.R04657), TETRAACYLDISACC4KIN-RXN (reaction.ecocyc.TETRAACYLDISACC4KIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Transfers the gamma-phosphate of ATP to the 4'-position of a tetraacyldisaccharide 1-phosphate intermediate (termed DS-1-P) to form tetraacyldisaccharide 1,4'-bis-phosphate (lipid IVA). {ECO:0000269|PubMed:9268317, ECO:0000269|PubMed:9575203}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04657|reaction.R04657]] `KEGG` `database` - via EC:2.7.1.130
- `catalyzes` --> [[reaction.ecocyc.TETRAACYLDISACC4KIN-RXN|reaction.ecocyc.TETRAACYLDISACC4KIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0915|gene.b0915]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27300`
- `KEGG:ecj:JW0898;eco:b0915;`
- `GeneID:945526;`
- `GO:GO:0005524; GO:0005886; GO:0009029; GO:0009244; GO:0009245; GO:0016020; GO:0016301`
- `EC:2.7.1.130`

## Notes

Tetraacyldisaccharide 4'-kinase (EC 2.7.1.130) (Lipid A 4'-kinase)
