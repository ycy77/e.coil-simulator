---
entity_id: "complex.ecocyc.NARQ-CPLX"
entity_type: "complex"
name: "sensor histidine kinase NarQ"
source_database: "EcoCyc"
source_id: "NARQ-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase NarQ

`complex.ecocyc.NARQ-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NARQ-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P27896|protein.P27896]]

## Enriched Summary

The E. coli NarQ and NARX-CPLX "NarX" proteins are paralogous sensor kinases that, together with the response regulators NarP and NarL, form a complex signal transduction system which controls anaerobic respiratory gene expression in response to nitrate and nitrite. NarQ reponds to nitrate and nitrite by autophosphorylating at a conserved histidine residue and transferring the phosphoryl group to a conserved aspartate residue of the response regulators NarL and NarP . Studies using the purified cytoplasmic domain of NarX and NarQ suggest a differential interaction with NarL . NarQ consists of two transmembrane helices, an N-terminal periplasmic domain that is responsible for signal ligand binding and a C-terminal cytoplasmic transmitter or output module . The E. coli NarQ and NARX-CPLX "NarX" proteins are paralogous sensor kinases that, together with the response regulators NarP and NarL, form a complex signal transduction system which controls anaerobic respiratory gene expression in response to nitrate and nitrite. NarQ reponds to nitrate and nitrite by autophosphorylating at a conserved histidine residue and transferring the phosphoryl group to a conserved aspartate residue of the response regulators NarL and NarP . Studies using the purified cytoplasmic domain of NarX and NarQ suggest a differential interaction with NarL...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

The E. coli NarQ and NARX-CPLX "NarX" proteins are paralogous sensor kinases that, together with the response regulators NarP and NarL, form a complex signal transduction system which controls anaerobic respiratory gene expression in response to nitrate and nitrite. NarQ reponds to nitrate and nitrite by autophosphorylating at a conserved histidine residue and transferring the phosphoryl group to a conserved aspartate residue of the response regulators NarL and NarP . Studies using the purified cytoplasmic domain of NarX and NarQ suggest a differential interaction with NarL . NarQ consists of two transmembrane helices, an N-terminal periplasmic domain that is responsible for signal ligand binding and a C-terminal cytoplasmic transmitter or output module .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P27896|protein.P27896]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:NARQ-CPLX`
- `QSPROTEOME:QS00049732`

## Notes

2*protein.P27896
