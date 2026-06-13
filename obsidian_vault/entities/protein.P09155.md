---
entity_id: "protein.P09155"
entity_type: "protein"
name: "rnd"
source_database: "UniProt"
source_id: "P09155"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnd b1804 JW1793"
---

# rnd

`protein.P09155`

## Static

- Type: `protein`
- Source: `UniProt:P09155`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Exonuclease involved in the 3' processing of various precursor tRNAs. Initiates hydrolysis at the 3'-terminus of an RNA molecule and releases 5'-mononucleotides. {ECO:0000255|HAMAP-Rule:MF_01899, ECO:0000269|PubMed:3041371, ECO:0000269|PubMed:6263886}. Ribonuclease D (RNase D) is an exonuclease involved in the 3' ribonucleolytic processing of precursor tRNA. Though RNase D appears to be a minor player in this task and is not required for viability or proper tRNA processing, it can support such processing in the absence of other exonucleases (RNase II, RNase BN, RNase T and RNase PH) . In vitro, RNase D cleaves tRNA nonprocessively (randomly) from the 3' end to yield 5"-mononucleotides and active tRNA. Cleavage of tRNA slows at the CCA nucleotide sequence, allowing aminoacylation of the tRNA that prevents additional cleavage . RNase D activity is very dependent on the structure of the 3' end of the target tRNA, with cleavage of altered tRNA proceeding much faster than cleavage of wild type, and no cleavage of tRNA bearing a 3' phosphate . When overexpressed in vivo, RNase D cleaves the 3' end of tRNA, eventually cleaving past the CCA sequence to yield damaged tRNA that cannot be fixed by tRNA nucleotidyltransferase...

## Biological Role

Catalyzes 3.1.13.5-RXN (reaction.ecocyc.3.1.13.5-RXN), RXN0-6483 (reaction.ecocyc.RXN0-6483), RXN0-6484 (reaction.ecocyc.RXN0-6484), RXN0-7473 (reaction.ecocyc.RXN0-7473). Bound by Cobalt ion (molecule.C00175), Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Exonuclease involved in the 3' processing of various precursor tRNAs. Initiates hydrolysis at the 3'-terminus of an RNA molecule and releases 5'-mononucleotides. {ECO:0000255|HAMAP-Rule:MF_01899, ECO:0000269|PubMed:3041371, ECO:0000269|PubMed:6263886}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.3.1.13.5-RXN|reaction.ecocyc.3.1.13.5-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6483|reaction.ecocyc.RXN0-6483]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6484|reaction.ecocyc.RXN0-6484]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7473|reaction.ecocyc.RXN0-7473]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1804|gene.b1804]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09155`
- `KEGG:ecj:JW1793;eco:b1804;`
- `GeneID:946328;`
- `GO:GO:0000166; GO:0000175; GO:0003676; GO:0005737; GO:0033890; GO:0042780`
- `EC:3.1.13.5`

## Notes

Ribonuclease D (RNase D) (EC 3.1.13.5)
