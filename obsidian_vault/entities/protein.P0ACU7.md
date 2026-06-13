---
entity_id: "protein.P0ACU7"
entity_type: "protein"
name: "yjdC"
source_database: "UniProt"
source_id: "P0ACU7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjdC cutA3 b4135 JW5733"
---

# yjdC

`protein.P0ACU7`

## Static

- Type: `protein`
- Source: `UniProt:P0ACU7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

HTH-type transcriptional regulator YjdC DicD, previously named YjdC, is involved in division control . It which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the RutR family of transcription factors . Upstream of the dicD gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the dicD gene is affected by heat stress . In E. coli BL21(DE3), DicD protein levels were found to be increased in response to the thiol-specific oxidant 2-hydroxyethyl disulfide and guanidine hydrochloride . Interconnectivity between the dicD gene and the gene encoding the TF DicA was found . Deletion of the dicD gene rescued the growth defect of a dicA hypomorphic allele mutant strain. In a dicA hypomorphic allele mutant strain, the dicD transcript showed a 3-fold decrease relative to the wild type .

## Annotation

HTH-type transcriptional regulator YjdC

## Outgoing Edges (3)

- `represses` --> [[gene.b1569|gene.b1569]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1570|gene.b1570]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1575|gene.b1575]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b4135|gene.b4135]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACU7`
- `KEGG:ecj:JW5733;eco:b4135;ecoc:C3026_22350;`
- `GeneID:93777689;948650;`
- `GO:GO:0003677; GO:0045892`

## Notes

HTH-type transcriptional regulator YjdC
