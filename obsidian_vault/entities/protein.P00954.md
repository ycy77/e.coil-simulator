---
entity_id: "protein.P00954"
entity_type: "protein"
name: "trpS"
source_database: "UniProt"
source_id: "P00954"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00140}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trpS b3384 JW3347"
---

# trpS

`protein.P00954`

## Static

- Type: `protein`
- Source: `UniProt:P00954`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00140}.

## Enriched Summary

FUNCTION: Catalyzes the attachment of tryptophan to tRNA(Trp). Amino acylates tRNA(Trp) with both L- and D-tryptophan, although D-tryptophan is a poor substrate (PubMed:10918062). {ECO:0000255|HAMAP-Rule:MF_00140, ECO:0000269|PubMed:10918062}. Tryptophan-tRNA ligase (TrpRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. TrpRS belongs to the Class I aminoacyl tRNA synthetases . The enzyme purified from E. coli B is a homodimer in solution . The dimer has two binding sites for both tryptophan and tRNATrp . Specificity determinants within tRNATrp that are important for recognition by TrpRS have been identified. The anticodon and the G73 discriminator base are the major identity determinants , and C35 is recognized as well . The apparent affinity of TrpRS for tryptophan appears to be dependent on the tRNA . The identity of tRNATrp predominantly affects the rate of transfer of tryptophan from the TrpRS-tryptophanyl adenylate to the tRNA . TrpRS also aminoacylates tRNATrp with D-tryptophan; the resulting D-Trp-tRNATrp can be hydrolyzed by EC-3.1.1.96 . A strain that can incorporate 4-fluorotryptophan in place of tryptophan into proteins has been isolated and contains, among others, mutations in TrpRS...

## Biological Role

Catalyzes L-tryptophan -tRNA(Trp) ligase (AMP-forming) (reaction.R03664). Component of tryptophan—tRNA ligase (complex.ecocyc.TRPS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of tryptophan to tRNA(Trp). Amino acylates tRNA(Trp) with both L- and D-tryptophan, although D-tryptophan is a poor substrate (PubMed:10918062). {ECO:0000255|HAMAP-Rule:MF_00140, ECO:0000269|PubMed:10918062}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03664|reaction.R03664]] `KEGG` `database` - via EC:6.1.1.2
- `is_component_of` --> [[complex.ecocyc.TRPS-CPLX|complex.ecocyc.TRPS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3384|gene.b3384]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00954`
- `KEGG:ecj:JW3347;eco:b3384;ecoc:C3026_18365;`
- `GeneID:947894;`
- `GO:GO:0004830; GO:0005524; GO:0005829; GO:0006436`
- `EC:6.1.1.2`

## Notes

Tryptophan--tRNA ligase (EC 6.1.1.2) (Tryptophanyl-tRNA synthetase) (TrpRS)
