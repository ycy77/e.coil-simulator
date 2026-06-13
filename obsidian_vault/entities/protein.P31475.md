---
entity_id: "protein.P31475"
entity_type: "protein"
name: "yieP"
source_database: "UniProt"
source_id: "P31475"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yieP b3755 JW5608"
---

# yieP

`protein.P31475`

## Static

- Type: `protein`
- Source: `UniProt:P31475`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized HTH-type transcriptional regulator YieP The transcriptional factor YieP appears to regulate genes involved in cellular membrane synthesis or structure, stress responses , and tolerance to 3-HYDROXY-PROPIONATE (3-HP) . YieP appears to belong to the GntR family of transcription factors . The yieP gene and the amino acid residues of its protein are highly conserved among Enterobacteriaceae, particularly in the helix-turn-helix DNA-binding region . The predicted structure of YieP consists of nine alpha helices, seven of which are located in the C-terminus . The helix-turn-helix DNA-binding region is located at the N-terminus, and a signal recognition domain is at the C-terminus . YieP was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . Compared to known global transcription factors (TFs), YieP exhibits some interesting regulatory features. First, it binds more frequently to intragenic regions in the genome and less to regions located within putative regulatory regions. Second, it has fewer binding sites than global TFs such as CRP, Lrp, Fnr, and ArcA. Third, it binds to a greater number of genes with putative functions. Finally, its expression level is lower compared to that of the majority of global TFs...

## Annotation

Uncharacterized HTH-type transcriptional regulator YieP

## Outgoing Edges (7)

- `activates` --> [[gene.b0804|gene.b0804]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3755|gene.b3755]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0306|gene.b0306]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0575|gene.b0575]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1206|gene.b1206]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2141|gene.b2141]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4597|gene.b4597]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b3755|gene.b3755]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31475`
- `KEGG:ecj:JW5608;eco:b3755;ecoc:C3026_20355;`
- `GeneID:948263;`
- `GO:GO:0000987; GO:0003700; GO:0005829; GO:0006355`

## Notes

Uncharacterized HTH-type transcriptional regulator YieP
