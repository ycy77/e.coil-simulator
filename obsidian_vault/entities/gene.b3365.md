---
entity_id: "gene.b3365"
entity_type: "gene"
name: "nirB"
source_database: "NCBI RefSeq"
source_id: "gene-b3365"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3365"
  - "nirB"
---

# nirB

`gene.b3365`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3365`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nirB (gene.b3365) is a gene entity. It encodes nirB (protein.P08201). Encoded protein function: Nitrite reductase (NADH) large subunit (EC 1.7.1.15) EcoCyc product frame: NIRB-MONOMER. Genomic coordinates: 3494011-3496554. EcoCyc protein note: nirB encodes the catalytic subunit of nitrite reductase . Expression of nirB is downregulated in response to cobalt and upregulated upon exposure to silver nanoparticles . NirB: "nitrite reductase"

## Biological Role

Repressed by ryhB (gene.b4451), fis (protein.P0A6R3), hns (protein.P0ACF8), cra (protein.P0ACP1). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08201|protein.P08201]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nirB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nirB; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nirB; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nirB; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nirB; function=-
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=nirB; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=nirB; function=-
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nirB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011003,ECOCYC:EG10653,GeneID:947868`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3494011-3496554:+; feature_type=gene
