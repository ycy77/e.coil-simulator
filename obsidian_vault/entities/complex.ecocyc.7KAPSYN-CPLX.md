---
entity_id: "complex.ecocyc.7KAPSYN-CPLX"
entity_type: "complex"
name: "8-amino-7-oxononanoate synthase"
source_database: "EcoCyc"
source_id: "7KAPSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 8-amino-7-oxononanoate synthase

`complex.ecocyc.7KAPSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:7KAPSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P12998|protein.P12998]]

## Enriched Summary

8-Amino-7-oxononanoate synthase catalyzes the decarboxylative condensation of L-alanine and CPD-558 or Pimeloyl-ACPs pimeloyl-[acp] to form 8-AMINO-7-OXONONANOATE . It has been suggested that Pimeloyl-ACPs pimeloyl-[acp] rather than CPD-558 is the physiological substrate . Crystal structures of apo- and PLP-bound 8-amino-7-oxononanoate synthase have been solved, providing a framework for understanding the catalytic mechanism . Further crystallographic and kinetic studies have provided a detailed view of the mechanism. L-alanine initially forms an external aldimine complex with PLP; addition of pimeloyl-CoA leads to formation of a quinonoid intermediate . Expression is repressed by the presence of biotin . Expression of bioF is increased more than 20-fold in a strain containing a ydgG deletion . A bioF mutant shows decreased biofilm formation . 8-Amino-7-oxononanoate synthase catalyzes the decarboxylative condensation of L-alanine and CPD-558 or Pimeloyl-ACPs pimeloyl-[acp] to form 8-AMINO-7-OXONONANOATE . It has been suggested that Pimeloyl-ACPs pimeloyl-[acp] rather than CPD-558 is the physiological substrate . Crystal structures of apo- and PLP-bound 8-amino-7-oxononanoate synthase have been solved, providing a framework for understanding the catalytic mechanism . Further crystallographic and kinetic studies have provided a detailed view of the mechanism...

## Biological Role

Catalyzes 7KAPSYN-RXN (reaction.ecocyc.7KAPSYN-RXN), RXN-11484 (reaction.ecocyc.RXN-11484). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

8-Amino-7-oxononanoate synthase catalyzes the decarboxylative condensation of L-alanine and CPD-558 or Pimeloyl-ACPs pimeloyl-[acp] to form 8-AMINO-7-OXONONANOATE . It has been suggested that Pimeloyl-ACPs pimeloyl-[acp] rather than CPD-558 is the physiological substrate . Crystal structures of apo- and PLP-bound 8-amino-7-oxononanoate synthase have been solved, providing a framework for understanding the catalytic mechanism . Further crystallographic and kinetic studies have provided a detailed view of the mechanism. L-alanine initially forms an external aldimine complex with PLP; addition of pimeloyl-CoA leads to formation of a quinonoid intermediate . Expression is repressed by the presence of biotin . Expression of bioF is increased more than 20-fold in a strain containing a ydgG deletion . A bioF mutant shows decreased biofilm formation .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.7KAPSYN-RXN|reaction.ecocyc.7KAPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11484|reaction.ecocyc.RXN-11484]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P12998|protein.P12998]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:7KAPSYN-CPLX`
- `QSPROTEOME:QS00182711`

## Notes

2*protein.P12998
