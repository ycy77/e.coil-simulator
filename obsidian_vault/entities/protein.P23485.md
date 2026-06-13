---
entity_id: "protein.P23485"
entity_type: "protein"
name: "fecR"
source_database: "UniProt"
source_id: "P23485"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9573190}; Single-pass membrane protein {ECO:0000255}. Note=Contains an internal twin-arginine motif immediately upstream of the transmembrane region which allows it to be translocated across the inner membrane via the Tat system. {ECO:0000269|PubMed:32015149}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fecR b4292 JW4252"
---

# fecR

`protein.P23485`

## Static

- Type: `protein`
- Source: `UniProt:P23485`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9573190}; Single-pass membrane protein {ECO:0000255}. Note=Contains an internal twin-arginine motif immediately upstream of the transmembrane region which allows it to be translocated across the inner membrane via the Tat system. {ECO:0000269|PubMed:32015149}.

## Enriched Summary

FUNCTION: Required for transcriptional activation of the fecABCDE operon by sigma factor FecI (PubMed:2254251, PubMed:7752886). Undergoes sequential cleavage to produce an N-terminal cytoplasmic fragment which is released from the membrane and binds to FecI, allowing it to activate transcription of the fecABCDE operon which mediates ferric citrate transport (PubMed:33865858). In the absence of citrate, FecR inactivates FecI (PubMed:2254251). {ECO:0000269|PubMed:2254251, ECO:0000269|PubMed:33865858, ECO:0000269|PubMed:7752886}. FecR is an inner membrane protein which participates in a trans-envelope signaling pathway to the iron starvation responsive, extracytoplasmic function (ECF) sigma factor, PD00440 FecI; FecR transmits a signal that is initiated by ferric chloride binding to the TonB-dependent outer membrane transporter EG10286-MONOMER FecA; FecR and FecI constitute a non-canonical anti-sigma factor/sigma factor pair; the molecular details of signal transmission remain unclear (see ). FecR is required for FecI-mediated transcriptional regulation of the fec-encoded ferric citrate transport genes (fecABCD); ; (and see ). FecR is a bitopic inner membrane protein, with globular cytoplasmic and periplasmic domains; FecR interacts with the TonB dependent, outer membrane ferric citrate transporter, FecA...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Required for transcriptional activation of the fecABCDE operon by sigma factor FecI (PubMed:2254251, PubMed:7752886). Undergoes sequential cleavage to produce an N-terminal cytoplasmic fragment which is released from the membrane and binds to FecI, allowing it to activate transcription of the fecABCDE operon which mediates ferric citrate transport (PubMed:33865858). In the absence of citrate, FecR inactivates FecI (PubMed:2254251). {ECO:0000269|PubMed:2254251, ECO:0000269|PubMed:33865858, ECO:0000269|PubMed:7752886}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4292|gene.b4292]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23485`
- `KEGG:ecj:JW4252;eco:b4292;ecoc:C3026_23145;`
- `GeneID:949104;`
- `GO:GO:0004888; GO:0005886; GO:0006826; GO:0006879; GO:0023019; GO:2000142`

## Notes

Ferric citrate uptake sigma factor regulator FecR
