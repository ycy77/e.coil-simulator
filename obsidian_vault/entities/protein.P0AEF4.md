---
entity_id: "protein.P0AEF4"
entity_type: "protein"
name: "dpiA"
source_database: "UniProt"
source_id: "P0AEF4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dpiA citB criR mpdA b0620 JW0612"
---

# dpiA

`protein.P0AEF4`

## Static

- Type: `protein`
- Source: `UniProt:P0AEF4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system DpiA/DpiB, which is essential for expression of citrate-specific fermentation genes and genes involved in plasmid inheritance. Could be involved in response to both the presence of citrate and external redox conditions. Regulates the transcription of citCDEFXGT, dpiAB, mdh and exuT. Binds specifically to the dpiB-citC intergenic region. {ECO:0000269|PubMed:18997424, ECO:0000269|PubMed:19202292}. CitB/DpiA is a dual transcriptional regulator involved in anaerobic citrate catabolism. In the presence of citrate and under anaerobic conditions it activates genes for citrate fermentation, the citCDEFXGT operon, the citAB operon, and mdh, as well as the exuTR operon for dissimilation of hexuronate . Due to the ability of CitB/DpiA to bind to A/T-rich sequences, multiple other roles have been assigned to CitB. When overexpressed in E. coli, it destabilizes plasmid inheritance, represses transcription of appY, encoding a regulator of anaerobic metabolism, and induces the SOS response by competing with DnaA and DnaB in binding to A/T-rich sequences at the replication origin . Moreover, inactivation of penicillin-binding protein 3, FtsI, either chemically or genetically, induces SOS in E. coli. This induction requires dpiBA . CitB/DpiA belongs to the two-component system DpiB/DpiA, or CitBA...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system DpiA/DpiB, which is essential for expression of citrate-specific fermentation genes and genes involved in plasmid inheritance. Could be involved in response to both the presence of citrate and external redox conditions. Regulates the transcription of citCDEFXGT, dpiAB, mdh and exuT. Binds specifically to the dpiB-citC intergenic region. {ECO:0000269|PubMed:18997424, ECO:0000269|PubMed:19202292}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (10)

- `activates` --> [[gene.b0613|gene.b0613]] `RegulonDB` `S` - regulator=DpiA; target=citG; function=+
- `activates` --> [[gene.b0614|gene.b0614]] `RegulonDB` `S` - regulator=DpiA; target=citX; function=+
- `activates` --> [[gene.b0615|gene.b0615]] `RegulonDB` `S` - regulator=DpiA; target=citF; function=+
- `activates` --> [[gene.b0616|gene.b0616]] `RegulonDB` `S` - regulator=DpiA; target=citE; function=+
- `activates` --> [[gene.b0617|gene.b0617]] `RegulonDB` `S` - regulator=DpiA; target=citD; function=+
- `activates` --> [[gene.b0618|gene.b0618]] `RegulonDB` `S` - regulator=DpiA; target=citC; function=+
- `activates` --> [[gene.b0619|gene.b0619]] `RegulonDB` `S` - regulator=DpiA; target=dpiB; function=+
- `activates` --> [[gene.b0620|gene.b0620]] `RegulonDB` `S` - regulator=DpiA; target=dpiA; function=+
- `activates` --> [[gene.b3093|gene.b3093]] `RegulonDB` `S` - regulator=DpiA; target=exuT; function=+
- `activates` --> [[gene.b3236|gene.b3236]] `RegulonDB` `S` - regulator=DpiA; target=mdh; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b0620|gene.b0620]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEF4`
- `KEGG:ecj:JW0612;eco:b0620;ecoc:C3026_03100;`
- `GeneID:75170624;75205018;947008;`
- `GO:GO:0000156; GO:0000160; GO:0003677; GO:0003700; GO:0005737`

## Notes

Transcriptional regulatory protein DpiA (Destabilizer of plasmid inheritance)
