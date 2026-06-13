---
entity_id: "protein.P05719"
entity_type: "protein"
name: "hsdS"
source_database: "UniProt"
source_id: "P05719"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hsdS hss b4348 JW4311"
---

# hsdS

`protein.P05719`

## Static

- Type: `protein`
- Source: `UniProt:P05719`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The specificity (S) subunit of a type I restriction enzyme; this subunit dictates DNA sequence specificity. The M and S subunits together form a methyltransferase (MTase) that methylates A-2 on the top and A-3 on the bottom strand of the sequence 5'-AACN(6)GTGC-3'. In the presence of the R subunit the complex can also act as an endonuclease, binding to the same target sequence but cutting the DNA some distance from this site. Whether the DNA is cut or modified depends on the methylation state of the target sequence. When the target site is unmodified, the DNA is cut. When the target site is hemimethylated, the complex acts as a maintenance MTase modifying the DNA so that both strands become methylated. After locating a non-methylated recognition site, the enzyme complex serves as a molecular motor that translocates DNA in an ATP-dependent manner until a collision occurs that triggers cleavage. {ECO:0000269|PubMed:4868368, ECO:0000269|PubMed:6255295, ECO:0000269|PubMed:8514761, ECO:0000269|PubMed:9033396}. HsdS is the specificity-determining component of the EcoKI restriction-modification system .

## Biological Role

Component of EcoKI restriction-modification system (complex.ecocyc.CPLX0-3958).

## Annotation

FUNCTION: The specificity (S) subunit of a type I restriction enzyme; this subunit dictates DNA sequence specificity. The M and S subunits together form a methyltransferase (MTase) that methylates A-2 on the top and A-3 on the bottom strand of the sequence 5'-AACN(6)GTGC-3'. In the presence of the R subunit the complex can also act as an endonuclease, binding to the same target sequence but cutting the DNA some distance from this site. Whether the DNA is cut or modified depends on the methylation state of the target sequence. When the target site is unmodified, the DNA is cut. When the target site is hemimethylated, the complex acts as a maintenance MTase modifying the DNA so that both strands become methylated. After locating a non-methylated recognition site, the enzyme complex serves as a molecular motor that translocates DNA in an ATP-dependent manner until a collision occurs that triggers cleavage. {ECO:0000269|PubMed:4868368, ECO:0000269|PubMed:6255295, ECO:0000269|PubMed:8514761, ECO:0000269|PubMed:9033396}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3958|complex.ecocyc.CPLX0-3958]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4348|gene.b4348]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05719`
- `KEGG:ecj:JW4311;eco:b4348;ecoc:C3026_23490;`
- `GeneID:948867;`
- `GO:GO:0003677; GO:0009307; GO:0019812`

## Notes

Type I restriction enzyme EcoKI specificity subunit (S protein) (Type I specificity subunit S.EcoKI) (S.EcoKI) (Type-1 restriction enzyme EcoKI specificity subunit)
