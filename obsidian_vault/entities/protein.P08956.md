---
entity_id: "protein.P08956"
entity_type: "protein"
name: "hsdR"
source_database: "UniProt"
source_id: "P08956"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hsdR hsr b4350 JW4313"
---

# hsdR

`protein.P08956`

## Static

- Type: `protein`
- Source: `UniProt:P08956`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The subtype A restriction (R) subunit of a type I restriction enzyme that recognizes 5'-AACN(6)GTGC-3' and cleaves a random distance away. The R subunit is required for both endonuclease and ATPase activities but not for modification (PubMed:12654995, PubMed:4868368, PubMed:6255295, PubMed:9033396). Has endonucleolytic activity that requires Mg(2+), ATP and S-adenosyl-L-methionine (SAM); ATP can be replaced by dATP, no tested molecule could substitute for SAM. Generates double-stranded DNA with no nicks, by cutting one strand then the other within a few seconds. Cleaves only non-methylated DNA, hemi-methylated and fully methylated DNA are not substrates (PubMed:4868368, PubMed:9033396). After locating a non-methylated recognition site, the enzyme complex serves as a molecular motor that translocates DNA in an ATP-dependent manner until a collision occurs that triggers cleavage (PubMed:6248234). {ECO:0000269|PubMed:4868368, ECO:0000269|PubMed:6248234, ECO:0000269|PubMed:6255295, ECO:0000269|PubMed:9033396, ECO:0000303|PubMed:12654995}. HsdR is the restriction endonuclease component of the EcoKI restriction-modification system .

## Biological Role

Component of EcoKI restriction-modification system (complex.ecocyc.CPLX0-3958).

## Annotation

FUNCTION: The subtype A restriction (R) subunit of a type I restriction enzyme that recognizes 5'-AACN(6)GTGC-3' and cleaves a random distance away. The R subunit is required for both endonuclease and ATPase activities but not for modification (PubMed:12654995, PubMed:4868368, PubMed:6255295, PubMed:9033396). Has endonucleolytic activity that requires Mg(2+), ATP and S-adenosyl-L-methionine (SAM); ATP can be replaced by dATP, no tested molecule could substitute for SAM. Generates double-stranded DNA with no nicks, by cutting one strand then the other within a few seconds. Cleaves only non-methylated DNA, hemi-methylated and fully methylated DNA are not substrates (PubMed:4868368, PubMed:9033396). After locating a non-methylated recognition site, the enzyme complex serves as a molecular motor that translocates DNA in an ATP-dependent manner until a collision occurs that triggers cleavage (PubMed:6248234). {ECO:0000269|PubMed:4868368, ECO:0000269|PubMed:6248234, ECO:0000269|PubMed:6255295, ECO:0000269|PubMed:9033396, ECO:0000303|PubMed:12654995}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3958|complex.ecocyc.CPLX0-3958]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4350|gene.b4350]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08956`
- `KEGG:ecj:JW4313;eco:b4350;ecoc:C3026_23500;`
- `GeneID:948878;`
- `GO:GO:0003677; GO:0004386; GO:0005524; GO:0005829; GO:0009035; GO:0009307; GO:0019812`
- `EC:3.1.21.3`

## Notes

Type I restriction enzyme EcoKI endonuclease subunit (EcoKI) (R protein) (EC 3.1.21.3)
