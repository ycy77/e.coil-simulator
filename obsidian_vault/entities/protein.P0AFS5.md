---
entity_id: "protein.P0AFS5"
entity_type: "protein"
name: "tqsA"
source_database: "UniProt"
source_id: "P0AFS5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tqsA ydgG b1601 JW1593"
---

# tqsA

`protein.P0AFS5`

## Static

- Type: `protein`
- Source: `UniProt:P0AFS5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in the transport of the quorum-sensing signal autoinducer 2 (AI-2) (PubMed:16385049). Controls the transport of AI-2 either by enhancing its secretion or inhibiting its uptake and consequently represses biofilm formation and motility and affects the global gene expression in biofilms (PubMed:16385049). {ECO:0000269|PubMed:16385049}. TqsA has been implicated in autoinducer 2 (AI-2) transport - it may be involved in exporting AI-2 or inhibiting its uptake. A tqsA knockout mutant (K-12 BW25113 ΔtqsA::kan) has significantly less extracellular AI-2 activity and signficantly more intracellular AI-2 activity compared to the wild-type strain, and is more resistant than wild-type to a number of drugs. The tqsA knockout increases biofilm formation in M9 glucose media - a phenotype that is complemented by the expression of tqsA in trans . The protein product is predicted to be a mostly α-helical membrane protein with seven or eight transmembrane segments . TqsA is a member of the Autoinducer-2 Exporter (AI-2E) Family of transporters . tqsA: transporter of quorum-sensing signal AI-2 Review:

## Biological Role

Catalyzes TRANS-RXN0-453 (reaction.ecocyc.TRANS-RXN0-453).

## Annotation

FUNCTION: Involved in the transport of the quorum-sensing signal autoinducer 2 (AI-2) (PubMed:16385049). Controls the transport of AI-2 either by enhancing its secretion or inhibiting its uptake and consequently represses biofilm formation and motility and affects the global gene expression in biofilms (PubMed:16385049). {ECO:0000269|PubMed:16385049}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-453|reaction.ecocyc.TRANS-RXN0-453]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1601|gene.b1601]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFS5`
- `KEGG:ecj:JW1593;eco:b1601;ecoc:C3026_09220;`
- `GeneID:93775749;946142;`
- `GO:GO:0005886; GO:0009372; GO:0015562; GO:0055085; GO:1905887`

## Notes

AI-2 transport protein TqsA (Transport of quorum-sensing signal protein)
