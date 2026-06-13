---
entity_id: "reaction.ecocyc.TRANS-RXN0-462"
entity_type: "reaction"
name: "TRANS-RXN0-462"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-462"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-462

`reaction.ecocyc.TRANS-RXN0-462`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-462`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Phosphorylation of hydroxymethylpyrimidine (HMP) by HMP kinase is the first step in a non-essential salvage reaction of the THISYN-PWY pathway. This pathway is common to both E.coli and S. typhimurium and has been extensively studied in both organisms. Salvage of HMP from the culture medium has been experimentally demonstrated in S. typhimurium . EcoCyc reaction equation: HMP -> HMP; direction=LEFT-TO-RIGHT. Phosphorylation of hydroxymethylpyrimidine (HMP) by HMP kinase is the first step in a non-essential salvage reaction of the THISYN-PWY pathway. This pathway is common to both E.coli and S. typhimurium and has been extensively studied in both organisms. Salvage of HMP from the culture medium has been experimentally demonstrated in S. typhimurium .

## Biological Role

Substrates: 4-Amino-5-hydroxymethyl-2-methylpyrimidine (molecule.C01279). Products: 4-Amino-5-hydroxymethyl-2-methylpyrimidine (molecule.C01279).

## Annotation

Phosphorylation of hydroxymethylpyrimidine (HMP) by HMP kinase is the first step in a non-essential salvage reaction of the THISYN-PWY pathway. This pathway is common to both E.coli and S. typhimurium and has been extensively studied in both organisms. Salvage of HMP from the culture medium has been experimentally demonstrated in S. typhimurium .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C01279|molecule.C01279]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01279|molecule.C01279]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-462`

## Notes

HMP -> HMP; direction=LEFT-TO-RIGHT
