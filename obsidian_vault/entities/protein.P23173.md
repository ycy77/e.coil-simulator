---
entity_id: "protein.P23173"
entity_type: "protein"
name: "tnaB"
source_database: "UniProt"
source_id: "P23173"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tnaB trpP b3709 JW5619/JW5622"
---

# tnaB

`protein.P23173`

## Static

- Type: `protein`
- Source: `UniProt:P23173`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in tryptophan transport across the cytoplasmic membrane. Plays a role in transporting tryptophan which is to be used catabolically. TnaB is one of three known transporters for tryptophan in E. coli, the others being MTR-MONOMER Mtr and EG10084 AroP. The tnaB gene is located in an operon with the EG11005 gene, encoding tryptophanase . Transcription of the tnaAB operon is regulated by tryptophan-induced transcriptional antitermination and is subject to catabolite repression . Whole cell transport experiments have indicated that TnaB is a low affinity tryptophan transporter (Km of about 70 μM) . TnaB is a member of the ArAAAP family of amino acid transporters and is homologous to the MTR-MONOMER Mtr and EG11041 TyrP transporters . Examination of EG10617, EG10084 and EG11006 mutants under various growth conditions has shown that TnaB is essential for growth on tryptophan as the sole carbon source and its primary role is probably uptake of tryptophan for catabolic purposes. Imported tryptophan can be utilized as a carbon and nitrogen source following its degradation to indole, pyruvate and ammonia by TRYPTOPHAN-MONOMER.

## Biological Role

Catalyzes tryptophan:proton symport (reaction.ecocyc.TRANS-RXN-76).

## Annotation

FUNCTION: Involved in tryptophan transport across the cytoplasmic membrane. Plays a role in transporting tryptophan which is to be used catabolically.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-76|reaction.ecocyc.TRANS-RXN-76]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3709|gene.b3709]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23173`
- `KEGG:ecj:JW5619;ecj:JW5622;eco:b3709;ecoc:C3026_20110;`
- `GeneID:948220;`
- `GO:GO:0003333; GO:0005886; GO:0006569; GO:0015173; GO:0015293; GO:0022857`

## Notes

Low affinity tryptophan permease
