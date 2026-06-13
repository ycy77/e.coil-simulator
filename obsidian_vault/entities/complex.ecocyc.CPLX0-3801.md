---
entity_id: "complex.ecocyc.CPLX0-3801"
entity_type: "complex"
name: "DNA polymerase III, clamp-loader complex"
source_database: "EcoCyc"
source_id: "CPLX0-3801"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "&beta"
  - "-clamp loading complex"
  - "CLC"
  - "gamma complex"
---

# DNA polymerase III, clamp-loader complex

`complex.ecocyc.CPLX0-3801`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3801`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06710|protein.P06710]], [[protein.P28631|protein.P28631]], [[protein.P28630|protein.P28630]], [[complex.ecocyc.CPLX0-7910|complex.ecocyc.CPLX0-7910]]

## Enriched Summary

The clamp-loader complex (CLC) binds primed ssDNA and loads the CPLX0-3761 onto ssDNA. Following this, the DNA polymerase III (pol III) core enzyme, linked by tau, binds and allows processive DNA polymerization . Several of the CLC subunits are required for binding and initiation of replication. The EG11412-MONOMER delta subunit interacts with the primer-template junction, ensuring proper placement of the CLC at a replication start site . The CLC binds CPLX0-8165 (SSB)-coated DNA with the assistance of associated CPLX0-7910 ψ-χ dimer . The interaction with SSB bound to DNA is a thousand-fold stronger than that with SSB alone; it also enhances the affinity of SSB for DNA, preventing premature dissociation from the initiation site . Contact between the CLC and the β sliding clamp is primarily mediated by the CLC delta subunit, which can bind to the carboxy-termini of β sliding clamp; the CLC can also remove the β sliding clamp from DNA in an ATP-independent manner . Free delta subunits are also present in the cell, possibly acting to remove β sliding clamps from DNA where no polymerase is present . CLC binding to the β sliding clamp does require ATP, suggesting a possible conformational change to reveal the delta subunit . The delta and delta' subunits themselves undergo only minor conformational changes on ATP binding...

## Biological Role

Component of DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Annotation

The clamp-loader complex (CLC) binds primed ssDNA and loads the CPLX0-3761 onto ssDNA. Following this, the DNA polymerase III (pol III) core enzyme, linked by tau, binds and allows processive DNA polymerization . Several of the CLC subunits are required for binding and initiation of replication. The EG11412-MONOMER delta subunit interacts with the primer-template junction, ensuring proper placement of the CLC at a replication start site . The CLC binds CPLX0-8165 (SSB)-coated DNA with the assistance of associated CPLX0-7910 ψ-χ dimer . The interaction with SSB bound to DNA is a thousand-fold stronger than that with SSB alone; it also enhances the affinity of SSB for DNA, preventing premature dissociation from the initiation site . Contact between the CLC and the β sliding clamp is primarily mediated by the CLC delta subunit, which can bind to the carboxy-termini of β sliding clamp; the CLC can also remove the β sliding clamp from DNA in an ATP-independent manner . Free delta subunits are also present in the cell, possibly acting to remove β sliding clamps from DNA where no polymerase is present . CLC binding to the β sliding clamp does require ATP, suggesting a possible conformational change to reveal the delta subunit . The delta and delta' subunits themselves undergo only minor conformational changes on ATP binding . The gamma subunit can also open the β sliding clamp, though less effectively than the delta subunit . Both the gamma and delta' subunits restrict opening of β sliding clamp by the delta subunit in the absence of ATP . The CLC loads β sliding clamp onto template DNA at a rate of 12 per sec, which is fast enough to account for the rate of lagging strand initiation . β sliding clamp loading and CLC release from DNA are both ATP-dependent processes. Each gamm

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (6)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7910|complex.ecocyc.CPLX0-7910]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P06710|protein.P06710]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P28630|protein.P28630]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P28631|protein.P28631]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P28632|protein.P28632]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P28905|protein.P28905]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-3801`
- `QSPROTEOME:QS00183223`

## Notes

3*protein.P06710|1*protein.P28631|1*protein.P28630|complex.ecocyc.CPLX0-7910
