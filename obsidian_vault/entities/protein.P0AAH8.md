---
entity_id: "protein.P0AAH8"
entity_type: "protein"
name: "sapF"
source_database: "UniProt"
source_id: "P0AAH8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sapF b1290 JW1283"
---

# sapF

`protein.P0AAH8`

## Static

- Type: `protein`
- Source: `UniProt:P0AAH8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides (PubMed:27803167). Does not stimulate K(+) uptake ability of TrkH on its own, but increases K(+) uptake by 20% in the presence of SapD; has no effect of TrkG (PubMed:11700350). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:27803167}. SapF is one of two ATP-binding proteins of a predicted ATP-binding cassette (ABC)-family transporter complex, SapABCDF, that may be involved in the uptake of a range of molecules, such as antimicrobial peptides, dipeptides and heme . Separately, a CPLX0-13226 SapBCDF complex has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of a ΔsapF strain is significantly reduced compared to wild type . SapF contains signature motifs conserved in ATP-binding cassette (ABC) proteins .

## Biological Role

Component of putative antimicrobial peptide ABC transporter (complex.ecocyc.ABC-29-CPLX), putative putrescine ABC exporter (complex.ecocyc.CPLX0-13226).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides (PubMed:27803167). Does not stimulate K(+) uptake ability of TrkH on its own, but increases K(+) uptake by 20% in the presence of SapD; has no effect of TrkG (PubMed:11700350). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:27803167}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-29-CPLX|complex.ecocyc.ABC-29-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-13226|complex.ecocyc.CPLX0-13226]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1290|gene.b1290]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAH8`
- `KEGG:ecj:JW1283;eco:b1290;ecoc:C3026_07575;`
- `GeneID:93775415;945335;`
- `GO:GO:0005524; GO:0005886; GO:0015489; GO:0015833; GO:0015847; GO:0016020; GO:0016887; GO:0055052`

## Notes

Putrescine export system ATP-binding protein SapF
