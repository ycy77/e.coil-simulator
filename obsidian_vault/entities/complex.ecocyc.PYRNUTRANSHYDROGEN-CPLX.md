---
entity_id: "complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX"
entity_type: "complex"
name: "pyridine nucleotide transhydrogenase"
source_database: "EcoCyc"
source_id: "PYRNUTRANSHYDROGEN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PntAB"
---

# pyridine nucleotide transhydrogenase

`complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PYRNUTRANSHYDROGEN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AB67|protein.P0AB67]], [[protein.P07001|protein.P07001]]

## Enriched Summary

PntAB is a membrane bound, proton translocating, pyridine nucleotide transhydrogenase which couples the reversible reduction of NADP+ by NADH to proton translocation across the membrane . The activity of PntAB is a major source of cytosolic NADPH in E. coli . The functional enzyme assembles as a tetramer composed of two α (PntA) and two β (PntB) subunits . The enzyme complex contains three domains: domains I and III protrude from the membrane and contain the binding sites for NAD(H) and NADP(H) respectively and domain II which spans the membrane and contains the proton translocation pathway. The transmembrane domain consists of 13 α-helices (4 from the α subunit and 9 from the β subunit) . E. coli also contains an energy independent UDHA-CPLX "soluble pyridine nucleotide transhydrogenase" encoded by the sthA gene. Its primary physiological role appears to be the reoxidation of NADPH . The two transhydrogenases are also distinguished by the stereospecificity of the reducing equivalents transfer (see ); PntAB is annotated as an AB (Re-Si)-specific transhydrogenase which acts on the pro-R hydrogen (or A hydrogen) of the nicotinamide ring of NADH and the pro-S hydrogen (B hydrogen) of NADPH...

## Biological Role

Catalyzes TRANS-RXN0-277 (reaction.ecocyc.TRANS-RXN0-277). Transports NAD+ (molecule.C00003), NADH (molecule.C00004), NADPH (molecule.C00005), NADP+ (molecule.C00006), hν (molecule.ecocyc.Light).

## Annotation

PntAB is a membrane bound, proton translocating, pyridine nucleotide transhydrogenase which couples the reversible reduction of NADP+ by NADH to proton translocation across the membrane . The activity of PntAB is a major source of cytosolic NADPH in E. coli . The functional enzyme assembles as a tetramer composed of two α (PntA) and two β (PntB) subunits . The enzyme complex contains three domains: domains I and III protrude from the membrane and contain the binding sites for NAD(H) and NADP(H) respectively and domain II which spans the membrane and contains the proton translocation pathway. The transmembrane domain consists of 13 α-helices (4 from the α subunit and 9 from the β subunit) . E. coli also contains an energy independent UDHA-CPLX "soluble pyridine nucleotide transhydrogenase" encoded by the sthA gene. Its primary physiological role appears to be the reoxidation of NADPH . The two transhydrogenases are also distinguished by the stereospecificity of the reducing equivalents transfer (see ); PntAB is annotated as an AB (Re-Si)-specific transhydrogenase which acts on the pro-R hydrogen (or A hydrogen) of the nicotinamide ring of NADH and the pro-S hydrogen (B hydrogen) of NADPH. Reviews:

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-277|reaction.ecocyc.TRANS-RXN0-277]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P07001|protein.P07001]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P0AB67|protein.P0AB67]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:PYRNUTRANSHYDROGEN-CPLX`
- `PDB:2BRU`
- `QSPROTEOME:QS00195967`

## Notes

2*protein.P0AB67|2*protein.P07001
