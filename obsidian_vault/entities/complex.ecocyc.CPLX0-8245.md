---
entity_id: "complex.ecocyc.CPLX0-8245"
entity_type: "complex"
name: "regulator of CsrB and CsrC decay"
source_database: "EcoCyc"
source_id: "CPLX0-8245"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# regulator of CsrB and CsrC decay

`complex.ecocyc.CPLX0-8245`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8245`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P13518|protein.P13518]]

## Enriched Summary

CsrD controls the degradation of the small RNAs CsrB and CsrC, thereby regulating the activity of CsrA and affecting the expression of CsrA-regulated genes. CsrD itself does not function as a ribonuclease ; instead, it enables the RNase E-mediated degradation of CsrB RNA by counteracting the protection against degradation that is due to the CsrB-CsrA interaction . The dynamics of the Csr signaling cascade has been investigated both by modeling and in vivo . Decay of CsrB and CsrC is stimulated when unphosphorylated CRR-MONOMER EIIAGlc binds to the EAL domain of CsrD. The phosphorylation state of EIIAGlc depends on the carbon source; growth on preferred sources, including glucose, leads to a net dephosphorylation of EIIAGlc and other PTS proteins. Thus, growth on a preferred carbon source promotes decay of CsrB/CsrC . CsrD contains two predicted transmembrane regions flanking a predicted periplasmic GAPES4 (gamma-proteobacterial periplasmic sensory) domain, and GGDEF and EAL signaling domains . The GGDEF and EAL domains lack several highly conserved sites thought to be essential for activity . While the transmembrane domains are not required for activity of CsrD, the GGDEF and EAL domains are. The regulatory activity of CsrD does not involve the signaling molecule c-di-GMP...

## Annotation

CsrD controls the degradation of the small RNAs CsrB and CsrC, thereby regulating the activity of CsrA and affecting the expression of CsrA-regulated genes. CsrD itself does not function as a ribonuclease ; instead, it enables the RNase E-mediated degradation of CsrB RNA by counteracting the protection against degradation that is due to the CsrB-CsrA interaction . The dynamics of the Csr signaling cascade has been investigated both by modeling and in vivo . Decay of CsrB and CsrC is stimulated when unphosphorylated CRR-MONOMER EIIAGlc binds to the EAL domain of CsrD. The phosphorylation state of EIIAGlc depends on the carbon source; growth on preferred sources, including glucose, leads to a net dephosphorylation of EIIAGlc and other PTS proteins. Thus, growth on a preferred carbon source promotes decay of CsrB/CsrC . CsrD contains two predicted transmembrane regions flanking a predicted periplasmic GAPES4 (gamma-proteobacterial periplasmic sensory) domain, and GGDEF and EAL signaling domains . The GGDEF and EAL domains lack several highly conserved sites thought to be essential for activity . While the transmembrane domains are not required for activity of CsrD, the GGDEF and EAL domains are. The regulatory activity of CsrD does not involve the signaling molecule c-di-GMP . CsrD belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . csrD is expressed during exponential growth. A csrD mutant shows strongly reduced expression of dgcC, dgcM and the csgBAC curli structural operon, reduced biofilm formation, as well as reduced CsgD accumulation and csgD mRNA levels . CsrA exerts negative feedback on the expression of CsrD . Genome-wide mRNA levels and stab

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P13518|protein.P13518]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8245`
- `QSPROTEOME:QS00216726`

## Notes

4*protein.P13518
