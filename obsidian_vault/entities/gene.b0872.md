---
entity_id: "gene.b0872"
entity_type: "gene"
name: "hcr"
source_database: "NCBI RefSeq"
source_id: "gene-b0872"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0872"
  - "hcr"
---

# hcr

`gene.b0872`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0872`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcr (gene.b0872) is a gene entity. It encodes hcr (protein.P75824). Encoded protein function: FUNCTION: NADH oxidoreductase acting in concert with HCP. EcoCyc product frame: G6456-MONOMER. EcoCyc synonyms: ybjV. Genomic coordinates: 911182-912150. EcoCyc protein note: The hcr gene encodes an NADH oxidoreductase that catalyzes the reduction of the G6457-MONOMER (HCP). The physiological roles of HCP and the oxidoreductase are not known. They are detected only during anaerobic growth in the presence of nitrate and nitrite .

## Biological Role

Repressed by nsrR (protein.P0AF63). Activated by fnr (protein.P0A9E5), oxyR (protein.P0ACQ4), narL (protein.P0AF28), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75824|protein.P75824]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=hcr; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=hcr; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=hcr; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=hcr; function=+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `C` - regulator=NsrR; target=hcr; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002960,ECOCYC:G6456,GeneID:947660`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:911182-912150:-; feature_type=gene
