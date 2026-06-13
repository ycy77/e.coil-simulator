---
entity_id: "molecule.C04807"
entity_type: "small_molecule"
name: "6-Hydroxymethyl-7,8-dihydropterin diphosphate"
source_database: "KEGG"
source_id: "C04807"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "6-Hydroxymethyl-7,8-dihydropterin diphosphate"
  - "(7,8-Dihydropterin-6-yl)methyl diphosphate"
  - "2-Amino-7,8-dihydro-4-hydroxy-6-(diphosphooxymethyl)pteridine"
  - "2-Amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate"
  - "7,8-Dihydropterin pyrophosphate"
---

# 6-Hydroxymethyl-7,8-dihydropterin diphosphate

`molecule.C04807`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04807`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 6-Hydroxymethyl-7,8-dihydropterin diphosphate; (7,8-Dihydropterin-6-yl)methyl diphosphate; 2-Amino-7,8-dihydro-4-hydroxy-6-(diphosphooxymethyl)pteridine; 2-Amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate; 7,8-Dihydropterin pyrophosphate EcoCyc common name: (7,8-dihydropterin-6-yl)methyl diphosphate. DIHYDROPTERIN-CH2OH-PP (6-hydroxymethyl-dihydropterin diphosphate) is the pterin precursor for the biosynthesis of several important cofactors, including THF, CPD-10763 and CPD-10764. The compound is always synthesized from GTP, but the enzymes involve may differ among organisms.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 6-Hydroxymethyl-7,8-dihydropterin diphosphate; (7,8-Dihydropterin-6-yl)methyl diphosphate; 2-Amino-7,8-dihydro-4-hydroxy-6-(diphosphooxymethyl)pteridine; 2-Amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate; 7,8-Dihydropterin pyrophosphate

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN|reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.H2PTEROATESYNTH-RXN|reaction.ecocyc.H2PTEROATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04807`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
