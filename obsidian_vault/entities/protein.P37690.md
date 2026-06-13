---
entity_id: "protein.P37690"
entity_type: "protein"
name: "envC"
source_database: "UniProt"
source_id: "P37690"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:12113939, ECO:0000269|PubMed:15165230, ECO:0000269|PubMed:19525345}. Note=Localizes at the septal ring."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "envC yibP b3613 JW5646"
---

# envC

`protein.P37690`

## Static

- Type: `protein`
- Source: `UniProt:P37690`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:12113939, ECO:0000269|PubMed:15165230, ECO:0000269|PubMed:19525345}. Note=Localizes at the septal ring.

## Enriched Summary

FUNCTION: Activator of the cell wall hydrolases AmiA and AmiB. Required for septal murein cleavage and daughter cell separation during cell division. In vitro, exhibits weak endoproteolytic activity on beta-casein. {ECO:0000269|PubMed:11976287, ECO:0000269|PubMed:15165230, ECO:0000269|PubMed:19525345, ECO:0000269|PubMed:20300061, ECO:0000269|PubMed:23796240}. EnvC is a divisome associated factor which activates the peptidoglycan (PG) hydrolases NACMURLALAAMI1-MONOMER "AmiA" and NACMURLALAAMI2-MONOMER "AmiB" required for septal splitting . EnvC-mediated amidase activation is regulated by direct interaction with the ABC-54-CPLX FtsEX transmembrane complex (reviewed in ). EnvC contains a structural element - the 'restraining arm' - that is implicated in a self-inhibition mechanism; FtsEX interaction with EnvC may drive conformational change that leads to amidase activation (see further ). EnvC is not essential for viability; an envC null mutant has cell division and cell envelope integrity defects, an FtsZ ring defect, and is unable to form colonies at 42oC . Temperature sensitivity can be rescued by addition of 5% betaine to the medium . EnvC does not degrade peptidoglycan in solution but does have murein hydrolytic activity in a zymogram assay and also shows weak protease activity toward beta-casein...

## Annotation

FUNCTION: Activator of the cell wall hydrolases AmiA and AmiB. Required for septal murein cleavage and daughter cell separation during cell division. In vitro, exhibits weak endoproteolytic activity on beta-casein. {ECO:0000269|PubMed:11976287, ECO:0000269|PubMed:15165230, ECO:0000269|PubMed:19525345, ECO:0000269|PubMed:20300061, ECO:0000269|PubMed:23796240}.

## Outgoing Edges (1)

- `activates` --> [[reaction.ecocyc.RXN-16938|reaction.ecocyc.RXN-16938]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b3613|gene.b3613]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37690`
- `KEGG:ecj:JW5646;eco:b3613;`
- `GeneID:75173810;75202185;948129;`
- `GO:GO:0000920; GO:0004222; GO:0005886; GO:0009273; GO:0009314; GO:0009410; GO:0016787; GO:0030288; GO:0032153; GO:0042597`

## Notes

Murein hydrolase activator EnvC (Septal ring factor)
