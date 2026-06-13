---
entity_id: "gene.b2185"
entity_type: "gene"
name: "rplY"
source_database: "NCBI RefSeq"
source_id: "gene-b2185"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2185"
  - "rplY"
---

# rplY

`gene.b2185`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2185`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplY (gene.b2185) is a gene entity. It encodes rplY (protein.P68919). Encoded protein function: FUNCTION: This is one of the proteins that binds to the 5S RNA in the ribosome where it forms part of the central protuberance. Binds to the 5S rRNA independently of L5 and L18. Not required for binding of the 5S rRNA/L5/L18 subcomplex to 23S rRNA. {ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:354687, ECO:0000269|PubMed:8925931}. EcoCyc product frame: EG10885-MONOMER. Genomic coordinates: 2282517-2282801. EcoCyc protein note: The L25 protein is a component of the 50S subunit of the ribosome and binds to 5S rRNA. L25 is not an essential protein . Binding of L25 to 5S rRNA has been studied in detail . Solution structures of L25 alone and in complex with a segment of 5S rRNA have been determined , and a crystal structure of L25 bound to a loop E-containing fragment of 5S rRNA has been solved at 1.8 Å resolution . The interaction of L25 with 5S rRNA is not required for incorporation of L25 into the ribosome, although it is important for its retention . Molecular dynamics of the main polypeptide Cα-atoms in the α-helices and β-sheets were simulated; the latter have much lower dynamics and higher stability . L25 can be crosslinked to 23S rRNA in the initiation complex and to ribosomal protein L19 . L25 is important for retention of ribosomal protein L16...

## Biological Role

Repressed by rplY (protein.P68919).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68919|protein.P68919]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P68919|protein.P68919]] `RegulonDB` `S` - regulator=RplY; target=rplY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007231,ECOCYC:EG10885,GeneID:945618`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2282517-2282801:+; feature_type=gene
