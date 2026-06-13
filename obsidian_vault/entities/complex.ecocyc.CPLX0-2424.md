---
entity_id: "complex.ecocyc.CPLX0-2424"
entity_type: "complex"
name: "DNA topoisomerase IV"
source_database: "EcoCyc"
source_id: "CPLX0-2424"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Topo IV"
---

# DNA topoisomerase IV

`complex.ecocyc.CPLX0-2424`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2424`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P20083|protein.P20083]], [[protein.P0AFI2|protein.P0AFI2]]

## Enriched Summary

E. coli possess multiple DNA topoisomerases which coordinate, as well as compete, in order to maintain chromosomes in the appropriate topological state commensurate with their need for replication and transcription. Topoisomerase IV (Topo IV) belongs to the type II topoisomerase family along with CPLX0-2425. Topo IV can remove double-stranded DNA crossings . It is essential for progression of the replication fork and chromosome segregation after replication . Topoisomerase IV decatenates the two daughter molecules after DNA replication and is able to relax both positive and negative DNA supercoils. Positive supercoils are relaxed at a 20-fold faster rate than negative supercoils . There are several Topo IV cleavage site determinants that are found throughout the genome . TopoIV, as well as DNA gyrase, appear to preferentially bind positively supercoiled DNA regions, to bind more strongly near the origin and weaker near the terminus, and is enriched downstream of active transcription units . Topo IV does have two strong non-canonical cleavage signals near the dif site of TERC . The minimum duplex length for topoisomerase IV function is 40 bp . Active Topo IV is a complex of two subunits each of the ParC and ParE polypeptides . The enzyme is ATP-dependent. Synthesized compounds that inhibit Topo IV are under intensive study in order to develop new antibiotics . Reviews: . E...

## Annotation

E. coli possess multiple DNA topoisomerases which coordinate, as well as compete, in order to maintain chromosomes in the appropriate topological state commensurate with their need for replication and transcription. Topoisomerase IV (Topo IV) belongs to the type II topoisomerase family along with CPLX0-2425. Topo IV can remove double-stranded DNA crossings . It is essential for progression of the replication fork and chromosome segregation after replication . Topoisomerase IV decatenates the two daughter molecules after DNA replication and is able to relax both positive and negative DNA supercoils. Positive supercoils are relaxed at a 20-fold faster rate than negative supercoils . There are several Topo IV cleavage site determinants that are found throughout the genome . TopoIV, as well as DNA gyrase, appear to preferentially bind positively supercoiled DNA regions, to bind more strongly near the origin and weaker near the terminus, and is enriched downstream of active transcription units . Topo IV does have two strong non-canonical cleavage signals near the dif site of TERC . The minimum duplex length for topoisomerase IV function is 40 bp . Active Topo IV is a complex of two subunits each of the ParC and ParE polypeptides . The enzyme is ATP-dependent. Synthesized compounds that inhibit Topo IV are under intensive study in order to develop new antibiotics . Reviews: .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0AFI2|protein.P0AFI2]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P20083|protein.P20083]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-2424`
- `QSPROTEOME:QS00127193`

## Notes

2*protein.P20083|2*protein.P0AFI2
