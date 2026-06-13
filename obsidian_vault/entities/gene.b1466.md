---
entity_id: "gene.b1466"
entity_type: "gene"
name: "narW"
source_database: "NCBI RefSeq"
source_id: "gene-b1466"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1466"
  - "narW"
---

# narW

`gene.b1466`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1466`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narW (gene.b1466) is a gene entity. It encodes narW (protein.P19317). Encoded protein function: FUNCTION: Chaperone required for proper molybdenum cofactor insertion and final assembly of the membrane-bound respiratory nitrate reductase 2. {ECO:0000250}. EcoCyc product frame: NARW-MONOMER. EcoCyc synonyms: chlZ. Genomic coordinates: 1536614-1537309. EcoCyc protein note: The polypeptide encoded by narW, the third gene in the narZYWV operon, is not part of the final nitrate reductase Z enzyme. By similarity to NarJ, it may act as a private chaperone during the incorporation of the molybdenum cofactor into NarZ, the α subunit of nitrate reductase Z . In vitro experiments detected interaction of NarW with both NarZ and NarG (the α subunit of nitrate reductase A) .

## Biological Role

Activated by ompR (protein.P0AA16), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19317|protein.P19317]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=narW; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=narW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004892,ECOCYC:EG10645,GeneID:946032`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1536614-1537309:-; feature_type=gene
