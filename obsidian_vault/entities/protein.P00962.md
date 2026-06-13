---
entity_id: "protein.P00962"
entity_type: "protein"
name: "glnS"
source_database: "UniProt"
source_id: "P00962"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00126}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnS b0680 JW0666"
---

# glnS

`protein.P00962`

## Static

- Type: `protein`
- Source: `UniProt:P00962`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00126}.

## Enriched Summary

Glutamine--tRNA ligase (EC 6.1.1.18) (Glutaminyl-tRNA synthetase) (GlnRS) Glutamine-tRNA ligase (GlnRS) is a member of the family of aminoacyl tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. GlnRS belongs to the Class I aminoacyl tRNA synthetases ; apart from sequence motifs within the active site, the different enzymes show little similarity in their primary amino acid sequences. Substrate recognition and discrimination by GlnRS has been studied extensively. Binding of tRNA and ATP to GlnRS is cooperative, and transfer of the aminoacyl adenylate to the tRNA is the rate determining step . Interactions between the tRNA identity nucleotides and GlnRS modulate the affinity of the enzyme for glutamine , and the terminal adenosine base of tRNAGln mediates amino acid recognition . tRNA binding to GlnRS results in conformational changes in the active site ; induced-fit changes in the active site structure by both amino acid and tRNA binding may contribute to enzyme specificity . Reports differ on whether the properties of the amino acid binding site allow the enzyme to specifically recognize glutamine and select against glutamate or function as a negative determinant, binding glutamate in a non-productive orientation...

## Biological Role

Catalyzes GLUTAMINE--TRNA-LIGASE-RXN (reaction.ecocyc.GLUTAMINE--TRNA-LIGASE-RXN).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Glutamine--tRNA ligase (EC 6.1.1.18) (Glutaminyl-tRNA synthetase) (GlnRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTAMINE--TRNA-LIGASE-RXN|reaction.ecocyc.GLUTAMINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0680|gene.b0680]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00962`
- `KEGG:ecj:JW0666;eco:b0680;ecoc:C3026_03380;`
- `GeneID:93776805;945310;`
- `GO:GO:0004819; GO:0005524; GO:0005829; GO:0006424; GO:0006425`
- `EC:6.1.1.18`

## Notes

Glutamine--tRNA ligase (EC 6.1.1.18) (Glutaminyl-tRNA synthetase) (GlnRS)
