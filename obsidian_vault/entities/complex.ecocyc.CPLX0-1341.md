---
entity_id: "complex.ecocyc.CPLX0-1341"
entity_type: "complex"
name: "SufBC2D Fe-S cluster scaffold complex"
source_database: "EcoCyc"
source_id: "CPLX0-1341"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# SufBC2D Fe-S cluster scaffold complex

`complex.ecocyc.CPLX0-1341`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1341`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77522|protein.P77522]], [[protein.P77499|protein.P77499]], [[protein.P77689|protein.P77689]]

## Enriched Summary

The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. The SufBC2D complex functions as the scaffold for de novo assembly of Fe-S clusters ; it performs assembly of iron-sulfur clusters in vitro and transfers them to the EG11378 SufA protein, which then delivers them to target protein . The sulfur source for the system is the G6905 SufE protein, which receives a sulfur atom from the CPLX0-246 SufS cysteine desulfurase and transfers it to the Cys254 residue of G6909-MONOMER SufB . The iron donor for the Suf pathway is unknown as of 2023. Unlike cluster synthesis by IscU, which proceeds through initial formation of two [2Fe-2S]2+ clusters that can be reductively coupled to form a single [4Fe-4S]2+ cluster, SufB was reported to synthesize a [4Fe-4S] cluster without any observable accumulation of [2Fe-2S] clusters during the process . A [2Fe-2S] SufB form could be obtained by anaerobic incubation of apo-SufB in the absence of DTT with a 3-fold molar excess of ferric iron and sulfide, but addition of DTT resulted in formation of a [4Fe-4S] cluster . Co-expression of the sufBCDSE genes resulted in SufB proteins carrying both [4Fe-4S] and linear [3Fe-4S] clusters . In vitro, both the [2Fe-2S] and [4Fe-4S] holo forms of SufB can transfer their cluster to client proteins...

## Annotation

The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. The SufBC2D complex functions as the scaffold for de novo assembly of Fe-S clusters ; it performs assembly of iron-sulfur clusters in vitro and transfers them to the EG11378 SufA protein, which then delivers them to target protein . The sulfur source for the system is the G6905 SufE protein, which receives a sulfur atom from the CPLX0-246 SufS cysteine desulfurase and transfers it to the Cys254 residue of G6909-MONOMER SufB . The iron donor for the Suf pathway is unknown as of 2023. Unlike cluster synthesis by IscU, which proceeds through initial formation of two [2Fe-2S]2+ clusters that can be reductively coupled to form a single [4Fe-4S]2+ cluster, SufB was reported to synthesize a [4Fe-4S] cluster without any observable accumulation of [2Fe-2S] clusters during the process . A [2Fe-2S] SufB form could be obtained by anaerobic incubation of apo-SufB in the absence of DTT with a 3-fold molar excess of ferric iron and sulfide, but addition of DTT resulted in formation of a [4Fe-4S] cluster . Co-expression of the sufBCDSE genes resulted in SufB proteins carrying both [4Fe-4S] and linear [3Fe-4S] clusters . In vitro, both the [2Fe-2S] and [4Fe-4S] holo forms of SufB can transfer their cluster to client proteins . The SufBCD complex can be primarily isolated in a 1:2:1 stoichiometry of the SufB:SufC:SufD subunits; this complex can not be assembled in vitro from isolated components. When purified anaerobically, the complex contains 1 eq of FADH2 with a dissociation constant (Kd) of 12 μM; the complex does not bind the oxidized form, FAD . A SufB2C2 complex containing Fe-S clusters and FADH2 has also been isolate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P77499|protein.P77499]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P77522|protein.P77522]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77689|protein.P77689]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-1341`
- `PDB:5AWG`
- `PDB:5AWF`
- `PDB:5AWG`
- `PDB:5AWF`
- `QSPROTEOME:QS00187917`

## Notes

1*protein.P77522|2*protein.P77499|1*protein.P77689
