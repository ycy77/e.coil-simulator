---
entity_id: "protein.P0AAH4"
entity_type: "protein"
name: "sapD"
source_database: "UniProt"
source_id: "P0AAH4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sapD trkE b1291 JW1284"
---

# sapD

`protein.P0AAH4`

## Static

- Type: `protein`
- Source: `UniProt:P0AAH4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides (PubMed:27803167). Stimulates K(+)-uptake proteins TrkG and TrkH to import K(+), may act via ATP-binding rather than ATP hydrolysis (PubMed:11700350). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:27803167}. SapD is one of two ATP-binding proteins of a predicted ATP-binding cassette (ABC)-family transporter complex, SapABCDF, that may be involved in the uptake of a range of molecules, such as antimicrobial peptides, dipeptides and heme . Separately, a CPLX0-13226 SapBCDF complex has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of a ΔsapD strain is significantly reduced compared to wild type . SapD contains signature motifs conserved in ATP-binding cassette (ABC) proteins . SapD (also known as TrkE) has been implicated in conferring ATP dependence to the K+ uptake proteins EG11020 "TrkG" and TRKH-MONOMER "TrkH" which are not related to the ABC superfamily . Mutation experiments suggest that ATP binding to SapD rather than ATP hydrolysis is sufficient for restoring TrkH mediated K+ uptake in E. coli .

## Biological Role

Component of putative antimicrobial peptide ABC transporter (complex.ecocyc.ABC-29-CPLX), putative putrescine ABC exporter (complex.ecocyc.CPLX0-13226).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides (PubMed:27803167). Stimulates K(+)-uptake proteins TrkG and TrkH to import K(+), may act via ATP-binding rather than ATP hydrolysis (PubMed:11700350). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:27803167}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-29-CPLX|complex.ecocyc.ABC-29-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-13226|complex.ecocyc.CPLX0-13226]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1291|gene.b1291]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAH4`
- `KEGG:ecj:JW1284;eco:b1291;ecoc:C3026_07580;`
- `GeneID:86859890;93775416;946203;`
- `GO:GO:0005524; GO:0015489; GO:0015833; GO:0015847; GO:0016020; GO:0016887; GO:0055052; GO:0071805`

## Notes

Putrescine export system ATP-binding protein SapD
