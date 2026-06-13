---
entity_id: "complex.ecocyc.RUVABC-CPLX"
entity_type: "complex"
name: "resolvasome"
source_database: "EcoCyc"
source_id: "RUVABC-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "RuvABC"
---

# resolvasome

`complex.ecocyc.RUVABC-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RUVABC-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A814|protein.P0A814]], [[protein.P0A812|protein.P0A812]], [[protein.P0A809|protein.P0A809]]

## Enriched Summary

The E. coli 'resolvasome' is an enzymatic complex of 3 proteins - RuvA, RuvB and RuvC - which function together to resolve Holliday junctions formed during the recombinational repair of damaged double strand DNA. The RuvAB complex also plays an important role in the rescue of blocked DNA replication forks via a process known as replication fork reversal . Overexpressed purified RuvA is tetrameric in solution and binds both single and double strand DNA . Purified RuvB has a low ATPase activity which is enhanced by RuvA in the presence of DNA . In the presence of ATP, RuvA and RuvB promote branch migration and the dissociation of synthetic Holliday structures and recombination intermediates made by RecA . RuvC interacts with synthetic Holliday junctions and RecA mediated intermediates in vitro and promotes their resolution by introducing nicks into two homologous strands of the same polarity . RuvC resolves recombination intermediates at specific sites with the consensus sequence 5'(A/T)TT(G/C)3' . RuvC binds its DNA substrate as a dimer . RuvA and RuvB interact in solution as well as at Holliday junctions . RuvA and RuvB form a complex comprised of a tetramer of RuvA and two hexamers of RuvB . RuvB interacts directly with RuvC in an in vitro reconstituted system for the formation and resolution of Holliday junctions...

## Annotation

The E. coli 'resolvasome' is an enzymatic complex of 3 proteins - RuvA, RuvB and RuvC - which function together to resolve Holliday junctions formed during the recombinational repair of damaged double strand DNA. The RuvAB complex also plays an important role in the rescue of blocked DNA replication forks via a process known as replication fork reversal . Overexpressed purified RuvA is tetrameric in solution and binds both single and double strand DNA . Purified RuvB has a low ATPase activity which is enhanced by RuvA in the presence of DNA . In the presence of ATP, RuvA and RuvB promote branch migration and the dissociation of synthetic Holliday structures and recombination intermediates made by RecA . RuvC interacts with synthetic Holliday junctions and RecA mediated intermediates in vitro and promotes their resolution by introducing nicks into two homologous strands of the same polarity . RuvC resolves recombination intermediates at specific sites with the consensus sequence 5'(A/T)TT(G/C)3' . RuvC binds its DNA substrate as a dimer . RuvA and RuvB interact in solution as well as at Holliday junctions . RuvA and RuvB form a complex comprised of a tetramer of RuvA and two hexamers of RuvB . RuvB interacts directly with RuvC in an in vitro reconstituted system for the formation and resolution of Holliday junctions . Mutations in ruvA, ruvB or ruvC increase sensitivity to UV light, ionizing radiation and mitomycin C . ruvA and ruvB were found to be organized into an SOS-inducible operon but ruvC belongs to an adjacent, non-inducible operon . Reviews:

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0A809|protein.P0A809]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P0A812|protein.P0A812]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P0A814|protein.P0A814]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:RUVABC-CPLX`

## Notes

2*protein.P0A814|12*protein.P0A812|4*protein.P0A809
