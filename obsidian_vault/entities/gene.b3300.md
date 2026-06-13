---
entity_id: "gene.b3300"
entity_type: "gene"
name: "secY"
source_database: "NCBI RefSeq"
source_id: "gene-b3300"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3300"
  - "secY"
---

# secY

`gene.b3300`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3300`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

secY (gene.b3300) is a gene entity. It encodes secY (protein.P0AGA2). Encoded protein function: FUNCTION: The central subunit of the protein translocation channel SecYEG. Consists of two halves formed by TMs 1-5 and 6-10. These two domains form a lateral gate at the front which open onto the bilayer between TMs 2 and 7, and are clamped together by SecE at the back. The channel is closed by both a pore ring composed of hydrophobic SecY resides and a short helix (helix 2A) on the extracellular side of the membrane which forms a plug. The plug probably moves laterally to allow the channel to open. The ring and the pore may move independently. SecY is required to insert newly synthesized SecY into the inner membrane. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true, overexpression also results in FtsH-mediated degradation of SecY. EcoCyc product frame: SECY. EcoCyc synonyms: prlA. Genomic coordinates: 3442766-3444097. EcoCyc protein note: The SecY inner membrane protein is the core component of the heterotrimeric SecYEG preprotein translocase; SecY forms the protein conducting channel with channel plug and hydrophobic seal; SecY contains a signal sequence binding pocket and cytosolic loops that interact with partner proteins (see and )...

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGA2|protein.P0AGA2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=secY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010814,ECOCYC:EG10766,GeneID:947799`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3442766-3444097:-; feature_type=gene
