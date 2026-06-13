---
entity_id: "protein.P27248"
entity_type: "protein"
name: "gcvT"
source_database: "UniProt"
source_id: "P27248"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gcvT b2905 JW2873"
---

# gcvT

`protein.P27248`

## Static

- Type: `protein`
- Source: `UniProt:P27248`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. {ECO:0000255|HAMAP-Rule:MF_00259, ECO:0000269|PubMed:8375392}. Together with GcvH, GcvP and E3 (Lpd), GvcT forms a loosely associated complex known as the glycine cleavage system. GvcT, also known as the T-protein, catalyzes the release of ammonia from the intermediate attached to the H-protein and the synthesis of methylenetetrahydrofolate in the presence of tetrahydrofolate . Residues involved in binding of folate have been identified by crosslinking and site-directed mutagenesis . The N-terminal region of GvcT is important for the proper conformation of GvcT, allowing interaction with the H-protein . Glycine cleavage system mutations cause a defect in utilization of glycine to form serine . Expression of the glycine cleavage enzyme system is induced by glycine , and the transcriptional regulation of the gcvTHP operon has been studied extensively. Review: Module 3.6.1.2

## Biological Role

Catalyzes [protein]-S8-aminomethyldihydrolipoyllysine:tetrahydrofolate aminomethyltransferase (ammonia-forming) (reaction.R04125), GCVT-RXN (reaction.ecocyc.GCVT-RXN). Component of glycine cleavage system (complex.ecocyc.GCVMULTI-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. {ECO:0000255|HAMAP-Rule:MF_00259, ECO:0000269|PubMed:8375392}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04125|reaction.R04125]] `KEGG` `database` - via EC:2.1.2.10
- `catalyzes` --> [[reaction.ecocyc.GCVT-RXN|reaction.ecocyc.GCVT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.GCVMULTI-CPLX|complex.ecocyc.GCVMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2905|gene.b2905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27248`
- `KEGG:ecj:JW2873;eco:b2905;ecoc:C3026_15925;`
- `GeneID:75205258;947390;`
- `GO:GO:0004047; GO:0005829; GO:0005960; GO:0006730; GO:0008483; GO:0019464`
- `EC:2.1.2.10`

## Notes

Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein)
