---
entity_id: "protein.P77295"
entity_type: "protein"
name: "ygaV"
source_database: "UniProt"
source_id: "P77295"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygaV b2667 JW2642"
---

# ygaV

`protein.P77295`

## Static

- Type: `protein`
- Source: `UniProt:P77295`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator that regulates large-scale gene expression in response to sulfide (PubMed:40005711). May act as a global regulator responsible for redox homeostasis (PubMed:40005711). It functions as both a repressor and an activator (PubMed:36552568, PubMed:40005711). In the absence of sulfide compounds, it negatively regulates many anaerobic respiratory genes, including formate, fumarate, lactate, nitrate and nitrite reductase genes (PubMed:36552568). In the presence of hydrogen sulfide (H(2)S), YgaV activity is attenuated, leading to the expression of anaerobic respiratory and ROS scavenging genes, which contributes to redox homeostasis, reactive oxygen species (ROS) scavenging and antibiotic tolerance (PubMed:36552568). It responds to H(2)O(2) scavenging and increases antibiotic tolerance under H(2)S-atmospheric conditions (PubMed:36552568). It also negatively regulates its own expression by binding to the ygaVP promoter region (PubMed:18245262, PubMed:36552568). May also be involved in regulatory mechanisms that operate independently of sulfide (PubMed:40005711). {ECO:0000269|PubMed:18245262, ECO:0000269|PubMed:36552568, ECO:0000269|PubMed:40005711}. YgaV is a transcriptional regulator involved in H2S-dependent antioxidative stress responses and antibiotic resistance...

## Annotation

FUNCTION: Transcriptional regulator that regulates large-scale gene expression in response to sulfide (PubMed:40005711). May act as a global regulator responsible for redox homeostasis (PubMed:40005711). It functions as both a repressor and an activator (PubMed:36552568, PubMed:40005711). In the absence of sulfide compounds, it negatively regulates many anaerobic respiratory genes, including formate, fumarate, lactate, nitrate and nitrite reductase genes (PubMed:36552568). In the presence of hydrogen sulfide (H(2)S), YgaV activity is attenuated, leading to the expression of anaerobic respiratory and ROS scavenging genes, which contributes to redox homeostasis, reactive oxygen species (ROS) scavenging and antibiotic tolerance (PubMed:36552568). It responds to H(2)O(2) scavenging and increases antibiotic tolerance under H(2)S-atmospheric conditions (PubMed:36552568). It also negatively regulates its own expression by binding to the ygaVP promoter region (PubMed:18245262, PubMed:36552568). May also be involved in regulatory mechanisms that operate independently of sulfide (PubMed:40005711). {ECO:0000269|PubMed:18245262, ECO:0000269|PubMed:36552568, ECO:0000269|PubMed:40005711}.

## Outgoing Edges (4)

- `activates` --> [[gene.b1102|gene.b1102]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2155|gene.b2155]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3070|gene.b3070]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4367|gene.b4367]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b2667|gene.b2667]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77295`
- `KEGG:ecj:JW2642;eco:b2667;ecoc:C3026_14700;`
- `GeneID:93779345;947136;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0097532`

## Notes

HTH-type transcriptional regulator YgaV (Sulfide-responsive transcription factor YgaV)
