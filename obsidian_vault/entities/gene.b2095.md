---
entity_id: "gene.b2095"
entity_type: "gene"
name: "gatZ"
source_database: "NCBI RefSeq"
source_id: "gene-b2095"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2095"
  - "gatZ"
---

# gatZ

`gene.b2095`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2095`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gatZ (gene.b2095) is a gene entity. It encodes gatZ (protein.P0C8J8). Encoded protein function: FUNCTION: Component of the tagatose-1,6-bisphosphate aldolase GatYZ that is required for full activity and stability of the Y subunit. Could have a chaperone-like function for the proper and stable folding of GatY. When expressed alone, GatZ does not show any aldolase activity. Is involved in the catabolism of galactitol. {ECO:0000269|PubMed:11976750, ECO:0000269|PubMed:8955298}. EcoCyc product frame: G7128-MONOMER. Genomic coordinates: 2175059-2176321. EcoCyc protein note: The GatZ protein has no catalytic activity, but may stabilize the tagatose-1,6-bisphosphate aldolase TAGAALDOL2-MONOMER GatY as a heterodimer. GatZ appears to be required for full activity of GatY, and thus may have a chaperone-like function . However, E. coli's gatZ gene shows high sequence similarity for genes with tagatose-6-phosphate epimerase activity in other Gram negative bacteria: the gatZ of TAX-571, the tagE gene of TAX-382 and the agaZ of TAX-358...

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C8J8|protein.P0C8J8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gatZ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gatZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006934,ECOCYC:G7128,GeneID:946641`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2175059-2176321:-; feature_type=gene
