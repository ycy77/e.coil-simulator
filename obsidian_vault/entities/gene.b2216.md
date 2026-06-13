---
entity_id: "gene.b2216"
entity_type: "gene"
name: "rcsD"
source_database: "NCBI RefSeq"
source_id: "gene-b2216"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2216"
  - "rcsD"
---

# rcsD

`gene.b2216`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2216`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcsD (gene.b2216) is a gene entity. It encodes rcsD (protein.P39838). Encoded protein function: FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. RcsD is a phosphotransfer intermediate between the sensor kinase RcsC and the response regulator RcsB. It acquires a phosphoryl group from RcsC and transfers it to RcsB. The system controls expression of genes involved in colanic acid capsule synthesis, biofilm formation and cell division. {ECO:0000255|HAMAP-Rule:MF_00980, ECO:0000269|PubMed:10564486, ECO:0000269|PubMed:11309126, ECO:0000269|PubMed:11758943, ECO:0000269|PubMed:13129944, ECO:0000269|PubMed:14651646}. EcoCyc product frame: MONOMER0-4189. EcoCyc synonyms: yojP, yojQ, yojN. Genomic coordinates: 2313488-2316160. EcoCyc protein note: Represents the phosphorylated form of EG12385-MONOMER "RcsD" - a phosphotransfer protein in the Rcs signal transduction system. EcoCyc protein note: RcsD is a phosphotransferase within the complex Rcs phosphorelay. RcsD mediates phosphate transfer between the hybrid histidine kinase RcsC and the transcription regulator RcsB. RcsD may be the primary interacting partner of the Rcs pathway inhibitor, G7741-MONOMER "IgaA" (see )...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39838|protein.P39838]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rcsD; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=rcsD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007330,ECOCYC:EG12385,GeneID:946717`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2313488-2316160:+; feature_type=gene
