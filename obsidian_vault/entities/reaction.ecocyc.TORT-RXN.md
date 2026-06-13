---
entity_id: "reaction.ecocyc.TORT-RXN"
entity_type: "reaction"
name: "TORT-RXN"
source_database: "EcoCyc"
source_id: "TORT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TORT-RXN

`reaction.ecocyc.TORT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TORT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction the inducer-binding protein TorT is bound to the inducer TMAO. This is the first step in the induction of the torCAD operon. Expression of the torCAD operon encoding TMAO reductase requires three signal transducting steps involving TorT, a periplasmic inducer-binding protein, TorS, a sensor kinase-phosphotransferase, and TorR, a transcriptional regulatory protein. Experimental evidence suggests that TMAO binds with the TorT protein. This protein-ligand complex then interacts with the TorS sensor protein, possibly to activate it. Subsequently TorS further activated by autophosphorylation activates the transcriptional regulator, TorR. EcoCyc reaction equation: TRIMETHYLAMINE-N-O + TORT-MONOMER -> BOUND-TORT; direction=. In this reaction the inducer-binding protein TorT is bound to the inducer TMAO. This is the first step in the induction of the torCAD operon. Expression of the torCAD operon encoding TMAO reductase requires three signal transducting steps involving TorT, a periplasmic inducer-binding protein, TorS, a sensor kinase-phosphotransferase, and TorR, a transcriptional regulatory protein. Experimental evidence suggests that TMAO binds with the TorT protein. This protein-ligand complex then interacts with the TorS sensor protein, possibly to activate it...

## Biological Role

Substrates: Trimethylamine N-oxide (molecule.C01104).

## Annotation

In this reaction the inducer-binding protein TorT is bound to the inducer TMAO. This is the first step in the induction of the torCAD operon. Expression of the torCAD operon encoding TMAO reductase requires three signal transducting steps involving TorT, a periplasmic inducer-binding protein, TorS, a sensor kinase-phosphotransferase, and TorR, a transcriptional regulatory protein. Experimental evidence suggests that TMAO binds with the TorT protein. This protein-ligand complex then interacts with the TorS sensor protein, possibly to activate it. Subsequently TorS further activated by autophosphorylation activates the transcriptional regulator, TorR.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_substrate_of` <-- [[molecule.C01104|molecule.C01104]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TORT-RXN`

## Notes

TRIMETHYLAMINE-N-O + TORT-MONOMER -> BOUND-TORT; direction=
