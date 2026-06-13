---
entity_id: "complex.ecocyc.CPLX0-237"
entity_type: "complex"
name: "serine acetyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-237"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# serine acetyltransferase

`complex.ecocyc.CPLX0-237`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-237`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9D4|protein.P0A9D4]]

## Enriched Summary

Serine acetyltransferase carries out the first step in the pathway of cysteine biosynthesis, converting L-serine into O-acetyl-L-serine. Serine acetyltransferase catalyzes the acetylation of L-serine to generate O-acetyl-L-serine . Cysteine strongly inhibits this activity by binding to the serine-binding site . This inhibition depends on the protein's carboxy terminus, and has been localized to Met-256 specifically . The carboxy-terminus is also required for formation of the complex with O-acetylserine sulhydrylase, as well as for destabilization of the serine acetyltransferase hexamer in cold temperatures . The carboxy-terminus of wild-type serine acetyltransferase is protected from proteolysis in the complexed state . The reaction mechanism of serine acetyltransferase has been examined in detail . Although serine acetyltransferase was identified as a tetramer based on a 3.0 Å-resolution crystal structure, later structural studies indicated that it is actually a dimer of trimers . A crystal structure to 2.2 Å resolution has confirmed this dimer of trimers arrangement . Mutants in cysE show increased biofilm formation. In these mutants, both cysteine and the extracellular signal O-acetylserine inhibit biofilm formation . Serine acetyltransferase carries out the first step in the pathway of cysteine biosynthesis, converting L-serine into O-acetyl-L-serine...

## Biological Role

Catalyzes SERINE-O-ACETTRAN-RXN (reaction.ecocyc.SERINE-O-ACETTRAN-RXN). Component of cysteine synthase complex (complex.ecocyc.CYSSYNMULTI-CPLX).

## Annotation

Serine acetyltransferase carries out the first step in the pathway of cysteine biosynthesis, converting L-serine into O-acetyl-L-serine. Serine acetyltransferase catalyzes the acetylation of L-serine to generate O-acetyl-L-serine . Cysteine strongly inhibits this activity by binding to the serine-binding site . This inhibition depends on the protein's carboxy terminus, and has been localized to Met-256 specifically . The carboxy-terminus is also required for formation of the complex with O-acetylserine sulhydrylase, as well as for destabilization of the serine acetyltransferase hexamer in cold temperatures . The carboxy-terminus of wild-type serine acetyltransferase is protected from proteolysis in the complexed state . The reaction mechanism of serine acetyltransferase has been examined in detail . Although serine acetyltransferase was identified as a tetramer based on a 3.0 Å-resolution crystal structure, later structural studies indicated that it is actually a dimer of trimers . A crystal structure to 2.2 Å resolution has confirmed this dimer of trimers arrangement . Mutants in cysE show increased biofilm formation. In these mutants, both cysteine and the extracellular signal O-acetylserine inhibit biofilm formation .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.SERINE-O-ACETTRAN-RXN|reaction.ecocyc.SERINE-O-ACETTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CYSSYNMULTI-CPLX|complex.ecocyc.CYSSYNMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9D4|protein.P0A9D4]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-237`
- `QSPROTEOME:QS00188425`

## Notes

6*protein.P0A9D4
