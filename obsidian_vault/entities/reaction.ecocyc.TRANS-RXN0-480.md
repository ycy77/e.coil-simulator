---
entity_id: "reaction.ecocyc.TRANS-RXN0-480"
entity_type: "reaction"
name: "TRANS-RXN0-480"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-480"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-480

`reaction.ecocyc.TRANS-RXN0-480`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-480`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Growth of E. coli in the presence of labeled selenite and increasing amounts of (unlabeled) selenocysteine results in decreasing incorporation of 75Se into the selenoprotein, formate dehydrogenase, which suggests that E. coli can transport selenocysteine and that it can serve as the selinide donor for selenophosphate formation. EcoCyc reaction equation: L-SELENOCYSTEINE -> L-SELENOCYSTEINE; direction=LEFT-TO-RIGHT. Growth of E. coli in the presence of labeled selenite and increasing amounts of (unlabeled) selenocysteine results in decreasing incorporation of 75Se into the selenoprotein, formate dehydrogenase, which suggests that E. coli can transport selenocysteine and that it can serve as the selinide donor for selenophosphate formation.

## Biological Role

Substrates: L-Selenocysteine (molecule.C05688). Products: L-Selenocysteine (molecule.C05688).

## Annotation

Growth of E. coli in the presence of labeled selenite and increasing amounts of (unlabeled) selenocysteine results in decreasing incorporation of 75Se into the selenoprotein, formate dehydrogenase, which suggests that E. coli can transport selenocysteine and that it can serve as the selinide donor for selenophosphate formation.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C05688|molecule.C05688]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05688|molecule.C05688]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-480`

## Notes

L-SELENOCYSTEINE -> L-SELENOCYSTEINE; direction=LEFT-TO-RIGHT
