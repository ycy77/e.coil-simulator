---
entity_id: "protein.P0AAE0"
entity_type: "protein"
name: "cycA"
source_database: "UniProt"
source_id: "P0AAE0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cycA dagA ytfD b4208 JW4166"
---

# cycA

`protein.P0AAE0`

## Static

- Type: `protein`
- Source: `UniProt:P0AAE0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Permease that is involved in the transport across the cytoplasmic membrane of D-alanine, D-serine, glycine and beta-alanine (PubMed:15221223, PubMed:23316042, PubMed:4574696, PubMed:4583203, PubMed:4926674). Also contributes to L-alanine uptake (PubMed:4574696, PubMed:4583203). In addition, in minimal media, transports the broad spectrum antibiotic D-cycloserine into the cell (PubMed:23316042, PubMed:4574696, PubMed:4926674). Transports D-cycloserine only in minimal media, and not in a complex medium, suggesting that CycA does not play a role in D-cycloserine transport when E.coli is grown in a complex or biologically relevant medium, probably due to competition from other CycA substrates present in the medium (PubMed:23316042). {ECO:0000269|PubMed:15221223, ECO:0000269|PubMed:23316042, ECO:0000269|PubMed:4574696, ECO:0000269|PubMed:4583203, ECO:0000269|PubMed:4926674}. CycA is an inner membrane protein which mediates the uptake of D-serine, D-alanine, and glycine; it also contributes to L-alanine uptake, is the major transporter for β-alanine uptake and is implicated in the uptake of D-cycloserine. cycA mutants are defective in the the uptake of D-serine, D-alanine and glycine and slightly impaired in L-alanine uptake; cycA mutants are unable to utilize D-alanine as a carbon source...

## Biological Role

Catalyzes D-serine:proton symport (reaction.ecocyc.RXN0-5130), β-alanine:proton symport (reaction.ecocyc.RXN0-5201), L-alanine:proton symport (reaction.ecocyc.RXN0-5202), D-cycloserine:proton symport (reaction.ecocyc.RXN0-5203), D-alanine:proton symport (reaction.ecocyc.TRANS-RXN-62A), glycine:proton symport (reaction.ecocyc.TRANS-RXN-62B). Transports Glycine (molecule.C00037), L-Alanine (molecule.C00041), D-Alanine (molecule.C00133), D-Serine (molecule.C00740), D-cycloserine (molecule.ecocyc.CPD-2482), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Permease that is involved in the transport across the cytoplasmic membrane of D-alanine, D-serine, glycine and beta-alanine (PubMed:15221223, PubMed:23316042, PubMed:4574696, PubMed:4583203, PubMed:4926674). Also contributes to L-alanine uptake (PubMed:4574696, PubMed:4583203). In addition, in minimal media, transports the broad spectrum antibiotic D-cycloserine into the cell (PubMed:23316042, PubMed:4574696, PubMed:4926674). Transports D-cycloserine only in minimal media, and not in a complex medium, suggesting that CycA does not play a role in D-cycloserine transport when E.coli is grown in a complex or biologically relevant medium, probably due to competition from other CycA substrates present in the medium (PubMed:23316042). {ECO:0000269|PubMed:15221223, ECO:0000269|PubMed:23316042, ECO:0000269|PubMed:4574696, ECO:0000269|PubMed:4583203, ECO:0000269|PubMed:4926674}.

## Outgoing Edges (12)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5130|reaction.ecocyc.RXN0-5130]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5201|reaction.ecocyc.RXN0-5201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5202|reaction.ecocyc.RXN0-5202]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5203|reaction.ecocyc.RXN0-5203]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-62A|reaction.ecocyc.TRANS-RXN-62A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-62B|reaction.ecocyc.TRANS-RXN-62B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-2482|molecule.ecocyc.CPD-2482]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4208|gene.b4208]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAE0`
- `KEGG:ecj:JW4166;eco:b4208;ecoc:C3026_22730;`
- `GeneID:93777613;948725;`
- `GO:GO:0001761; GO:0001762; GO:0005886; GO:0015180; GO:0015187; GO:0015293; GO:0015808; GO:0015816; GO:0022857; GO:0042941; GO:0042942; GO:0042944; GO:0042945`

## Notes

D-serine/D-alanine/glycine transporter (Amino acid carrier CycA)
