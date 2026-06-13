---
entity_id: "protein.P0AA47"
entity_type: "protein"
name: "plaP"
source_database: "UniProt"
source_id: "P0AA47"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "plaP yeeF b2014 JW5330"
---

# plaP

`protein.P0AA47`

## Static

- Type: `protein`
- Source: `UniProt:P0AA47`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Putrescine importer. Required for induction of type 1 pili-driven surface motility. {ECO:0000269|PubMed:21266585}. PlaP is a low-affinity putrescine importer . PlaP is a member of the APC (amino acid/polyamine/organocation) superfamily and functions as a putrescine:proton symporter . PlaP is required for the induction of type-I pili driven motility induced by putrescine as a signaling molecule (see also ). Expression of plaP decreased in response to treatment with acetate and sodium salicylate . CRP was identified as a repressor for plaP expression using run-off transcription/microarray analysis . The binding site of CRP overlaps the binding site of RNA polymerase . plaP has also shown to be repressed under anaerobic conditions . PlaP and B1296-MONOMER PuuP are receptors for the group 5 CDI ionophore toxins . plaP: putrescine low affinity permease

## Biological Role

Catalyzes putrescine:proton symport (reaction.ecocyc.TRANS-RXN-69). Transports Putrescine (molecule.C00134), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Putrescine importer. Required for induction of type 1 pili-driven surface motility. {ECO:0000269|PubMed:21266585}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-69|reaction.ecocyc.TRANS-RXN-69]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2014|gene.b2014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA47`
- `KEGG:ecj:JW5330;eco:b2014;ecoc:C3026_11360;`
- `GeneID:86860148;93775161;946533;`
- `GO:GO:0005886; GO:0006865; GO:0015295; GO:0015489; GO:0015847; GO:0022857; GO:0048870`

## Notes

Low-affinity putrescine importer PlaP (Putrescine low affinity permease)
