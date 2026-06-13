---
entity_id: "protein.P15770"
entity_type: "protein"
name: "aroE"
source_database: "UniProt"
source_id: "P15770"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroE b3281 JW3242"
---

# aroE

`protein.P15770`

## Static

- Type: `protein`
- Source: `UniProt:P15770`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the chorismate, which leads to the biosynthesis of aromatic amino acids. Catalyzes the reversible NADPH linked reduction of 3-dehydroshikimate (DHSA) to yield shikimate (SA). It displays no activity in the presence of NAD. {ECO:0000255|HAMAP-Rule:MF_00222, ECO:0000269|PubMed:12637497, ECO:0000269|PubMed:3883995}. Shikimate dehydrogenase (AroE) catalyzes the NADPH-linked reduction of 3-dehydroshikimate to shikimate . The reaction is part of the ARO-PWY pathway, which provides the common precursor for the biosynthesis of aromatic amino acids, folate, quinones and enterochelin. Phylogenomic analysis of the shikimate dehydrogenase family showed that the two enzymes encoded in E. coli, AroE and CPLX0-7462 YdiB, belong to different subclasses; the authors suggested that YdiB was acquired by horizontal gene transfer. Common and subclass-specific catalytic residues and substrate binding motifs were identified . AroE is NADP+-specific and has much higher catalytic efficiency than YdiB, which has broader substrate specificity and can use either NADP+ or NAD+ as a co-substrate . Mutant data and the results from metabolic engineering experiments strongly suggest that YdiB is unable to replace AroE under normal physiological conditions. AroE transfers hydrogen stereospecifically from the A-side of NADPH...

## Biological Role

Catalyzes SHIKIMATE-5-DEHYDROGENASE-RXN (reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the chorismate, which leads to the biosynthesis of aromatic amino acids. Catalyzes the reversible NADPH linked reduction of 3-dehydroshikimate (DHSA) to yield shikimate (SA). It displays no activity in the presence of NAD. {ECO:0000255|HAMAP-Rule:MF_00222, ECO:0000269|PubMed:12637497, ECO:0000269|PubMed:3883995}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3281|gene.b3281]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15770`
- `KEGG:ecj:JW3242;eco:b3281;ecoc:C3026_17845;`
- `GeneID:947776;`
- `GO:GO:0000166; GO:0004764; GO:0005829; GO:0008652; GO:0009073; GO:0009423; GO:0019632; GO:0050661`
- `EC:1.1.1.25`

## Notes

Shikimate dehydrogenase (NADP(+)) (SD) (SDH) (EC 1.1.1.25)
