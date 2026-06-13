---
entity_id: "protein.P0AEL6"
entity_type: "protein"
name: "fepB"
source_database: "UniProt"
source_id: "P0AEL6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:10986237, ECO:0000269|PubMed:3011753, ECO:0000305|PubMed:2529253}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fepB b0592 JW0584"
---

# fepB

`protein.P0AEL6`

## Static

- Type: `protein`
- Source: `UniProt:P0AEL6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:10986237, ECO:0000269|PubMed:3011753, ECO:0000305|PubMed:2529253}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:3011753). Binds ferric enterobactin (PubMed:10986237, PubMed:25173704, PubMed:7551033). Can also bind ferric enantioenterobactin, the left-handed stereoisomer of the natural E.coli siderophore, and the apo-siderophore, enterobactin, but does not bind ferric agrobactin (PubMed:10986237). {ECO:0000269|PubMed:10986237, ECO:0000269|PubMed:25173704, ECO:0000269|PubMed:3011753, ECO:0000269|PubMed:7551033}. FepB is the periplasmic binding protein of a ferric enterobactin ABC transport system. Purified FepB binds ferric enterobactin and enterobactin with high affinity (Kd = 30nM and 60nM respectively). Varying the periplasmic concentration of FepB does not affect the rate of uptake of labeled ferric enterobactin suggesting that the rate limiting step in ferric enterobactin uptake is transport across the outer membrane. FepB is synthesized at relatively low levels - approximately 3800 molecules per cell . Solution structures of FepB with and without bound gallium enterobactin suggest that ligand binding does not induce large conformational changes . FepB is synthesized with a cleavable signal sequence . Isoforms of FepB have been observed in several studies but this may be an artifact of overexpression . fepB is a member of the Fur regulon...

## Biological Role

Component of ferric enterobactin ABC transporter (complex.ecocyc.ABC-10-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:3011753). Binds ferric enterobactin (PubMed:10986237, PubMed:25173704, PubMed:7551033). Can also bind ferric enantioenterobactin, the left-handed stereoisomer of the natural E.coli siderophore, and the apo-siderophore, enterobactin, but does not bind ferric agrobactin (PubMed:10986237). {ECO:0000269|PubMed:10986237, ECO:0000269|PubMed:25173704, ECO:0000269|PubMed:3011753, ECO:0000269|PubMed:7551033}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-10-CPLX|complex.ecocyc.ABC-10-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0592|gene.b0592]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEL6`
- `KEGG:ecj:JW0584;eco:b0592;ecoc:C3026_02955;`
- `GeneID:947538;`
- `GO:GO:0006974; GO:0015685; GO:0016020; GO:0030288; GO:0033212; GO:0055052`

## Notes

Ferric enterobactin-binding periplasmic protein FepB
