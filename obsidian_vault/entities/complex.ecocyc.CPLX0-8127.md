---
entity_id: "complex.ecocyc.CPLX0-8127"
entity_type: "complex"
name: "2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA thioesterase"
source_database: "EcoCyc"
source_id: "CPLX0-8127"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA thioesterase

`complex.ecocyc.CPLX0-8127`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8127`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P77181|protein.P77181]]

## Enriched Summary

PaaY is a 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA thioesterase. 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA is a compound that is formed spontaneously from CPDMETA-13650, an intermediate of the PWY0-321 pathway, and that inhibits PaaZ activity . The paaY gene is part of the gene cluster required for growth on phenylacetate as the sole source of carbon. Transposon insertions in paaY have no effect on the ability of E. coli W to degrade phenylacetate . However, a paaY mutant shows an extensive lag period when grown on phenylacetate as the sole source of carbon . The E. coli W enzyme is a homotrimer . paaY is co-transcribed with the transcriptional repressor paaX . PaaY activity is increased in cells grown on phenylacetate . PaaY: "phenylacetic acid degradation" PaaY is a 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA thioesterase. 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA is a compound that is formed spontaneously from CPDMETA-13650, an intermediate of the PWY0-321 pathway, and that inhibits PaaZ activity . The paaY gene is part of the gene cluster required for growth on phenylacetate as the sole source of carbon. Transposon insertions in paaY have no effect on the ability of E. coli W to degrade phenylacetate . However, a paaY mutant shows an extensive lag period when grown on phenylacetate as the sole source of carbon . The E. coli W enzyme is a homotrimer...

## Biological Role

Catalyzes RXN0-7103 (reaction.ecocyc.RXN0-7103).

## Annotation

PaaY is a 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA thioesterase. 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA is a compound that is formed spontaneously from CPDMETA-13650, an intermediate of the PWY0-321 pathway, and that inhibits PaaZ activity . The paaY gene is part of the gene cluster required for growth on phenylacetate as the sole source of carbon. Transposon insertions in paaY have no effect on the ability of E. coli W to degrade phenylacetate . However, a paaY mutant shows an extensive lag period when grown on phenylacetate as the sole source of carbon . The E. coli W enzyme is a homotrimer . paaY is co-transcribed with the transcriptional repressor paaX . PaaY activity is increased in cells grown on phenylacetate . PaaY: "phenylacetic acid degradation"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7103|reaction.ecocyc.RXN0-7103]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77181|protein.P77181]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8127`
- `QSPROTEOME:QS00196159`

## Notes

3*protein.P77181
