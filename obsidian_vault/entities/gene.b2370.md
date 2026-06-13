---
entity_id: "gene.b2370"
entity_type: "gene"
name: "evgS"
source_database: "NCBI RefSeq"
source_id: "gene-b2370"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2370"
  - "evgS"
---

# evgS

`gene.b2370`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2370`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

evgS (gene.b2370) is a gene entity. It encodes evgS (protein.P30855). Encoded protein function: FUNCTION: Member of the two-component regulatory system EvgS/EvgA (PubMed:9535079). Histidine kinase that phosphorylates EvgA via a four-step phosphorelay in response to environmental signals (PubMed:26151934, PubMed:9535079). Involved in adaptation to low pH environments and the control of acid resistance genes (PubMed:24957621, PubMed:24995530, PubMed:29140975). {ECO:0000269|PubMed:24957621, ECO:0000269|PubMed:24995530, ECO:0000269|PubMed:26151934, ECO:0000269|PubMed:29140975, ECO:0000269|PubMed:9535079}. EcoCyc product frame: MONOMER0-4184. Genomic coordinates: 2484374-2487967. EcoCyc protein note: This is the His-721 phosphorylated form of EVGS-MONOMER "EvgS" - the sensor histidine kinase of the EvgSA two-component signal transduction system. EcoCyc protein note: This is the His-1137 phosphorylated form of EVGS-MONOMER EvgS - the sensor histidine kinase of the EvgSA two-component signal transduction system. EcoCyc protein note: This is the Asp-1009 phosphorylated form of EVGS-MONOMER "EvgS" - the sensor histidine kinase of the EvgSA two-component signal transduction system.

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), evgA (protein.P0ACZ4), rpoS (protein.P13445).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30855|protein.P30855]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=evgS; function=+
- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=evgS; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=evgS; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=evgS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007819,ECOCYC:EG11610,GeneID:946844`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2484374-2487967:+; feature_type=gene
