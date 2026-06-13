---
entity_id: "gene.b2710"
entity_type: "gene"
name: "norV"
source_database: "NCBI RefSeq"
source_id: "gene-b2710"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2710"
  - "norV"
---

# norV

`gene.b2710`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2710`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

norV (gene.b2710) is a gene entity. It encodes norV (protein.Q46877). Encoded protein function: FUNCTION: Anaerobic nitric oxide reductase; uses NADH to detoxify nitric oxide (NO), protecting several 4Fe-4S NO-sensitive enzymes. Has at least 2 reductase partners, only one of which (NorW, flavorubredoxin reductase) has been identified. NO probably binds to the di-iron center; electrons enter from the reductase at rubredoxin and are transferred sequentially to the FMN center and the di-iron center. Also able to function as an aerobic oxygen reductase. EcoCyc product frame: G7413-MONOMER. EcoCyc synonyms: ygaJ, ygaI, ygaK. Genomic coordinates: 2832476-2833915.

## Biological Role

Activated by rpoN (protein.P24255), norR (protein.P37013).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46877|protein.Q46877]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=norV; function=+
- `activates` <-- [[protein.P37013|protein.P37013]] `RegulonDB` `C` - regulator=NorR; target=norV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008910,ECOCYC:G7413,GeneID:948979`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2832476-2833915:+; feature_type=gene
