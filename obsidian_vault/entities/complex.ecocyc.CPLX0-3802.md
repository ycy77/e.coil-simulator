---
entity_id: "complex.ecocyc.CPLX0-3802"
entity_type: "complex"
name: "DNA polymerase III τ dimer"
source_database: "EcoCyc"
source_id: "CPLX0-3802"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "DNA polymerase III subunit tau"
---

# DNA polymerase III τ dimer

`complex.ecocyc.CPLX0-3802`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3802`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06710|protein.P06710]]

## Enriched Summary

The τ (tau) subunit of CPLX0-3803 has multiple roles. When it binds to EG10238-MONOMER (DnaE), it dimerizes, thus dimerizing the CPLX0-2361 as a consequence . This dimerization of the core polymerase is required for processive lagging strand synthesis . The α subunit of the core of DNA polymerase III binds within the tau carboxy-terminus . Tau interacts with DnaE α subunit at the EG10242-MONOMER binding site with high affinity in the presence of duplex DNA and low affinity in the presence of primed ssDNA. As a consequence, when synthesis is complete tau blocks beta binding, leading to release of polymerase from the beta clamp . Tau also binds the EG10236-MONOMER (DnaB). This requires the fourth of five domains in tau, and leads to binding of the hexameric CPLX0-3621 ([DnaB]6) by more than one tau, suggesting both taus in the polymerase III holoenzyme are bound . This interaction is required to allow DNA synthesis to proceed at its normal rate of one thousand nucleotides per second. Without this interaction, DNA polymerase III moves at the rate of DnaB alone, about thirty-five nucleotides per second . In the absence of tau, leading-strand synthesis by DNA polymerase III is not highly processive and requires an excess of core enzyme...

## Biological Role

Component of DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Annotation

The τ (tau) subunit of CPLX0-3803 has multiple roles. When it binds to EG10238-MONOMER (DnaE), it dimerizes, thus dimerizing the CPLX0-2361 as a consequence . This dimerization of the core polymerase is required for processive lagging strand synthesis . The α subunit of the core of DNA polymerase III binds within the tau carboxy-terminus . Tau interacts with DnaE α subunit at the EG10242-MONOMER binding site with high affinity in the presence of duplex DNA and low affinity in the presence of primed ssDNA. As a consequence, when synthesis is complete tau blocks beta binding, leading to release of polymerase from the beta clamp . Tau also binds the EG10236-MONOMER (DnaB). This requires the fourth of five domains in tau, and leads to binding of the hexameric CPLX0-3621 ([DnaB]6) by more than one tau, suggesting both taus in the polymerase III holoenzyme are bound . This interaction is required to allow DNA synthesis to proceed at its normal rate of one thousand nucleotides per second. Without this interaction, DNA polymerase III moves at the rate of DnaB alone, about thirty-five nucleotides per second . In the absence of tau, leading-strand synthesis by DNA polymerase III is not highly processive and requires an excess of core enzyme . Tau also has an ssDNA-dependent ATPase activity, as well as DNA-DNA and DNA-RNA annealing activities that do not require ATP binding or hydrolysis . Based on the annealing activities, a role for tau in primer stabilization has been suggested . As described in the MONOMER0-2383 summary, DnaX undergoes a programmed -1 frameshift roughly half of the time yielding a new stop codon just after the frameshift point resulting in DnaX-γ. Tau shares the first three of its five domains with the gamma subunit. The third domain is required for oligomeriz

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P06710|protein.P06710]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3802`
- `QSPROTEOME:QS00049613`

## Notes

2*protein.P06710
