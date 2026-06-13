---
entity_id: "protein.P37902"
entity_type: "protein"
name: "gltI"
source_database: "UniProt"
source_id: "P37902"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1091635}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltI ybeJ yzzK b0655 JW5092"
---

# gltI

`protein.P37902`

## Static

- Type: `protein`
- Source: `UniProt:P37902`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1091635}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Binds to both glutamate and aspartate. {ECO:0000269|PubMed:1091635, ECO:0000269|PubMed:1091636, ECO:0000269|PubMed:336628, ECO:0000305|PubMed:9593292}. GltI is the periplasmic binding protein of a glutamate/aspartate ABC transport system. Purified GltI (released from E. coli K-12 strains by osmotic shock treatment) binds L-glutamate and L-aspartate with µM affinity; binding is competitively inhibited by L-glutamine and L-asparagine . The amount of GltI is significantly reduced when E. coli W strain D2W is grown with glucose rather than succinate [Willis75]. Synthesis of GltI is repressed when the small regulatory RNA, GCVB-RNA "GcvB" is expressed from a plasmid in a ΔgcvA ΔgcvB background .

## Biological Role

Component of glutamate / aspartate ABC transporter (complex.ecocyc.ABC-13-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Binds to both glutamate and aspartate. {ECO:0000269|PubMed:1091635, ECO:0000269|PubMed:1091636, ECO:0000269|PubMed:336628, ECO:0000305|PubMed:9593292}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-13-CPLX|complex.ecocyc.ABC-13-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0655|gene.b0655]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37902`
- `KEGG:ecj:JW5092;eco:b0655;ecoc:C3026_03275;`
- `GeneID:946938;`
- `GO:GO:0005576; GO:0006865; GO:0015813; GO:0016020; GO:0016595; GO:0030288; GO:0055052; GO:0070335; GO:0070778; GO:0098712; GO:0140009`

## Notes

Glutamate/aspartate import solute-binding protein
