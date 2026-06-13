---
entity_id: "gene.b0589"
entity_type: "gene"
name: "fepG"
source_database: "NCBI RefSeq"
source_id: "gene-b0589"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0589"
  - "fepG"
---

# fepG

`gene.b0589`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0589`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fepG (gene.b0589) is a gene entity. It encodes fepG (protein.P23877). Encoded protein function: FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:1479347, PubMed:1838574). Responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:1479347, ECO:0000269|PubMed:1838574, ECO:0000305}. EcoCyc product frame: FEPG-MONOMER. Genomic coordinates: 620196-621188. EcoCyc protein note: FepG is the predicted integral membrane subunit of a ferrric enterobactin ABC transporter complex; insertional inactivation of fepG results in the loss of ferric eneterobactin uptake .

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23877|protein.P23877]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fepG; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fepG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002027,ECOCYC:EG10298,GeneID:945209`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:620196-621188:-; feature_type=gene
