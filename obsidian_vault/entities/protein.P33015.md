---
entity_id: "protein.P33015"
entity_type: "protein"
name: "tsuA"
source_database: "UniProt"
source_id: "P33015"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tsuA yeeE b2013 JW1995"
---

# tsuA

`protein.P33015`

## Static

- Type: `protein`
- Source: `UniProt:P33015`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Mediates thiosulfate uptake. {ECO:0000269|PubMed:32779574, ECO:0000269|PubMed:32923628}. TsuA is an inner membrane protein that imports S2O3 as a sulfur source. Deletion of tsuA inhibits the ability of strains (ΔABC-7-CPLX cysPUWA or ΔEG10183 cysA) lacking the sulfate/thiosulfate ABC-type transporters to grow with thiosulfate as sole sulfur source . EG11894-MONOMER TsuB is required for TsuA-mediated thiosulfate uptake in vivo and the two proteins may physically interact . TsuA is predicted to be an inner membrane protein with nine transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . tsuA is a member of the PC00040 CysB regulon; TsuA may be subject to post-transcriptional control by G7459-MONOMER RppH-dependent mRNA degradation; TsuA supports the preferential use of thiosulfate as a sulfur source in ΔrppH cells . Expression of tsuA is downregulated in response to cobalt and upregulated in response to hydroquinone . Several genes described to be responsive to sulfur availability, including tsuA , were among the most strongly upregulated genes in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . TsuA: "thiosulfate uptake"

## Biological Role

Catalyzes TRANS-RXN-496 (reaction.ecocyc.TRANS-RXN-496).

## Annotation

FUNCTION: Mediates thiosulfate uptake. {ECO:0000269|PubMed:32779574, ECO:0000269|PubMed:32923628}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-496|reaction.ecocyc.TRANS-RXN-496]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2013|gene.b2013]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33015`
- `KEGG:ecj:JW1995;eco:b2013;ecoc:C3026_11355;`
- `GeneID:946526;`
- `GO:GO:0005886; GO:0015117; GO:0015709`

## Notes

Thiosulfate transporter TsuA (Thiosulfate uptake protein A)
