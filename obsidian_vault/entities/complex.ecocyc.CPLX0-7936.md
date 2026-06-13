---
entity_id: "complex.ecocyc.CPLX0-7936"
entity_type: "complex"
name: "5-phospho-α-D-ribosyl 1,2-cyclic phosphate phosphodiesterase"
source_database: "EcoCyc"
source_id: "CPLX0-7936"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 5-phospho-α-D-ribosyl 1,2-cyclic phosphate phosphodiesterase

`complex.ecocyc.CPLX0-7936`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7936`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16692|protein.P16692]]

## Enriched Summary

PhnP is a 5-phospho-α-D-ribosyl 1,2-cyclic phosphate phosphodiesterase. 5-phospho-α-D-ribosyl 1,2-cyclic phosphate is an intermediate in the catabolism of organophosphonates . Phosphodiesterase activity towards bis(p-nitrophenyl)phosphate and 2',3'-cyclic nucleotides was first shown by . The pathway for the catabolism of phosphonates has been elucidated . phnP is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . Crystal structures of PhnP have been solved . The H200 residue was thought to provide the general acid for catalysis; however, results from site-directed mutagenesis of that residue indicate a different role. An alternate reaction mechanism has been proposed . PhnP is a 5-phospho-α-D-ribosyl 1,2-cyclic phosphate phosphodiesterase. 5-phospho-α-D-ribosyl 1,2-cyclic phosphate is an intermediate in the catabolism of organophosphonates . Phosphodiesterase activity towards bis(p-nitrophenyl)phosphate and 2',3'-cyclic nucleotides was first shown by . The pathway for the catabolism of phosphonates has been elucidated . phnP is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . Crystal structures of PhnP have been solved...

## Biological Role

Catalyzes phosphoribosyl 1,2-cyclic phosphodiesterase (reaction.ecocyc.RXN0-6710). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

PhnP is a 5-phospho-α-D-ribosyl 1,2-cyclic phosphate phosphodiesterase. 5-phospho-α-D-ribosyl 1,2-cyclic phosphate is an intermediate in the catabolism of organophosphonates . Phosphodiesterase activity towards bis(p-nitrophenyl)phosphate and 2',3'-cyclic nucleotides was first shown by . The pathway for the catabolism of phosphonates has been elucidated . phnP is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . Crystal structures of PhnP have been solved . The H200 residue was thought to provide the general acid for catalysis; however, results from site-directed mutagenesis of that residue indicate a different role. An alternate reaction mechanism has been proposed .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6710|reaction.ecocyc.RXN0-6710]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P16692|protein.P16692]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7936`
- `QSPROTEOME:QS00181817`

## Notes

2*protein.P16692
