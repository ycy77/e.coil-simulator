---
entity_id: "gene.b3928"
entity_type: "gene"
name: "zapB"
source_database: "NCBI RefSeq"
source_id: "gene-b3928"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3928"
  - "zapB"
---

# zapB

`gene.b3928`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3928`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zapB (gene.b3928) is a gene entity. It encodes zapB (protein.P0AF36). Encoded protein function: FUNCTION: Non-essential, abundant cell division factor that is required for proper Z-ring formation. It is recruited early to the divisome by direct interaction with FtsZ, stimulating Z-ring assembly and thereby promoting cell division earlier in the cell cycle. Its recruitment to the Z-ring requires functional FtsA or ZipA. {ECO:0000269|PubMed:18394147}. EcoCyc product frame: EG11878-MONOMER. EcoCyc synonyms: yiiU. Genomic coordinates: 4118515-4118760. EcoCyc protein note: The ZapB protein is a cell division factor that is required for proper Z ring formation and is recruited to the inner face of the Z ring by ZapA . The N terminus of ZapB is required for its interaction with ZapA . ZapB interacts with EG12855-MONOMER MatP, thereby anchoring the Ter macrodomain in mid-cell . In the absence of functional Min and nucleoid exclusion (SlmA) systems, the MatP-ZapB-ZapA system positions the Z ring over the nucleoid in mid-cell . The protein network formed by the divisome proteins FtsZ, ZapA, ZapB and MatP has been studied using superresolution imaging, showing that these proteins form a multi-layered protein network that extends from the cell membrane to the chromosome and that stabilizes the FtsZ ring...

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF36|protein.P0AF36]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=zapB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012835,ECOCYC:EG11878,GeneID:948420`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4118515-4118760:+; feature_type=gene
