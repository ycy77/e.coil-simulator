---
entity_id: "protein.P0AGH5"
entity_type: "protein"
name: "sapC"
source_database: "UniProt"
source_id: "P0AGH5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sapC b1292 JW1285"
---

# sapC

`protein.P0AGH5`

## Static

- Type: `protein`
- Source: `UniProt:P0AGH5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides. {ECO:0000269|PubMed:27803167}. SapC is one of two integral membrane subunits of a predicted ATP-binding cassette (ABC)-family transporter complex, SapABCDF, that may be involved in the uptake of a range of molecules, such as antimicrobial peptides, dipeptides and heme . Separately, a CPLX0-13226 SapBCDF complex has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of a ΔsapC strain is significantly reduced compared to wild type . Overexpression of sapC from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide .

## Biological Role

Component of putative antimicrobial peptide ABC transporter (complex.ecocyc.ABC-29-CPLX), putative putrescine ABC exporter (complex.ecocyc.CPLX0-13226).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides. {ECO:0000269|PubMed:27803167}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-29-CPLX|complex.ecocyc.ABC-29-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-13226|complex.ecocyc.CPLX0-13226]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1292|gene.b1292]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGH5`
- `KEGG:ecj:JW1285;eco:b1292;ecoc:C3026_07585;`
- `GeneID:93775417;945266;`
- `GO:GO:0005886; GO:0015489; GO:0015833; GO:0015847; GO:0016020; GO:0055052`

## Notes

Putrescine export system permease protein SapC
