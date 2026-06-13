---
entity_id: "gene.b4577"
entity_type: "gene"
name: "sgrS"
source_database: "NCBI RefSeq"
source_id: "gene-b4577"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4577"
  - "sgrS"
---

# sgrS

`gene.b4577`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4577`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgrS (gene.b4577) is a gene entity. EcoCyc product frame: RNA0-241. EcoCyc synonyms: ryaA. Genomic coordinates: 77367-77593.

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoD (protein.P00579), rpoS (protein.P13445), sgrR (protein.P33595).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (8)

- `represses` --> [[gene.b1101|gene.b1101]] `RegulonDB` `S` - regulator=SgrS; target=ptsG; function=-
- `represses` --> [[gene.b1658|gene.b1658]] `RegulonDB` `S` - regulator=SgrS; target=purR; function=-
- `represses` --> [[gene.b1817|gene.b1817]] `RegulonDB` `S` - regulator=SgrS; target=manX; function=-
- `represses` --> [[gene.b1818|gene.b1818]] `RegulonDB` `S` - regulator=SgrS; target=manY; function=-
- `represses` --> [[gene.b1819|gene.b1819]] `RegulonDB` `S` - regulator=SgrS; target=manZ; function=-
- `represses` --> [[gene.b2152|gene.b2152]] `RegulonDB` `S` - regulator=SgrS; target=yeiB; function=-
- `represses` --> [[gene.b2153|gene.b2153]] `RegulonDB` `S` - regulator=SgrS; target=folE; function=-
- `represses` --> [[gene.b4116|gene.b4116]] `RegulonDB` `S` - regulator=SgrS; target=adiY; function=-

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sgrS; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sgrS; function=+
- `activates` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `C` - regulator=SgrR; target=sgrS; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=sgrS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285090,ECOCYC:G0-9941,GeneID:4056038`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:77367-77593:+; feature_type=gene
