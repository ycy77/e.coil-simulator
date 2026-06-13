---
entity_id: "complex.ecocyc.CPLX0-1601"
entity_type: "complex"
name: "selenate reductase"
source_database: "EcoCyc"
source_id: "CPLX0-1601"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "YnfFGH"
  - "YnfEFGH"
---

# selenate reductase

`complex.ecocyc.CPLX0-1601`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1601`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77374|protein.P77374]], [[protein.P77783|protein.P77783]], [[protein.P0AAJ1|protein.P0AAJ1]], [[protein.P76173|protein.P76173]]

## Enriched Summary

On the basis of sequence similarity, the ynfEFGH gene cluster is predicted to encode an oxidoreductase complex closely related to the dimethyl sulfoxide reductase heterotrimer DIMESULFREDUCT-CPLX "DmsABC". YnfE and YnfF are both similar to the catalytic subunit DmsA; YnfG is similar to the electron transferring Fe-S containing subunit DmsB and YnfH is similar to the membrane anchor subunit DmsC. A strain carrying a deletion of dmsABC and containing ynfFGH on a multicopy plasmid is able to grow, albeit poorly, under anaerobic conditions utilizing dimethyl sulfoxide as a terminal oxidant . More recently, genetic analysis of E. coli ynfE and ynfF null mutants has implicated the cluster in selenate reduction . E. coli ubiE and menA null mutants are unable to reduce selenate to elemental red selenium in vivo, thus implicating menaquinone in the reductase activity . Similarly, deletion of menC, menD or menE leads to loss of the ability to reduce selenate . On the basis of sequence similarity, the ynfEFGH gene cluster is predicted to encode an oxidoreductase complex closely related to the dimethyl sulfoxide reductase heterotrimer DIMESULFREDUCT-CPLX "DmsABC". YnfE and YnfF are both similar to the catalytic subunit DmsA; YnfG is similar to the electron transferring Fe-S containing subunit DmsB and YnfH is similar to the membrane anchor subunit DmsC...

## Biological Role

Catalyzes RXN-24479 (reaction.ecocyc.RXN-24479).

## Annotation

On the basis of sequence similarity, the ynfEFGH gene cluster is predicted to encode an oxidoreductase complex closely related to the dimethyl sulfoxide reductase heterotrimer DIMESULFREDUCT-CPLX "DmsABC". YnfE and YnfF are both similar to the catalytic subunit DmsA; YnfG is similar to the electron transferring Fe-S containing subunit DmsB and YnfH is similar to the membrane anchor subunit DmsC. A strain carrying a deletion of dmsABC and containing ynfFGH on a multicopy plasmid is able to grow, albeit poorly, under anaerobic conditions utilizing dimethyl sulfoxide as a terminal oxidant . More recently, genetic analysis of E. coli ynfE and ynfF null mutants has implicated the cluster in selenate reduction . E. coli ubiE and menA null mutants are unable to reduce selenate to elemental red selenium in vivo, thus implicating menaquinone in the reductase activity . Similarly, deletion of menC, menD or menE leads to loss of the ability to reduce selenate .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-24479|reaction.ecocyc.RXN-24479]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AAJ1|protein.P0AAJ1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76173|protein.P76173]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77374|protein.P77374]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77783|protein.P77783]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-1601`
- `QSPROTEOME:QS00195315`

## Notes

1*protein.P77374|1*protein.P77783|1*protein.P0AAJ1|1*protein.P76173
