---
entity_id: "protein.P0A6H5"
entity_type: "protein"
name: "hslU"
source_database: "UniProt"
source_id: "P0A6H5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hslU htpI b3931 JW3902"
---

# hslU

`protein.P0A6H5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6H5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: ATPase subunit of a proteasome-like degradation complex; this subunit has chaperone activity. The binding of ATP and its subsequent hydrolysis by HslU are essential for unfolding of protein substrates subsequently hydrolyzed by HslV. HslU recognizes the N-terminal part of its protein substrates and unfolds these before they are guided to HslV for hydrolysis. {ECO:0000269|PubMed:10419524, ECO:0000269|PubMed:10452560, ECO:0000269|PubMed:15696175, ECO:0000269|PubMed:8650174, ECO:0000269|PubMed:8662828, ECO:0000269|PubMed:9288941, ECO:0000269|PubMed:9393683}.

## Biological Role

Component of HslU hexamer (complex.ecocyc.CPLX0-1161), HslVU protease (complex.ecocyc.CPLX0-1163).

## Annotation

FUNCTION: ATPase subunit of a proteasome-like degradation complex; this subunit has chaperone activity. The binding of ATP and its subsequent hydrolysis by HslU are essential for unfolding of protein substrates subsequently hydrolyzed by HslV. HslU recognizes the N-terminal part of its protein substrates and unfolds these before they are guided to HslV for hydrolysis. {ECO:0000269|PubMed:10419524, ECO:0000269|PubMed:10452560, ECO:0000269|PubMed:15696175, ECO:0000269|PubMed:8650174, ECO:0000269|PubMed:8662828, ECO:0000269|PubMed:9288941, ECO:0000269|PubMed:9393683}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1161|complex.ecocyc.CPLX0-1161]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CPLX0-1163|complex.ecocyc.CPLX0-1163]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b3931|gene.b3931]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6H5`
- `KEGG:ecj:JW3902;eco:b3931;ecoc:C3026_21245;`
- `GeneID:93777967;948430;`
- `GO:GO:0000287; GO:0005524; GO:0005829; GO:0006508; GO:0008233; GO:0009376; GO:0009408; GO:0016020; GO:0016887; GO:0019904; GO:0030164; GO:0034605; GO:0036402; GO:0042802; GO:0043335; GO:0051603`

## Notes

ATP-dependent protease ATPase subunit HslU (Heat shock protein HslU) (Unfoldase HslU)
