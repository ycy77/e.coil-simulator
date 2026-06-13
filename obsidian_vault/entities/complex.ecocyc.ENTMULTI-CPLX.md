---
entity_id: "complex.ecocyc.ENTMULTI-CPLX"
entity_type: "complex"
name: "enterobactin synthase"
source_database: "EcoCyc"
source_id: "ENTMULTI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "enterobactin synthetase multienzyme complex"
---

# enterobactin synthase

`complex.ecocyc.ENTMULTI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ENTMULTI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.ENTB-CPLX|complex.ecocyc.ENTB-CPLX]], [[protein.P19925|protein.P19925]], [[protein.P11454|protein.P11454]], [[complex.ecocyc.ENTE-CPLX|complex.ecocyc.ENTE-CPLX]]

## Enriched Summary

Enterobactin contains three units of 2,3-dihydroxybenzoylserine joined in a cyclic structure by lactone linkages. Studies have suggested that the later steps of enterobactin synthesis are carried out by a multienzyme complex consisting of the entD, entE, entF and entB gene products . Proteins EntB, EntD, EntE and EntF of the enterobactin synthase multienzyme complex have been purified and characterized, but no evidence has been obtained for the existence of a stable multienzyme complex. These proteins are required for the ATP-dependent conversion of three molecules each of 2,3-dihydroxybenzoate and L-serine to enterobactin . Proteins EntB, EntE and EntF together contain domains that comprise a nonribosomal peptide synthase (NRPS). EntE provides an adenylation domain, EntB provides an aryl carrier protein domain (located at its C-terminus), and EntF provides condensation, adenylation, peptidyl carrier protein, and chain-releasing thioesterase domains. Thus, six domains of three proteins comprise a two-module NRPS . EntD is a phosphopantetheinyl transferase that adds this cofactor to the peptidyl carrier protein domains of EntB and EntF . The activities of EntE, the EntB C-terminal domain, and EntF assemble enterobactin in an iterative manner . Enterobactin contains three units of 2,3-dihydroxybenzoylserine joined in a cyclic structure by lactone linkages...

## Biological Role

Catalyzes ENTMULTI-RXN (reaction.ecocyc.ENTMULTI-RXN).

## Annotation

Enterobactin contains three units of 2,3-dihydroxybenzoylserine joined in a cyclic structure by lactone linkages. Studies have suggested that the later steps of enterobactin synthesis are carried out by a multienzyme complex consisting of the entD, entE, entF and entB gene products . Proteins EntB, EntD, EntE and EntF of the enterobactin synthase multienzyme complex have been purified and characterized, but no evidence has been obtained for the existence of a stable multienzyme complex. These proteins are required for the ATP-dependent conversion of three molecules each of 2,3-dihydroxybenzoate and L-serine to enterobactin . Proteins EntB, EntE and EntF together contain domains that comprise a nonribosomal peptide synthase (NRPS). EntE provides an adenylation domain, EntB provides an aryl carrier protein domain (located at its C-terminus), and EntF provides condensation, adenylation, peptidyl carrier protein, and chain-releasing thioesterase domains. Thus, six domains of three proteins comprise a two-module NRPS . EntD is a phosphopantetheinyl transferase that adds this cofactor to the peptidyl carrier protein domains of EntB and EntF . The activities of EntE, the EntB C-terminal domain, and EntF assemble enterobactin in an iterative manner .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ENTMULTI-RXN|reaction.ecocyc.ENTMULTI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (6)

- `is_component_of` <-- [[complex.ecocyc.ENTB-CPLX|complex.ecocyc.ENTB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.ENTE-CPLX|complex.ecocyc.ENTE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0ADI4|protein.P0ADI4]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P10378|protein.P10378]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P11454|protein.P11454]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P19925|protein.P19925]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:ENTMULTI-CPLX`
- `QSPROTEOME:QS00199113`

## Notes

1*complex.ecocyc.ENTB-CPLX|1*protein.P19925|1*protein.P11454|1*complex.ecocyc.ENTE-CPLX
