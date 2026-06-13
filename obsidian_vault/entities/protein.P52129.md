---
entity_id: "protein.P52129"
entity_type: "protein"
name: "rnlA"
source_database: "UniProt"
source_id: "P52129"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:17895580}. Note=May associate with ribosomes, it sediments in a P100 fraction (pellet of a 100,000 x g centrifugation). {ECO:0000305|PubMed:17895580}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnlA std yfjN b2630 JW2611"
---

# rnlA

`protein.P52129`

## Static

- Type: `protein`
- Source: `UniProt:P52129`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:17895580}. Note=May associate with ribosomes, it sediments in a P100 fraction (pellet of a 100,000 x g centrifugation). {ECO:0000305|PubMed:17895580}.

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:20980243, PubMed:24112600). A stable (half-life 27.6 minutes) endoribonuclease that in the absence of cognate antitoxin RnlB causes generalized RNA degradation. Degrades late enterobacteria phage T4 mRNAs, protecting the host against T4 reproduction. Activity is inhibited by cognate antitoxin RnlB and by enterobacteria phage T4 protein Dmd (PubMed:20980243, PubMed:22403819). Targets cyaA mRNA (PubMed:19019153). {ECO:0000269|PubMed:17895580, ECO:0000269|PubMed:19019153, ECO:0000269|PubMed:20980243, ECO:0000269|PubMed:22403819, ECO:0000269|PubMed:24112600}.

## Biological Role

Component of RnlA-RnlB toxin-antitoxin complex (complex.ecocyc.CPLX0-7909), CP4-57 prophage; RNase LS, toxin of the RnlAB toxin-antitoxin system (complex.ecocyc.CPLX0-8095).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:20980243, PubMed:24112600). A stable (half-life 27.6 minutes) endoribonuclease that in the absence of cognate antitoxin RnlB causes generalized RNA degradation. Degrades late enterobacteria phage T4 mRNAs, protecting the host against T4 reproduction. Activity is inhibited by cognate antitoxin RnlB and by enterobacteria phage T4 protein Dmd (PubMed:20980243, PubMed:22403819). Targets cyaA mRNA (PubMed:19019153). {ECO:0000269|PubMed:17895580, ECO:0000269|PubMed:19019153, ECO:0000269|PubMed:20980243, ECO:0000269|PubMed:22403819, ECO:0000269|PubMed:24112600}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7909|complex.ecocyc.CPLX0-7909]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8095|complex.ecocyc.CPLX0-8095]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2630|gene.b2630]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52129`
- `KEGG:ecj:JW2611;eco:b2630;ecoc:C3026_14550;`
- `GeneID:947107;`
- `GO:GO:0004521; GO:0005737; GO:0006355; GO:0006402; GO:0016787; GO:0040008; GO:0042803; GO:0044010; GO:0051607; GO:0110001`
- `EC:3.1.-.-`

## Notes

mRNA endoribonuclease toxin LS (EC 3.1.-.-) (RNase LS) (Toxin LS)
