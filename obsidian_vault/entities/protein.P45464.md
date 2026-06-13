---
entity_id: "protein.P45464"
entity_type: "protein"
name: "lpoA"
source_database: "UniProt"
source_id: "P45464"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}; Lipid-anchor {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}; Periplasmic side {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}. Note=Localizes at the sidewall of elongating cells."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpoA yraM b3147 JW3116"
---

# lpoA

`protein.P45464`

## Static

- Type: `protein`
- Source: `UniProt:P45464`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}; Lipid-anchor {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}; Periplasmic side {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}. Note=Localizes at the sidewall of elongating cells.

## Enriched Summary

FUNCTION: Regulator of peptidoglycan synthesis that is essential for the function of penicillin-binding protein 1A (PBP1a). Stimulates transpeptidase activity of PBP1a in vitro. {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}. LpoA is an outer membrane lipoprotein that forms a complex with, and is essential for the in vivo function of, CPLX0-7717 "penicillin binding protein 1A (PBP1A)" . LpoA stimulates the transpeptidase activity of PBP1A in vitro (see also ). LpoA stimulates the glycosyltransferase activity of PB1A in vivo . An lpoA- mutant is synthetically lethal in a PBP1B defective strain and this phenotype can be corrected by the expression of lpoA from a plasmid . An lpoA-lpoB- mutant displays a similar terminal phenotype to PBP1A- PBP1B- cells . Peptidoglycan isolated from an lpoA-lpoB- mutant prior to lysis shows a substantial decrease in peptidoglycan cross-linking and and an increase in pentapeptide containing muropeptides - a similar biochemistry is observed in the peptidoglycan of PBP1A- PBP1B- cells . Pull-down assays using tagged LpoA indicate that it specifically associates with PBP1A; an in vivo stoichiometry of 1:1 has been estimated . LpoA localises independently of PBP1A but like PBP1A, it concentrates at the sidewall of elongating cells...

## Annotation

FUNCTION: Regulator of peptidoglycan synthesis that is essential for the function of penicillin-binding protein 1A (PBP1a). Stimulates transpeptidase activity of PBP1a in vitro. {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}.

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN-16659|reaction.ecocyc.RXN-16659]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b3147|gene.b3147]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45464`
- `KEGG:ecj:JW3116;eco:b3147;ecoc:C3026_17145;`
- `GeneID:947663;`
- `GO:GO:0004553; GO:0008360; GO:0009252; GO:0009279; GO:0019899; GO:0030234; GO:0031241; GO:0042597`

## Notes

Penicillin-binding protein activator LpoA (PBP activator LpoA) (Lipoprotein activator of PBP from the outer membrane A)
