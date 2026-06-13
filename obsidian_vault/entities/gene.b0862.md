---
entity_id: "gene.b0862"
entity_type: "gene"
name: "artQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0862"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0862"
  - "artQ"
---

# artQ

`gene.b0862`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0862`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

artQ (gene.b0862) is a gene entity. It encodes artQ (protein.P0AE34). Encoded protein function: FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:8801422}. EcoCyc product frame: ARTQ-MONOMER. Genomic coordinates: 901534-902250. EcoCyc protein note: Sequence analysis indicates that ArtQ has similarity to the HisQ membrane component of the histine/LAO (lysine/arginine/ornithine) ABC transporter system in Salmonella typhimurium. ArtQ is predicted to be a hydrophobic protein containing 4 transmembrane regions .

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE34|protein.P0AE34]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=artQ; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=artQ; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=artQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002933,ECOCYC:EG11626,GeneID:949046`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:901534-902250:-; feature_type=gene
