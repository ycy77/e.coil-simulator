---
entity_id: "gene.b0614"
entity_type: "gene"
name: "citX"
source_database: "NCBI RefSeq"
source_id: "gene-b0614"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0614"
  - "citX"
---

# citX

`gene.b0614`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0614`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

citX (gene.b0614) is a gene entity. It encodes citX (protein.P0A6G5). Encoded protein function: FUNCTION: Transfers 2-(5''-triphosphoribosyl)-3'-dephosphocoenzyme-A on a serine residue to the apo-acyl carrier protein (gamma chain) of the citrate lyase to yield holo-acyl carrier protein. {ECO:0000269|PubMed:10924139, ECO:0000269|PubMed:11042274}. EcoCyc product frame: G6340-MONOMER. EcoCyc synonyms: ybdU. Genomic coordinates: 647484-648035. EcoCyc protein note: CitX catalyzes the transfer of the citrate lyase prosthetic group 2'-(5''-phosphoribosyl)-3'-dephospho-CoA to the apo-ACP protein of citrate lyase, ACPSUB-MONOMER CitD, converting it to the active holo-ACP form . In vitro, the enzyme also functions as a nucleotidyltransferase . Following the computational prediction of a zinc-binding site in the protein, the presence of the cofactor was verified by ICP-MS. C145, C148, C155 and H161 are involved in metal binding. The presence of the zinc ion confers thermal stability on the protein. Crystal structures were solved by X-ray crystallography at 2.5 Å resolution and by molecular replacement at 1.7 Å resolution, confirming the presence of the zinc ion .

## Biological Role

Activated by dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6G5|protein.P0A6G5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=citX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002116,ECOCYC:G6340,GeneID:949084`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:647484-648035:-; feature_type=gene
