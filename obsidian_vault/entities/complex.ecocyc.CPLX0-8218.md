---
entity_id: "complex.ecocyc.CPLX0-8218"
entity_type: "complex"
name: "diguanylate cyclase DosC"
source_database: "EcoCyc"
source_id: "CPLX0-8218"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# diguanylate cyclase DosC

`complex.ecocyc.CPLX0-8218`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8218`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AA89|protein.P0AA89]]

## Enriched Summary

The DosC protein is composed of an N-terminal sensory globin domain that binds heme in an apolar binding pocket, a middle domain, and a C-terminal GGDEF diguanylate cyclase domain. DosC binds oxygen with a Kd of 10-20 µM . Diguanylate cyclase activity of DosC was shown in a coupled assay together with the DosP c-di-GMP phosphodiesterase . Crystal structures of individual domains of DosC in several forms have been solved. A structure of the homodimeric full-length protein was proposed based on the structures of the individual domains . The catalytic properties of DosC under various heme loading conditions have been determined; the Fe(III) and Fe(II)-O2 complexes have diguanylate cyclase activity. The enzyme has very low turnover numbers . Tyr43 is required for oxygen recognition , and Leu63 is required for stability of the heme Fe(II)-O2 complex . The Fe(II)-CO form of the heme domain is quite rigid; mutations in Leu65 further reduce the flexibility of the heme domain, while mutations of the Tyr43 increase the flexibility . Overexpression of DosC leads to increased levels of c-di-GMP in the cell and has a deleterious effect on cell division, increases biofilm formation and decreases motility . DosC stimulates expression of csgBAC and pgaABCD...

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Annotation

The DosC protein is composed of an N-terminal sensory globin domain that binds heme in an apolar binding pocket, a middle domain, and a C-terminal GGDEF diguanylate cyclase domain. DosC binds oxygen with a Kd of 10-20 µM . Diguanylate cyclase activity of DosC was shown in a coupled assay together with the DosP c-di-GMP phosphodiesterase . Crystal structures of individual domains of DosC in several forms have been solved. A structure of the homodimeric full-length protein was proposed based on the structures of the individual domains . The catalytic properties of DosC under various heme loading conditions have been determined; the Fe(III) and Fe(II)-O2 complexes have diguanylate cyclase activity. The enzyme has very low turnover numbers . Tyr43 is required for oxygen recognition , and Leu63 is required for stability of the heme Fe(II)-O2 complex . The Fe(II)-CO form of the heme domain is quite rigid; mutations in Leu65 further reduce the flexibility of the heme domain, while mutations of the Tyr43 increase the flexibility . Overexpression of DosC leads to increased levels of c-di-GMP in the cell and has a deleterious effect on cell division, increases biofilm formation and decreases motility . DosC stimulates expression of csgBAC and pgaABCD . Deletion of dosC partially restores motility of a yhjH mutant, suggesting that DosC is one of four diguanylate cyclases that adjust c-di-GMP concentration for motility control . However, DosC does not appear to act as a global regulator of gene expression . More recently, dgcO (dosC), G6972 and G6673 expression were upregulated. Deletion of dgcO and dgcM resulted in decreased swarming motility, with dgcO having the most significant effect, likely due to the concomitant decrease in the exopolysaccharide colanic acid which provides s

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AA89|protein.P0AA89]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8218`
- `QSPROTEOME:QS00049687`

## Notes

2*protein.P0AA89
