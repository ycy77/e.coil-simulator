---
entity_id: "protein.P08957"
entity_type: "protein"
name: "hsdM"
source_database: "UniProt"
source_id: "P08957"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hsdM hsm b4349 JW4312"
---

# hsdM

`protein.P08957`

## Static

- Type: `protein`
- Source: `UniProt:P08957`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The subtype gamma methyltransferase (M) subunit of a type I restriction enzyme. The M and S subunits together form a methyltransferase (MTase) that methylates A-2 on the top and A-3 on the bottom strand of the sequence 5'-AACN(6)GTGC-3'. In the presence of the R subunit the complex can also act as an endonuclease, binding to the same target sequence but cutting the DNA some distance from this site. Whether the DNA is cut or modified depends on the methylation state of the target sequence. When the target site is unmodified, the DNA is cut. When the target site is hemimethylated, the complex acts as a maintenance MTase modifying the DNA so that both strands become methylated. After locating a non-methylated recognition site, the enzyme complex serves as a molecular motor that translocates DNA in an ATP-dependent manner until a collision occurs that triggers cleavage. {ECO:0000269|PubMed:4868368, ECO:0000269|PubMed:6255295, ECO:0000269|PubMed:8514761, ECO:0000269|PubMed:9033396}. HsdM is the modification methyltransferase component of the EcoKI restriction-modification system .

## Biological Role

Component of EcoKI restriction-modification system (complex.ecocyc.CPLX0-3958).

## Annotation

FUNCTION: The subtype gamma methyltransferase (M) subunit of a type I restriction enzyme. The M and S subunits together form a methyltransferase (MTase) that methylates A-2 on the top and A-3 on the bottom strand of the sequence 5'-AACN(6)GTGC-3'. In the presence of the R subunit the complex can also act as an endonuclease, binding to the same target sequence but cutting the DNA some distance from this site. Whether the DNA is cut or modified depends on the methylation state of the target sequence. When the target site is unmodified, the DNA is cut. When the target site is hemimethylated, the complex acts as a maintenance MTase modifying the DNA so that both strands become methylated. After locating a non-methylated recognition site, the enzyme complex serves as a molecular motor that translocates DNA in an ATP-dependent manner until a collision occurs that triggers cleavage. {ECO:0000269|PubMed:4868368, ECO:0000269|PubMed:6255295, ECO:0000269|PubMed:8514761, ECO:0000269|PubMed:9033396}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3958|complex.ecocyc.CPLX0-3958]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4349|gene.b4349]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08957`
- `KEGG:ecj:JW4312;eco:b4349;ecoc:C3026_23495;`
- `GeneID:948872;`
- `GO:GO:0003677; GO:0005829; GO:0008170; GO:0009007; GO:0009307; GO:0019812; GO:0032259`
- `EC:2.1.1.72`

## Notes

Type I restriction enzyme EcoKI methylase subunit (M protein) (EC 2.1.1.72) (Type I methyltransferase M.EcoKI) (M.EcoKI)
