---
entity_id: "protein.P0A8L1"
entity_type: "protein"
name: "serS"
source_database: "UniProt"
source_id: "P0A8L1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "serS b0893 JW0876"
---

# serS

`protein.P0A8L1`

## Static

- Type: `protein`
- Source: `UniProt:P0A8L1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the attachment of serine to tRNA(Ser) (PubMed:7537870). Is also able to aminoacylate tRNA(Sec) with serine, to form the misacylated tRNA L-seryl-tRNA(Sec), which will be further converted into selenocysteinyl-tRNA(Sec). {ECO:0000269|PubMed:2963963, ECO:0000269|PubMed:7537870, ECO:0000269|PubMed:8065908}. Serine-tRNA ligase (SerRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. SerRS belongs to the Class II aminoacyl tRNA synthetases, which share three regions of homology . SerRS is a dimer in solution . Specificity determinants within tRNASer that are important for recognition by SerRS have been identified . SerRS also aminoacylates a special tRNA, tRNASec, with serine . The charging efficiency for tRNASec is approximately 1% of that for tRNASer . The serine residue of Ser-tRNASec is subsequently converted to selenocysteine by CPLX0-1141. tRNASec recognizes the stop codon UGA. SerRS lacks an editing domain, but pre-transfer editing (hydrolysis) of non-cognate aminoacyl adenylate intermediates may proceed within the enzyme active site itself...

## Biological Role

Catalyzes L-serine:tRNA(Ser) ligase (AMP-forming) (reaction.R03662), L-serine:tRNASec ligase (AMP-forming) (reaction.R08218). Component of serine—tRNA ligase (complex.ecocyc.SERS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of serine to tRNA(Ser) (PubMed:7537870). Is also able to aminoacylate tRNA(Sec) with serine, to form the misacylated tRNA L-seryl-tRNA(Sec), which will be further converted into selenocysteinyl-tRNA(Sec). {ECO:0000269|PubMed:2963963, ECO:0000269|PubMed:7537870, ECO:0000269|PubMed:8065908}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R03662|reaction.R03662]] `KEGG` `database` - via EC:6.1.1.11
- `catalyzes` --> [[reaction.R08218|reaction.R08218]] `KEGG` `database` - via EC:6.1.1.11
- `is_component_of` --> [[complex.ecocyc.SERS-CPLX|complex.ecocyc.SERS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0893|gene.b0893]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8L1`
- `KEGG:ecj:JW0876;eco:b0893;ecoc:C3026_05525;`
- `GeneID:86863415;93776527;945506;`
- `GO:GO:0000287; GO:0004828; GO:0005524; GO:0005829; GO:0006434; GO:0016260; GO:0042802`
- `EC:6.1.1.11`

## Notes

Serine--tRNA ligase (EC 6.1.1.11) (Seryl-tRNA synthetase) (SerRS) (Seryl-tRNA(Ser/Sec) synthetase)
