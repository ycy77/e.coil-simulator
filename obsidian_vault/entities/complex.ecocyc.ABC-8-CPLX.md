---
entity_id: "complex.ecocyc.ABC-8-CPLX"
entity_type: "complex"
name: "dipeptide ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-8-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "DppABCDF"
---

# dipeptide ABC transporter

`complex.ecocyc.ABC-8-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-8-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P0AAG0|protein.P0AAG0]], [[protein.P37313|protein.P37313]], [[protein.P0AEF8|protein.P0AEF8]], [[protein.P0AEG1|protein.P0AEG1]], [[protein.P23847|protein.P23847]]

## Enriched Summary

DppABCDF is a dipeptide transporter that is a member of the ATP-binding cassette (ABC) superfamily. DppA is the periplasmic dipeptide binding protein , DppB and DppC are the predicted integral membrane subunits and DppD and DppF are the predicted ATP-binding subunits . Early studies in E. coli W and E.coli K-12 characterised 3 systems for peptide transport termed opp, dpp and tpp. opp mutants were selected by resistance to the toxic tripeptide triornithine; dpp mutants were selected for resistance to the toxic dipeptide Lys-aminoxyA (under conditions that maintained the opp locus) and tpp mutants, selected by resistance to the toxic peptide analogue alanylalanine phosphonate (see review by and references therein). opp dpp double mutants show greater resistance to a range of toxic dipeptide analogues than the single mutations alone while triple opp dpp tpp mutants are resistant to all aminoxy peptides and have no detectable peptide transport (see also ). The Dpp system transports dipeptide substrates with varying affinity (Gly-Gly is a poor substrate) and also transports tripeptides to a lesser extent; dipeptides containing D-residues are not transported; some modifications to the peptide structure are tolerated (eg.alkylation of the N-terminal amino group) while others are not (eg...

## Biological Role

Catalyzes ABC-8-RXN (reaction.ecocyc.ABC-8-RXN). Transports a dipeptide (molecule.ecocyc.DIPEPTIDES), hν (molecule.ecocyc.Light).

## Annotation

DppABCDF is a dipeptide transporter that is a member of the ATP-binding cassette (ABC) superfamily. DppA is the periplasmic dipeptide binding protein , DppB and DppC are the predicted integral membrane subunits and DppD and DppF are the predicted ATP-binding subunits . Early studies in E. coli W and E.coli K-12 characterised 3 systems for peptide transport termed opp, dpp and tpp. opp mutants were selected by resistance to the toxic tripeptide triornithine; dpp mutants were selected for resistance to the toxic dipeptide Lys-aminoxyA (under conditions that maintained the opp locus) and tpp mutants, selected by resistance to the toxic peptide analogue alanylalanine phosphonate (see review by and references therein). opp dpp double mutants show greater resistance to a range of toxic dipeptide analogues than the single mutations alone while triple opp dpp tpp mutants are resistant to all aminoxy peptides and have no detectable peptide transport (see also ). The Dpp system transports dipeptide substrates with varying affinity (Gly-Gly is a poor substrate) and also transports tripeptides to a lesser extent; dipeptides containing D-residues are not transported; some modifications to the peptide structure are tolerated (eg.alkylation of the N-terminal amino group) while others are not (eg. cyclization and modifications that remove the positive charge from the N-terminal α-amino group) . When a foreign outer membrane heme receptor is expressed in E. coli, the dipeptide ABC transporter is also capable of transporting heme and the heme precursor, 5-aminolevulinic acid, from the periplasm into the cytoplasm . Bacterial peptide transporters, including the dpp-encoded dipeptide transporter, are targets for the development of novel peptide-based antibiotics .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-8-RXN|reaction.ecocyc.ABC-8-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.DIPEPTIDES|molecule.ecocyc.DIPEPTIDES]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P0AAG0|protein.P0AAG0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEF8|protein.P0AEF8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEG1|protein.P0AEG1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P23847|protein.P23847]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P37313|protein.P37313]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-8-CPLX`
- `QSPROTEOME:QS00049296`

## Notes

1*protein.P0AAG0|1*protein.P37313|1*protein.P0AEF8|1*protein.P0AEG1|1*protein.P23847
