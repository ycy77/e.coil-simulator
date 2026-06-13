---
entity_id: "complex.ecocyc.CPLX0-3930"
entity_type: "complex"
name: "FlhDC DNA-binding transcriptional dual regulator"
source_database: "EcoCyc"
source_id: "CPLX0-3930"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FlhDC"
---

# FlhDC DNA-binding transcriptional dual regulator

`complex.ecocyc.CPLX0-3930`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3930`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A8S9|protein.P0A8S9]], [[protein.P0ABY7|protein.P0ABY7]]

## Enriched Summary

The FlhD and FlhC proteins are transcriptional factors that form heterohexamers (FlhD4C2) . The complex transcription factor is the principal regulator of bacterial flagellum biogenesis and swarming migration ; it is also involved in glucose and fructose uptake and catabolism and other carbon source metabolic pathways . This heteromeric regulator activates class II genes involved in the flagellar basal body , proteins of the export machinery, the flagellar σ subunit (FliA), and its anti-σ factor, FlgM . Currently, no inducer for this regulator has been reported in the literature. A microarray analysis showed that the master regulator, FlhD4C2, regulates several nonflagellar genes, but the direct effect has not been determined. In a gene expression study during the transition from aerobic to anaerobic conditions, part of the regulatory cascade involving the protein FlhDC was analyzed . It has been observed that although the flhDC operon remains expressed, the flagellar system is not always active; rather, spontaneous switching occurs, turning on and off the system, and this behavior appears to be dependent on YdiV, the anti-FlhDC protein...

## Annotation

The FlhD and FlhC proteins are transcriptional factors that form heterohexamers (FlhD4C2) . The complex transcription factor is the principal regulator of bacterial flagellum biogenesis and swarming migration ; it is also involved in glucose and fructose uptake and catabolism and other carbon source metabolic pathways . This heteromeric regulator activates class II genes involved in the flagellar basal body , proteins of the export machinery, the flagellar σ subunit (FliA), and its anti-σ factor, FlgM . Currently, no inducer for this regulator has been reported in the literature. A microarray analysis showed that the master regulator, FlhD4C2, regulates several nonflagellar genes, but the direct effect has not been determined. In a gene expression study during the transition from aerobic to anaerobic conditions, part of the regulatory cascade involving the protein FlhDC was analyzed . It has been observed that although the flhDC operon remains expressed, the flagellar system is not always active; rather, spontaneous switching occurs, turning on and off the system, and this behavior appears to be dependent on YdiV, the anti-FlhDC protein . In addition, in Escherichia coli B2 phylogroup strains, Tls (a truncated version of the K-12 MG1655 chemoreceptor gene trg) sequesters the flagellar master regulator FlhDC, thereby inhibiting FlhDC activity and repressing class 2/3 flagellar gene expression and motility under liquid-growth conditions . Nonmotile cells are generated when the insertion sequence upstream, G7029, is deleted. This allowed comparisons of colonization rates between active and non-active flagellar motility in microfluidic channels, with non-motile cells colonizing surfaces more rapidly . FlhD and FlhC are part of the unusual flhDC operon that encodes two trans

## Outgoing Edges (13)

- `activates` --> [[gene.b0569|gene.b0569]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1043|gene.b1043]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1241|gene.b1241]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1937|gene.b1937]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1938|gene.b1938]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1944|gene.b1944]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2169|gene.b2169]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2170|gene.b2170]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2415|gene.b2415]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2927|gene.b2927]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3916|gene.b3916]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4014|gene.b4014]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4018|gene.b4018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0A8S9|protein.P0A8S9]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P0ABY7|protein.P0ABY7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3930`
- `PDB:2AVU`
- `PDB:2AVU`
- `QSPROTEOME:QS00190993`

## Notes

4*protein.P0A8S9|2*protein.P0ABY7
