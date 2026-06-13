---
entity_id: "protein.P0A6G7"
entity_type: "protein"
name: "clpP"
source_database: "UniProt"
source_id: "P0A6G7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "clpP lopP b0437 JW0427"
---

# clpP

`protein.P0A6G7`

## Static

- Type: `protein`
- Source: `UniProt:P0A6G7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Cleaves peptides in various proteins in a process that requires ATP hydrolysis. Has a chymotrypsin-like activity. Plays a major role in the degradation of misfolded proteins. May play the role of a master protease which is attracted to different substrates by different specificity factors such as ClpA or ClpX. Participates in the final steps of RseA-sigma-E degradation, liberating sigma-E to induce the extracytoplasmic-stress response. Degrades antitoxin MazE (PubMed:24375411). {ECO:0000255|HAMAP-Rule:MF_00444, ECO:0000269|PubMed:12941278, ECO:0000269|PubMed:15371343, ECO:0000269|PubMed:24375411}.

## Biological Role

Component of ClpP serine protease (complex.ecocyc.CPLX0-3101), ClpAP (complex.ecocyc.CPLX0-3104), ClpXP (complex.ecocyc.CPLX0-3107), ClpAXP (complex.ecocyc.CPLX0-3108).

## Annotation

FUNCTION: Cleaves peptides in various proteins in a process that requires ATP hydrolysis. Has a chymotrypsin-like activity. Plays a major role in the degradation of misfolded proteins. May play the role of a master protease which is attracted to different substrates by different specificity factors such as ClpA or ClpX. Participates in the final steps of RseA-sigma-E degradation, liberating sigma-E to induce the extracytoplasmic-stress response. Degrades antitoxin MazE (PubMed:24375411). {ECO:0000255|HAMAP-Rule:MF_00444, ECO:0000269|PubMed:12941278, ECO:0000269|PubMed:15371343, ECO:0000269|PubMed:24375411}.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3101|complex.ecocyc.CPLX0-3101]] `EcoCyc` `database` - EcoCyc component coefficient=14 | EcoCyc protcplxs.col coefficient=14
- `is_component_of` --> [[complex.ecocyc.CPLX0-3104|complex.ecocyc.CPLX0-3104]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=14
- `is_component_of` --> [[complex.ecocyc.CPLX0-3107|complex.ecocyc.CPLX0-3107]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=14
- `is_component_of` --> [[complex.ecocyc.CPLX0-3108|complex.ecocyc.CPLX0-3108]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=14

## Incoming Edges (1)

- `encodes` <-- [[gene.b0437|gene.b0437]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6G7`
- `KEGG:ecj:JW0427;eco:b0437;ecoc:C3026_02140;`
- `GeneID:86862982;93777017;945082;`
- `GO:GO:0004176; GO:0004252; GO:0005829; GO:0006515; GO:0008236; GO:0009266; GO:0009314; GO:0009368; GO:0009376; GO:0009408; GO:0010498; GO:0016020; GO:0042802; GO:0043068; GO:0051117`
- `EC:3.4.21.92`

## Notes

ATP-dependent Clp protease proteolytic subunit (EC 3.4.21.92) (Caseinolytic protease) (Endopeptidase Clp) (Heat shock protein F21.5) (Protease Ti)
