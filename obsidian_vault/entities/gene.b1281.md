---
entity_id: "gene.b1281"
entity_type: "gene"
name: "pyrF"
source_database: "NCBI RefSeq"
source_id: "gene-b1281"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1281"
  - "pyrF"
---

# pyrF

`gene.b1281`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1281`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrF (gene.b1281) is a gene entity. It encodes pyrF (protein.P08244). Encoded protein function: FUNCTION: Catalyzes the decarboxylation of orotidine 5'-monophosphate (OMP) to uridine 5'-monophosphate (UMP). EcoCyc product frame: OROTPDECARB-MONOMER. Genomic coordinates: 1341921-1342658.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08244|protein.P08244]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pyrF; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=pyrF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004304,ECOCYC:EG10809,GeneID:947121`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1341921-1342658:+; feature_type=gene
