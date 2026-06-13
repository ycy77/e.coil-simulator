---
entity_id: "protein.E2JKY7"
entity_type: "protein"
name: "mgtL"
source_database: "UniProt"
source_id: "E2JKY7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mgtL b4702 JW4200.1"
---

# mgtL

`protein.E2JKY7`

## Static

- Type: `protein`
- Source: `UniProt:E2JKY7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Makes mgtA transcription sensitive to intracellular proline levels. Under low levels of proline this protein cannot be fully translated, and a stem loop forms which permits transcription of the downstream mgtA gene (By similarity). {ECO:0000250}. MgtL functions as a leader peptide, affecting the expression of MgtA in response to magnesium ion levels . The MgtL peptide contains an N-terminal region that acts as a translation-aborting sequence. Mutations that change the residues EPDP, and in particular the acidic residues E and D, lead to increased translation through this region, while translation aborts more frequently in a ΔEG10889 rpmE strain. Both in vitro and in vivo, addition of increasing levels of Mg2+ lead to a decrease in aborted translation of MgtL. This effect is dependent on the presence of the N-terminal MEPDPT sequence and RpmE. Thus, the N-terminal region of MgtL appears to act as an intrinsic ribosome-destabilizing element. Translation of MgtA is directly correlated with aborted translation of MgtL. Regulation of MgtA expression via the MgtL leader peptide was first investigated in Salmonella enterica; regulation by Mg2+ levels appears to be the result of transcription attenuation .

## Annotation

FUNCTION: Makes mgtA transcription sensitive to intracellular proline levels. Under low levels of proline this protein cannot be fully translated, and a stem loop forms which permits transcription of the downstream mgtA gene (By similarity). {ECO:0000250}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4702|gene.b4702]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:E2JKY7`
- `KEGG:eco:b4702;`
- `GeneID:86861359;93777583;9797237;`
- `GO:GO:0031556; GO:0032026`

## Notes

mgtA leader peptide (Regulatory leader peptide for mgtA)
