---
entity_id: "protein.P30860"
entity_type: "protein"
name: "artJ"
source_database: "UniProt"
source_id: "P30860"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8801422}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "artJ b0860 JW0844"
---

# artJ

`protein.P30860`

## Static

- Type: `protein`
- Source: `UniProt:P30860`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8801422}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Binds L-arginine with high affinity. {ECO:0000269|PubMed:8801422}. artJ encodes the periplasmic binding protein of an L- arginine ABC transporter. Sequence analysis indicates that ArtJ has similarity to the histidine-binding periplasmic protein (HisJ) and lysine/arginine/ornithine binding periplasmic protein (ArgT), both from Salmonella typhimurium. Overexpression of artJ from a plasmid results in the stimulation of L- arginine uptake. Purified ArtJ binds L- arginine with high affinity. It does not bind to the other common amino acids nor to putrescine. ArtJ contains a cleavable signal sequence - the mature protein is located in the periplasmic space .

## Biological Role

Component of L-arginine ABC transporter (complex.ecocyc.ABC-4-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Binds L-arginine with high affinity. {ECO:0000269|PubMed:8801422}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-4-CPLX|complex.ecocyc.ABC-4-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0860|gene.b0860]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30860`
- `KEGG:ecj:JW0844;eco:b0860;ecoc:C3026_05360;`
- `GeneID:948981;`
- `GO:GO:0015276; GO:0016020; GO:0016597; GO:0030288; GO:0034618; GO:0042597; GO:0055052; GO:0097638; GO:1903826`

## Notes

ABC transporter arginine-binding protein 1
