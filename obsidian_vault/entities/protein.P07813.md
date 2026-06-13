---
entity_id: "protein.P07813"
entity_type: "protein"
name: "leuS"
source_database: "UniProt"
source_id: "P07813"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "leuS b0642 JW0637"
---

# leuS

`protein.P07813`

## Static

- Type: `protein`
- Source: `UniProt:P07813`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Leucine--tRNA ligase (EC 6.1.1.4) (Leucyl-tRNA synthetase) (LeuRS) Leucine-tRNA ligase (LeuRS) is a member of the family of aminoacyl tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. LeuRS belongs to the Class IB aminoacyl tRNA synthetases; apart from sequence motifs within the active site, the different enzymes show little similarity in their primary amino acid sequences . Correct aminoacylation by LeuRS requires both an activation and an editing function . The CCA acceptor end of tRNALeu is essential for both the aminoacylation and editing reaction . Measurement of kinetic parameters for both reactions showed that the rate-limiting step for posttransfer editing is product release, and that its active site functions by kinetic partitioning between hydrolysis and dissociation of misacylated tRNA . LeuRS shows high initial substrate discrimination and appears to correct mistakes by posttransfer editing alone . LeuRS editing defects are lethal to the cell . The CP1 (connective polypeptide 1) domain, which splits the nucleotide binding fold , is required for the posttransfer editing function...

## Biological Role

Catalyzes LEUCINE--TRNA-LIGASE-RXN (reaction.ecocyc.LEUCINE--TRNA-LIGASE-RXN), RXN-23951 (reaction.ecocyc.RXN-23951), RXN-23952 (reaction.ecocyc.RXN-23952).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

Leucine--tRNA ligase (EC 6.1.1.4) (Leucyl-tRNA synthetase) (LeuRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.LEUCINE--TRNA-LIGASE-RXN|reaction.ecocyc.LEUCINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23951|reaction.ecocyc.RXN-23951]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23952|reaction.ecocyc.RXN-23952]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0642|gene.b0642]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07813`
- `KEGG:ecj:JW0637;eco:b0642;ecoc:C3026_03210;`
- `GeneID:947497;`
- `GO:GO:0002161; GO:0004823; GO:0005524; GO:0005829; GO:0006429`
- `EC:6.1.1.4`

## Notes

Leucine--tRNA ligase (EC 6.1.1.4) (Leucyl-tRNA synthetase) (LeuRS)
