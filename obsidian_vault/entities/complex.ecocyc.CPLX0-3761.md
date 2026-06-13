---
entity_id: "complex.ecocyc.CPLX0-3761"
entity_type: "complex"
name: "β sliding clamp"
source_database: "EcoCyc"
source_id: "CPLX0-3761"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# β sliding clamp

`complex.ecocyc.CPLX0-3761`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3761`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A988|protein.P0A988]]

## Enriched Summary

The β subunit of CPLX0-3803 (DNA Pol III) dimerizes to form the sliding clamp that links the core polymerase to DNA and allows fast, processive DNA replication. It also plays a role in switching to the error-prone polymerases for translesion synthesis and for methyl-directed mismatch repair in response to stress. β binds 3' to an RNA primer at an ssDNA/duplex DNA junction in an ATP-dependent process catalyzed by the preinitiation complex . The presence of β stimulates DNA Pol III activity, resulting in increased product length and processivity . The complete DNA Pol III holoenzyme with both β and ATP is at least twenty times more processive than core enzyme or holoenzyme lacking either of those components . β may contribute to the regulation of replication initiation . Divalent magnesium is required for β to maintain its dimer structure ; the dynamics of the β clamp in solution and its loading dynamics have been investigated. ATP hydrolysis is involved in modulating the binding of the CPLX0-3801 (clamp loading complex) to the β sliding clamp ; the clamp loading complex may actively open the β sliding clamp for loading onto DNA . The β-clamp is very stable on DNA, requiring the ATP-dependent action of DNA Pol III δ subunit for removal . On its own, the β dimer diffuses bidirectionally on DNA in an ATP-independent fashion...

## Biological Role

Component of Hda-β-clamp complex (complex.ecocyc.CPLX0-10342), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Annotation

The β subunit of CPLX0-3803 (DNA Pol III) dimerizes to form the sliding clamp that links the core polymerase to DNA and allows fast, processive DNA replication. It also plays a role in switching to the error-prone polymerases for translesion synthesis and for methyl-directed mismatch repair in response to stress. β binds 3' to an RNA primer at an ssDNA/duplex DNA junction in an ATP-dependent process catalyzed by the preinitiation complex . The presence of β stimulates DNA Pol III activity, resulting in increased product length and processivity . The complete DNA Pol III holoenzyme with both β and ATP is at least twenty times more processive than core enzyme or holoenzyme lacking either of those components . β may contribute to the regulation of replication initiation . Divalent magnesium is required for β to maintain its dimer structure ; the dynamics of the β clamp in solution and its loading dynamics have been investigated. ATP hydrolysis is involved in modulating the binding of the CPLX0-3801 (clamp loading complex) to the β sliding clamp ; the clamp loading complex may actively open the β sliding clamp for loading onto DNA . The β-clamp is very stable on DNA, requiring the ATP-dependent action of DNA Pol III δ subunit for removal . On its own, the β dimer diffuses bidirectionally on DNA in an ATP-independent fashion . β binds to the core polymerase via the seven carboxy-terminal residues of the α subunit . α interacts with the same portion of β as the preinitiation protein δ, displacing δ and the preinitiation complex when it binds . A number of β crystal structures have been evaluated . Based on a structure at 2.5 Å resolution, the β homodimer forms a head-to-tail ring with twelve internal α-helices, and each β monomer has three identical domains . Methylation of I

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10342|complex.ecocyc.CPLX0-10342]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc component coefficient=2

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A988|protein.P0A988]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3761`
- `QSPROTEOME:QS00122807`

## Notes

2*protein.P0A988
