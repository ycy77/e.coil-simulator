---
entity_id: "gene.b3662"
entity_type: "gene"
name: "nepI"
source_database: "NCBI RefSeq"
source_id: "gene-b3662"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3662"
  - "nepI"
---

# nepI

`gene.b3662`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3662`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nepI (gene.b3662) is a gene entity. It encodes nepI (protein.P0ADL1). Encoded protein function: FUNCTION: Involved in the efflux of purine ribonucleosides, such as inosine and guanosine (PubMed:16040204). Adenosine may also be a substrate (PubMed:16040204). Confers resistance to the hypoxanthine analog 6-mercaptopurine, however the level of resistance is rather low (PubMed:16040204). {ECO:0000269|PubMed:16040204}. EcoCyc product frame: YICM-MONOMER. EcoCyc synonyms: yicM. Genomic coordinates: 3840549-3841739. EcoCyc protein note: The NepI protein is a member of the major facilitator superfamily (MFS) of transporters . nepI encodes a purine ribonucleoside exporter. It was discovered due to its ability to confer resistance to 6-mercaptopurine. Its overexpression in sensitive cells resulted in increased resistance to inosine and guanosine. Overexpression also reduced the growth rate of cells in media with inosine and guanosine as sole carbon source. Inosine accumulation in purine nucleoside phosphorylase deficient cells and the rate of excretion of inosine by an inosine producing strain were increased upon overexpression of nepI . NepI: "nucleoside efflux permease-inosine"

## Biological Role

Activated by soxS (protein.P0A9E2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADL1|protein.P0ADL1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=nepI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011967,ECOCYC:EG11689,GeneID:948213`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3840549-3841739:-; feature_type=gene
