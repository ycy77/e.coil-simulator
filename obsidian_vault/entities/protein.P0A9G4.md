---
entity_id: "protein.P0A9G4"
entity_type: "protein"
name: "cueR"
source_database: "UniProt"
source_id: "P0A9G4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cueR copR ybbI b0487 JW0476"
---

# cueR

`protein.P0A9G4`

## Static

- Type: `protein`
- Source: `UniProt:P0A9G4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Regulates the transcription of the copA and cueO genes. It detects cytoplasmic copper stress and activates transcription in response to increasing copper concentrations. {ECO:0000269|PubMed:10915804, ECO:0000269|PubMed:11167016, ECO:0000269|PubMed:11399769}.

## Biological Role

Component of CueR-Cu+ (complex.ecocyc.CPLX0-7702), DNA-binding transcriptional dual regulator CueR-Cu+ (complex.ecocyc.CPLX0-7708).

## Annotation

FUNCTION: Regulates the transcription of the copA and cueO genes. It detects cytoplasmic copper stress and activates transcription in response to increasing copper concentrations. {ECO:0000269|PubMed:10915804, ECO:0000269|PubMed:11167016, ECO:0000269|PubMed:11399769}.

## Outgoing Edges (6)

- `activates` --> [[gene.b0123|gene.b0123]] `RegulonDB` `C` - regulator=CueR; target=cueO; function=+
- `activates` --> [[gene.b0484|gene.b0484]] `RegulonDB` `C` - regulator=CueR; target=copA; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7702|complex.ecocyc.CPLX0-7702]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7708|complex.ecocyc.CPLX0-7708]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=CueR; target=rmf; function=-
- `represses` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=CueR; target=rsd; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0487|gene.b0487]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9G4`
- `KEGG:ecj:JW0476;eco:b0487;ecoc:C3026_02395;`
- `GeneID:86863039;93776962;945332;`
- `GO:GO:0000976; GO:0000987; GO:0001216; GO:0003700; GO:0005507; GO:0005737; GO:0006351; GO:0032993; GO:0042802; GO:0045893`

## Notes

HTH-type transcriptional regulator CueR (Copper efflux regulator) (Copper export regulator)
