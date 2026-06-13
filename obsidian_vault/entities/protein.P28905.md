---
entity_id: "protein.P28905"
entity_type: "protein"
name: "holC"
source_database: "UniProt"
source_id: "P28905"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "holC b4259 JW4216"
---

# holC

`protein.P28905`

## Static

- Type: `protein`
- Source: `UniProt:P28905`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity. Genetically identified as involved in the repair of replication forks and tolerance of the chain-terminating nucleoside analog 3' AZT (PubMed:26544712, PubMed:33582602, PubMed:34181484). This subunit may stabilize YoaA and/or stimulate the helicase activity of YoaA (PubMed:36509145). {ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:26544712, ECO:0000269|PubMed:33582602, ECO:0000269|PubMed:34181484, ECO:0000269|PubMed:36509145}. HolC is the χ subunit of the χ-ψ dimer. χ has more recently been found to form a complex with G6992-MONOMER in vitro. The YoaA-χ dimer has DNA-dependent helicase activity and requires a 5' single-stranded overhang or ssDNA gap for DNA unwinding; YoaA-χ unwinds DNA with a 5' flap and various types of damaged DNA (see ). CPLX0-8165 SSB interacts with YoaA-χ and affects the helicase activity of YoaA-χ in a substrate-dependent manner; YoaA-χ may pull SSB along while it translocates on DNA .

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379). Component of replisome (complex.ecocyc.CPLX0-13320), DNA polymerase III, clamp-loader complex (complex.ecocyc.CPLX0-3801), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803), DNA polymerase III, ψ-χ dimer (complex.ecocyc.CPLX0-7910).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity. Genetically identified as involved in the repair of replication forks and tolerance of the chain-terminating nucleoside analog 3' AZT (PubMed:26544712, PubMed:33582602, PubMed:34181484). This subunit may stabilize YoaA and/or stimulate the helicase activity of YoaA (PubMed:36509145). {ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:26544712, ECO:0000269|PubMed:33582602, ECO:0000269|PubMed:34181484, ECO:0000269|PubMed:36509145}.

## Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - via EC:2.7.7.7
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-3801|complex.ecocyc.CPLX0-3801]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-7910|complex.ecocyc.CPLX0-7910]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4259|gene.b4259]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28905`
- `KEGG:ecj:JW4216;eco:b4259;ecoc:C3026_22975;`
- `GeneID:948787;`
- `GO:GO:0003677; GO:0003887; GO:0006260; GO:0006261; GO:0009314; GO:0009360; GO:0030894; GO:0032298; GO:0043846`
- `EC:2.7.7.7`

## Notes

DNA polymerase III subunit chi (EC 2.7.7.7) (Accessory clamp loader complex subunit chi) (Replication clamp loader subunit HolC)
