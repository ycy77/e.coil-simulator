---
entity_id: "complex.ecocyc.CPLX0-3482"
entity_type: "complex"
name: "aldehyde dehydrogenase B"
source_database: "EcoCyc"
source_id: "CPLX0-3482"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aldehyde dehydrogenase B

`complex.ecocyc.CPLX0-3482`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3482`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37685|protein.P37685]]

## Enriched Summary

AldB has NADP-dependent acetaldehyde dehydrogenase activity , which may be identical to the activity detected by Heim and Strehler in crude cell extracts . The enzyme is a homotetramer. Similar to the human liver mitochondrial aldehyde dehydrogenase, MgCl2 increases the enzymatic activity of AldB on a variety of substrates . AldB expression is induced by ethanol and at the beginning of stationary phase and may play a role in detoxifying alcohols and aldehydes present during stationary phase . Based on sequence similarity, AldB was also predicted to be an EC-1.2.1.19 . A transposon insertion in the intergenic region between yiaW and aldB causes increased sensitivity to various antimicrobial drugs, but an aldB deletion mutant shows no such effect . Since AldB is known to be be active upon aromatic aldehydes, it was inactivated together with the five most similar genes (EG10036, EG10110, G6755, G7961, and EG11329) to create a strain with greatly reduced aromatic aldehyde oxidation activity (the strain was named ROAR for reduced oxidation and reduction of aromatic aldehydes) . AldB has NADP-dependent acetaldehyde dehydrogenase activity , which may be identical to the activity detected by Heim and Strehler in crude cell extracts . The enzyme is a homotetramer...

## Biological Role

Catalyzes RXN0-3962 (reaction.ecocyc.RXN0-3962). Bound by Magnesium cation (molecule.C00305).

## Annotation

AldB has NADP-dependent acetaldehyde dehydrogenase activity , which may be identical to the activity detected by Heim and Strehler in crude cell extracts . The enzyme is a homotetramer. Similar to the human liver mitochondrial aldehyde dehydrogenase, MgCl2 increases the enzymatic activity of AldB on a variety of substrates . AldB expression is induced by ethanol and at the beginning of stationary phase and may play a role in detoxifying alcohols and aldehydes present during stationary phase . Based on sequence similarity, AldB was also predicted to be an EC-1.2.1.19 . A transposon insertion in the intergenic region between yiaW and aldB causes increased sensitivity to various antimicrobial drugs, but an aldB deletion mutant shows no such effect . Since AldB is known to be be active upon aromatic aldehydes, it was inactivated together with the five most similar genes (EG10036, EG10110, G6755, G7961, and EG11329) to create a strain with greatly reduced aromatic aldehyde oxidation activity (the strain was named ROAR for reduced oxidation and reduction of aromatic aldehydes) .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3962|reaction.ecocyc.RXN0-3962]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37685|protein.P37685]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-3482`
- `QSPROTEOME:QS00183219`

## Notes

4*protein.P37685
