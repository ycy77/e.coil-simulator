---
entity_id: "reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN"
entity_type: "reaction"
name: "2-OXOPENT-4-ENOATE-HYDRATASE-RXN"
source_database: "EcoCyc"
source_id: "2-OXOPENT-4-ENOATE-HYDRATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2-KETO-4-PENTENOATE HYDRATASE"
---

# 2-OXOPENT-4-ENOATE-HYDRATASE-RXN

`reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-OXOPENT-4-ENOATE-HYDRATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the sixth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate. Also acts, more slowly, on cis-2-oxohex-4-enoate, but not on the trans-isomer. This is the sixth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate. EcoCyc reaction equation: 4-HYDROXY-2-KETOVALERATE -> CPD-14447 + WATER; direction=PHYSIOL-RIGHT-TO-LEFT. This is the sixth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate. Also acts, more slowly, on cis-2-oxohex-4-enoate, but not on the trans-isomer. This is the sixth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate.

## Biological Role

Catalyzed by 2-hydroxypentadienoate hydratase (complex.ecocyc.CPLX0-7951). Substrates: 4-Hydroxy-2-oxopentanoate (molecule.C03589). Products: H2O (molecule.C00001), (2Z)-2-hydroxypenta-2,4-dienoate (molecule.ecocyc.CPD-14447).

## Enriched Pathways

- `ecocyc.PWY-5162` 2-hydroxypenta-2,4-dienoate degradation (EcoCyc)

## Annotation

This is the sixth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate. Also acts, more slowly, on cis-2-oxohex-4-enoate, but not on the trans-isomer. This is the sixth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate.

## Pathways

- `ecocyc.PWY-5162` 2-hydroxypenta-2,4-dienoate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7951|complex.ecocyc.CPLX0-7951]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-14447|molecule.ecocyc.CPD-14447]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03589|molecule.C03589]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2-OXOPENT-4-ENOATE-HYDRATASE-RXN`

## Notes

4-HYDROXY-2-KETOVALERATE -> CPD-14447 + WATER; direction=PHYSIOL-RIGHT-TO-LEFT
