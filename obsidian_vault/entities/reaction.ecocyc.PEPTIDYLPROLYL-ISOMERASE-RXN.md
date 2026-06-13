---
entity_id: "reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN"
entity_type: "reaction"
name: "PEPTIDYLPROLYL-ISOMERASE-RXN"
source_database: "EcoCyc"
source_id: "PEPTIDYLPROLYL-ISOMERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PPIASE"
  - "CYCLOPHILIN"
  - "PEPTIDYLPROLYL CIS-TRANS ISOMERASE"
---

# PEPTIDYLPROLYL-ISOMERASE-RXN

`reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PEPTIDYLPROLYL-ISOMERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

CIS-TRANS ISOMERIZATION OF PROLINE IMIDIC PEPTIDE BONDS IN OLIGOPEPTIDES. EcoCyc reaction equation: CPD-8624 -> CPD-8625; direction=REVERSIBLE. CIS-TRANS ISOMERIZATION OF PROLINE IMIDIC PEPTIDE BONDS IN OLIGOPEPTIDES.

## Biological Role

Catalyzed by peptidyl-prolyl cis-trans isomerase/OMP chaperone FkpA (complex.ecocyc.CPLX0-10157), peptidyl-prolyl cis-trans isomerase FklB (complex.ecocyc.CPLX0-3924), FKBP-type peptidyl-prolyl cis-trans isomerase SlyD (complex.ecocyc.CPLX0-7536), tig (protein.P0A850), ppiC (protein.P0A9L5), surA (protein.P0ABZ6), fkpB (protein.P0AEM0), ppiA (protein.P0AFL3), and 1 more. Substrates: a [protein]-L-proline (ω = 180) (molecule.ecocyc.CPD-8624). Products: a [protein]-L-proline (ω = 0) (molecule.ecocyc.CPD-8625).

## Annotation

CIS-TRANS ISOMERIZATION OF PROLINE IMIDIC PEPTIDE BONDS IN OLIGOPEPTIDES.

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-10157|complex.ecocyc.CPLX0-10157]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3924|complex.ecocyc.CPLX0-3924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7536|complex.ecocyc.CPLX0-7536]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A850|protein.P0A850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A9L5|protein.P0A9L5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABZ6|protein.P0ABZ6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AEM0|protein.P0AEM0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFL3|protein.P0AFL3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P23869|protein.P23869]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-8625|molecule.ecocyc.CPD-8625]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-8624|molecule.ecocyc.CPD-8624]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-10016|molecule.ecocyc.CPD-10016]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-14676|molecule.ecocyc.CPD-14676]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HYDROXYNAPHTHOQUINONE|molecule.ecocyc.HYDROXYNAPHTHOQUINONE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PEPTIDYLPROLYL-ISOMERASE-RXN`

## Notes

CPD-8624 -> CPD-8625; direction=REVERSIBLE
