---
entity_id: "gene.b2096"
entity_type: "gene"
name: "gatY"
source_database: "NCBI RefSeq"
source_id: "gene-b2096"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2096"
  - "gatY"
---

# gatY

`gene.b2096`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2096`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gatY (gene.b2096) is a gene entity. It encodes gatY (protein.P0C8J6). Encoded protein function: FUNCTION: Catalytic subunit of the tagatose-1,6-bisphosphate aldolase GatYZ, which catalyzes the reversible aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to produce tagatose 1,6-bisphosphate (TBP) (PubMed:11976750, PubMed:8955298). Requires GatZ subunit for full activity and stability (PubMed:11976750). Is involved in the catabolism of galactitol (PubMed:11976750, PubMed:8955298). Has a high aldolase activity for TBP and a very low one for fructose 1,6-bisphosphate (FBP) (PubMed:11976750). {ECO:0000269|PubMed:11976750, ECO:0000269|PubMed:8955298}. EcoCyc product frame: TAGAALDOL2-MONOMER. EcoCyc synonyms: yegF. Genomic coordinates: 2176350-2177204. EcoCyc protein note: There are two distinct tagatose-1,6-bisphosphate aldolases in E. coli, the EG12768 kbaY-encoded aldolase 1 and the EG12419 gatY-encoded aldolase 2, both of which participate in galactitol catabolism. They catalyze the reversible aldol condensation of glycerone phosphate (dihydroxyacetone phosphate) with D-glyceraldehyde 3-phosphate to form tagatose 1,6-bisphosphate . The G7128-MONOMER GatZ protein has no catalytic activity, but appears to stabilize GatY, is required for full activity of GatY, and thus may have a chaperone-like function...

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C8J6|protein.P0C8J6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gatY; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gatY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006938,ECOCYC:EG12419,GeneID:946636`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2176350-2177204:-; feature_type=gene
