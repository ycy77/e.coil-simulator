---
entity_id: "protein.P75713"
entity_type: "protein"
name: "allE"
source_database: "UniProt"
source_id: "P75713"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19935661, ECO:0000269|PubMed:20038185}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allE glxB6 ylbA b0515 JW0503"
---

# allE

`protein.P75713`

## Static

- Type: `protein`
- Source: `UniProt:P75713`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19935661, ECO:0000269|PubMed:20038185}.

## Enriched Summary

FUNCTION: Involved in the anaerobic nitrogen utilization via the assimilation of allantoin. Catalyzes the second stereospecific hydrolysis reaction (deamination) of the allantoin degradation pathway, producing S-ureidoglycolate and ammonia from S-ureidoglycine. {ECO:0000269|PubMed:19935661, ECO:0000269|PubMed:20038185}. (S)-ureidoglycine aminohydrolase catalyzes the second, stereospecific hydrolysis reaction of the allantoin degradation pathway, producing CPD-1091 and ammonia from CPD0-2298 . Although hydrolysis of ureidoglycine can proceed spontaneously, the spontaneous reaction appears to be slow and not stereospecific . UghY: "(S)-ureidoglycine aminohydrolase"

## Biological Role

Catalyzes URUR-RXN (reaction.ecocyc.URUR-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Involved in the anaerobic nitrogen utilization via the assimilation of allantoin. Catalyzes the second stereospecific hydrolysis reaction (deamination) of the allantoin degradation pathway, producing S-ureidoglycolate and ammonia from S-ureidoglycine. {ECO:0000269|PubMed:19935661, ECO:0000269|PubMed:20038185}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.URUR-RXN|reaction.ecocyc.URUR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0515|gene.b0515]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75713`
- `KEGG:ecj:JW0503;eco:b0515;ecoc:C3026_02525;`
- `GeneID:945149;`
- `GO:GO:0005737; GO:0006145; GO:0010136; GO:0030145; GO:0071522`
- `EC:3.5.3.26`

## Notes

(S)-ureidoglycine aminohydrolase (UGHY) (UGlyAH) (EC 3.5.3.26)
