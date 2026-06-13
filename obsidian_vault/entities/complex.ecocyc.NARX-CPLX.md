---
entity_id: "complex.ecocyc.NARX-CPLX"
entity_type: "complex"
name: "sensor histidine kinase NarX"
source_database: "EcoCyc"
source_id: "NARX-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase NarX

`complex.ecocyc.NARX-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NARX-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P0AFA2|protein.P0AFA2]]

## Enriched Summary

The E. coli NarX and NARQ-CPLX "NarQ" proteins are paralogous sensor kinases that, together with the response regulators NarL and NarP, form a complex signal transduction system which controls anaerobic respiratory gene expression in response to nitrate and nitrite. Early experiments implicated NarX as the sensing component of a two-component regulatory system controlling nitrate regulation of gene expression Purified NarX acts as an ATP-dependent autokinase that transfers the resulting phosphoryl group to NarL; purified NarX also enhances the rate of dephosphorylation of NarL-phosphate (see also . Both sensor kinases, NarX and NarQ, communicate with both response regulators, NarP and NarL to regulate target operon expression in response to nitrate and nitrite; in response to nitrate NarX phosphorylates both regulators; in response to nitrite NarX phosphorylates NarP but acts primarily as a NarL-phosphate phosphatase . Nar X detects nitrate or nitrite in the periplasm and transmits signal across its membrane domain to the cytoplasmic domain . Autophosphorylation of NarX is stimulated 6-fold and 3-fold by nitrate and nitrite respectively (see also ). NarX has a greater preference for its cognate partner NarL over the non-cognate NarP; the NarX-NarL and NarQ-NarP cross regulatory network is asymmetric in nature (see also )...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN), RXN0-7297 (reaction.ecocyc.RXN0-7297).

## Annotation

The E. coli NarX and NARQ-CPLX "NarQ" proteins are paralogous sensor kinases that, together with the response regulators NarL and NarP, form a complex signal transduction system which controls anaerobic respiratory gene expression in response to nitrate and nitrite. Early experiments implicated NarX as the sensing component of a two-component regulatory system controlling nitrate regulation of gene expression Purified NarX acts as an ATP-dependent autokinase that transfers the resulting phosphoryl group to NarL; purified NarX also enhances the rate of dephosphorylation of NarL-phosphate (see also . Both sensor kinases, NarX and NarQ, communicate with both response regulators, NarP and NarL to regulate target operon expression in response to nitrate and nitrite; in response to nitrate NarX phosphorylates both regulators; in response to nitrite NarX phosphorylates NarP but acts primarily as a NarL-phosphate phosphatase . Nar X detects nitrate or nitrite in the periplasm and transmits signal across its membrane domain to the cytoplasmic domain . Autophosphorylation of NarX is stimulated 6-fold and 3-fold by nitrate and nitrite respectively (see also ). NarX has a greater preference for its cognate partner NarL over the non-cognate NarP; the NarX-NarL and NarQ-NarP cross regulatory network is asymmetric in nature (see also ). NarX undergoes intermolecular autophosphorylation in which one subunit of the NarX dimer binds ATP and phosphorylates the other subunit; NarX and NarQ do not form functional heterodimers . NarX contains two predicted transmembrane domains located near the amino terminus which bound a predicted periplasmic domain that is responsible for signal ligand binding and a C-terminal cytoplasmic transmitter or output module (see . The crystal structure of the se

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7297|reaction.ecocyc.RXN0-7297]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AFA2|protein.P0AFA2]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:NARX-CPLX`
- `QSPROTEOME:QS00049733`

## Notes

2*protein.P0AFA2
