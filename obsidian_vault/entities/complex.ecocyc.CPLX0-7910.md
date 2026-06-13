---
entity_id: "complex.ecocyc.CPLX0-7910"
entity_type: "complex"
name: "DNA polymerase III, ψ-χ dimer"
source_database: "EcoCyc"
source_id: "CPLX0-7910"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA polymerase III, ψ-χ dimer

`complex.ecocyc.CPLX0-7910`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7910`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P28905|protein.P28905]], [[protein.P28632|protein.P28632]]

## Enriched Summary

The ψ-χ dimer is an accessory protein that significantly enhances the ability of the CPLX0-3801 to bind template DNA and initiate replication. ψ-χ acts in multiple ways to improve polymerase binding and subsequent activity. The dimer interacts directly with single-strand binding protein (SSB) via binding to the carboxy-terminus of SSB . This increases the overall affinity of the clamp-loader complex for SSB-bound template . The interaction between the ψ subunit of ψ-χ and the clamp-loader complex also stabilizes the high-DNA-affinity, post-ATP state of the clamp-loader complex, helping maintain the complex's affinity for template DNA . Finally, the binding of the χ subunit to SSB disrupts the SSB-primase interaction, aiding release of primase from the primer, thus paving the way for the initiation of replication . ψ-χ interacts with the clamp-loader complex via binding of the ψ amino-terminus to the complex. A 3.5 Å structure of the isolated ψ amino-terminus bound to this complex suggests tight binding . Crystal structures of the ψ-χ dimer are available . The ψ-χ dimer is an accessory protein that significantly enhances the ability of the CPLX0-3801 to bind template DNA and initiate replication. ψ-χ acts in multiple ways to improve polymerase binding and subsequent activity...

## Biological Role

Component of DNA polymerase III, clamp-loader complex (complex.ecocyc.CPLX0-3801), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Annotation

The ψ-χ dimer is an accessory protein that significantly enhances the ability of the CPLX0-3801 to bind template DNA and initiate replication. ψ-χ acts in multiple ways to improve polymerase binding and subsequent activity. The dimer interacts directly with single-strand binding protein (SSB) via binding to the carboxy-terminus of SSB . This increases the overall affinity of the clamp-loader complex for SSB-bound template . The interaction between the ψ subunit of ψ-χ and the clamp-loader complex also stabilizes the high-DNA-affinity, post-ATP state of the clamp-loader complex, helping maintain the complex's affinity for template DNA . Finally, the binding of the χ subunit to SSB disrupts the SSB-primase interaction, aiding release of primase from the primer, thus paving the way for the initiation of replication . ψ-χ interacts with the clamp-loader complex via binding of the ψ amino-terminus to the complex. A 3.5 Å structure of the isolated ψ amino-terminus bound to this complex suggests tight binding . Crystal structures of the ψ-χ dimer are available .

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3801|complex.ecocyc.CPLX0-3801]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc component coefficient=2

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P28632|protein.P28632]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P28905|protein.P28905]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-7910`
- `PDB:1EM8`
- `PDB:3SXU`
- `QSPROTEOME:QS00181715`

## Notes

1*protein.P28905|1*protein.P28632
