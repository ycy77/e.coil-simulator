---
entity_id: "reaction.ecocyc.TRANS-RXN0-524"
entity_type: "reaction"
name: "TRANS-RXN0-524"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-524"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-524

`reaction.ecocyc.TRANS-RXN0-524`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-524`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli K-12 can use thymidine as a sole carbon source and thymine can be detected in the culture supernatant when cells are grown under this limitation . This reaction was added based on a reconstructed genome-scale metabolic network of E. coli MG1655 . A transport mechanism has not been described. EcoCyc reaction equation: THYMINE -> THYMINE; direction=PHYSIOL-LEFT-TO-RIGHT. E. coli K-12 can use thymidine as a sole carbon source and thymine can be detected in the culture supernatant when cells are grown under this limitation . This reaction was added based on a reconstructed genome-scale metabolic network of E. coli MG1655 . A transport mechanism has not been described.

## Biological Role

Substrates: Thymine (molecule.C00178). Products: Thymine (molecule.C00178).

## Annotation

E. coli K-12 can use thymidine as a sole carbon source and thymine can be detected in the culture supernatant when cells are grown under this limitation . This reaction was added based on a reconstructed genome-scale metabolic network of E. coli MG1655 . A transport mechanism has not been described.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-524`

## Notes

THYMINE -> THYMINE; direction=PHYSIOL-LEFT-TO-RIGHT
