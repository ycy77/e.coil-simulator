---
entity_id: "gene.b1901"
entity_type: "gene"
name: "araF"
source_database: "NCBI RefSeq"
source_id: "gene-b1901"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1901"
  - "araF"
---

# araF

`gene.b1901`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1901`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araF (gene.b1901) is a gene entity. It encodes araF (protein.P02924). Encoded protein function: FUNCTION: Involved in the high-affinity L-arabinose membrane transport system. Binds with high affinity to arabinose, but can also bind D-galactose (approximately 2-fold reduction) and D-fucose (approximately 40-fold reduction). EcoCyc product frame: ARAF-MONOMER. Genomic coordinates: 1985139-1986128. EcoCyc protein note: araF encodes the periplasmic binding protein of the high-affinity arabinose transport system. Purified AraF binds L-arabinose

## Biological Role

Repressed by spf (gene.b3864), nac (protein.Q47005). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fur (protein.P0A9A9), araC (protein.P0A9E0), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02924|protein.P02924]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araF; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=araF; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araF; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=araF; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=araF; function=+
- `represses` <-- [[gene.b3864|gene.b3864]] `RegulonDB` `S` - regulator=Spf; target=araF; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=araF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006330,ECOCYC:EG10057,GeneID:946409`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1985139-1986128:-; feature_type=gene
