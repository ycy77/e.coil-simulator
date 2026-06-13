---
entity_id: "protein.P16703"
entity_type: "protein"
name: "cysM"
source_database: "UniProt"
source_id: "P16703"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysM b2421 JW2414"
---

# cysM

`protein.P16703`

## Static

- Type: `protein`
- Source: `UniProt:P16703`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Two cysteine synthase enzymes are found. Both catalyze the same reaction. Cysteine synthase B can also use thiosulfate in place of sulfide to give cysteine thiosulfonate as a product. Cysteine synthase B (CysM) is one of two isozymes in E. coli that catalyze the formation of L-cysteine from O-acetyl-L-serine and sulfide . Unlike cysteine synthase A, cysteine synthase B does not form a complex with serine acetyltransferase . Cysteine synthase B can also use thiosulfate in place of sulfide, producing S-sulfocysteine . The broad substrate specificity of cysteine synthase was exploited for the synthesis of unnatural L-α-amino acids . Initial synthesis rates of nonproteinaceous amino acids have been determined . CysM provides one of the activities that is able to provide sulfur for Fe-S cluster biosynthesis in vitro . CysM is one of at least five enzymes that exhibit cysteine desulfhydrase activity (CD) in E. coli. Deletion of each of the cysM, metC, tnaA, cysK and malY genes individually decreases CD activity Crystal structures of CysM have been solved at 2.1, 2.7 and 1.33 Å resolution . The differing substrate specificities of the two isozymes CysK and CysM could be explained by comparison of the CysM structure to that of CysK from Salmonella Typhimurium . Mutants in predicted active site residues were investigated...

## Biological Role

Catalyzes O-acetyl-L-serine:thiosulfate 2-amino-2-carboxyethyltransferase (reaction.R03132). Component of cysteine synthase B (complex.ecocyc.ACSERLYB-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Two cysteine synthase enzymes are found. Both catalyze the same reaction. Cysteine synthase B can also use thiosulfate in place of sulfide to give cysteine thiosulfonate as a product.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03132|reaction.R03132]] `KEGG` `database` - via EC:2.5.1.144
- `is_component_of` --> [[complex.ecocyc.ACSERLYB-CPLX|complex.ecocyc.ACSERLYB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2421|gene.b2421]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16703`
- `KEGG:ecj:JW2414;eco:b2421;ecoc:C3026_13455;`
- `GeneID:946888;`
- `GO:GO:0004124; GO:0005737; GO:0006535; GO:0016226; GO:0019344; GO:0019345; GO:0019450; GO:0030170; GO:0042803; GO:0080146`
- `EC:2.5.1.47`

## Notes

Cysteine synthase B (CSase B) (EC 2.5.1.47) (O-acetylserine (thiol)-lyase B) (OAS-TL B) (O-acetylserine sulfhydrylase B)
