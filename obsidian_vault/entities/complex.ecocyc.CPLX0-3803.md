---
entity_id: "complex.ecocyc.CPLX0-3803"
entity_type: "complex"
name: "DNA polymerase III, holoenzyme"
source_database: "EcoCyc"
source_id: "CPLX0-3803"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA polymerase III, holoenzyme

`complex.ecocyc.CPLX0-3803`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3803`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-2361|complex.ecocyc.CPLX0-2361]], [[complex.ecocyc.CPLX0-3801|complex.ecocyc.CPLX0-3801]], [[complex.ecocyc.CPLX0-3761|complex.ecocyc.CPLX0-3761]], [[complex.ecocyc.CPLX0-3802|complex.ecocyc.CPLX0-3802]], [[complex.ecocyc.CPLX0-7910|complex.ecocyc.CPLX0-7910]]

## Enriched Summary

DNA polymerase III holoenzyme is the enzyme primarily responsible for replicative DNA synthesis in E. coli. It carries out primer-initiated 5' to 3' polymerization of DNA on a single-stranded DNA template, as well as 3' to 5' exonucleolytic editing of mispaired nucleotides. Replicative DNA polymerization begins when the preinitiation complex binds single-stranded DNA near an RNA primer. The preinitiation complex then loads the beta processivity clamp onto the DNA at this site, after which three core polymerases, chaperoned into place by the tau subunit, bind to the processivity clamp, with one polymerase on the leading strand and two on the lagging. DNA is synthesized 5' to 3' from primers on both the leading and lagging strands, covalently attaching the newly synthesized DNA to the primer. Tau displaces beta in the presence of duplex DNA, dissociating the polymerase from the template when it reaches a temporary stop on the lagging strand or when synthesis is complete on either strand . For more detailed discussion of the stages of polymerase binding and DNA synthesis, see the individual entries for CPLX0-3801, CPLX0-3761, CPLX0-3802, CPLX0-2361 and their constituent parts...

## Biological Role

Component of replisome (complex.ecocyc.CPLX0-13320).

## Annotation

DNA polymerase III holoenzyme is the enzyme primarily responsible for replicative DNA synthesis in E. coli. It carries out primer-initiated 5' to 3' polymerization of DNA on a single-stranded DNA template, as well as 3' to 5' exonucleolytic editing of mispaired nucleotides. Replicative DNA polymerization begins when the preinitiation complex binds single-stranded DNA near an RNA primer. The preinitiation complex then loads the beta processivity clamp onto the DNA at this site, after which three core polymerases, chaperoned into place by the tau subunit, bind to the processivity clamp, with one polymerase on the leading strand and two on the lagging. DNA is synthesized 5' to 3' from primers on both the leading and lagging strands, covalently attaching the newly synthesized DNA to the primer. Tau displaces beta in the presence of duplex DNA, dissociating the polymerase from the template when it reaches a temporary stop on the lagging strand or when synthesis is complete on either strand . For more detailed discussion of the stages of polymerase binding and DNA synthesis, see the individual entries for CPLX0-3801, CPLX0-3761, CPLX0-3802, CPLX0-2361 and their constituent parts. DNA polymerase III binds a region about 30 nucleotides long upstream of the RNA primer, with the alpha subunit making contact 9 nucleotides upstream and the beta clamp making contact 22 nucleotides upstream . The preinitiation complex binds an area larger than this prior to being displaced by the core polymerase . In the presence of DNA polymerase III, RNA primer length is limited to 10 nucleotides, a limitation that is independent of the epsilon-mediated 3' to 5' exonuclease activity . During polymerization, DNA polymerase III pauses at sites of potential secondary structure . The holoenzyme can tra

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (14)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-2361|complex.ecocyc.CPLX0-2361]] `EcoCyc` `database` - EcoCyc component coefficient=3
- `is_component_of` <-- [[complex.ecocyc.CPLX0-3761|complex.ecocyc.CPLX0-3761]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[complex.ecocyc.CPLX0-3801|complex.ecocyc.CPLX0-3801]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-3802|complex.ecocyc.CPLX0-3802]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-7910|complex.ecocyc.CPLX0-7910]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P03007|protein.P03007]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P06710|protein.P06710]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A988|protein.P0A988]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P0ABS8|protein.P0ABS8]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P10443|protein.P10443]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P28630|protein.P28630]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P28631|protein.P28631]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P28632|protein.P28632]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P28905|protein.P28905]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-3803`
- `PDB:4GX9`
- `PDB:4GX8`
- `PDB:5FKW`
- `PDB:5FKV`
- `PDB:5FKU`
- `PDB:5M1S`

## Notes

3*complex.ecocyc.CPLX0-2361|1*complex.ecocyc.CPLX0-3801|2*complex.ecocyc.CPLX0-3761|1*complex.ecocyc.CPLX0-3802|2*complex.ecocyc.CPLX0-7910
