---
entity_id: "gene.b4321"
entity_type: "gene"
name: "gntP"
source_database: "NCBI RefSeq"
source_id: "gene-b4321"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4321"
  - "gntP"
---

# gntP

`gene.b4321`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4321`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gntP (gene.b4321) is a gene entity. It encodes gntP (protein.P0AC94). Encoded protein function: FUNCTION: High-affinity gluconate transporter with fairly broad specificity, including low affinity for glucuronate, several disaccharides, and some hexoses, but not glucose. EcoCyc product frame: GNTP-MONOMER. EcoCyc synonyms: yjiB. Genomic coordinates: 4549953-4551296. EcoCyc protein note: GntP is a member of the GntP family transporters and is homologous to the E. coli GntT and GntU gluconate transporters. GntP transports D-fructuronate/D-gluconate . Whole cell experiments have shown that the cloned gntP gene confers gluconate transport with a Km of approx 25 μM, but its expression is not induced by gluconate . gntP gene is induced by fructuronate, the first intermediate of the glucuronate metabolism pathway. It is a member of UxuR regulon which is composed of genes induced by glucuronate via its conversion to fructuronate and these genes are repressed by UxuR . gntP mutants were unable to grow using fructuronate as their sole carbon source. Taken together, these results indicate that GntP is the primary fructuronate transporter . gntP was predicted to be a target of the small RNA OmrB. Overexpression of both OmrB and OmrA decreases the expression of gntP . gntP was found to be downregulated in a MG1655 lysogen carrying the Stx2a phage PA8 .

## Biological Role

Repressed by uxuR (protein.P39161).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC94|protein.P0AC94]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P39161|protein.P39161]] `RegulonDB` `C` - regulator=UxuR; target=gntP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014161,ECOCYC:EG12563,GeneID:948848`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4549953-4551296:-; feature_type=gene
