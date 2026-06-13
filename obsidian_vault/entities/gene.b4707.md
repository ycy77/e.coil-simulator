---
entity_id: "gene.b4707"
entity_type: "gene"
name: "esrE"
source_database: "NCBI RefSeq"
source_id: "gene-b4707"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4707"
  - "esrE"
---

# esrE

`gene.b4707`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4707`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

esrE (gene.b4707) is a gene entity. EcoCyc product frame: RNA0-372. Genomic coordinates: 4019978-4020229.

## Biological Role

Activated by rpoD (protein.P00579), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=esrE; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=esrE; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10737,GeneID:14678511`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4019978-4020229:+; feature_type=gene
