---
entity_id: "protein.P37590"
entity_type: "protein"
name: "pmrD"
source_database: "UniProt"
source_id: "P37590"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pmrD b2259 JW2254"
---

# pmrD

`protein.P37590`

## Static

- Type: `protein`
- Source: `UniProt:P37590`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Interacts with phosphorylated BasR protein to mediate transcriptional induction of BasR-activated genes to induce polymyxin resistance in some natural isolates. {ECO:0000269|PubMed:15569938}. PmrD is similar to the Salmonella enterica serovar Typhimurium PmrD, which confers resistance to polymyxin B when it is overexpressed ; in Salmonella, PmrD controls the activity of the PmrA-PmrB two-component system at a post-transcriptional level . E. coli PmrD is functional as a PhoP/PhoQ - PmrA/PmrB connector in Salmonella, but does not function in E. coli . The E. coli and Salmonella PmrD proteins have functionally diverged. In E. coli, PmrD is produced under conditions of low Mg2+ concentration in a PhoP-dependent manner; however, unlike in Salmonella, PmrD does not activate the PmrA-PmrB two-component system (known as PWY0-1482 "BasSR" in E. coli K-12) . This may explain why E. coli is unable to modify its LPS to become resistant to polymyxin B in medium containing low concentrations of Mg2+, such as LB . In addition, PmrA does not repress transcription of E. coli pmrD . Nevertheless, a recent study showed that pmrD expression was partially reduced in a phoP phoQ double mutant and phoP phoQ pmrA and phoP phoQ pmrB triple mutants...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Interacts with phosphorylated BasR protein to mediate transcriptional induction of BasR-activated genes to induce polymyxin resistance in some natural isolates. {ECO:0000269|PubMed:15569938}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2259|gene.b2259]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37590`
- `KEGG:ecj:JW2254;eco:b2259;ecoc:C3026_12620;`
- `GeneID:93774914;945130;`
- `GO:GO:0046677`

## Notes

Signal transduction protein PmrD (BasR post-transcriptional activator) (Polymyxin resistance protein PmrD)
