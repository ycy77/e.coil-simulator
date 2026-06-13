---
entity_id: "protein.P0A8R9"
entity_type: "protein"
name: "hdfR"
source_database: "UniProt"
source_id: "P0A8R9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hdfR pssR yifA yifD b4480 JW5607"
---

# hdfR

`protein.P0A8R9`

## Static

- Type: `protein`
- Source: `UniProt:P0A8R9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Negatively regulates the transcription of the flagellar master operon flhDC by binding to the upstream region of the operon. {ECO:0000269|PubMed:10913108}. "Hns-dependent flhDC regulator," HdfR, negatively regulates the expression of the flagellar master operon, flhDC and positively regulates the expression of the gltBD operon . H-NS is a direct activator of the flhDC operon and represses transcription of hdfR. Using a machine learning framework that integrates and analyzes data from 10 different sources, it was determined that HdfR is involved in antibiotic resistance . HdfR is a transcriptional regulator that belongs to the LysR family. It consist of two domains, an amino-terminal domain that contains a potential helix-turn-helix DNA-binding motif and a carboxy-terminal domain involved in co-inducer recognition . Little is known about the regulatory role of HdfR, and the binding sites for this transcription factor have not yet been determined. In systematic studies of oligomerization, it was shown that some members of the LysR family, like HdfR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The hdfR gene loss of function caused by an amino acid change of glutamate to lysine favored NADPH availability in E. coli strain BW25113...

## Annotation

FUNCTION: Negatively regulates the transcription of the flagellar master operon flhDC by binding to the upstream region of the operon. {ECO:0000269|PubMed:10913108}.

## Outgoing Edges (5)

- `activates` --> [[gene.b3212|gene.b3212]] `RegulonDB` `S` - regulator=HdfR; target=gltB; function=+
- `activates` --> [[gene.b3213|gene.b3213]] `RegulonDB` `S` - regulator=HdfR; target=gltD; function=+
- `activates` --> [[gene.b3214|gene.b3214]] `RegulonDB` `S` - regulator=HdfR; target=gltF; function=+
- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=HdfR; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=HdfR; target=flhD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4480|gene.b4480]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8R9`
- `KEGG:ecj:JW5607;eco:b4480;ecoc:C3026_20390;`
- `GeneID:2847698;93778187;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0045892`

## Notes

HTH-type transcriptional regulator HdfR (H-NS-dependent flhDC regulator)
