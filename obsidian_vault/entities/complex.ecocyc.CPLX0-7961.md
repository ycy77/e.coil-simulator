---
entity_id: "complex.ecocyc.CPLX0-7961"
entity_type: "complex"
name: "chloride:H+ antiporter ClcA"
source_database: "EcoCyc"
source_id: "CPLX0-7961"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# chloride:H+ antiporter ClcA

`complex.ecocyc.CPLX0-7961`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7961`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37019|protein.P37019]]

## Enriched Summary

ClcA is a member of the chloride carrier/channel (ClC) family and mediates a chloride:proton antiport reaction (a secondary carrier type transport reaction) in which two chloride ions exchange for one proton . ClcA forms part of E. coli's response to extreme acid conditions ; ClcA function may help to limit the internal positive charge build-up that occurs during extreme acid stress and assist in restoring the correct (interior-negative) transmembrane potential once acid stress has abated (and see ). ClcA mediated import of chloride also serves to activate GLUTDECARBOXB-CPLX as an early response to acid stress ClcA is a functional homodimer . Each subunit within the dimer forms its own independent pore and selectivity filter (see also ). Cl-/H+ exchange is preserved in ClcA dimers constrained by covalent cross-links across their dimer interface and in ClcA mutants in which the dimer interface is destabilised suggesting that the ClcA monomer contains all the essential components of the transport mechanism. ClcA undergoes dynamic assembly in lipid membranes and can exchange subunits; a thermodynamic analysis of dimerization has been reported . The mechanism of ClcA mediated ion exchange has been intensively studied and continues to be elucidated . A detailed topology map for ClcA has been reported...

## Biological Role

Catalyzes chloride:proton antiport (reaction.ecocyc.RXN0-2501).

## Annotation

ClcA is a member of the chloride carrier/channel (ClC) family and mediates a chloride:proton antiport reaction (a secondary carrier type transport reaction) in which two chloride ions exchange for one proton . ClcA forms part of E. coli's response to extreme acid conditions ; ClcA function may help to limit the internal positive charge build-up that occurs during extreme acid stress and assist in restoring the correct (interior-negative) transmembrane potential once acid stress has abated (and see ). ClcA mediated import of chloride also serves to activate GLUTDECARBOXB-CPLX as an early response to acid stress ClcA is a functional homodimer . Each subunit within the dimer forms its own independent pore and selectivity filter (see also ). Cl-/H+ exchange is preserved in ClcA dimers constrained by covalent cross-links across their dimer interface and in ClcA mutants in which the dimer interface is destabilised suggesting that the ClcA monomer contains all the essential components of the transport mechanism. ClcA undergoes dynamic assembly in lipid membranes and can exchange subunits; a thermodynamic analysis of dimerization has been reported . The mechanism of ClcA mediated ion exchange has been intensively studied and continues to be elucidated . A detailed topology map for ClcA has been reported . Cells lacking both ClcA and YNFJ-MONOMER "ClcB" do not survive extreme acid shock conditions (pH 2.5, 2 hrs at 37°C in minimal medium); expression of clcA from a low-copy number plasmid rescues this phenotype . eriC: 'Escherichia coli-derived ClC Cl- channel homolog' Reviews: Comments: Related reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2501|reaction.ecocyc.RXN0-2501]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P37019|protein.P37019]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7961`
- `QSPROTEOME:QS00182677`
- `PDB:8GA0`
- `PDB:8GAH`
- `PDB:8GA5`
- `PDB:8GA3`
- `PDB:8GA1`
- `PDB:7RP5`
- `PDB:7N8P`
- `PDB:7RSB`

## Notes

2*protein.P37019
