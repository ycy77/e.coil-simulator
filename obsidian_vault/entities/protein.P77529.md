---
entity_id: "protein.P77529"
entity_type: "protein"
name: "tcyP"
source_database: "UniProt"
source_id: "P77529"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tcyP ydjN b1729 JW1718"
---

# tcyP

`protein.P77529`

## Static

- Type: `protein`
- Source: `UniProt:P77529`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in L-cystine import (PubMed:25139244, PubMed:25837721, PubMed:26350134, PubMed:27481704). Low affinity L-cystine transporter that is mainly involved in L-cystine uptake from outside as a nutrient (PubMed:25837721). Is the primary transporter at high concentrations of cystine (PubMed:26350134). Probably functions as a proton symporter (Probable). Can also transport D-cystine, cysteine and homocystine as a methionine precursor (PubMed:25139244, PubMed:26350134). Mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244). Can also transport S-sulfocysteine and is required for growth on S-sulfocysteine as a sulfur source (PubMed:27481704). Plays the principal role in the 3-mercaptopyruvate sulfurtransferase (3MST)-mediated generation of endogenous hydrogen sulfide (H2S) (PubMed:28533366). {ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000269|PubMed:27481704, ECO:0000269|PubMed:28533366, ECO:0000305|PubMed:26350134}. tcyP encodes an inner membrane L-cystine transporter in E. coli K-12 . Two cystine uptake systems (now known to be the ABC transporter CPLX0-8152 "TcyJLN" and TcyP) were first identified in E. coli W . TcyP is responsible for the majority (approx...

## Biological Role

Catalyzes L-cystine:proton symport (reaction.ecocyc.TRANS-RXN-285), homocystine:proton symport (reaction.ecocyc.TRANS-RXN-286), sulfocysteine:proton symport (reaction.ecocyc.TRANS-RXN-330), D-cystine:proton symport (reaction.ecocyc.TRANS-RXN0-616). Transports L-Cystine (molecule.C00491), L-Homocystine (molecule.C01817), S-Sulfo-L-cysteine (molecule.C05824), D-cystine (molecule.ecocyc.CPD0-1564), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in L-cystine import (PubMed:25139244, PubMed:25837721, PubMed:26350134, PubMed:27481704). Low affinity L-cystine transporter that is mainly involved in L-cystine uptake from outside as a nutrient (PubMed:25837721). Is the primary transporter at high concentrations of cystine (PubMed:26350134). Probably functions as a proton symporter (Probable). Can also transport D-cystine, cysteine and homocystine as a methionine precursor (PubMed:25139244, PubMed:26350134). Mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244). Can also transport S-sulfocysteine and is required for growth on S-sulfocysteine as a sulfur source (PubMed:27481704). Plays the principal role in the 3-mercaptopyruvate sulfurtransferase (3MST)-mediated generation of endogenous hydrogen sulfide (H2S) (PubMed:28533366). {ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000269|PubMed:27481704, ECO:0000269|PubMed:28533366, ECO:0000305|PubMed:26350134}.

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-285|reaction.ecocyc.TRANS-RXN-285]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-286|reaction.ecocyc.TRANS-RXN-286]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-330|reaction.ecocyc.TRANS-RXN-330]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-616|reaction.ecocyc.TRANS-RXN0-616]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00491|molecule.C00491]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01817|molecule.C01817]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C05824|molecule.C05824]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1729|gene.b1729]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77529`
- `KEGG:ecj:JW1718;eco:b1729;ecoc:C3026_09885;`
- `GeneID:946238;`
- `GO:GO:0000099; GO:0000101; GO:0005886; GO:0006791; GO:0015184; GO:0015293; GO:0015811`

## Notes

L-cystine transporter TcyP (S-sulfocysteine transporter)
