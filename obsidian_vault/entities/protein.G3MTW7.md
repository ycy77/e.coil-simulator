---
entity_id: "protein.G3MTW7"
entity_type: "protein"
name: "pmrR"
source_database: "UniProt"
source_id: "G3MTW7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pmrR b4703 JW4072.1"
---

# pmrR

`protein.G3MTW7`

## Static

- Type: `protein`
- Source: `UniProt:G3MTW7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: May bind to BasS and modulate its sensor kinase activity. {ECO:0000305}. First characterized in TAX-90371 , pmrR encodes a small inner membrane protein which, under BasSR-inducing conditions (high concentrations of Fe3+, mildly acidic pH), inhibits the G7146-MONOMER LpxT-dependent generation of lipid A-core 1-diphosphate . Inactivation of pmrR in the polymyxin-resistant, deoxycholate-sensitive EG11615 BasR(PmrA)-constitutive strain WD101 results in sensitivity to polymyxin B and resistance to deoxycholate . PmrR-mediated regulation of LpxT activity in Salmonella, constitutes a negative feedback mechanism for control of the PmrA-PmrB two-component system which governs transcription of lipopolysaccharide-modifying genes .

## Annotation

FUNCTION: May bind to BasS and modulate its sensor kinase activity. {ECO:0000305}.

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.RXN0-5383|reaction.ecocyc.RXN0-5383]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b4703|gene.b4703]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:G3MTW7`
- `KEGG:eco:b4703;ecoc:C3026_22215;`
- `GeneID:11115379;86861500;`
- `GO:GO:0004857; GO:0005886`

## Notes

Putative membrane protein PmrR
