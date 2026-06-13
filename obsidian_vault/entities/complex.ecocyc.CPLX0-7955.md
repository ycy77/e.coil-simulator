---
entity_id: "complex.ecocyc.CPLX0-7955"
entity_type: "complex"
name: "acetate/glycolate:cation symporter"
source_database: "EcoCyc"
source_id: "CPLX0-7955"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acetate/glycolate:cation symporter

`complex.ecocyc.CPLX0-7955`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7955`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32705|protein.P32705]]

## Enriched Summary

ActP (formerly YjcG) is an acetate/glycolate permease in the Solute:Sodium Symporter (SSS) Family (TC:2.A.21). The gene actP is cotranscribed with acs, a gene encoding acetyl coenzyme A synthetase, which is involved in the scavenging of acetate . ActP has been found as a dimer in the inner membrane . Residual acetate uptake is observed in ActP deficient mutants suggesting the possibility of another transporter for this compound - EG11512 "SatP" was characterised as an acetate/succinate symporter by . ActP also contributes to tellurite uptake; ActP catalysed transport occurs during the early stages of exposure to tellurite. A ΔactP strain exhibits increased tolerance to tellurite; a strain overexpressing actP has increased intracellular tellurite levels compared to wild type. actP expression increases slightly during the first 10 minutes of tellurite exposure while pitA and pitB (encoding phosphate transporters) are induced later . ActP (formerly YjcG) is an acetate/glycolate permease in the Solute:Sodium Symporter (SSS) Family (TC:2.A.21). The gene actP is cotranscribed with acs, a gene encoding acetyl coenzyme A synthetase, which is involved in the scavenging of acetate . ActP has been found as a dimer in the inner membrane...

## Biological Role

Catalyzes acetate:Na+ symport (reaction.ecocyc.RXN0-1981), glycolate:Na+ symport (reaction.ecocyc.RXN0-5111), tellurite:Na+ symport (reaction.ecocyc.TRANS-RXN0-576). Transports Acetate (molecule.C00033), Glycolate (molecule.C00160), Sodium cation (molecule.C01330), tellurite (molecule.ecocyc.CPD-4544).

## Annotation

ActP (formerly YjcG) is an acetate/glycolate permease in the Solute:Sodium Symporter (SSS) Family (TC:2.A.21). The gene actP is cotranscribed with acs, a gene encoding acetyl coenzyme A synthetase, which is involved in the scavenging of acetate . ActP has been found as a dimer in the inner membrane . Residual acetate uptake is observed in ActP deficient mutants suggesting the possibility of another transporter for this compound - EG11512 "SatP" was characterised as an acetate/succinate symporter by . ActP also contributes to tellurite uptake; ActP catalysed transport occurs during the early stages of exposure to tellurite. A ΔactP strain exhibits increased tolerance to tellurite; a strain overexpressing actP has increased intracellular tellurite levels compared to wild type. actP expression increases slightly during the first 10 minutes of tellurite exposure while pitA and pitB (encoding phosphate transporters) are induced later .

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1981|reaction.ecocyc.RXN0-1981]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5111|reaction.ecocyc.RXN0-5111]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-576|reaction.ecocyc.TRANS-RXN0-576]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P32705|protein.P32705]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-7955`
- `QSPROTEOME:QS00049453`

## Notes

2*protein.P32705
