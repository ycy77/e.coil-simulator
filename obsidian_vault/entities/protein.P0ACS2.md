---
entity_id: "protein.P0ACS2"
entity_type: "protein"
name: "soxR"
source_database: "UniProt"
source_id: "P0ACS2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "soxR marC b4063 JW4024"
---

# soxR

`protein.P0ACS2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACS2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Activates the transcription of the soxS gene which itself controls the superoxide response regulon. SoxR contains a 2Fe-2S iron-sulfur cluster that may act as a redox sensor system that recognizes superoxide. The variable redox state of the Fe-S cluster is employed in vivo to modulate the transcriptional activity of SoxR in response to specific types of oxidative stress. Upon reduction of 2Fe-2S cluster, SoxR reversibly loses its transcriptional activity, but retains its DNA binding affinity. The SoxR protein, for "Superoxide Response protein", is negatively autoregulated and controls the transcription of the regulon involved in defense against redox-cycling drugs and in responses to nitric oxide . SoxR also appears to be involved in resistance to ciprofloxacin , cefuroxime, gentamicin , pyocyanin and other antimicrobials . In a gene expression study during the transition from aerobic to anaerobic conditions, part of the regulatory cascade involving the protein SoxR was analyzed . SoxR belongs to the MerR family and is a homodimer in solution . This protein contains two essential [2Fe-2S] clusters for its transcriptional activity . Each SoxR polypeptide contains a [2Fe-2S] cluster that senses the oxidants in the cell. Both Fe-SoxR and apo-SoxR bind to the promoter region, but only Fe-SoxR contributes to the activation in its oxidized form...

## Annotation

FUNCTION: Activates the transcription of the soxS gene which itself controls the superoxide response regulon. SoxR contains a 2Fe-2S iron-sulfur cluster that may act as a redox sensor system that recognizes superoxide. The variable redox state of the Fe-S cluster is employed in vivo to modulate the transcriptional activity of SoxR in response to specific types of oxidative stress. Upon reduction of 2Fe-2S cluster, SoxR reversibly loses its transcriptional activity, but retains its DNA binding affinity.

## Outgoing Edges (8)

- `activates` --> [[gene.b1611|gene.b1611]] `RegulonDB` `S` - regulator=SoxR; target=fumC; function=+
- `activates` --> [[gene.b2600|gene.b2600]] `RegulonDB` `S` - regulator=SoxR; target=tyrA; function=+
- `activates` --> [[gene.b2601|gene.b2601]] `RegulonDB` `S` - regulator=SoxR; target=aroF; function=+
- `activates` --> [[gene.b3207|gene.b3207]] `RegulonDB` `S` - regulator=SoxR; target=yrbL; function=+
- `activates` --> [[gene.b3908|gene.b3908]] `RegulonDB` `S` - regulator=SoxR; target=sodA; function=+
- `activates` --> [[gene.b4060|gene.b4060]] `RegulonDB` `S` - regulator=SoxR; target=yjcB; function=+
- `activates` --> [[gene.b4062|gene.b4062]] `RegulonDB` `C` - regulator=SoxR; target=soxS; function=+
- `represses` --> [[gene.b4063|gene.b4063]] `RegulonDB` `C` - regulator=SoxR; target=soxR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4063|gene.b4063]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACS2`
- `KEGG:ecj:JW4024;eco:b4063;ecoc:C3026_21955;`
- `GeneID:86861537;86944605;948566;`
- `GO:GO:0003677; GO:0003700; GO:0005737; GO:0006355; GO:0006979; GO:0046872; GO:0051537`

## Notes

Redox-sensitive transcriptional activator SoxR
