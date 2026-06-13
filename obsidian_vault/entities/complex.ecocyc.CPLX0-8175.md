---
entity_id: "complex.ecocyc.CPLX0-8175"
entity_type: "complex"
name: "sulfurtransferase for molybdenum cofactor sulfuration"
source_database: "EcoCyc"
source_id: "CPLX0-8175"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sulfurtransferase for molybdenum cofactor sulfuration

`complex.ecocyc.CPLX0-8175`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8175`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P32177|protein.P32177]]

## Enriched Summary

FdhD is a sulfur carrier that appears to transfer sulfur from G7325-MONOMER IscS to the molybdenum cofactor prior to its insertion into formate dehydrogenases . FdhD interacts directly with IscS and stimulates its cysteine desulfurate activity . It also binds the molybdenum cofactor (Mo-bisPGD) and GDP (a surrogate for studying Mo-bisPGD binding) . FdhD is required for wild-type FORMATEDEHYDROGN-CPLX (Fdh-N) , FORMATEDEHYDROGO-CPLX (Fdh-O) and FORMATEDEHYDROGH-MONOMER (Fdh-H) activity, but not for synthesis of the Fdh-N protein . A crystal structure of FdhD in complex with GDP has been solved. Structure-guided mutagenesis of residues involved in GDP binding showed that these residues were required for FdhD activity . The conserved C121 residue of FdhD is required for accepting persulfide sufur from IscS and for the ability to activate FORMATEDEHYDROGH-MONOMER . FdhD is soluble and is not a component of the membrane-bound FORMATEDEHYDROGN-CPLX , and is not required for wild-type fdnGHI and fdoGHI transcription. Expression of fdhD is repressed by aerobiosis . FdhD is a sulfur carrier that appears to transfer sulfur from G7325-MONOMER IscS to the molybdenum cofactor prior to its insertion into formate dehydrogenases . FdhD interacts directly with IscS and stimulates its cysteine desulfurate activity...

## Biological Role

Catalyzes RXN-21550 (reaction.ecocyc.RXN-21550), RXN-21562 (reaction.ecocyc.RXN-21562).

## Annotation

FdhD is a sulfur carrier that appears to transfer sulfur from G7325-MONOMER IscS to the molybdenum cofactor prior to its insertion into formate dehydrogenases . FdhD interacts directly with IscS and stimulates its cysteine desulfurate activity . It also binds the molybdenum cofactor (Mo-bisPGD) and GDP (a surrogate for studying Mo-bisPGD binding) . FdhD is required for wild-type FORMATEDEHYDROGN-CPLX (Fdh-N) , FORMATEDEHYDROGO-CPLX (Fdh-O) and FORMATEDEHYDROGH-MONOMER (Fdh-H) activity, but not for synthesis of the Fdh-N protein . A crystal structure of FdhD in complex with GDP has been solved. Structure-guided mutagenesis of residues involved in GDP binding showed that these residues were required for FdhD activity . The conserved C121 residue of FdhD is required for accepting persulfide sufur from IscS and for the ability to activate FORMATEDEHYDROGH-MONOMER . FdhD is soluble and is not a component of the membrane-bound FORMATEDEHYDROGN-CPLX , and is not required for wild-type fdnGHI and fdoGHI transcription. Expression of fdhD is repressed by aerobiosis .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-21550|reaction.ecocyc.RXN-21550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21562|reaction.ecocyc.RXN-21562]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P32177|protein.P32177]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8175`
- `QSPROTEOME:QS00196203`

## Notes

2*protein.P32177
