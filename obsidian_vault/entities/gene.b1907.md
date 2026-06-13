---
entity_id: "gene.b1907"
entity_type: "gene"
name: "tyrP"
source_database: "NCBI RefSeq"
source_id: "gene-b1907"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1907"
  - "tyrP"
---

# tyrP

`gene.b1907`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1907`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tyrP (gene.b1907) is a gene entity. It encodes tyrP (protein.P0AAD4). Encoded protein function: FUNCTION: Transports tyrosine across the cytoplasmic membrane (PubMed:6090409). The transport system is energized by the proton motive force (PubMed:6090409). {ECO:0000269|PubMed:6090409}. EcoCyc product frame: TYRP-MONOMER. Genomic coordinates: 1989681-1990892. EcoCyc protein note: TyrP is a tyrosine-specific permease. It is a member of the Hydroxy/Aromatic Amino Acid Permease (HAAP) family. Studies, , found a single promoter whose expression was repressed by the TyrR protein in the presence of tyrosine and activated by the TyrR protein in the presence of phenylalanine.

## Biological Role

Repressed by tyrR (protein.P07604), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), tyrR (protein.P07604), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAD4|protein.P0AAD4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tyrP; function=+
- `activates` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=tyrP; function=-+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=tyrP; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006355,ECOCYC:EG11041,GeneID:946412`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1989681-1990892:+; feature_type=gene
