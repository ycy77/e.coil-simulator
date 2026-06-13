---
entity_id: "complex.ecocyc.PHOSPHO-OMPR"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator OmpR-phosphorylated"
source_database: "EcoCyc"
source_id: "PHOSPHO-OMPR"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "OmpR-P<SUP>asp55</SUP>"
  - "OmpR response regulator - phosphorylated"
---

# DNA-binding transcriptional dual regulator OmpR-phosphorylated

`complex.ecocyc.PHOSPHO-OMPR`

## Static

- Type: `complex`
- Source: `EcoCyc:PHOSPHO-OMPR`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `regulatory`
- Components: [[protein.P0AA16|protein.P0AA16]]

## Enriched Summary

The response regulator OmpR, for "Outer membrane protein Regulator," , controls the transcriptional expression of several genes whose products are involved in adaptation to changes in osmolarity, such as major outer membrane porins , and it negatively regulates the expression of flagella , promotes biofilm formation , increases curli gene expression , increases expression of several drug exporter genes , and confers increased beta-lactam resistance . It also appears to play an important role as a key regulator of bacterial virulence, growth, and metabolism . The OmpR regulon is differentially regulated during E. coli colonization of the mouse intestine . OmpR is required for acidification under acid and osmotic stress conditions . In addition, this regulator appears to control genes involved in resistance or sensitivity to the antibacterial peptide TAT-RasGAP317-326 . Inhibition of ompR expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic pyocyanin, but reduced it under treatment with polymyxin B . In a genome-scale study based on ChIP-exo, RNA-seq analysis, and DNA motif sequence identification, the OmpR regulon was characterized. A total of 37 genes in 24 transcription units (TUs) were identified to be under this regulons control during osmotic stress (NaCl treatment)...

## Annotation

The response regulator OmpR, for "Outer membrane protein Regulator," , controls the transcriptional expression of several genes whose products are involved in adaptation to changes in osmolarity, such as major outer membrane porins , and it negatively regulates the expression of flagella , promotes biofilm formation , increases curli gene expression , increases expression of several drug exporter genes , and confers increased beta-lactam resistance . It also appears to play an important role as a key regulator of bacterial virulence, growth, and metabolism . The OmpR regulon is differentially regulated during E. coli colonization of the mouse intestine . OmpR is required for acidification under acid and osmotic stress conditions . In addition, this regulator appears to control genes involved in resistance or sensitivity to the antibacterial peptide TAT-RasGAP317-326 . Inhibition of ompR expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic pyocyanin, but reduced it under treatment with polymyxin B . In a genome-scale study based on ChIP-exo, RNA-seq analysis, and DNA motif sequence identification, the OmpR regulon was characterized. A total of 37 genes in 24 transcription units (TUs) were identified to be under this regulons control during osmotic stress (NaCl treatment) . In a gene expression study during the transition from aerobic to anaerobic conditions, part of the regulatory cascade involving the protein OmpR was analyzed . OmpR belongs to the two-component system EnvZ/OmpR . EnvZ is an osmosensor histidine kinase and is known to be a transmembrane protein composed of three domains: an external sensory domain (amino terminal), a cytoplasmic transmitter domain (carboxyl terminal), and a transmembrane hydrophobic central domain . The se

## Outgoing Edges (20)

- `activates` --> [[gene.b0113|gene.b0113]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0221|gene.b0221]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0222|gene.b0222]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0464|gene.b0464]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0813|gene.b0813]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0814|gene.b0814]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1857|gene.b1857]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2777|gene.b2777]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3035|gene.b3035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3089|gene.b3089]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3364|gene.b3364]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4396|gene.b4396]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0484|gene.b0484]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0964|gene.b0964]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1677|gene.b1677]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1829|gene.b1829]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2276|gene.b2276]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2943|gene.b2943]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3088|gene.b3088]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4034|gene.b4034]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AA16|protein.P0AA16]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PHOSPHO-OMPR`

## Notes

2*protein.P0AA16
