---
entity_id: "protein.P0A6T9"
entity_type: "protein"
name: "gcvH"
source_database: "UniProt"
source_id: "P0A6T9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gcvH b2904 JW2872"
---

# gcvH

`protein.P0A6T9`

## Static

- Type: `protein`
- Source: `UniProt:P0A6T9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. The H protein shuttles the methylamine group of glycine from the P protein to the T protein. {ECO:0000255|HAMAP-Rule:MF_00272, ECO:0000269|PubMed:8375392}. The H-protein, coded for by the gcvH gene, is a lipoylprotein that is reduced as it shuttles the methylamine group of glycine from the P-protein to the T-protein and is reoxidized by the dihydrolipoamide dehydrogenase. GcvH functions as a substrate for the three enzymes of the gcv complex. Residues 61-65 are predicted to contain the lipoyl modification (on lysine), based on conservation of these residues and their correspondence to the lipoate attachment site of the Pisum sativum protein . The interaction between GcvH and GcvT has been examined . Interaction between the two proteins may be necessary to form the folate binding site, in which the folate polyglutamyl region binds, exposing the pteridine ring . The GcvT N terminus is important for interaction with GcvH, probably by mediating a conformational change, and residue D43 of GcvH is proximal to GcvT in the GcvH-GcvT complex . Glycine cleavage system (gcv) mutations cause a defect in utilization of glycine to form serine . Purification and overproduction of the enzymes of the glycine cleavage system have been described . Regulation has been described . Review: .

## Biological Role

Component of glycine cleavage system (complex.ecocyc.GCVMULTI-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. The H protein shuttles the methylamine group of glycine from the P protein to the T protein. {ECO:0000255|HAMAP-Rule:MF_00272, ECO:0000269|PubMed:8375392}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GCVMULTI-CPLX|complex.ecocyc.GCVMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2904|gene.b2904]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6T9`
- `KEGG:ecj:JW2872;eco:b2904;ecoc:C3026_15920;`
- `GeneID:93779098;947393;`
- `GO:GO:0005737; GO:0005829; GO:0005960; GO:0006730; GO:0019464`

## Notes

Glycine cleavage system H protein
