---
entity_id: "complex.ecocyc.CPLX0-8555"
entity_type: "complex"
name: "cyclic di-GMP phosphodiesterase PdeK"
source_database: "EcoCyc"
source_id: "CPLX0-8555"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cyclic di-GMP phosphodiesterase PdeK

`complex.ecocyc.CPLX0-8555`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8555`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P37649|protein.P37649]]

## Enriched Summary

The c-di-GMP phosphodiesterase PdeK is involved in the regulation of cellulose biosynthesis. The physical interactions between PdeK, the diguanylate cyclase EG11257-MONOMER DgcC, and the EG12259-MONOMER BcsB subunit of cellulose synthase create a local microenvironment where the c-di-GMP signal is produced and degraded in proximity to its regulatory target, the catalytic subunit of cellulose synthase EG12260-MONOMER BcsA, resulting in local c-di-GMP signaling . PdeK contains an N-terminal periplasmic GAPES3 (gamma-proteobacterial periplasmic sensory) domain followed by a HAMP domain, a degenerate GGDEF domain, and a C-terminal EAL domain . PdeK interacts with BcsB via its transmembrane regions and interacts with DgcC via its periplasmic GAPES3 domain . PdeK belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . The purified cytoplasmic region of PdeK shows c-di-GMP phosphodiesterase in vitro, suggesting that the degenerate GGDEF domain supports catalytic activity. However, deletion of pdeK or point mutations that eliminate catalytic activity have only minor effects under the tested conditions in vivo . pdeK is expressed in LB medium and during stationary phase; expression is higher during growth at 28°C than at 37°C...

## Biological Role

Catalyzes RXN0-4181 (reaction.ecocyc.RXN0-4181).

## Annotation

The c-di-GMP phosphodiesterase PdeK is involved in the regulation of cellulose biosynthesis. The physical interactions between PdeK, the diguanylate cyclase EG11257-MONOMER DgcC, and the EG12259-MONOMER BcsB subunit of cellulose synthase create a local microenvironment where the c-di-GMP signal is produced and degraded in proximity to its regulatory target, the catalytic subunit of cellulose synthase EG12260-MONOMER BcsA, resulting in local c-di-GMP signaling . PdeK contains an N-terminal periplasmic GAPES3 (gamma-proteobacterial periplasmic sensory) domain followed by a HAMP domain, a degenerate GGDEF domain, and a C-terminal EAL domain . PdeK interacts with BcsB via its transmembrane regions and interacts with DgcC via its periplasmic GAPES3 domain . PdeK belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . The purified cytoplasmic region of PdeK shows c-di-GMP phosphodiesterase in vitro, suggesting that the degenerate GGDEF domain supports catalytic activity. However, deletion of pdeK or point mutations that eliminate catalytic activity have only minor effects under the tested conditions in vivo . pdeK is expressed in LB medium and during stationary phase; expression is higher during growth at 28°C than at 37°C . A ΔpdeK strain accumulates more c-di-GMP in the cytoplasm than wild type . PdeK: "phosphodiesterase K"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P37649|protein.P37649]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8555`
- `QSPROTEOME:QS00196493`

## Notes

2*protein.P37649
