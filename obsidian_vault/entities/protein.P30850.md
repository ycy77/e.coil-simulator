---
entity_id: "protein.P30850"
entity_type: "protein"
name: "rnb"
source_database: "UniProt"
source_id: "P30850"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnb b1286 JW1279"
---

# rnb

`protein.P30850`

## Static

- Type: `protein`
- Source: `UniProt:P30850`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in mRNA degradation. Hydrolyzes single-stranded polyribonucleotides processively in the 3' to 5' direction (PubMed:11948193). RNases 2 and R (rnr) contribute to rRNA degradation during starvation, while RNase R and PNPase (pnp) are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). This RNase is required to decrease expression of RNase PH (rnp) at 42 degrees Celsius during starvation, which in turn represses rRNA degradation (PubMed:28625967). {ECO:0000269|PubMed:11948193, ECO:0000269|PubMed:21135037, ECO:0000269|PubMed:28625967}. Ribonuclease II (RNase II) is a single-strand-specific exoribonuclease that cleaves RNA processively from the 3' end to produce ribonucleoside 5'-monophosphates. It has roles in the maturation, turnover and quality control of different RNA types. RNase II is one of six exonucleases (RNase II, RNase D, RNase BN, RNase T, RNase PH and PNPase) that can process tRNA and is responsible for the first step in the conversion of precursor tyrosine tRNA to its final form . It has been shown in vitro to cleave long 3' tRNA sequences to yield 2-4 nucleotide intermediates for subsequent processing...

## Biological Role

Catalyzes 3.1.13.1-RXN (reaction.ecocyc.3.1.13.1-RXN), exoribonuclease (reaction.ecocyc.RXN-24139), RXN0-6524 (reaction.ecocyc.RXN0-6524), poly(A)-specific ribonuclease (reaction.ecocyc.RXN0-7463), RXN0-7477 (reaction.ecocyc.RXN0-7477), RXN0-7482 (reaction.ecocyc.RXN0-7482). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Involved in mRNA degradation. Hydrolyzes single-stranded polyribonucleotides processively in the 3' to 5' direction (PubMed:11948193). RNases 2 and R (rnr) contribute to rRNA degradation during starvation, while RNase R and PNPase (pnp) are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). This RNase is required to decrease expression of RNase PH (rnp) at 42 degrees Celsius during starvation, which in turn represses rRNA degradation (PubMed:28625967). {ECO:0000269|PubMed:11948193, ECO:0000269|PubMed:21135037, ECO:0000269|PubMed:28625967}.

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.3.1.13.1-RXN|reaction.ecocyc.3.1.13.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24139|reaction.ecocyc.RXN-24139]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6524|reaction.ecocyc.RXN0-6524]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7463|reaction.ecocyc.RXN0-7463]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7477|reaction.ecocyc.RXN0-7477]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7482|reaction.ecocyc.RXN0-7482]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1286|gene.b1286]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30850`
- `KEGG:ecj:JW1279;eco:b1286;ecoc:C3026_07555;`
- `GeneID:945864;`
- `GO:GO:0003723; GO:0005829; GO:0006402; GO:0008408; GO:0008859; GO:0016078`
- `EC:3.1.13.1`

## Notes

Exoribonuclease 2 (EC 3.1.13.1) (Exoribonuclease II) (RNase II) (Ribonuclease II)
