---
entity_id: "gene.b0861"
entity_type: "gene"
name: "artM"
source_database: "NCBI RefSeq"
source_id: "gene-b0861"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0861"
  - "artM"
---

# artM

`gene.b0861`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0861`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

artM (gene.b0861) is a gene entity. It encodes artM (protein.P0AE30). Encoded protein function: FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:8801422}. EcoCyc product frame: ARTM-MONOMER. Genomic coordinates: 900866-901534. EcoCyc protein note: Sequence analysis indicates that ArtM has similarity to the HisM membrane component of the histine/LAO (ltsine/arginine/ornithine) ABC transporter system in Salmonella typhimurium. ArtM is predicted to be a hydrophobic protein containing 3 transmembrane regions .

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE30|protein.P0AE30]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=artM; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=artM; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=artM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002931,ECOCYC:EG11627,GeneID:949066`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:900866-901534:-; feature_type=gene
