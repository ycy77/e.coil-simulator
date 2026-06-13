---
entity_id: "complex.ecocyc.CPLX0-3953"
entity_type: "complex"
name: "30S ribosomal subunit"
source_database: "EcoCyc"
source_id: "CPLX0-3953"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ribosome, small subunit"
---

# 30S ribosomal subunit

`complex.ecocyc.CPLX0-3953`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3953`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AG67|protein.P0AG67]], [[protein.P0A7V0|protein.P0A7V0]], [[protein.P0A7V3|protein.P0A7V3]], [[protein.P0A7V8|protein.P0A7V8]], [[protein.P0A7W1|protein.P0A7W1]], [[protein.P02358|protein.P02358]], [[protein.P02359|protein.P02359]], [[protein.P0A7W7|protein.P0A7W7]], [[protein.P0A7X3|protein.P0A7X3]], [[protein.P0A7R5|protein.P0A7R5]], [[protein.P0A7R9|protein.P0A7R9]], [[protein.P0A7S3|protein.P0A7S3]], [[protein.P0A7S9|protein.P0A7S9]], [[protein.P0AG59|protein.P0AG59]], [[protein.P0ADZ4|protein.P0ADZ4]], [[protein.P0A7T3|protein.P0A7T3]], [[protein.P0AG63|protein.P0AG63]], [[protein.P0A7T7|protein.P0A7T7]], [[protein.P0A7U3|protein.P0A7U3]], [[protein.P0A7U7|protein.P0A7U7]], [[protein.P68679|protein.P68679]]

## Enriched Summary

Assembly and biogenesis of the ribosome and the two subunits, the small 30S and large 50S ribosomal subunits, in E. coli have been ongoing for more than 50 years. Initial studies focused on identification and mapping of proteins involved in vitro (e.g. ). Assembly of the 30S ribosomal subunit has been studied in real time. Initial assembly is linked to the formation of structured 16S rRNA regions, while later steps involve induced fit between ribosomal proteins and the rRNA . Discovery single-particle profiling was used to visualize assembly of the 30S ribosomal subunit by indentifying and following changes among 14 subunit assembly intermediates over time . The kinetically favored assembly pathway of the 30S preinitiation complex has been determined . The function of the ribosomal P site has been reviewed . Assembly and biogenesis of the ribosome and the two subunits, the small 30S and large 50S ribosomal subunits, in E. coli have been ongoing for more than 50 years. Initial studies focused on identification and mapping of proteins involved in vitro (e.g. ). Assembly of the 30S ribosomal subunit has been studied in real time. Initial assembly is linked to the formation of structured 16S rRNA regions, while later steps involve induced fit between ribosomal proteins and the rRNA...

## Biological Role

Component of ribosome (complex.ecocyc.CPLX0-3964).

## Annotation

Assembly and biogenesis of the ribosome and the two subunits, the small 30S and large 50S ribosomal subunits, in E. coli have been ongoing for more than 50 years. Initial studies focused on identification and mapping of proteins involved in vitro (e.g. ). Assembly of the 30S ribosomal subunit has been studied in real time. Initial assembly is linked to the formation of structured 16S rRNA regions, while later steps involve induced fit between ribosomal proteins and the rRNA . Discovery single-particle profiling was used to visualize assembly of the 30S ribosomal subunit by indentifying and following changes among 14 subunit assembly intermediates over time . The kinetically favored assembly pathway of the 30S preinitiation complex has been determined . The function of the ribosomal P site has been reviewed .

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-3964|complex.ecocyc.CPLX0-3964]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (21)

- `is_component_of` <-- [[protein.P02358|protein.P02358]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02359|protein.P02359]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7R5|protein.P0A7R5]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7R9|protein.P0A7R9]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7S3|protein.P0A7S3]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7S9|protein.P0A7S9]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7T3|protein.P0A7T3]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7T7|protein.P0A7T7]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7U3|protein.P0A7U3]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7U7|protein.P0A7U7]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7V0|protein.P0A7V0]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7V3|protein.P0A7V3]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7V8|protein.P0A7V8]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7W1|protein.P0A7W1]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7W7|protein.P0A7W7]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A7X3|protein.P0A7X3]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0ADZ4|protein.P0ADZ4]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0AG59|protein.P0AG59]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0AG63|protein.P0AG63]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0AG67|protein.P0AG67]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P68679|protein.P68679]] `EcoCyc` `database` - EcoCyc component coefficient=

## External IDs

- `EcoCyc:CPLX0-3953`
- `PDB:1P6G`
- `PDB:2AVY`
- `PDB:1P87`

## Notes

protein.P0AG67|protein.P0A7V0|protein.P0A7V3|protein.P0A7V8|protein.P0A7W1|protein.P02358|protein.P02359|protein.P0A7W7|protein.P0A7X3|protein.P0A7R5|protein.P0A7R9|protein.P0A7S3|protein.P0A7S9|protein.P0AG59|protein.P0ADZ4|protein.P0A7T3|protein.P0AG63|protein.P0A7T7|protein.P0A7U3|protein.P0A7U7|protein.P68679
