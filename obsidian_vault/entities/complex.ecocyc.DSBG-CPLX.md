---
entity_id: "complex.ecocyc.DSBG-CPLX"
entity_type: "complex"
name: "protein sulfenic acid reductase and chaperone DsbG"
source_database: "EcoCyc"
source_id: "DSBG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "DsbG<sub>reduced</sub>"
---

# protein sulfenic acid reductase and chaperone DsbG

`complex.ecocyc.DSBG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DSBG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77202|protein.P77202]]

## Enriched Summary

dsbG encodes a dimeric periplasmic protein which contains a typical thiol-disulfide exchange motif (CXXC) . The protein is present in the reduced state in the wild type but is completely oxidized in a dsbD null background (see also ). Partly inconsistent reports on the thiol-disulfide exchange activities of the purified protein are available . Purified DsbG exhibits chaperone activity in vitro, suppressing the aggregation of citrate synthase and luciferase; DsbG displays chaperone activity in both its reduced and oxidized form . DsbG controls the level of cysteine sulfenylation in the periplasm and rescues single cysteine residues from oxidation: DsbG interacts with G6422-MONOMER "LdtB" (formerly YbiS) in vivo and in vitro; DsbG reduces LdtB-TNB* in vitro with the release of a TNB anion . The DsbGCXXA mutant forms stable (presumably mixed disulfide) complexes with LdtB, G7073-MONOMER "LdtA" and G6904-MONOMER "LdtE" in vivo and these three L,D-transpeptidases are putative DsbG substrates; protein sulfenic acids accumulate in the periplasm of a dsbGdsbC double null strain...

## Biological Role

Catalyzes 5.3.4.1-RXN (reaction.ecocyc.5.3.4.1-RXN), RXN-20019 (reaction.ecocyc.RXN-20019).

## Annotation

dsbG encodes a dimeric periplasmic protein which contains a typical thiol-disulfide exchange motif (CXXC) . The protein is present in the reduced state in the wild type but is completely oxidized in a dsbD null background (see also ). Partly inconsistent reports on the thiol-disulfide exchange activities of the purified protein are available . Purified DsbG exhibits chaperone activity in vitro, suppressing the aggregation of citrate synthase and luciferase; DsbG displays chaperone activity in both its reduced and oxidized form . DsbG controls the level of cysteine sulfenylation in the periplasm and rescues single cysteine residues from oxidation: DsbG interacts with G6422-MONOMER "LdtB" (formerly YbiS) in vivo and in vitro; DsbG reduces LdtB-TNB* in vitro with the release of a TNB anion . The DsbGCXXA mutant forms stable (presumably mixed disulfide) complexes with LdtB, G7073-MONOMER "LdtA" and G6904-MONOMER "LdtE" in vivo and these three L,D-transpeptidases are putative DsbG substrates; protein sulfenic acids accumulate in the periplasm of a dsbGdsbC double null strain . Overexpression of DsbG suppresses the protein-folding defect of, and restores peptidoglycan biosynthesis in, a ΔelyC strain; DsbG suppresses the phenotype of ΔelyC mutant cells independently of its known L,D transpeptidase substrates and independently of its reductase activity; DsbG suppresses the ΔelyC phenotype via its chaperone activity . DsbG contains an unstable disulfide; the equilibrium between the disulfide and dithiol forms strongly favors the reduced form; the DsbG homodimer forms a 'V-shaped' molecule; the structure has overall similarity to the DSBC-CPLX "protein disulfide isomerase DsbC", however specific characteristics of the potential substrate binding cleft, such as size and surface ch

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.5.3.4.1-RXN|reaction.ecocyc.5.3.4.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20019|reaction.ecocyc.RXN-20019]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77202|protein.P77202]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DSBG-CPLX`
- `QSPROTEOME:QS00195301`
- `BIGG:dsbgrd`

## Notes

2*protein.P77202
