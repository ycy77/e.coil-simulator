---
entity_id: "protein.P0A6D7"
entity_type: "protein"
name: "aroK"
source_database: "UniProt"
source_id: "P0A6D7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroK b3390 JW5947"
---

# aroK

`protein.P0A6D7`

## Static

- Type: `protein`
- Source: `UniProt:P0A6D7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the specific phosphorylation of the 3-hydroxyl group of shikimic acid using ATP as a cosubstrate. {ECO:0000269|PubMed:1309529}. Shikimate kinase catalyzes the fifth step in the ARO-PWY pathway. Chorismate is the common precursor for the biosynthesis of the aromatic amino acids tyrosine, phenylalanine and tryptophan. The existence of two shikimate kinase isozymes was initially suggested because sucrose density gradient centrifugation and column chromatography of cell extracts showed two peaks of shikimate kinase activity. Although shikimate kinase 1 (AroK, described here) has not been assayed in pure form, mention that AroK has an approximately 100-fold lower affinity for shikimate than AROL-MONOMER (AroL). A fortuituously obtained L133P mutant of AroK appears to have lost shikimate kinase activity . The reportedly high KM value of AroK for shikimate suggested that the enzyme may have a different primary function in the cell . However, using purified AroK, the KM for shikimiate is 400 µM, similar to AroL's KM of 200 µM ; the specific activity of purified AroK is less than a third of that of AroL . Loss of AroK expression, but not loss of its shikimate kinase activity, confers increased resistance to mecillinam...

## Biological Role

Catalyzes SHIKIMATE-KINASE-RXN (reaction.ecocyc.SHIKIMATE-KINASE-RXN).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the specific phosphorylation of the 3-hydroxyl group of shikimic acid using ATP as a cosubstrate. {ECO:0000269|PubMed:1309529}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SHIKIMATE-KINASE-RXN|reaction.ecocyc.SHIKIMATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3390|gene.b3390]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6D7`
- `KEGG:ecj:JW5947;eco:b3390;ecoc:C3026_18395;`
- `GeneID:2847759;86862212;93778608;`
- `GO:GO:0000287; GO:0004765; GO:0005524; GO:0005829; GO:0008652; GO:0009073; GO:0009423; GO:0046677`
- `EC:2.7.1.71`

## Notes

Shikimate kinase 1 (SK 1) (EC 2.7.1.71) (Shikimate kinase I) (SKI)
