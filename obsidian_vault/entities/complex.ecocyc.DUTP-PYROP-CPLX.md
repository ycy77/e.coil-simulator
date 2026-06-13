---
entity_id: "complex.ecocyc.DUTP-PYROP-CPLX"
entity_type: "complex"
name: "dUTP diphosphatase"
source_database: "EcoCyc"
source_id: "DUTP-PYROP-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dUTP diphosphatase

`complex.ecocyc.DUTP-PYROP-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DUTP-PYROP-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06968|protein.P06968]]

## Enriched Summary

dUTP diphosphatase (dUTPase) catalyzes the hydrolysis of dUTP, maintaining a low intracellular concentration of dUTP to avoid the incorporation of uracil into DNA . dUTPase is highly specific for dUTP as a substrate . Crystal structures of wild-type and mutant dUTPase alone and in complex with substrate, product and substrate analogs have been determined . The enzyme is a symmetrical trimer with the C-terminal arm of each subunit extending to the neighboring subunit . The conserved Tyr93 residue is required for activity and likely part of the active site . The C-terminal 11 amino acid glycine-rich region is important for dUTPase function and may close over the active site during catalysis . NMR spectroscopy showed that the C-terminal residues are highly flexible . Potential catalytic mechanisms for different subfamilies of dUTPases have been proposed . Mg2+ enhances binding of the dUTP substrate 100-fold . During catalysis, the divalent metal ion may promote product stabilization by binding to the β- and γ-phosphate groups of dUTP . Additional crystal structures of dUTPase enabled localization of the Mg2+ cofactor and allowed further insights into the catalytic mechanism . The conserved Ser72 residue plays a role in catalysis...

## Biological Role

Catalyzes DUTP-PYROP-RXN (reaction.ecocyc.DUTP-PYROP-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

dUTP diphosphatase (dUTPase) catalyzes the hydrolysis of dUTP, maintaining a low intracellular concentration of dUTP to avoid the incorporation of uracil into DNA . dUTPase is highly specific for dUTP as a substrate . Crystal structures of wild-type and mutant dUTPase alone and in complex with substrate, product and substrate analogs have been determined . The enzyme is a symmetrical trimer with the C-terminal arm of each subunit extending to the neighboring subunit . The conserved Tyr93 residue is required for activity and likely part of the active site . The C-terminal 11 amino acid glycine-rich region is important for dUTPase function and may close over the active site during catalysis . NMR spectroscopy showed that the C-terminal residues are highly flexible . Potential catalytic mechanisms for different subfamilies of dUTPases have been proposed . Mg2+ enhances binding of the dUTP substrate 100-fold . During catalysis, the divalent metal ion may promote product stabilization by binding to the β- and γ-phosphate groups of dUTP . Additional crystal structures of dUTPase enabled localization of the Mg2+ cofactor and allowed further insights into the catalytic mechanism . The conserved Ser72 residue plays a role in catalysis . Strains containing dut mutant alleles accumulate of short DNA fragments during chromosomal replication due to misincorporation of dUTP into DNA and subsequent excision repair . The mechanism of chromosomal fragmentation due to uracil incorporation appears to be the collapse of the replication fork at uracil excision nicks . Uracil levels in wild type E. coli genomic DNA are below the detection limit; a dut-1 mutant contains ~19-31 uracil residues per 106 nucleotides, depending on the growth phase . dut mutants show an increased recombination freq

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DUTP-PYROP-RXN|reaction.ecocyc.DUTP-PYROP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P06968|protein.P06968]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:DUTP-PYROP-CPLX`
- `QSPROTEOME:QS00181521`

## Notes

3*protein.P06968
