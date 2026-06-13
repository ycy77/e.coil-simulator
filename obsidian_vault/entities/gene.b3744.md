---
entity_id: "gene.b3744"
entity_type: "gene"
name: "asnA"
source_database: "NCBI RefSeq"
source_id: "gene-b3744"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3744"
  - "asnA"
---

# asnA

`gene.b3744`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3744`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asnA (gene.b3744) is a gene entity. It encodes asnA (protein.P00963). Encoded protein function: FUNCTION: May amidate Asp of the extracellular death factor precursor Asn-Asn-Trp-Asp-Asn to generate Asn-Asn-Trp-Asn-Asn. {ECO:0000305|PubMed:17962566}. EcoCyc product frame: ASNSYNA-MONOMER. Genomic coordinates: 3927155-3928147.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00963|protein.P00963]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=asnA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=asnA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012242,ECOCYC:EG10091,GeneID:948258`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3927155-3928147:+; feature_type=gene
